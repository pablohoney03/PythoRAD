from datetime import datetime
import lorem
import re
import math
import os
import string

def questao_1():
    print("\n")
    try:
        with open("notas.txt", "r") as arquivo:
            conteudo = arquivo.read()
            print(conteudo)

    except FileNotFoundError as e:
        print(f"Arquivo {e.filename} não foi encontrado.")

        with open("notas.txt", "w") as arquivo:
            arquivo.write("Arquivo criado")
        with open("notas.txt", "r") as arquivo:
            conteudo = arquivo.read()
            print(conteudo)

    pass

def questao_2():
    print("\n")
    try:

        
        with open("frases.txt", "w") as arquivo:
            arquivo.write(lorem.text())

        with open("frases.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            
        count = 0
        for linha in linhas:
            if linha.strip() != '':
                count += 1

        print(f"Existem {count} linhas não vazias")
    

    except PermissionError:
        print("Erro de Permissão")

    pass

def questao_3():
    print("\n")
    try:
        comentarios_exemplo = """Este é um comentário com espaços  duplos e algumas reticências... aqui.
        Outro comentário,  também com reticências... e espaços  duplos."""

        with open("comentarios.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write(comentarios_exemplo)

        with open("comentarios.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()

    except UnicodeDecodeError:
        print("Erro ao ler em utf-8")

        with open("comentarios.txt", "r", encoding="latin-1") as arquivo:
            conteudo = arquivo.read()

    conteudo = ' '.join(conteudo.split())
    conteudo = conteudo.replace("...", '.')

    with open("comentarios_limpos.txt", "w", encoding="utf-8") as arquivo_saida:
        arquivo_saida.write(conteudo)

    print("Arquivo com comentarios limpos criado")

    pass

def questao_4():
    print("\n")
    jogadores = """
    Aaron Rodgers, Green Bay Packers.
    Patrick Mahomes, Kansas City Chiefs.
    Josh Allen, Buffalo Bills.
    Tom Brady, Tampa Bay Buccaneers.
    Joe Burrow, Cincinnati Bengals.
    Derrick Henry, Tennessee Titans.
    Jonathan Taylor Indianapolis Colts.
    Nick Chubb Cleveland Browns.
    """

    with open("jogadores.txt", "w") as arquivo:
        arquivo.write(jogadores)

    jogadores_times ={}
    
    try:
        with open("jogadores.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        for linha in linhas:
                try:
                    linha = linha.strip()
                    if ',' in linha:
                        nome, time = linha.split(",", 1)  
                        jogadores_times[nome.strip()] = time.strip()



                    else:
                        with open("linhas_invalidas.log", "a") as log:
                            log.write(linha + "\n")
                except Exception:
                    print("Um erro ocorreu.")
        print(jogadores_times)

    except FileNotFoundError as e:
        print(f"O arquivo {e.filename} não foi encontrado.")

    pass

def questao_5():
    print("\n")

    lista_a = """
    Maçã
    Banana
    Laranja
    Melancia
    Morango
    Pera
    Manga
    Kiwi
    Maçã
    """
    lista_b = """
    Abacaxi
    Morango
    Laranja
    Maçã
    Pera
    Uva
    Banana
    Kiwi
    Melancia
    """

    with open("lista_a.txt", "w") as lista_a:
        lista_a.write(lista_a)

    with open("lista_b.txt", "w") as lista_b:
        lista_b.write(lista_b)

    lista_unica = set()

    try:
        with open("lista_a.txt", "r") as lista_a:
            itens_a = lista_a.readlines()
            lista_unica.update(item.strip()for item in itens_a)

    except FileNotFoundError as e:    
        print(f"Erro: {e.filename} não foi encontrado.")

    try:
        with open("lista_b.txt", "r") as lista_b:
            itens_b = lista_b.readlines()
            lista_unica.update(item.strip()for item in itens_b)
    except FileNotFoundError as e:    
        print(f"Erro: {e.filename} não foi encontrado.")

        lista_ordenada = sorted(lista_unica)

        with open("lista_uniq.txt", "w") as arquivo_saida:
            for item in lista_ordenada:
                arquivo_saida.write(item + "\n")

            print("Arquivo de listas unica foi criado com sucesso")

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

    pass

def questao_6():
    print("\n")
    try:
        with open("texto.txt", "r") as arquivo:
            conteudo = arquivo.read()

        conteudo = conteudo.lower()
        conteudo = conteudo.translate(str.maketrans("","", string.punctuation))

        palavras = conteudo.split()
        palavras_distintas = set(palavras)

        print(f"Quantidade de palavras distintas: {len(palavras_distintas)}")

    except FileNotFoundError as e:
        print(f"Arquivo {e.filename} não encontrado")

    pass

def questao_7():
    print("\n")

    lista_a = """
    Maçã
    Banana
    Laranja
    Melancia
    Morango
    Pera
    Manga
    Kiwi
    Maçã
    """
    lista_b = """
    Abacaxi
    Morango
    Laranja
    Maçã
    Pera
    Uva
    Banana
    Kiwi
    Melancia
    """

    with open("lista_a.txt", "w") as lista_a:
        lista_a.write(lista_a)

    with open("lista_b.txt", "w") as lista_b:
        lista_b.write(lista_b)

    lista_unica = set()

    try:
        with open("lista_a.txt", "r") as lista_a:
            itens_a = lista_a.readlines()
            lista_unica.update(item.strip()for item in itens_a)

    except FileNotFoundError as e:    
        print(f"Erro: {e.filename} não foi encontrado.")

    try:
        with open("lista_b.txt", "r") as lista_b:
            itens_b = lista_b.readlines()
            lista_unica.update(item.strip()for item in itens_b)
    except FileNotFoundError as e:    
        print(f"Erro: {e.filename} não foi encontrado.")

        lista_ordenada = sorted(lista_unica)

        with open("lista_uniq.txt", "w") as arquivo_saida:
            for item in lista_ordenada:
                arquivo_saida.write(item + "\n")

            print("Arquivo de listas unica foi criado com sucesso")

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

    pass


questoes = {
    "1":("Questão 1 ", questao_1),
    "2":("Questão 2 ", questao_2),
    "3":("Questão 3 ", questao_3),
    "4":("Questão 4 ", questao_4),
    "5":("Questão 5 ", questao_5),
    "6":("Questão 6 ", questao_6),
    "7":("Questão 7 ", questao_7),

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
