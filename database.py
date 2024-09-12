#Aqui nos vamos criar a conexão com o banco de dados e ter as funções de busca e retorno relacionados aos bancos de daos
import mysql.connector
import string
import random 
'''
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Sophia2010!',
    database='meu_banco',
)
if conexao.is_connected():
    print("Con//exão Bem Sucedida")
else:
    print("erro")
conexao.close()

cursor = conexao.cursor()
'''
#Vamos definir agora as funções referentes as configurações dos bancos de dados

def conectar():
    conn = mysql.connector.conect(
        host="",
        user="",
        password="",
        database="",
    )
    return conn

def fechar_conexao(conn):
    conn.close()

def fechar_cursor(cursor):
    cursor.close()


def gerar_codigo_aleatorio(tamanho=6):
    caracteres = string.ascii_letters + string.digits  # Letras maiúsculas, minúsculas e dígitos
    codigo_aleatorio = ''.join(random.choices(caracteres, k=tamanho))
    return codigo_aleatorio

def buscar_produto(codigo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos WHERE codigo=%s",(codigo))
    produto=cursor.fetchone()
    fechar_cursor(cursor)
    fechar_conexao(conn)
    return produto

def verificar_login (usuario,senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT usuario,senha,cargo FROM login WHERE user=%s AND senha=%s"(usuario,senha))
    resultado=cursor.fetchone()#Aqui ele retorna a primeira linha encontrada
    fechar_cursor(cursor)#Fecha a conexao do cursor
    fechar_conexao(conn)#Fecha a conexao com o banco de dados
    return resultado

def cadastro_funcionario (nome_completo,senha,usuario,cargo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO funcionarios (nome_completo,cargo,usuario,senha) VALUES (%s,%s,%s,%s)",(nome_completo,cargo,usuario,senha))
    fechar_cursor(cursor)
    fechar_conexao(conn)
    print("Usuario cadastrado com sucesso")

def excluir_funcionario(id_usuario,senha_admin):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute = ("DELETE FROM funcionarios WHERE VALUES(%s)",(id_usuario,senha_admin))
    fechar_cursor(cursor)
    fechar_conexao(conn)
    print("Usuario eliminado!")

def consulta_funcionario(id_usuario):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("Select * FROM funcionarios WHERE id_usuario=%s",(id_usuario))
    funcionario = cursor.fetchone()
    fechar_cursor(cursor)
    fechar_conexao(conn)
    return funcionario

def alterar_informacoes(id_usuario,senha):
    print("Q")




