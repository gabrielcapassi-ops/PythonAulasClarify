import sqlite3 

#conectar ao banco de dados (ou criar um novo se nao existir)
def conectarBanco():
    conexao = sqlite3.connect('bancodedados.db') 
    return conexao 


#Criar uma tabela
def criarTabela():
    conexao = conectarBanco() #abre a conexao
    cursor = conexao.cursor() #cria um cursor para executar os comandos sql
    #cria a tabela se ela nao existir
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        idade INTEGER 
                             )
''')
    conexao.commit()
    conexao.close()

def inserirUsuario(nome,idade):
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO usuarios (nome, idade) VALUES(?,?)''',(nome, idade))

    conexao.commit()
    conexao.close()

def listarUsuarios():
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('''
        SELECT * FROM usuarios
           ''')
    usuarios= cursor.fetchall()
    for usuario in usuarios:
        print(usuario)
    conexao.close()


def atualizarUsuario(id, novoNome, novaIdade):
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('''
        UPDATE usuarios SET nome = ?, idade = ?
        WHERE id = ?
           ''',(novoNome, novaIdade,id))
    conexao.commit()
    conexao.close()

def excluirUsuario(id):
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute(''' DELETE FROM usuarios WHERE id = ? ''',(id,))
    conexao.commit()
    conexao.close()

#exemplos de uso das funcoes crud

#criar tabela
criarTabela()

#inserir dados do banco.
#inserirUsuario ('Caio',38)
#inserirUsuario ('Myke',35)
#inserirUsuario ('Gabriel',37)
#inserirUsuario ('Gustavo',40)
#inserirUsuario ('joão',36)

#listar todos os usuarios cadastrados no banco
print('usuarios antes de atualizar')
listarUsuarios()
print('---------------')

#atualizar a idade e nome de um usuario
atualizarUsuario(1, 'Enzo', 20)
atualizarUsuario(2, 'Valentina', 60)

#excluirusuario
excluirUsuario(6)



print('Usuarios depois da atualização')
listarUsuarios()
print("-----------")





