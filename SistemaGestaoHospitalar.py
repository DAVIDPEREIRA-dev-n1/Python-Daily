# ========================================
# SISTEMA DE GESTÃO HOSPITALAR
# ========================================
# Programa educativo para gerenciamento de clientes hospitais
# Desenvolvido para Aula PSI - 10º Ano

# Códigos ANSI para cores
COR_VERDE = '\033[92m'
COR_VERMELHO = '\033[91m'
COR_AMARELO = '\033[93m'
COR_AZUL = '\033[94m'
COR_RESET = '\033[0m'

# Estrutura de dados principal
hospital = {
    "clientes": [],
    "consultas": [
        "Cardiologia",
        "Ortopedia",
        "Pediatria",
        "Oftalmologia",
        "Dermatologia",
        "Neurologia",
        "Psicologia",
        "Oncologia"
    ],
    "marcacoes_consultas": []
}

# Variável global para ID automático
proxima_id = 1


# ========================================
# FUNÇÕES AUXILIARES
# ========================================

def limpar_tela():
    """Limpa a tela do terminal"""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def pausa():
    """Pausa a execução até o utilizador pressionar Enter"""
    input("\nPressione ENTER para continuar...")


def separador(char="=", tamanho=50):
    """Imprime uma linha separadora"""
    print(char * tamanho)


def titulo(texto):
    """Imprime um título formatado"""
    separador()
    print(f" {texto.center(48)}")
    separador()


def validar_inteiro(mensagem, minimo=None, maximo=None):
    """
    Valida entrada de números inteiros
    
    Args:
        mensagem: texto a mostrar
        minimo: valor mínimo aceito (opcional)
        maximo: valor máximo aceito (opcional)
    
    Returns:
        int: número validado
    """
    while True:
        try:
            valor = int(input(mensagem))
            
            if minimo is not None and valor < minimo:
                print(f"❌ Erro: Valor mínimo é {minimo}")
                continue
            
            if maximo is not None and valor > maximo:
                print(f"❌ Erro: Valor máximo é {maximo}")
                continue
            
            return valor
        
        except ValueError:
            print("❌ Erro: Digite apenas números inteiros!")


def validar_string(mensagem, minimo_caracteres=1):
    """
    Valida entrada de texto
    
    Args:
        mensagem: texto a mostrar
        minimo_caracteres: mínimo de caracteres
    
    Returns:
        str: texto validado
    """
    while True:
        valor = input(mensagem).strip()
        
        if len(valor) < minimo_caracteres:
            print(f"❌ Erro: Mínimo {minimo_caracteres} caractere(s)")
            continue
        
        return valor


# ========================================
# FUNÇÕES DE GESTÃO DE CLIENTES
# ========================================

def obter_proximo_id():
    """Retorna e incrementa o ID automático"""
    global proxima_id
    id_atual = proxima_id
    proxima_id += 1
    return id_atual


def cadastrar_cliente():
    """Cadastra um novo cliente no hospital"""
    titulo("CADASTRAR NOVO CLIENTE")
    
    try:
        # Recolher dados
        nome = validar_string("Nome do cliente: ")
        idade = validar_inteiro("Idade: ", minimo=0, maximo=150)
        morada = input("Morada (opcional, pressione ENTER): ").strip()
        
        # Criar dicionário do cliente
        cliente = {
            "id": obter_proximo_id(),
            "nome": nome.title(),
            "idade": idade,
            "morada": morada if morada else "Não registada",
            "doenças": [],
            "observacoes": [] 
        }
        
        hospital["clientes"].append(cliente)
        print(f"\n{COR_VERDE}✅ Cliente '{cliente['nome']}' cadastrado com sucesso!{COR_RESET}")
        print(f"   ID atribuído: {cliente['id']}")
        
    except Exception as e:
        print(f"{COR_VERMELHO}❌ Erro ao cadastrar cliente: {e}{COR_RESET}")
    
    pausa()


