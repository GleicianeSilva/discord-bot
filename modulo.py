def pegaNome():
    nome = input("Digite seu nome: ")
    print(f"Meu nome é: {nome}")

#pegaNome()


def gam():
    gamma = input("digite o valor numerico ")
    print(f"o valor é: {gamma} ")
    
#gam()


def cidade():
    cid = input("Qual cidade você é: ")
    print("Moro em: ", cid)

#cidade()


def peganumero ():
    n1 = input("Digite um numero: ")
    print("Dado esse numero, se o dividirmos por 10, teremos {} e {} de resto".format( int(n1) // 10 , int(n1) % 10 ))

'''peganumero()'''

#TypeError: unsupported operand type(s) for /: 'str' and 'int'
#Todo retorno de uma função input é um dado do tipo string (ou seja, texto)