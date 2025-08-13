#Questão 1
nome = input("Digite a cadeia: ").upper()
nome = "".join(reversed(nome))
print(nome)

#Questão 2
with open("texto.txt", "r") as arquivo:
    conteudo = arquivo.read()
print("A quantidade de palavras no arquivo:", len(conteudo.split()))

#Questão 3
with open("texto.txt", "r") as arquivo:
    conteudo = arquivo.read()
conteudo = conteudo.replace(" ", "_")
print(conteudo)

#Questão 4
with open("texto.txt", "r") as arquivo:
    conteudo = arquivo.read()
conteudo = list(dict.fromkeys(conteudo.split()))
print(conteudo) 