def ver_clientes():
    """Mostra tabela de todos os clientes"""
    titulo("LISTA DE CLIENTES")
    
    if not hospital["clientes"]:
        print(f"\n{COR_VERMELHO}❌ Nenhum cliente registado{COR_RESET}\n")
        pausa()
        return
    
    # Imprimir cabeçalho da tabela
    print(f"\n{'ID':>5} {'Nome':<25} {'Idade':>8} {'Morada':<20}")
    separador("-", 60)
    
    # Imprimir cada cliente
    for cliente in hospital["clientes"]:
        morada = cliente["morada"][:17] + "..." if len(cliente["morada"]) > 20 else cliente["morada"]
        print(f"{cliente['id']:>5} {cliente['nome']:<25} {cliente['idade']:>8} {morada:<20}")
    
    print(f"\nTotal de clientes: {len(hospital['clientes'])}\n")
    pausa()


def adicionar_doenca():
    """Adiciona doença ao histórico de um cliente"""
    titulo("ADICIONAR DOENÇA")
    
    if not hospital["clientes"]:
        print(f"{COR_VERMELHO}❌ Nenhum cliente registado{COR_RESET}")
        pausa()
        return
    
    cliente_id = validar_inteiro("ID do cliente: ")
    cliente = procurar_cliente_por_id(cliente_id)
    
    if not cliente:
        print(f"{COR_VERMELHO}❌ Cliente não encontrado{COR_RESET}")
        pausa()
        return
    
    doenca = validar_string("Nome da doença: ")
    cliente["doenças"].append(doenca.title())
    print(f"{COR_VERDE}✅ Doença '{doenca}' adicionada ao cliente {cliente['nome']}{COR_RESET}")
    pausa()


def adicionar_observacao():
    """Adiciona observação médica a um cliente"""
    titulo("ADICIONAR OBSERVAÇÃO MÉDICA")
    
    if not hospital["clientes"]:
        print(f"{COR_VERMELHO}❌ Nenhum cliente registado{COR_RESET}")
        pausa()
        return
    
    cliente_id = validar_inteiro("ID do cliente: ")
    cliente = procurar_cliente_por_id(cliente_id)
    
    if not cliente:
        print(f"{COR_VERMELHO}❌ Cliente não encontrado{COR_RESET}")
        pausa()
        return
    
    observacao = validar_string("Observação médica: ")
    cliente["observacoes"].append(observacao)
    print(f"{COR_VERDE}✅ Observação adicionada ao cliente {cliente['nome']}{COR_RESET}")
    pausa()


# ========================================
# FUNÇÕES DE PESQUISA
# ========================================

def procurar_cliente_por_id(cliente_id):
    """Procura cliente pelo ID"""
    for cliente in hospital["clientes"]:
        if cliente["id"] == cliente_id:
            return cliente
    return None


def procurar_cliente_por_nome(nome_parcial):
    """Procura clientes pelo nome (pesquisa parcial)"""
    resultados = []
    nome_lower = nome_parcial.lower()
    
    for cliente in hospital["clientes"]:
        if nome_lower in cliente["nome"].lower():
            resultados.append(cliente)
    
    return resultados


def pesquisar_cliente():
    """Pesquisa cliente por nome ou ID"""
    titulo("PESQUISAR CLIENTE")
    
    if not hospital["clientes"]:
        print(f"{COR_VERMELHO}❌ Nenhum cliente registado{COR_RESET}")
        pausa()
        return
    
    print("\n1. Pesquisar por ID")
    print("2. Pesquisar por Nome")
    opcao = validar_inteiro("Escolha uma opção (1-2): ", minimo=1, maximo=2)
    
    if opcao == 1:
        cliente_id = validar_inteiro("ID do cliente: ")
        cliente = procurar_cliente_por_id(cliente_id)
        
        if cliente:
            mostrar_detalhes_cliente(cliente)
        else:
            print(f"{COR_VERMELHO}❌ Cliente não encontrado{COR_RESET}")
    
    else:
        nome = validar_string("Nome (parcial) do cliente: ")
        resultados = procurar_cliente_por_nome(nome)
        
        if resultados:
            print(f"\n{COR_VERDE}✅ {len(resultados)} cliente(s) encontrado(s):{COR_RESET}\n")
            for cliente in resultados:
                mostrar_detalhes_cliente(cliente)
        else:
            print(f"{COR_VERMELHO}❌ Nenhum cliente encontrado com esse nome{COR_RESET}")
    
    pausa()


