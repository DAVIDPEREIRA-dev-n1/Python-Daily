# Algoritmo de Pesquisa de Clientes
# Pesquisa por ID, Nome ou Código (NIF)

import os

# Base de dados de clientes
clientes = [
    {"ID": 1, "Nome": "João Silva", "Idade": 45, "NIF": "123456789", "Morada": "Rua A, nº 10", "Telefone": "961234567"},
    {"ID": 2, "Nome": "Maria Santos", "Idade": 38, "NIF": "987654321", "Morada": "Rua B, nº 20", "Telefone": "962345678"},
    {"ID": 3, "Nome": "Pedro Costa", "Idade": 52, "NIF": "456789123", "Morada": "Rua C, nº 30", "Telefone": "963456789"},
    {"ID": 4, "Nome": "Ana Ferreira", "Idade": 41, "NIF": "789123456", "Morada": "Rua D, nº 40", "Telefone": "964567890"},
    {"ID": 5, "Nome": "Carlos Oliveira", "Idade": 35, "NIF": "321654987", "Morada": "Rua E, nº 50", "Telefone": "965678901"},
]

def limpar_tela():
    """Limpa a tela do console"""
    os.system('cls' if os.name == 'nt' else 'clear')

def pesquisa_por_id(id_cliente):
    """
    Pesquisa cliente por ID
    Argumentos: id_cliente (int)
    Retorna: dicionário do cliente ou None
    """
    for cliente in clientes:
        if cliente["ID"] == id_cliente:
            return cliente
    return None

def pesquisa_por_nome(nome):
    """
    Pesquisa cliente por Nome (pesquisa parcial)
    Argumentos: nome (str)
    Retorna: lista de clientes encontrados
    """
    resultados = []
    nome_normalizado = nome.lower().strip()
    
    for cliente in clientes:
        if nome_normalizado in cliente["Nome"].lower():
            resultados.append(cliente)
    
    return resultados

def pesquisa_por_nif(nif):
    """
    Pesquisa cliente por NIF (Código)
    Argumentos: nif (str)
    Retorna: dicionário do cliente ou None
    """
    nif_normalizado = nif.strip()
    
    for cliente in clientes:
        if cliente["NIF"] == nif_normalizado:
            return cliente
    return None

def pesquisa_binaria_por_id(id_cliente):
    """
    Pesquisa binária por ID (mais eficiente para grandes listas ordenadas)
    Argumentos: id_cliente (int)
    Retorna: dicionário do cliente ou None
    """
    esquerda = 0
    direita = len(clientes) - 1
    
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        
        if clientes[meio]["ID"] == id_cliente:
            return clientes[meio]
        elif clientes[meio]["ID"] < id_cliente:
            esquerda = meio + 1
        else:
            direita = meio - 1
    
    return None

def exibir_cliente(cliente):
    """Exibe os dados de um cliente de forma formatada"""
    print("\n" + "="*50)
    print(f"ID:       {cliente['ID']}")
    print(f"Nome:     {cliente['Nome']}")
    print(f"Idade:    {cliente['Idade']}")
    print(f"NIF:      {cliente['NIF']}")
    print(f"Morada:   {cliente['Morada']}")
    print(f"Telefone: {cliente['Telefone']}")
    print("="*50)

def menu_pesquisa():
    """Menu principal de pesquisa"""
    while True:
        limpar_tela()
        print("\n" + "="*50)
        print("   SISTEMA DE PESQUISA DE CLIENTES")
        print("="*50)
        print("5. Pesquisar por ID")
        print("0. Sair")
        print("="*50)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "5":
            limpar_tela()
            print("\n--- PESQUISA POR ID ---")
            try:
                id_cliente = int(input("Digite o ID do cliente: "))
                resultado = pesquisa_por_id(id_cliente)
                
                if resultado:
                    print("\n✓ Cliente encontrado!")
                    exibir_cliente(resultado)
                else:
                    print(f"\n✗ Cliente com ID {id_cliente} não encontrado!")
            except ValueError:
                print("\n✗ Erro: O ID deve ser um número inteiro!")
            
            input("\nPressione Enter para continuar...")
        
        elif opcao == "0":
            limpar_tela()
            print("\nAté à próxima!")
            break
        
        else:
            print("\n✗ Opção inválida! Tente novamente.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    menu_pesquisa()
