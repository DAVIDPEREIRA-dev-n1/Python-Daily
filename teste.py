# Projeto Final - Sistema de Gestão
import os
from datetime import datetime
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
    print("2. Editar Cliente")
    print("3. Listar clientes ")
    print("4. Marcar Consulta")
    print("5. Ver Consultas Marcadas")
    print("6. Pesquisar Cliente por ID")
    print("7. Estatísticas dos Clientes")
    print("8. Filtrar Clientes por Categoria")
    print("9. Eliminar Cliente")
    print("10. Exportar Dados para Ficheiro .txt")
    print("0. Sair")

# defenir a função para adicionar clientes
def clientes():
    limpar_tela()
    print("==================Adicionar Clientes==================")
    num_clientes =int(input("Digite o número de clientes a adicionar: "))
    while num_clientes <= 0 or num_clientes >= 30  :
            num_clientes = int(input("O número de clientes deve ser entre (1 e 30). Por favor, tente novamente: "))

    for i in range(num_clientes):
        
        print(f"\nRegisto do cliente {i+1}:")
       
        cliente = {"ID": len(vetor_clientes) + 1, "Nome": "", "Idade": 0, "Sexo": "", "Telefone": 0}
        
        cliente["Nome"] = input("Digite o nome do cliente: ")
        while len(cliente["Nome"]) <=0:
            cliente["Nome"] = input("O Nome deve ser Preenchido. Por favor, tente novamente: ")
            
            
        cliente["Idade"] = int(input("Digite a idade do cliente: "))
        while cliente["Idade"] < 0 or cliente["Idade"] >=130:
            cliente["Idade"] = int(input("A idade deve estar entre (0 e 130). Por favor, tente novamente: "))

        cliente["Sexo"] = input("Digite o sexo do cliente (M/F): ")
        while cliente["Sexo"].upper() not in ["M", "F"]:
            cliente["Sexo"] = input("Sexo inválido. Por favor, digite M ou F: ")

        cliente["Telefone"] = int(input("Digite o telefone do cliente (9 dígitos): "))
        while len(str(cliente["Telefone"])) != 9 :
            cliente["Telefone"] = int(input("Telefone inválido. Por favor, digite um telefone com 9 dígitos: "))
            
            
        vetor_clientes.append(cliente)
        
    
        print(f"Cliente {cliente['Nome']} adicionado com sucesso!")
    input("\nPressione Enter para voltar ao menu...")

