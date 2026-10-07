# Projeto Final - Sistema de Gestão
import os

# Lista para armazenar clientes
lista_clientes = []

#criar funcao para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

#criar visualizacao do menu
def menu():
    print("Bem-vindo ao Sistema de Gestão Hospitalar")
    print("1. Adicionar Cliente")
    print("2. Ver clientes cadastrados")
    print("3. Observações")
    print("4. Sair")

# defenir a função para cadastrar clientes
def cadastrar_cliente():
    limpar_tela()
    num_clientes = int(input("Digite o número de clientes a cadastrar: "))
    
    for i in range(num_clientes):
        print(f"\nCadastro do cliente {i+1}:")
        cliente = {"ID": len(lista_clientes) + 1, "Nome": "", "Idade": 0, "Sexo": "", "NIF": 0, "Morada": "", "Telefone": 0}
        
        cliente["Nome"] = input("Digite o nome do cliente: ")
        cliente["Idade"] = int(input("Digite a idade do cliente: "))
        cliente["Sexo"] = input("Digite o sexo do cliente (M/F): ")
        cliente["NIF"] = int(input("Digite o NIF do cliente (9 dígitos): "))
        cliente["Morada"] = input("Digite a morada do cliente (opcional): ")
        cliente["Telefone"] = int(input("Digite o telefone do cliente (9 dígitos): "))
        
        lista_clientes.append(cliente)
        print(f"Cliente {cliente['Nome']} cadastrado com sucesso!")
    
    input("\nPressione Enter para voltar ao menu...")

def ver_clientes():
    limpar_tela()
    
    if len(lista_clientes) == 0:
        print("Nenhum cliente cadastrado.")
        input("\nPressione Enter para voltar ao menu...")
        return
    
    print("\n" + "=" * 70)
    print(f"{'ID':<5} {'Nome':<25} {'Idade':<8} {'Contacto':<15}")
    print("=" * 70)
    
    for cliente in lista_clientes:
        print(f"{cliente['ID']:<5} {cliente['Nome']:<25} {cliente['Idade']:<8} {cliente['Telefone']:<15}")
    
    print("=" * 70 + "\n")
    input("Pressione Enter para voltar ao menu...")

def observacoes():
    limpar_tela()
    print("Observações do Sistema")
    print("Este é um sistema de gestão hospitalar.")
    input("\nPressione Enter para voltar ao menu...")

#Prog principal 
while True:
    menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        ver_clientes()
    elif opcao == "3":
        observacoes()
    elif opcao == "4":
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")