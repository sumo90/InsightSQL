import oracledb

conn = oracledb.connect(
    user="system",
    password="root",
    dsn="localhost/FREEPDB1"
)

def execute_query(query):
    cursor = conn.cursor()

    cursor.execute(query)

    columns = [col[0] for col in cursor.description]

    rows = cursor.fetchall()

    cursor.close()

    return columns, rows