def editar_cliente():
    limpar_tela()
    print("="*50)
    print("Editar Clientes")
    print("="*50)
    
    if len(vetor_clientes) == 0:
        print("Nenhum cliente adicionado.")
        input("\nPressione Enter para voltar ao menu...")
        return
    
    print("1. Procurar por ID")
    print("2. Procurar por Nome")
    opcao_busca = input("Escolha como procurar (1 ou 2): ")
    
    cliente_encontrado = None
    
    if opcao_busca == "1":
        id_cliente = int(input("Digite o ID do cliente a editar: "))
        
        for cliente in vetor_clientes:
            if cliente["ID"] == id_cliente:
                cliente_encontrado = cliente
                break
        
        if cliente_encontrado == None:
            print(f"Cliente com ID {id_cliente} não encontrado!")
            input("\nPressione Enter para voltar ao menu...")
            return
    
    elif opcao_busca == "2":
        nome_cliente = input("Digite o nome do cliente a editar: ")
        clientes_encontrados = []
        
        for cliente in vetor_clientes:
            if nome_cliente.lower() in cliente["Nome"].lower():
                clientes_encontrados.append(cliente)
        
        if len(clientes_encontrados) == 0:
            print(f"Nenhum cliente com o nome '{nome_cliente}' encontrado!")
            input("\nPressione Enter para voltar ao menu...")
            return
        
        if len(clientes_encontrados) == 1:
            cliente_encontrado = clientes_encontrados[0]
        else:
            print("\nVários clientes encontrados:")
            for i in range(len(clientes_encontrados)):
                print(f"{i + 1}. ID: {clientes_encontrados[i]['ID']} - Nome: {clientes_encontrados[i]['Nome']}")
            
            escolha = int(input("Escolha qual cliente editar (número): "))
            while escolha < 1 or escolha > len(clientes_encontrados):
                escolha = int(input("Opção inválida! Tente novamente: "))
            
            cliente_encontrado = clientes_encontrados[escolha - 1]
    else:
        print("Opção inválida!")
        input("\nPressione Enter para voltar ao menu...")
        return
    
    while True:
        limpar_tela()
        print("="*50)
        print(f"Editar Cliente: {cliente_encontrado['Nome']}")
        print("="*50)
        print(f"1. Nome: {cliente_encontrado['Nome']}")
        print(f"2. Idade: {cliente_encontrado['Idade']}")
        print(f"3. Sexo: {cliente_encontrado['Sexo']}")
        print(f"4. Telefone: {cliente_encontrado['Telefone']}")
        print("0. Guardar e Sair")
        print("="*50)
        
        opcao = input("Escolha o campo a editar (0-4): ")
        
        if opcao == "1":
            novo_nome = input("Digite o novo nome: ")
            while len(novo_nome) <= 0:
                novo_nome = input("O Nome deve ser Preenchido. Por favor, tente novamente: ")
            cliente_encontrado["Nome"] = novo_nome
            print(f"Nome atualizado para: {novo_nome}")
            input("\nPressione Enter para continuar...")
            
        elif opcao == "2":
            nova_idade = int(input("Digite a nova idade: "))
            while nova_idade < 0 or nova_idade >= 130:
                nova_idade = int(input("A idade deve estar entre (0 e 130). Por favor, tente novamente: "))
            cliente_encontrado["Idade"] = nova_idade
            print(f"Idade atualizada para: {nova_idade}")
            input("\nPressione Enter para continuar...")
            
        elif opcao == "3":
            novo_sexo = input("Digite o novo sexo (M/F): ")
            while novo_sexo.upper() not in ["M", "F"]:
                novo_sexo = input("Sexo inválido. Por favor, digite M ou F: ")
            cliente_encontrado["Sexo"] = novo_sexo.upper()
            print(f"Sexo atualizado para: {novo_sexo.upper()}")
            input("\nPressione Enter para continuar...")
            
        elif opcao == "4":
            novo_telefone = int(input("Digite o novo telefone (9 dígitos): "))
            while len(str(novo_telefone)) != 9:
                novo_telefone = int(input("Telefone inválido. Por favor, digite um telefone com 9 dígitos: "))
            cliente_encontrado["Telefone"] = novo_telefone
            print(f"Telefone atualizado para: {novo_telefone}")
            input("\nPressione Enter para continuar...")
            
        elif opcao == "0":
            print("Alterações guardadas com sucesso!")
            input("\nPressione Enter para voltar ao menu...")
            return
        else:
            print("Opção inválida!")
            input("\nPressione Enter para tentar novamente...")

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
    data_hoje = datetime.now().date()
    limpar_tela()
    print("=" * 50)
    print("Marcar Consulta")
    print("=" * 50)
    
    if len(vetor_clientes) == 0:
        print("Nenhum cliente adicionado. Adicione um cliente primeiro.")
        input("\nPressione Enter para voltar ao menu...")
        return
    
    
    nome_cliente = input("Digite o nome do cliente: ")
    

    cliente_encontrado = None
    for cliente in vetor_clientes:
        if cliente["Nome"].lower() == nome_cliente.lower():
            cliente_encontrado = cliente
            break
    
    if cliente_encontrado == None:
        print(f"Cliente com nome '{nome_cliente}' não encontrado!")
        input("\nPressione Enter para voltar ao menu...")
        return
    
    print(f"\nCliente: {cliente_encontrado['Nome']}")
    
    
    print("\nConsultas disponíveis a marcar:")
    print("=" * 30)
    for i in range(len(vetor_consultas)):
        print(f"{i + 1}. {vetor_consultas[i]}")
    print("0-Sair")

    print("=" * 30)
    
    
    opcao_consulta = int(input("\nEscolha o número da consulta(0 a 6): "))
    
    while opcao_consulta < 0 or opcao_consulta > 6:
        print("Opção inválida!")
        opcao_consulta = int(input("\nEscolha o número da consulta(0 a 6): ")) 
        if opcao_consulta == 0:
            return
    
    consulta_escolhida = vetor_consultas[opcao_consulta - 1]
    
    data_valida = False
    while not data_valida:
        data_str = input("Digite a data da consulta(dd/m/aaaa): ")
        partes = data_str.split("/")
        
        if len(partes) == 3 and partes[0].isdigit() and partes[1].isdigit() and partes[2].isdigit():
            dia = int(partes[0])
            mes = int(partes[1])
            ano = int(partes[2])
            
            data_consulta = datetime(ano, mes, dia).date()
            if data_consulta >= data_hoje:
                data_valida = True
            else:
                print("Data inválida! Deve ser igual ou superior a hoje.")
        else:
            print("Formato inválido! Use dd/m/aaaa")
    
    marcacao = {
        "ID_Cliente": cliente_encontrado["ID"],
        "Nome_Cliente": cliente_encontrado["Nome"],
        "Tipo_Consulta": consulta_escolhida,
        "Data": data_str
    }
    
    vetor_marcacoes.append(marcacao)
    
    print(f"\nConsulta marcada com sucesso!")
    print(f"Tipo: {consulta_escolhida}")
    print(f"Data: {data_str}")
    print(f"Cliente: {cliente_encontrado['Nome']}")
    
    input("\nPressione Enter para voltar ao menu...")

