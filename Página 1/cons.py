import mysql.connector
from mysql.connector import Error

try:
    # Conectar ao banco de dados MySQL através do proxy
    conn = mysql.connector.connect(
        host="roundhouse.proxy.rlwy.net",
    user="root",
    password="iRbSpeeGcmSPdDoHaVHGekOPGTSEGVdo",
    database="railway"  # Substitua pelo seu banco de dados
    )
    if conn.is_connected():
        print("Conexão estabelecida com sucesso!")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM minha_tabela")
        rows = cursor.fetchall()
        if not rows:
            print("Nenhum registro encontrado.")
        else:
            for row in rows:
                print(row)
except Error as e:
    print(f"Erro ao conectar ao MySQL: {e}")
finally:
    try:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Conexão encerrada.")
    except NameError:
        print("Não foi possível encerrar a conexão porque ela não foi estabelecida.")
