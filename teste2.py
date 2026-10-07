# Projeto Final - Sistema de Gestão
import os
# criar vetores para armazenar clientes, consultas e marcações
vetor_clientes = []
vetor_consultas = ["Cardiologia", "Ortopedia", "Pediatria", "Oftalmologia", "Dermatologia", "Neurologia"]
vetor_marcacoes = []
#criar funcao para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

#criar visualizacao do menu
def menu():
    limpar_tela()
    print("="*50)
    print("Bem-vindo ao Sistema de Gestão Hospitalar")
    print("="*50)
    print("1. Adicionar Cliente")
    print("2. Listar clientes ")
    print("3. Marcar Consulta")
    print("4. Ver Consultas Marcadas")
    print("5. Pesquisar Cliente por ID")
    print("6. Estatísticas dos Clientes")
    print("0. Sair")
    

# defenir a função para adicionar clientes
def clientes():
    limpar_tela()
    print("==================Adicionar Clientes==================")
    num_clientes =int(input("Digite o número de clientes a adicionar: "))
    
    while num_clientes <= 0 or num_clientes>=30:
            num_clientes = int(input("O número de clientes deve ser entre (1 e 30). Por favor, tente novamente: "))

    for i in range(num_clientes):
        
        print(f"\nRegisto do cliente {i+1}:")
       
        cliente = {"ID": len(vetor_clientes) + 1, "Nome": "", "Idade": 0, "Sexo": "", "NIF": 0, "Morada": "", "Telefone": 0}
        
        cliente["Nome"] = input("Digite o nome do cliente: ")
        while len(cliente["Nome"]) <=0:
            cliente["Nome"] = input("O Nome deve ser Preenchido. Por favor, tente novamente.")
            
            
        cliente["Idade"] = int(input("Digite a idade do cliente: "))
        while cliente["Idade"] < 0 or cliente["Idade"] >=130:
            cliente["Idade"] = int(input("A idade deve estar entre (0 e 130). Por favor, tente novamente: "))

        cliente["Sexo"] = input("Digite o sexo do cliente (M/F): ")
        if cliente["Sexo"].upper() not in ["M", "F"]:
            cliente["Sexo"] = input("Sexo inválido. Por favor, digite M ou F: ")

        cliente["Telefone"] = int(input("Digite o telefone do cliente (9 dígitos): "))
        if len(str(cliente["Telefone"])) != 9:
            cliente["Telefone"] = int(input("Telefone inválido. Por favor, digite um telefone com 9 dígitos: "))
            
        if cliente["Telefone"] == "":
            cliente["Telefone"] = int(input("O telefone não pode ser vazio. Por favor, tente novamente."))
            
        if cliente["Telefone"] == str or cliente["Telefone"] == float or cliente["Telefone"] == bool:
            cliente["Telefone"] = int(input("O telefone deve ser um número inteiro. Por favor, tente novamente."))
             

        vetor_clientes.append(cliente)
        
    
        print(f"Cliente {cliente['Nome']} adicionado com sucesso!")
    input("\nPressione Enter para voltar ao menu...")

def ver_clientes():
    limpar_tela()
    
    if len(vetor_clientes) == 0:
        print("Nenhum cliente adicionado.")
        input("\nPressione Enter para voltar ao menu...")
        return
    
    print("\n" + "=" * 70)
    print(f"{'ID':<5} {'Nome':<25} {'Idade':<8} {'Contacto':<15}")
    print("=" * 70)
    
    for cliente in vetor_clientes:
        print(f"{cliente['ID']:<5} {cliente['Nome']:<25} {cliente['Idade']:<8} {cliente['Telefone']:<15}")
    
    print("=" * 70 + "\n")
    input("Pressione Enter para voltar ao menu...")

