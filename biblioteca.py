import json

livros = []

while True:
    print("=-=Menu da Biblioteca=-=")
    print("0-Sair") 
    print("1-cadastrar")
    print("2-Deletar")
    print("3-exibir")
    print("4-Editar")
    print("5-Pesquisar")
    print("6-GerarRelatório")

    op = input("Escolha uma opação do menu: ")

    if op == "0":
        print("Saindo da Biblioteca...")
        break
    
    elif op == "1":
        nome = input("Informe o nome do livro: ")
        autor = input("Informe o nome do autor: ")
        anopu = input("Informe o ano de publicação do livro: ")
        gen = input("Informe o gênero do livro: ")

        livro = {
            "Nome": nome,
            "Autor": autor,
            "Ano de Publicação": anopu,
            "Gênero": gen
        }

        livros.append(livro)

        with open("id.json", "w", encoding="utf-8") as arquivo:
            json.dump(livros, arquivo, indent=4, ensure_ascii=False)

        with open("id.json", "r", encoding="utf-8") as arquivo:
            livro = json.load(arquivo)

        with open("id.txt", "w", encoding="utf-8") as arquivo:
            for livro in livros:
                arquivo.write(f"Nome: {livro['Nome']}\n")
                arquivo.write(f"Autor: {livro['Autor']}\n")
                arquivo.write(f"Ano de Publicação: {livro['Ano de Publicação']}\n")
                arquivo.write(f"Gênero: {livro['Gênero']}\n")
                arquivo.write("------------------------------------\n")

        print("Livros cadastrados")

    elif op == "2":
        print("Função deletar")

    elif op == "3":
        print("Função exibir")

    elif op == "4":
        print("Função editar")

    elif op == "5":
        print("Função pesquisar")

    elif op == "6":
        print("Função gerar relatório")

    else:
        print("Essa opção não está do menu, por favor, escolha novamente")
        
        

       
        