def mostrar_detalhes_cliente(cliente):
    """Mostra informações detalhadas de um cliente"""
    separador("-", 50)
    print(f"ID: {cliente['id']}")
    print(f"Nome: {cliente['nome']}")
    print(f"Idade: {cliente['idade']} anos")
    print(f"Morada: {cliente['morada']}")
    
    print(f"\nDoenças registadas: ", end="")
    if cliente["doenças"]:
        print(", ".join(cliente["doenças"]))
    else:
        print("Nenhuma")
    
    print(f"Observações médicas: ")
    if cliente["observacoes"]:
        for i, obs in enumerate(cliente["observacoes"], 1):
            print(f"  {i}. {obs}")
    else:
        print("  Nenhuma")
    separador("-", 50)


# ========================================
# FUNÇÕES DE CONSULTAS
# ========================================

def ver_consultas_disponiveis():
    """Mostra consultas disponíveis"""
    titulo("CONSULTAS DISPONÍVEIS")
    
    print("\nConsultas disponíveis:\n")
    for i, consulta in enumerate(hospital["consultas"], 1):
        print(f"  {i}. {consulta}")
    
    pausa()


def criar_consulta():
    """Cria uma consulta para um cliente"""
    titulo("MARCAR CONSULTA")
    
    if not hospital["clientes"]:
        print(f"{COR_VERMELHO}❌ Nenhum cliente registado{COR_RESET}")
        pausa()
        return
    
    cliente_id = validar_inteiro("ID do cliente: ")
    cliente = procurar_cliente_por_id(cliente_id)
    
    if not cliente:
        print(f"{COR_VERMELHO}❌ Cliente não encontrado{COR_RESET}")
        pausa()
        return
    
    print(f"\nCliente: {cliente['nome']}\n")
    print("Consultas disponíveis:")
    for i, consulta in enumerate(hospital["consultas"], 1):
        print(f"  {i}. {consulta}")
    
    opcao = validar_inteiro("\nEscolha a consulta (número): ", 
                           minimo=1, maximo=len(hospital["consultas"]))
    
    consulta_escolhida = hospital["consultas"][opcao - 1]
    data = validar_string("Data da consulta (ex: 15/12/2024): ")
    
    marcacao = {
        "id_cliente": cliente_id,
        "nome_cliente": cliente["nome"],
        "consulta": consulta_escolhida,
        "data": data
    }
    
    hospital["marcacoes_consultas"].append(marcacao)
    print(f"{COR_VERDE}✅ Consulta de {consulta_escolhida} marcada para {cliente['nome']}{COR_RESET}")
    pausa()


# ========================================
# FUNÇÕES DE ESTATÍSTICAS
# ========================================

def calcular_estatisticas():
    """Calcula e mostra estatísticas dos clientes"""
    titulo("ESTATÍSTICAS")
    
    if not hospital["clientes"]:
        print(f"{COR_VERMELHO}❌ Nenhum cliente registado{COR_RESET}")
        pausa()
        return
    
    idades = [cliente["idade"] for cliente in hospital["clientes"]]
    
    media_idade = sum(idades) / len(idades)
    idade_maxima = max(idades)
    idade_minima = min(idades)
    
    cliente_mais_velho = None
    cliente_mais_novo = None
    
    for cliente in hospital["clientes"]:
        if cliente["idade"] == idade_maxima:
            cliente_mais_velho = cliente
        if cliente["idade"] == idade_minima:
            cliente_mais_novo = cliente
    
    print(f"\nTotal de clientes: {len(hospital['clientes'])}")
    print(f"Média de idades: {media_idade:.2f} anos")
    print(f"Idade máxima: {idade_maxima} anos")
    print(f"Idade mínima: {idade_minima} anos")
    
    print(f"\nCliente mais velho: {cliente_mais_velho['nome']} ({idade_maxima} anos)")
    print(f"Cliente mais novo: {cliente_mais_novo['nome']} ({idade_minima} anos)")
    
    print(f"\nTotal de consultas marcadas: {len(hospital['marcacoes_consultas'])}")
    
    pausa()


