import pyodbc

# Veritabanı bağlantı bilgilerini buraya girin
conn_string = (
    r'DRIVER={SQL Server};'
    r'SERVER=ALI;'
    r'DATABASE=journey_management2;'
    r'UID=;'
    r'PWD=;'
)

try:
    conn = pyodbc.connect(conn_string)
    cursor = conn.cursor()

    # Sorgunu çalıştır
    cursor.execute("SELECT * FROM JOURNEY WHERE departureCity='İstanbul'")

    # Sonuçları bir listeye ata
    results = cursor.fetchall()
    print(results)

    # Sonuçları yazdırma (örnek)
    for row in results:
        print(row)

except pyodbc.Error as ex:
    print(ex)

finally:
    conn.close()