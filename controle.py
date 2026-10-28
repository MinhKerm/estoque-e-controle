
materiais = {
    "mouse": 10,
    "teclado": 6,
    "cabo": 20
}
 
nome = input("Qual material deseja retirar? ").lower()
 
try:
    quantidade = int(input("Quantas unidades? "))
 
    # 1. Verificar se o material existe
    if nome not in materiais:
        print("Material não encontrado no estoque!")
 
    # 2. Impedir quantidades iguais ou menores que zero
    elif quantidade <= 0:
        print("A quantidade deve ser maior que zero!")
 
    # 3. Impedir retirada maior que o estoque disponível
    elif quantidade > materiais[nome]:
        print("Estoque insuficiente! Quantidade disponível:", materiais[nome])
 
    # 4. Atualizar o estoque
    else:
        materiais[nome] - quantidade
       
        print("Retirada realizada com sucesso!")
 
    # 5. Exibir o estoque atualizado
    print("\nEstoque atual:")
    print(materiais)
 
except ValueError:
    print("Digite uma quantidade numérica válida!")