# ========================================
# FUNÇÕES DE ORDENAÇÃO (SELECTION SORT)
# ========================================

def selection_sort_crescente(lista, chave="idade"):
    """
    Selection Sort em ordem crescente
    
    Args:
        lista: lista de clientes
        chave: campo a ordenar ('idade' ou 'nome')
    
    Returns:
        list: lista ordenada
    """
    lista_copia = lista.copy()
    n = len(lista_copia)
    
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if chave == "idade":
                if lista_copia[j]["idade"] < lista_copia[indice_minimo]["idade"]:
                    indice_minimo = j
            else:  # nome
                if lista_copia[j]["nome"] < lista_copia[indice_minimo]["nome"]:
                    indice_minimo = j
        
        # Trocar elementos
        lista_copia[i], lista_copia[indice_minimo] = lista_copia[indice_minimo], lista_copia[i]
    
    return lista_copia


def selection_sort_decrescente(lista, chave="idade"):
    """
    Selection Sort em ordem decrescente
    
    Args:
        lista: lista de clientes
        chave: campo a ordenar ('idade' ou 'nome')
    
    Returns:
        list: lista ordenada
    """
    lista_copia = lista.copy()
    n = len(lista_copia)
    
    for i in range(n):
        indice_maximo = i
        for j in range(i + 1, n):
            if chave == "idade":
                if lista_copia[j]["idade"] > lista_copia[indice_maximo]["idade"]:
                    indice_maximo = j
            else:  # nome
                if lista_copia[j]["nome"] > lista_copia[indice_maximo]["nome"]:
                    indice_maximo = j
        
        # Trocar elementos
        lista_copia[i], lista_copia[indice_maximo] = lista_copia[indice_maximo], lista_copia[i]
    
    return lista_copia


def ordenar_clientes():
    """Menu para ordenar clientes"""
    titulo("ORDENAR CLIENTES")
    
    if not hospital["clientes"]:
        print(f"{COR_VERMELHO}❌ Nenhum cliente registado{COR_RESET}")
        pausa()
        return
    
    print("\n1. Ordenar por Idade (Crescente)")
    print("2. Ordenar por Idade (Decrescente)")
    print("3. Ordenar por Nome (A-Z)")
    print("4. Ordenar por Nome (Z-A)")
    
    opcao = validar_inteiro("\nEscolha uma opção (1-4): ", minimo=1, maximo=4)
    
    if opcao == 1:
        clientes_ordenados = selection_sort_crescente(hospital["clientes"], "idade")
        titulo("CLIENTES - ORDENADO POR IDADE (CRESCENTE)")
    elif opcao == 2:
        clientes_ordenados = selection_sort_decrescente(hospital["clientes"], "idade")
        titulo("CLIENTES - ORDENADO POR IDADE (DECRESCENTE)")
    elif opcao == 3:
        clientes_ordenados = selection_sort_crescente(hospital["clientes"], "nome")
        titulo("CLIENTES - ORDENADO POR NOME (A-Z)")
    else:
        clientes_ordenados = selection_sort_decrescente(hospital["clientes"], "nome")
        titulo("CLIENTES - ORDENADO POR NOME (Z-A)")
    
    # Mostrar tabela ordenada
    print(f"\n{'ID':>5} {'Nome':<25} {'Idade':>8} {'Morada':<20}")
    separador("-", 60)
    
    for cliente in clientes_ordenados:
        morada = cliente["morada"][:17] + "..." if len(cliente["morada"]) > 20 else cliente["morada"]
        print(f"{cliente['id']:>5} {cliente['nome']:<25} {cliente['idade']:>8} {morada:<20}")
    
    print()
    pausa()


