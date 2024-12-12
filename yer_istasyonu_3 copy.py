import sys
import pyodbc
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
    QMessageBox,
    QPushButton
)

# Configurable database connection string
def get_connection_string(server, database, username, password):
    return (
        rf"DRIVER={{SQL Server}};"
        rf"SERVER={server};"
        rf"DATABASE={database};"
        rf"UID={username};"
        rf"PWD={password};"
    )

class DatabaseManager:
    """Handles database connections and queries."""

    def __init__(self, conn_string):
        self.conn_string = conn_string

    def fetch_tickets(self):
        """Fetches ticket data from the database."""
        try:
            with pyodbc.connect(self.conn_string) as conn:
                cursor = conn.cursor()
                query = """
                SELECT TOP (1000) [ticketID], [seatNumber], [purchaseDate],
                                  [amount], [customerID], [paymentID], [journeyID]
                FROM [journey_management3].[dbo].[Ticket]
                """
                cursor.execute(query)
                data = cursor.fetchall()
                headers = [desc[0] for desc in cursor.description]
                return headers, data
        except pyodbc.Error as e:
            raise RuntimeError(f"Database error: {e}")

class TicketViewer(QMainWindow):
    """Main window to display ticket data."""

    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self.setWindowTitle("Ticket Viewer")
        self.setGeometry(100, 100, 800, 400)

        # Main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Table widget
        self.tableWidget = QTableWidget()
        self.layout.addWidget(self.tableWidget)

        # Load data
        self.load_tickets()

    def load_tickets(self):
        """Loads tickets into the table."""
        try:
            headers, data = self.db_manager.fetch_tickets()
            self.populate_table(headers, data)
        except RuntimeError as e:
            QMessageBox.critical(self, "Error", str(e))

    def populate_table(self, headers, data):
        """Populates the table widget with data."""
        self.tableWidget.setColumnCount(len(headers) + 1)  # Extra column for the button
        self.tableWidget.setHorizontalHeaderLabels(headers + ["Action"])  # Add "Action" column for the button
        self.tableWidget.setRowCount(len(data))

        for row_idx, row in enumerate(data):
            # Populate table with data
            for col_idx, value in enumerate(row):
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
            
            # Create and add a button in the last column of each row
            button = QPushButton("View Details")
            button.clicked.connect(lambda checked, row=row: self.on_button_click(row))  # Pass the row data to the handler
            self.tableWidget.setCellWidget(row_idx, len(row), button)  # Add button in the last column

    def on_button_click(self, row_data):
        """Handles the button click event."""
        # Show a message box with the ticket details when the button is clicked
        ticket_info = f"Ticket ID: {row_data[0]}\nSeat Number: {row_data[1]}\nPurchase Date: {row_data[2]}\nAmount: {row_data[3]}"
        QMessageBox.information(self, "Ticket Details", ticket_info)

if __name__ == "__main__":
    # Database connection details
    SERVER_NAME = "ALI"
    DATABASE_NAME = "journey_management3"
    USERNAME = ""
    PASSWORD = ""

    conn_string = get_connection_string(SERVER_NAME, DATABASE_NAME, USERNAME, PASSWORD)
    db_manager = DatabaseManager(conn_string)

    app = QApplication(sys.argv)
    viewer = TicketViewer(db_manager)
    viewer.show()
    sys.exit(app.exec_())