def ver_marcacoes_consultas():
    limpar_tela()
    print("==================Consultas Marcadas==================")
    
    if len(vetor_marcacoes) == 0:
        print("Nenhuma consulta marcada.")
        input("\nPressione Enter para voltar ao menu...")
        return
    
    # tabela
    print("\n" + "=" * 90)
    print(f"{'ID':<5} {'Nome Cliente':<25} {'Tipo de Consulta':<20} {'Data':<15}")
    print("=" * 90)
    
    # Mostrar  marcação
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
    
    
    while True:
        id_cliente = input("Digite o ID do cliente a pesquisar: ")
        
        if id_cliente.isdigit():
            id_cliente = int(id_cliente)
            break 
        else:
            print("Erro: Por favor, digite apenas números.")

        
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
    
    
    total_clientes = 0
    soma = 0
    idade_minima = None
    idade_maxima = None
    clientes_masculinos = 0
    clientes_femininos = 0

    for cliente in vetor_clientes:
        idade = cliente["Idade"]
        sexo = cliente["Sexo"].upper()

        soma += idade
        total_clientes += 1

        if idade_minima is None or idade < idade_minima:
            idade_minima = idade
        if idade_maxima is None or idade > idade_maxima:
            idade_maxima = idade

        if sexo == "M":
            clientes_masculinos += 1
        elif sexo == "F":
            clientes_femininos += 1

    media_idade = soma / total_clientes if total_clientes > 0 else 0

    print(f"Total de clientes: {total_clientes}")
    print(f"Soma das idades dos clientes: {soma} anos")
    print(f"Idade média dos clientes: {media_idade:.2f} anos")
    print(f"Idade mínima dos clientes: {idade_minima} anos")
    print(f"Idade máxima dos clientes: {idade_maxima} anos")
    print(f"Clientes do sexo masculino: {clientes_masculinos}")
    print(f"Clientes do sexo feminino: {clientes_femininos}")
    
    lista_crescente = [cliente.copy() for cliente in vetor_clientes]
    ordenacao_selecao(lista_crescente, "Idade", crescente=True)
    
    print("\n" + "="*50)
    print("CLIENTES ORDENADOS POR IDADE (CRESCENTE):")
    print("="*50)
    print(f"{'ID':<5} {'Nome':<25} {'Idade':<8}")
    print("="*50)
    for cliente in lista_crescente:
        print(f"{cliente['ID']:<5} {cliente['Nome']:<25} {cliente['Idade']:<8}")
    print("="*50)
    
    lista_decrescente = [cliente.copy() for cliente in vetor_clientes]
    ordenacao_selecao(lista_decrescente, "Idade", crescente=False)
    
    print("\n" + "="*50)
    print("CLIENTES ORDENADOS POR IDADE (DECRESCENTE):")
    print("="*50)
    print(f"{'ID':<5} {'Nome':<25} {'Idade':<8}")
    print("="*50)
    for cliente in lista_decrescente:
        print(f"{cliente['ID']:<5} {cliente['Nome']:<25} {cliente['Idade']:<8}")
    print("="*50)
    
    input("\nPressione Enter para voltar ao menu...")

