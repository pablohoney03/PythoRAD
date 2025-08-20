from datetime import datetime
import re
import math
import os

def questao_1():
    print("\n")
    try:
        with open("texto.txt", "w") as arquivo:
            for i in range(1, 11):
                linha = f"9 x {i} = {9 * i}\n"
                arquivo.write(linha)
        print("Tabuada de 9 inserida com sucesso!")
    except Exception:
        print("Ocorreu um erro")

    pass
def questao_2():
    print("\n")
    try:
        with open("texto.txt", "w") as arquivo:
            nome = input("Digite seu nome:")
            RG= int(input("Digite seu RG:"))
            CPF = int(input("Digite seu CPF:"))
            ano_nasc = int(input("Digite seu ano de nascimento:"))
            idade = datetime.now().year - ano_nasc

            arquivo.write(f"Nome: {nome}\n")
            arquivo.write(f"RG: {RG}\n")
            arquivo.write(f"CPF: {CPF}\n")
            arquivo.write(f"Ano de Nascimento: {ano_nasc}\n")
            arquivo.write(f"Idade: {idade} anos\n")
            print("Dados inseridos com sucesso!")
    except Exception:
        print("Ocorreu um erro")
            

    pass

def questao_3():
    print("\n")
    try:
        with open("texto.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            lista = [linha.strip() for linha in linhas]
        print(lista)

    except Exception:
        print("Ocorreu um erro")

    pass

def questao_4():
    print("\n")
    try:
        with open("texto.txt", "w") as arquivo:
            nome = input("Digite seu nome:")
            while True:
                nota1 = float(input("Nota 1: "))
                nota2 = float(input("Nota 2: "))

                if nota1 >= 0 and nota2 >= 0:
                    break
                print("As notas devem ser positivas. Tente novamente.\n")
            media = (nota1 + nota2)/2
            if(media >= 6):
                arquivo.write(f"O aluno {nome} foi Aprovado com a nota de {media}")
            else:
                arquivo.write(f"O aluno {nome} foi Reprovado com a nota de {media}")
        print("Dados inseridos com sucesso!")

    except Exception:
        print("Ocorreu um erro")
            
    pass

def questao_5():
    print("\n")
    try:
        num1 = int(input("Digite o primeiro número inteiro: "))
        num2 = int(input("Digite o segundo número inteiro: "))

        soma = num1 + num2
        subtracao = num1 - num2
        multiplicacao = num1 * num2


        if num2 != 0:
            divisao = num1 / num2

        with open("resultados_calculadora.txt", "w") as arquivo:
            arquivo.write(f"Número 1: {num1}\n")
            arquivo.write(f"Número 2: {num2}\n")
            arquivo.write(f"Soma: {soma}\n")
            arquivo.write(f"Subtração: {subtracao}\n")
            arquivo.write(f"Multiplicação: {multiplicacao}\n")
            arquivo.write(f"Divisão: {divisao}\n")

        print("Resultados salvos em 'resultados_calculadora.txt'.")

    except ValueError:
        print("Valor Invalido")
    except ZeroDivisionError:
        print("Divisao por zero")

    pass

def questao_6():
    print("\n")
    try:
        nome = input("Digite seu nome: ")
        if re.search(r'\d', nome):
            raise ValueError("O nome não pode conter números.")
        
    except ValueError as e:
        print(f"Erro: {e}")

    pass

def questao_7():
    print("\n")
    try:
        num1 = int(input("Valor 1: "))
        num2 = int(input("Valor 2: "))

        divide = num1/num2
        print(f"O resultado da divisão é: {divide}")

    except ValueError:
        print("O numero informado é invalido")
    except ZeroDivisionError:
        print("Divisao por zero")

    pass

def questao_8():
    print("\n")
    try:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))

        fatorial_num1 = math.factorial(num1)
        fatorial_num2 = math.factorial(num2)

        print(f"O fatorial de {num1} é {fatorial_num1}")
        print(f"O fatorial de {num2} é {fatorial_num2}")

    except ValueError:
        print("Valor Invalido")
    except ZeroDivisionError:
        print("Divisao por zero")
    pass

def questao_9():
    print("\n")
    nome_arquivo = "texto.txt"
    
    if not os.path.exists(nome_arquivo):
        print(f"O arquivo '{nome_arquivo}' não foi encontrado no diretório.")
        return
    
    total_linhas = 0
    total_palavras = 0

    try:
        with open(nome_arquivo, 'r') as arquivo:

            for linha in arquivo:
                total_linhas += 1  
                total_palavras += len(linha.split()) 

        print(f"O arquivo '{nome_arquivo}' contém {total_linhas} linhas.")
        print(f"O arquivo '{nome_arquivo}' contém {total_palavras} palavras.")
    
    except Exception:
        print("Ocorreu um erro ao tentar ler o arquivo")

def questao_10():
    print("\n")
    try:

        nome = input("Digite seu nome completo: ").strip()
        
        nome_formatado = " ".join([parte.capitalize() for parte in nome.split()])

        nome_arquivo = "nome.txt"
        
        if os.path.exists(nome_arquivo):
            print("O arquivo {nome_arquivo} já existe.")
            return
            

        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(nome_formatado)
            
        print(f"O nome formatado '{nome_formatado}' foi salvo no arquivo '{nome_arquivo}'.")
    
    except Exception as e:
        print(f"Ocorreu um erro ao tentar criar o arquivo: {e}")

questoes = {
    "1":("Questão 1 ", questao_1),
    "2":("Questão 2 ", questao_2),
    "3":("Questão 3 ", questao_3),
    "4":("Questão 4 ", questao_4),
    "5":("Questão 5 ", questao_5),
    "6":("Questão 6 ", questao_6),
    "7":("Questão 7 ", questao_7),
    "8":("Questão 8 ", questao_8),
    "9":("Questão 9 ", questao_9),
    "10":("Questão 10 ", questao_10)

}

def menu():
    while True:
        print("\n" + "="*50)
        print("Menu de Exercicios".center(50))
        print("" + "="*50)

        for key, (questao,_) in questoes.items():
            print(f"[{key}] {questao}")
        print("[0] Sair")
            
        opcao = input("\n Digite a questão que deseja ver: ")

        match opcao:
            case "0":
                break
            case i if opcao in questoes:
                questoes[opcao][1]()
            case _:
                print("Opção invalida.")
        

if __name__ == "__main__":
    menu()
