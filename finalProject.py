import pandas as pd

Estoque = {"ID": [], 
           "Nome": [],
           "Categoria": [],
           "Quantidade": [],
           "Preço": [],
           "Localização": []}

def dataframe_estoque(): #DataFrame do estoque atual.
    print("==="*30)
    print(pd.DataFrame(Estoque))
    print("==="*30)

def Cadastro_Produto1(id,nome,categoria,quantidade,preco,localizacao):
    if id in Estoque["ID"]: #Verifica se o item já existe
        print("Este Produto ja está cadastrado.")
        pass
    else: #Adiciona os novos produtos em um dicionário.
        Estoque["ID"].append(id)
        Estoque["Nome"].append(nome)
        Estoque["Categoria"].append(categoria)
        Estoque["Quantidade"].append(quantidade)
        Estoque["Preço"].append(preco)
        Estoque["Localização"].append(localizacao)
        print("Produto Cadastrado com sucesso!")

def atualizacao_Produto2(): # Alterar, excluir ou renomear um produto!
    atualizar_nome = int(input("Digite o ID do produto que deseja a alteração: ")) #Pede a ID do produto para identificação
    if atualizar_nome in Estoque["ID"]: #Verifica se existe um ID no dicionário.
        print("Digite (1) para renomear\n"
            "Digite (2) para alterar a categoria\n"
            "Digite (3) para alterar a quantidade\n"
            "Digite (4) para alterar o preço\n"
            "Digite (5) para alterar a localização\n"
            "Digite (6) para excluir um produto\n")
        mudanca = int(input("Escolha o que deseja fazer: "))
        if mudanca == 1:
            index_prod = Estoque["ID"].index(atualizar_nome) #Cria uma variavel com o indice do produto escolhido
            Estoque["Nome"].pop(index_prod) #Exclui o produto com o valor anterior
            renomeacao = input("Como deseja renomear? ") #Pergunta ao usuário a substituição desejada
            Estoque["Nome"].insert(index_prod,renomeacao) #Adiciona o novo valor no index do valor anterior.
            print(f"Renomeado! para {renomeacao}")
        elif mudanca == 2:
            index_prod = Estoque["ID"].index(atualizar_nome)
            Estoque["Categoria"].pop(index_prod)
            renomeacao = input("Como deseja renomear? ")
            Estoque["Categoria"].insert(index_prod,renomeacao)
            print(f"Categoria Alterada para {renomeacao}")
        elif mudanca == 3:
            index_prod = Estoque["ID"].index(atualizar_nome)
            Estoque["Quantidade"].pop(index_prod)
            renomeacao = input("Qual quantidade deseja alterar? ")
            Estoque["Quantidade"].insert(index_prod,renomeacao)
            print(f"Quantidade Alterada para {renomeacao}")
        elif mudanca == 4:
            index_prod = Estoque["ID"].index(atualizar_nome)
            Estoque["Preço"].pop(index_prod)
            renomeacao = input("Qual quantidade deseja alterar ")
            Estoque["Preço"].insert(index_prod,renomeacao)
            print(f"Preço Alterado para {renomeacao}")
        elif mudanca == 5:
            index_prod = Estoque["ID"].index(atualizar_nome)
            Estoque["Localização"].pop(index_prod)
            renomeacao = input("Como deseja renomear? ")
            Estoque["Localização"].insert(index_prod,renomeacao)
            print("Localização Alterada")
        elif mudanca == 6: #Exclui todos itens de listas com o mesmo index do ID selecionado pelo usuário.
            index_prod = Estoque["ID"].index(atualizar_nome)
            Estoque["ID"].pop(index_prod)
            Estoque["Nome"].pop(index_prod)
            Estoque["Categoria"].pop(index_prod)
            Estoque["Quantidade"].pop(index_prod)
            Estoque["Preço"].pop(index_prod)
            Estoque["Localização"].pop(index_prod)
            print("Item excluido!")
        else:
            print("Produto não encontrado!\n")
            pass

def rastreio_produto3():
    prod_rastreio = int(input("Qual ID de produto deseja rastrear? "))
    if prod_rastreio in Estoque["ID"]:
        index_prod = Estoque["ID"].index(prod_rastreio)
        print(f"Seu produto está localizado em: {Estoque["Localização"][index_prod]}")
    else:
        print("Produto não encontrado")
        pass

def relatorios4():
    dataframe_estoque() #Mostra ao usuário um DataFrame do dicionário "Estoque"
    for produtos in Estoque["Quantidade"]: #Verifica um produto por vez
        if produtos <= 20: #caso algum produto tenha menos de 20 unidades, receberá um aviso de falta.
            index_prod = Estoque["Quantidade"].index(produtos)
            print(f"O produto {Estoque["Nome"][index_prod]} está em falta contendo apenas {produtos} unidades restantes.")
        elif produtos > 100: #Caso o produto tenha mais de 100 unidades, receberá um aviso de excesso de estoque.
            index_prod = Estoque["Quantidade"].index(produtos)
            print(f"O produto {Estoque["Nome"][index_prod]} está com o estoque excessivo de {produtos} unidades.")

def tabela_verdade5(quant_table,price_table):
    df_tabelaVerdade = {"Nome": Estoque["Nome"], "Quantidade": [], "Preço": []}
    for produtos in Estoque["Quantidade"]:
        if produtos > quant_table:
            df_tabelaVerdade["Quantidade"].append(True)
        else:
            df_tabelaVerdade["Quantidade"].append(False)

    for valores in Estoque["Preço"]:
        if valores > price_table:
            df_tabelaVerdade["Preço"].append(True)
        else:
            df_tabelaVerdade["Preço"].append(False)
    print(f"Caso a quantidade de produtos ultrapassem {quant_table} e caso preço seja maior que R${price_table} = True\n"
    f"Caso a quantidade de produtos NÃO ultrapassem {quant_table} e caso o valor seja menor que R${price_table} = False\n"
    )
    print(pd.DataFrame(df_tabelaVerdade))

def menu():
    while True:
        try:
            escolha = int(input("X-----  Gerenciamento de Estoque  -----X \n" #Escolhe a função que deseja executar.
                "Digite (1) para cadastrar um produto \n"
                "Digite (2) para atualizar o um produto \n"
                "Digite (3) para rastrear um produto \n"
                "Digite (4) para gerar um relatório sobre os produtos \n"
                "Digite (5) para fechar o sistema \n\n"))
            if escolha == 1: 
                id = int(input("Qual o ID do produto? "))
                nome = input("Qual produto deseja cadastrar? ").capitalize() 
                categoria = input("Qual a categoria do produto? ").capitalize()
                quantidade = int(input("Quantas unidades deseja cadastrar? "))
                preco = float(input("Qual o preço unitário do produto? "))
                localizacao = input("Em que seção o produto estará localizado? ").capitalize()
                Cadastro_Produto1(id,nome,categoria,quantidade,preco,localizacao) #Função para fazer o cadastro
            elif escolha == 2:
                atualizacao_Produto2() #Função para atualizar um produto
            elif escolha == 3:
                rastreio_produto3() #Função para rastrear um produto
            elif escolha == 4:
                relatorios4() #Função para gerar um relatório dos produtos cadastrados
            elif escolha == 5:
                print("Encerrando sistema...") 
                break #Encerra o loop, fechando o sistema
        except ValueError: #Caso o usuário insira um valor iválido.
            print("Comando Inválido")

menu()