# ========================================
# FUNÇÕES DE EDIÇÃO
# ========================================

def editar_cliente():
    """Edita dados de um cliente existente"""
    titulo("EDITAR DADOS DO CLIENTE")
    
    if not hospital["clientes"]:
        print(f"{COR_VERMELHO}❌ Nenhum cliente registado{COR_RESET}")
        pausa()
        return
    
    cliente_id = validar_inteiro("ID do cliente a editar: ")
    cliente = procurar_cliente_por_id(cliente_id)
    
    if not cliente:
        print(f"{COR_VERMELHO}❌ Cliente não encontrado{COR_RESET}")
        pausa()
        return
    
    print(f"\nEditar cliente: {cliente['nome']}")
    print("\n1. Editar Nome")
    print("2. Editar Idade")
    print("3. Editar Morada")
    print("4. Cancelar")
    
    opcao = validar_inteiro("\nEscolha uma opção (1-4): ", minimo=1, maximo=4)
    
    if opcao == 1:
        novo_nome = validar_string("Novo nome: ")
        cliente["nome"] = novo_nome.title()
        print(f"{COR_VERDE}✅ Nome alterado com sucesso!{COR_RESET}")
    
    elif opcao == 2:
        nova_idade = validar_inteiro("Nova idade: ", minimo=0, maximo=150)
        cliente["idade"] = nova_idade
        print(f"{COR_VERDE}✅ Idade alterada com sucesso!{COR_RESET}")
    
    elif opcao == 3:
        nova_morada = validar_string("Nova morada: ")
        cliente["morada"] = nova_morada
        print(f"{COR_VERDE}✅ Morada alterada com sucesso!{COR_RESET}")
    
    elif opcao == 4:
        print(f"{COR_AMARELO}⚠️  Edição cancelada{COR_RESET}")
    
    pausa()


# ========================================
# FUNÇÕES DE EXPORTAÇÃO
# ========================================

def exportar_dados():
    """Exporta dados para ficheiro .txt"""
    titulo("EXPORTAR DADOS")
    
    if not hospital["clientes"]:
        print(f"{COR_VERMELHO}❌ Nenhum cliente registado para exportar{COR_RESET}")
        pausa()
        return
    
    try:
        nome_ficheiro = "relatorio_hospital.txt"
        
        with open(nome_ficheiro, "w", encoding="utf-8") as ficheiro:
            ficheiro.write("=" * 70 + "\n")
            ficheiro.write("RELATÓRIO - SISTEMA DE GESTÃO HOSPITALAR\n")
            ficheiro.write("=" * 70 + "\n\n")
            
            # Seção de clientes
            ficheiro.write("CLIENTES REGISTADOS\n")
            ficheiro.write("-" * 70 + "\n")
            for cliente in hospital["clientes"]:
                ficheiro.write(f"\nID: {cliente['id']}\n")
                ficheiro.write(f"Nome: {cliente['nome']}\n")
                ficheiro.write(f"Idade: {cliente['idade']} anos\n")
                ficheiro.write(f"Morada: {cliente['morada']}\n")
                ficheiro.write(f"Doenças: {', '.join(cliente['doenças']) if cliente['doenças'] else 'Nenhuma'}\n")
                ficheiro.write(f"Observações: {len(cliente['observacoes'])} registos\n")
                if cliente["observacoes"]:
                    for i, obs in enumerate(cliente["observacoes"], 1):
                        ficheiro.write(f"  {i}. {obs}\n")
                ficheiro.write("-" * 70 + "\n")
            
            # Seção de consultas marcadas
            ficheiro.write("\n\nCONSULTAS MARCADAS\n")
            ficheiro.write("-" * 70 + "\n")
            if hospital["marcacoes_consultas"]:
                for marcacao in hospital["marcacoes_consultas"]:
                    ficheiro.write(f"Cliente: {marcacao['nome_cliente']}\n")
                    ficheiro.write(f"Consulta: {marcacao['consulta']}\n")
                    ficheiro.write(f"Data: {marcacao['data']}\n")
                    ficheiro.write("-" * 70 + "\n")
            else:
                ficheiro.write("Nenhuma consulta marcada\n")
            
            # Seção de estatísticas
            ficheiro.write("\n\nESTATÍSTICAS\n")
            ficheiro.write("-" * 70 + "\n")
            if hospital["clientes"]:
                idades = [c["idade"] for c in hospital["clientes"]]
                media = sum(idades) / len(idades)
                ficheiro.write(f"Total de clientes: {len(hospital['clientes'])}\n")
                ficheiro.write(f"Média de idades: {media:.2f} anos\n")
                ficheiro.write(f"Idade máxima: {max(idades)} anos\n")
                ficheiro.write(f"Idade mínima: {min(idades)} anos\n")
                ficheiro.write(f"Total de consultas marcadas: {len(hospital['marcacoes_consultas'])}\n")
            
            ficheiro.write("\n" + "=" * 70 + "\n")
        
        print(f"{COR_VERDE}✅ Dados exportados com sucesso para '{nome_ficheiro}'{COR_RESET}")
    
    except Exception as e:
        print(f"{COR_VERMELHO}❌ Erro ao exportar dados: {e}{COR_RESET}")
    
    pausa()


