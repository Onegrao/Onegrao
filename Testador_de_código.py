#Aqui vou testar todos os codigos deste projeto PDV para testar e aprender fazendo
from database import * 

#Agora vamos testar todas as funcionalidades com o database

#Cadastro de funcionarios
print("Cadastro de Funcionario")
senha = gerar_codigo_aleatorio()
usuario = "NewUser"
nome_completo = input("Informe seu nome")
cargo = input("Informe seu Cargo")
cadastro_funcionario(nome_completo,senha,usuario,cargo)


#Consulta de funcionarios
print("Consulta de Funcionarios")
id_usuario = int(input("Insira o id de funcionario"))
consulta_funcionario(id_usuario)

#Alterar senha
print
#Excluir funcionario
#Cadastrar produto
#Alterara produto
#Consulta Produto
#Excluir Produto