def filtrar_clientes():
    limpar_tela()
    print("="*50)
    print("Filtrar Clientes por Categoria")
    print("="*50)
    
    if len(vetor_clientes) == 0:
        print("Nenhum cliente adicionado.")
        input("\nPressione Enter para voltar ao menu...")
        return
    
    print("\n1. Filtrar por Sexo")
    print("2. Filtrar por Faixa Etária")
    print("3. Filtrar por Idade Exata")
    print("0. Voltar")
    
    opcao = input("\nEscolha uma opção (0-3): ")
    
    clientes_filtrados = []
    titulo_filtro = ""
    
    if opcao == "1":
        sexo = input("Digite o sexo a filtrar (M/F): ").upper()
        while sexo not in ["M", "F"]:
            sexo = input("Sexo inválido! Digite M ou F: ").upper()
        
        for cliente in vetor_clientes:
            if cliente["Sexo"].upper() == sexo:
                clientes_filtrados.append(cliente)
        
        titulo_filtro = f"Sexo: {sexo}"
    
    elif opcao == "2":
        idade_min = int(input("Digite a idade mínima: "))
        idade_max = int(input("Digite a idade máxima: "))
        
        for cliente in vetor_clientes:
            if cliente["Idade"] >= idade_min and cliente["Idade"] <= idade_max:
                clientes_filtrados.append(cliente)
        
        titulo_filtro = f"Faixa Etária: {idade_min} a {idade_max} anos"
    
    elif opcao == "3":
        idade = int(input("Digite a idade: "))
        for cliente in vetor_clientes:
            if cliente["Idade"] == idade:
                clientes_filtrados.append(cliente)
        
        titulo_filtro = f"Idade: {idade} anos"
    
    elif opcao == "0":
        return
    else:
        print("Opção inválida!")
        input("\nPressione Enter para voltar ao menu...")
        return
    
    if len(clientes_filtrados) == 0:
        print(f"\nNenhum cliente encontrado com o filtro: {titulo_filtro}")
    else:
        limpar_tela()
        print(f"\nClientes Filtrados - {titulo_filtro}")
        print("=" * 70)
        print(f"{'ID':<5} {'Nome':<25} {'Idade':<8} {'Sexo':<5} {'Telefone':<15}")
        print("=" * 70)
        
        for cliente in clientes_filtrados:
            print(f"{cliente['ID']:<5} {cliente['Nome']:<25} {cliente['Idade']:<8} {cliente['Sexo']:<5} {cliente['Telefone']:<15}")
        
        print("=" * 70)
        print(f"Total encontrado: {len(clientes_filtrados)} cliente(s)")
    
    input("\nPressione Enter para voltar ao menu...")

def eliminar_cliente():
    limpar_tela()
    print("="*50)
    print("Eliminar Cliente")
    print("="*50)
    
    if len(vetor_clientes) == 0:
        print("Nenhum cliente adicionado.")
        input("\nPressione Enter para voltar ao menu...")
        return
    
    print("\n1. Procurar por ID")
    print("2. Procurar por Nome")
    opcao_busca = input("Escolha como procurar (1 ou 2): ")
    
    cliente_encontrado = None
    indice_cliente = -1
    
    if opcao_busca == "1":
        id_cliente = int(input("Digite o ID do cliente a eliminar: "))
        
        for i in range(len(vetor_clientes)):
            if vetor_clientes[i]["ID"] == id_cliente:
                cliente_encontrado = vetor_clientes[i]
                indice_cliente = i
                break
        
        if cliente_encontrado == None:
            print(f"Cliente com ID {id_cliente} não encontrado!")
            input("\nPressione Enter para voltar ao menu...")
            return
    
    elif opcao_busca == "2":
        nome_cliente = input("Digite o nome do cliente a eliminar: ")
        clientes_encontrados = []
        
        for i in range(len(vetor_clientes)):
            if nome_cliente.lower() in vetor_clientes[i]["Nome"].lower():
                clientes_encontrados.append(i)
        
        if len(clientes_encontrados) == 0:
            print(f"Nenhum cliente com o nome '{nome_cliente}' encontrado!")
            input("\nPressione Enter para voltar ao menu...")
            return
        
        if len(clientes_encontrados) == 1:
            indice_cliente = clientes_encontrados[0]
            cliente_encontrado = vetor_clientes[indice_cliente]
        else:
            print("\nVários clientes encontrados:")
            for j in range(len(clientes_encontrados)):
                idx = clientes_encontrados[j]
                print(f"{j + 1}. ID: {vetor_clientes[idx]['ID']} - Nome: {vetor_clientes[idx]['Nome']}")
            
            escolha = int(input("Escolha qual cliente eliminar (número): "))
            while escolha < 1 or escolha > len(clientes_encontrados):
                escolha = int(input("Opção inválida! Tente novamente: "))
            
            indice_cliente = clientes_encontrados[escolha - 1]
            cliente_encontrado = vetor_clientes[indice_cliente]
    else:
        print("Opção inválida!")
        input("\nPressione Enter para voltar ao menu...")
        return
    
    print("\n" + "="*50)
    print(f"Tem certeza que deseja eliminar?")
    print(f"ID:      {cliente_encontrado['ID']}")
    print(f"Nome:    {cliente_encontrado['Nome']}")
    print(f"Idade:   {cliente_encontrado['Idade']}")
    print(f"Sexo:    {cliente_encontrado['Sexo']}")
    print(f"Telefone:{cliente_encontrado['Telefone']}")
    print("="*50)
    
    confirmacao = input("\nDigite 'SIM' para confirmar a eliminação: ").upper()
    
    if confirmacao == "SIM":
        id_eliminado = cliente_encontrado["ID"]
        del vetor_clientes[indice_cliente]
        
        for i in range(len(vetor_marcacoes) - 1, -1, -1):
            if vetor_marcacoes[i]["ID_Cliente"] == id_eliminado:
                del vetor_marcacoes[i]
        
        print(f"\nCliente '{cliente_encontrado['Nome']}' eliminado com sucesso!")
    else:
        print("\nEliminação cancelada.")
    
    input("\nPressione Enter para voltar ao menu...")

