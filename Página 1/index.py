from flask import Flask, render_template, request, jsonify
import mysql.connector
import logging

app = Flask(__name__)

# Configurando logging
logging.basicConfig(level=logging.DEBUG)

# Conectar ao banco de dados MySQL (substitua as informações com as suas)
mydb = mysql.connector.connect(
    host="roundhouse.proxy.rlwy.net",
    user="root",
    password="iRbSpeeGcmSPdDoHaVHGekOPGTSEGVdo",
    database="railway"
)

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para cadastrar usuário
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    app.logger.debug('Recebida uma requisição POST para /cadastrar')
    data = request.get_json()
    app.logger.debug(f'Requisição JSON recebida: {data}')
    
    usuario = data.get('usuario')
    senha = data.get('senha')
    app.logger.debug(f'Usuário: {usuario}, Senha: {senha}')

    # Criar cursor para executar comandos SQL
    mycursor = mydb.cursor()

    # Comando SQL para inserir dados
    sql = "INSERT INTO usuarios (usuario, senha) VALUES (%s, %s)"
    val = (usuario, senha)

    try:
        # Executar o comando SQL
        mycursor.execute(sql, val)
        app.logger.debug('Comando SQL executado com sucesso')

        # Commit para salvar as mudanças no banco de dados
        mydb.commit()
        app.logger.debug('Commit realizado')

        return jsonify({'message': 'Usuário cadastrado com sucesso!'}), 200
    except mysql.connector.Error as err:
        # Se ocorrer um erro, desfazer a operação e retornar uma mensagem de erro
        mydb.rollback()
        app.logger.error(f'Erro ao cadastrar usuário: {err}')
        return jsonify({'error': f'Erro ao cadastrar usuário: {err}'}), 500
    finally:
        # Fechar o cursor
        mycursor.close()
        app.logger.debug('Cursor fechado')

if __name__ == '__main__':
    app.run(debug=True)