def marcar_consulta():
    limpar_tela()
    print("=" * 50)
    print("Marcar Consulta")
    print("=" * 50)
    
    if len(vetor_clientes) == 0:
        print("Nenhum cliente adicionado. Adicione um cliente primeiro.")
        input("\nPressione Enter para voltar ao menu...")
        return
    
    
    id_cliente = int(input("Digite o ID do cliente: "))
    

    cliente_encontrado = None
    for cliente in vetor_clientes:
        if cliente["ID"] == id_cliente:
            cliente_encontrado = cliente
            break
    
    if cliente_encontrado == None:
        print(f"Cliente com ID {id_cliente} não encontrado!")
        input("\nPressione Enter para voltar ao menu...")
        return
    
    print(f"\nCliente: {cliente_encontrado['Nome']}")
    
    
    print("\nConsultas disponíveis a marcar:")
    print("=" * 30)
    for i in range(len(vetor_consultas)):
        print(f"{i + 1}. {vetor_consultas[i]}")
    print("=" * 30)
    
    
    opcao_consulta = int(input("\nEscolha o número da consulta: "))
    
    if opcao_consulta < 1 or opcao_consulta > len(vetor_consultas):
        print("Opção inválida!")
        input("\nPressione Enter para voltar ao menu...")
        return
    
    consulta_escolhida = vetor_consultas[opcao_consulta - 1]
    
    
    data_consulta = input("Digite a data da consulta (ex: 15/12/2024): ")
    
    marcacao = {
        "ID_Cliente": id_cliente,
        "Nome_Cliente": cliente_encontrado["Nome"],
        "Tipo_Consulta": consulta_escolhida,
        "Data": data_consulta
    }
    
    vetor_marcacoes.append(marcacao)
    
    print(f"\nConsulta marcada com sucesso!")
    print(f"Tipo: {consulta_escolhida}")
    print(f"Data: {data_consulta}")
    print(f"Cliente: {cliente_encontrado['Nome']}")
    
    input("\nPressione Enter para voltar ao menu...")

def ver_marcacoes_consultas():
    limpar_tela()
    print("==================Consultas Marcadas==================")
    
    if len(vetor_marcacoes) == 0:
        print("Nenhuma consulta marcada.")
        input("\nPressione Enter para voltar ao menu...")
        return
    
    # Cabeçalho da tabela
    print("\n" + "=" * 90)
    print(f"{'ID':<5} {'Nome Cliente':<25} {'Tipo de Consulta':<20} {'Data':<15}")
    print("=" * 90)
    
    # Mostrar cada marcação
    for marcacao in vetor_marcacoes:
        print(f"{marcacao['ID_Cliente']:<5} {marcacao['Nome_Cliente']:<25} {marcacao['Tipo_Consulta']:<20} {marcacao['Data']:<15}")
    
    print("=" * 90)
    print(f"Total de consultas marcadas: {len(vetor_marcacoes)}\n")
    input("Pressione Enter para voltar ao menu...")

def pesquisar_cliente_por_id():
    limpar_tela()
    print("=" * 50)
    print("Pesquisar Cliente por ID")
    print("=" * 50)
    
    if len(vetor_clientes) == 0:
        print("Nenhum cliente adicionado.")
        input("\nPressione Enter para voltar ao menu...")
        return
    
    id_cliente = int(input("Digite o ID do cliente a pesquisar: "))
    
    cliente_encontrado = None
    for cliente in vetor_clientes:
        if cliente["ID"] == id_cliente:
            cliente_encontrado = cliente
            break
    
    if cliente_encontrado == None:
        print(f"\nCliente com ID {id_cliente} não encontrado!")
    else:
        print("\n" + "=" * 50)
        print(f"ID:      {cliente_encontrado['ID']}")
        print(f"Nome:    {cliente_encontrado['Nome']}")
        print(f"Idade:   {cliente_encontrado['Idade']}")
        print(f"Sexo:    {cliente_encontrado['Sexo']}")
        print(f"Telefone:{cliente_encontrado['Telefone']}")
        print("=" * 50)
    
    input("\nPressione Enter para voltar ao menu...")

def estat_clientes():
    limpar_tela()
    print("==================Estatísticas dos Clientes==================")
    
    if len(vetor_clientes) == 0:
        print("Nenhum cliente adicionado.")
        input("\nPressione Enter para voltar ao menu...")
        return
    
    # Calcular estatísticas diretamente usando sum(), min(), max()
    soma_idades = sum(cliente["Idade"] for cliente in vetor_clientes)
    media_idade = soma_idades / len(vetor_clientes)
    idade_minima = min(cliente["Idade"] for cliente in vetor_clientes)
    idade_maxima = max(cliente["Idade"] for cliente in vetor_clientes)
    
    print(f"Total de clientes: {len(vetor_clientes)}")
    print(f"Idade média dos clientes: {media_idade:.2f} anos")
    print(f"Idade mínima dos clientes: {idade_minima} anos")
    print(f"Idade máxima dos clientes: {idade_maxima} anos")
    print(f"Clientes do sexo masculino: {sum(1 for cliente in vetor_clientes if cliente['Sexo'].upper() == 'M')}")
    print(f"Clientes do sexo feminino: {sum(1 for cliente in vetor_clientes if cliente['Sexo'].upper() == 'F')}")
    input("\nPressione Enter para voltar ao menu...")
#Prog principal 
while True:
    menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        clientes()
    elif opcao == "2":
        ver_clientes()
    elif opcao == "3":
        marcar_consulta()
    elif opcao == "4":
        ver_marcacoes_consultas()
    elif opcao == "5":
        pesquisar_cliente_por_id()
    elif opcao == "6":
        estat_clientes()
    elif opcao == "0":
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")