def n2():
    #TODA FUNÇÃO TEM PARÊNTESES!
    nome = input("Digite um nome: ").strip()
    print ("Analisando seu nome...")
    print ("Seu nome tem {} letras".format ( len(nome) - nome.count (" ") ))