# ========================================
# MENU PRINCIPAL
# ========================================

def menu_principal():
    """Exibe e gerencia o menu principal"""
    while True:
        limpar_tela()
        titulo("SISTEMA DE GESTÃO HOSPITALAR")
        
        print("\n1. Cadastrar cliente")
        print("2. Ver clientes")
        print("3. Editar cliente")
        print("4. Consultas disponíveis")
        print("5. Marcar consulta")
        print("6. Adicionar observações médicas")
        print("7. Pesquisar cliente")
        print("8. Estatísticas")
        print("9. Ordenar clientes (Selection Sort)")
        print("10. Exportar dados (ficheiro .txt)")
        print("11. Sair")
        
        print()
        opcao = validar_inteiro("Escolha uma opção (1-11): ", minimo=1, maximo=11)
        
        if opcao == 1:
            limpar_tela()
            cadastrar_cliente()
        
        elif opcao == 2:
            limpar_tela()
            ver_clientes()
        
        elif opcao == 3:
            limpar_tela()
            editar_cliente()
        
        elif opcao == 4:
            limpar_tela()
            ver_consultas_disponiveis()
        
        elif opcao == 5:
            limpar_tela()
            criar_consulta()
        
        elif opcao == 6:
            limpar_tela()
            print("1. Adicionar doença")
            print("2. Adicionar observação médica")
            sub_opcao = validar_inteiro("Escolha uma opção (1-2): ", minimo=1, maximo=2)
            limpar_tela()
            if sub_opcao == 1:
                adicionar_doenca()
            else:
                adicionar_observacao()
        
        elif opcao == 7:
            limpar_tela()
            pesquisar_cliente()
        
        elif opcao == 8:
            limpar_tela()
            calcular_estatisticas()
        
        elif opcao == 9:
            limpar_tela()
            ordenar_clientes()
        
        elif opcao == 10:
            limpar_tela()
            exportar_dados()
        
        elif opcao == 11:
            limpar_tela()
            titulo("FIM DO PROGRAMA")
            print(f"\n{COR_VERDE}✅ Obrigado por usar o Sistema de Gestão Hospitalar!{COR_RESET}")
            print("   Até à próxima!\n")
            break


# ========================================
# PROGRAMA PRINCIPAL
# ========================================

if __name__ == "__main__":
    menu_principal()
    