def exportar_dados():
    limpar_tela()
    print("="*50)
    print("Exportar Dados para Ficheiro .txt")
    print("="*50)
    
    if len(vetor_clientes) == 0:
        print("Nenhum cliente adicionado. Nada a exportar.")
        input("\nPressione Enter para voltar ao menu...")
        return
    
    nome_ficheiro = input("\nDigite o nome do ficheiro (sem .txt): ")
    if len(nome_ficheiro) == 0:
        nome_ficheiro = "clientes_exportado"
    
    nome_ficheiro = nome_ficheiro + ".txt"
    
    ficheiro = open(nome_ficheiro, "w")
    
    ficheiro.write("="*70 + "\n")
    ficheiro.write("SISTEMA DE GESTAO HOSPITALAR - EXPORTACAO DE DADOS\n")
    ficheiro.write("="*70 + "\n\n")
    
    ficheiro.write("CLIENTES REGISTADOS\n")
    ficheiro.write("-" * 70 + "\n\n")
    
    for cliente in vetor_clientes:
        ficheiro.write(f"ID: {cliente['ID']}\n")
        ficheiro.write(f"Nome: {cliente['Nome']}\n")
        ficheiro.write(f"Idade: {cliente['Idade']} anos\n")
        ficheiro.write(f"Sexo: {cliente['Sexo']}\n")
        ficheiro.write(f"Telefone: {cliente['Telefone']}\n")
        ficheiro.write("-" * 70 + "\n\n")
    
    ficheiro.write("\n" + "="*70 + "\n")
    ficheiro.write("CONSULTAS MARCADAS\n")
    ficheiro.write("="*70 + "\n\n")
    
    if len(vetor_marcacoes) == 0:
        ficheiro.write("Nenhuma consulta marcada.\n")
    else:
        for marcacao in vetor_marcacoes:
            ficheiro.write(f"Cliente: {marcacao['Nome_Cliente']} (ID: {marcacao['ID_Cliente']})\n")
            ficheiro.write(f"Tipo de Consulta: {marcacao['Tipo_Consulta']}\n")
            ficheiro.write(f"Data: {marcacao['Data']}\n")
            ficheiro.write("-" * 70 + "\n\n")
    
    ficheiro.close()
    
    print(f"\nDados exportados com sucesso para o ficheiro: {nome_ficheiro}")
    input("\nPressione Enter para voltar ao menu...")


def ordenacao_selecao(lista, campo, crescente=True):
    
    for i in range(len(lista) - 1):
        indice_ordenador = i
        
        
        for j in range(i + 1, len(lista)):
            if crescente:
                
                if lista[j][campo] < lista[indice_ordenador][campo]:
                    indice_ordenador = j
            else:
            
                if lista[j][campo] > lista[indice_ordenador][campo]:
                    indice_ordenador = j

        lista[i], lista[indice_ordenador] = lista[indice_ordenador], lista[i]

#Prog principal 

while True:
    menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        clientes()
    elif opcao == "2":
        editar_cliente()
    elif opcao == "3":
        ver_clientes()
    elif opcao == "4":
        marcar_consulta()
    elif opcao == "5":
        ver_marcacoes_consultas()
    elif opcao == "6":
        pesquisar_cliente_por_id()
    elif opcao == "7":
        estat_clientes()
    elif opcao == "8":
        filtrar_clientes()
    elif opcao == "9":
        eliminar_cliente()
    elif opcao == "10":
        exportar_dados()
    elif opcao == "0":
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")