# ==================================================
# SISTEMA DE CONTROLE DE ESTOQUE
# ==================================================
 
estoque = []
 
 
# ==================================================
# 1. CADASTRAR PRODUTO
# ==================================================
 
def cadastrar_produto():
    print("\n========== CADASTRAR PRODUTO ==========")
 
    try:
        codigo = int(input("Código do produto: "))
 
        # CORREÇÃO: percorremos a lista para verificar
        # se já existe um produto com o mesmo código.
        for produto in estoque:
            if produto["codigo"] == codigo:
                print("Já existe um produto com esse código!")
                return
 
        nome = input("Nome do produto: ")
 
        quantidade = int(input("Quantidade inicial: "))
 
        # Aceita preço digitado com vírgula ou ponto.
        preco = float(input("Preço do produto: ").replace(",", "."))
 
        if quantidade < 0 or preco < 0:
            print("Quantidade e preço não podem ser negativos!")
            return
 
        # Cada produto é representado por um dicionário.
        produto = {
            "codigo": codigo,
            "nome": nome,
            "quantidade": quantidade,
            "preco": preco
        }
 
        # Adiciona o dicionário à lista de estoque.
        estoque.append(produto)
 
        print("Produto cadastrado com sucesso!")
 
    except ValueError:
        # CORREÇÃO: impede que entradas não numéricas
        # causem o encerramento inesperado do programa.
        print("Digite números válidos para código, quantidade e preço!")
 
 
# ==================================================
# 2. LISTAR PRODUTOS
# ==================================================
 
def listar_produtos():
    print("\n========== LISTA DE PRODUTOS ==========")
 
    # Verifica se a lista está vazia.
    if len(estoque) == 0:
        print("Nenhum produto cadastrado.")
        return
 
    # Percorre todos os produtos cadastrados.
    for produto in estoque:
        print("------------------------------")
        print("Código:", produto["codigo"])
        print("Nome:", produto["nome"])
        print("Quantidade:", produto["quantidade"])
        print("Preço: R$", produto["preco"])
 
 
# ==================================================
# 3. PESQUISAR PRODUTO
# ==================================================
 
def pesquisar_produto():
    print("\n========== PESQUISAR PRODUTO ==========")
 
    try:
        codigo = int(input("Digite o código do produto: "))
 
        for produto in estoque:
 
            if produto["codigo"] == codigo:
                print("\nProduto encontrado!")
                print("Código:", produto["codigo"])
                print("Nome:", produto["nome"])
                print("Quantidade:", produto["quantidade"])
                print("Preço: R$", produto["preco"])
 
                # Encerra a função quando encontra o produto.
                return
 
        # CORREÇÃO: fica fora do for para só aparecer
        # depois que todos os produtos forem verificados.
        print("Produto não encontrado.")
 
    except ValueError:
        print("Digite um código numérico válido!")
 
 
# ==================================================
# 4. REGISTRAR ENTRADA DE ESTOQUE
# ==================================================
 
def registrar_entrada():
    print("\n========== ENTRADA DE ESTOQUE ==========")
 
    try:
        codigo = int(input("Código do produto: "))
 
        quantidade_entrada = int(
            input("Quantidade que chegou: ")
        )
 
        if quantidade_entrada <= 0:
            print("A quantidade deve ser maior que zero!")
            return
 
        for produto in estoque:
 
            if produto["codigo"] == codigo:
 
                # CORREÇÃO: entrada soma os itens recebidos.
                # Exemplo: 5 unidades + 3 unidades = 8.
                produto["quantidade"] = produto + quantidade_entrada
 
                print("Entrada registrada com sucesso!")
                print("Quantidade atual:", produto["quantidade"])
 
                return
 
        print("Produto não encontrado.")
 
    except ValueError:
        print("Digite números inteiros válidos!")
 
 
# ==================================================
# 5. RELATÓRIO DE ESTOQUE
# ==================================================
 
def relatorio_estoque():
    print("\n========== RELATÓRIO DE ESTOQUE ==========")
 
    if len(estoque) == 0:
        print("Não há produtos para gerar o relatório.")
        return
 
    # Acumulador que guardará o valor total do estoque.
    valor_total = 0
 
    for produto in estoque:
 
        # CORREÇÃO: utilizamos a chave "preco",
        # que é a mesma utilizada no dicionário.
        valor_produto = (
            produto["quantidade"] * produto["preco"]
        )
 
        # Soma o valor de cada produto ao total.
        valor_total += valor_produto
 
    print("Quantidade de produtos cadastrados:", len(estoque))
    print("Valor total do estoque: R$", valor_total)
 
 
# ==================================================
# 6. REMOVER PRODUTO
# ==================================================
 
def remover_produto():
    print("\n========== REMOVER PRODUTO ==========")
 
    try:
        codigo = int(
            input("Código do produto que deseja remover: ")
        )
 
        for produto in estoque:
 
            if produto["codigo"] == codigo:
 
                print("Produto encontrado:", produto["nome"])
 
                confirmacao = input(
                    "Confirma a remoção? (S/N): "
                )
 
                # Transforma a resposta em maiúscula.
                confirmacao = confirmacao.upper()
 
                if confirmacao == "S":
 
                    # Remove o dicionário encontrado da lista.
                    estoque.remove(produto)
 
                    print("Produto removido com sucesso!")
 
                else:
                    print("Remoção cancelada.")
 
                return
 
        print("Produto não encontrado.")
 
    except ValueError:
        print("Digite um código numérico válido!")
 
 
# ==================================================
# 7. LISTAR PRODUTOS COM ESTOQUE BAIXO
# ==================================================
 
def listar_estoque_baixo():
    print("\n========== ESTOQUE BAIXO ==========")
 
    # Controla se algum produto atende ao filtro.
    encontrou = False
 
    # Novo contador: quantos produtos precisam de reposição.
    quantidade_baixa = 0
 
    for produto in estoque:
 
        # Exibe somente produtos com menos de 5 unidades.
        if produto["quantidade"] < 5:
 
            print("------------------------------")
            print("Código:", produto["codigo"])
            print("Produto:", produto["nome"])
            print("Quantidade:", produto["quantidade"])
 
            encontrou = True
 
            # Conta mais um produto com estoque baixo.
            quantidade_baixa += 1
 
    if encontrou == False:
        print("Nenhum produto com estoque baixo.")
 
    else:
        print("------------------------------")
        print("Produtos que precisam de reposição:",
              quantidade_baixa)
 
 
# ==================================================
# 8. MENU PRINCIPAL
# ==================================================
 
def menu():
 
    # Mantém o menu funcionando até o usuário sair.
    while True:
 
        print("\n========== MENU ==========")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Pesquisar produto")
        print("4 - Registrar entrada")
        print("5 - Relatório de estoque")
        print("6 - Remover produto")
        print("7 - Listar produtos com estoque baixo")
        print("8 - Sair")
 
        opcao = input("Escolha uma opção: ")
 
        if opcao == "1":
            cadastrar_produto()
 
        elif opcao == "2":
            listar_produtos()
 
        elif opcao == "3":
            pesquisar_produto()
 
        elif opcao == "4":
            registrar_entrada()
 
        elif opcao == "5":
            relatorio_estoque()
 
        elif opcao == "6":
            remover_produto()
 
        elif opcao == "7":
            listar_estoque_baixo()
 
        elif opcao == "8":
            print("Sistema encerrado!")
 
            # Encerra o while do menu.
            break
 
        else:
            print("Opção inválida! Tente novamente.")
 
 
# ==================================================
# INÍCIO DO PROGRAMA
# ==================================================
 
menu()