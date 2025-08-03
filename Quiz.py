# Teste nº 1:

# Versão 0.2

# \\--\\--\\ Introdução \\--\\--\\

import time

def cores(mensagem, cor_mensagem): 
    print(f"\033[{cor_mensagem}m{mensagem}\033[0m")

cores("Olá, seja bem vindo ao jogo de respostas!", 33)

while True:
    try:
        time.sleep(1)
        print("Para começar, me diga qual é o seu nome."), time.sleep(1)
        nome = (input())
        if nome == "":
            time.sleep(1)
            cores("Insira o seu nome!", 31)
            print(" ")
        if nome != "":
            time.sleep(1)
            cores(f"Prazer em conhecê-lo, [{nome}]!", 32)
            break
    except ValueError:
        time.sleep(1)
        print("Insira um nome válido!"), time.sleep(1)
        print(" ")

# \\--\\--\\ Pergunta 1 \\--\\--\\

while True:
    try:
        print(" ")
        time.sleep(1.3)
        cores(f"1) Para começar, [{nome}], escolha um número inteiro de '1' a '10'", 33)
    
        a = int(input())

        if a >= 11:
            time.sleep(1)
            cores("Escolha um número menor!", 31)
            time.sleep(1)
            print(f"O número '{a}' é maior que 10!")

        if a <= 0:
            time.sleep(1)
            cores("Escolha um número maior!", 31)
            time.sleep(1)
            print(f"O número '{a}' é menor que 1!")

        if a >= 1 and a <= 10:
            time.sleep(1)
            cores("Ótima escolha!", 32)
            time.sleep(1.3)
            print(f"O número '{a}' está entre 1 e 10!")
            time.sleep(1)
            print("Preparando próxima pergunta. . .")
            time.sleep(1)
            break
    except ValueError:
        time.sleep(1)
        cores("Insira um número válido!", 31)

# \\--\\--\\ Pergunta 2 \\--\\--\\

import time

Resposta1 = 6

while True:
    try:
        print(" ")
        cores("2) Quanto é 2x3?", 33)
        
        c = int(input())
        
        if c != Resposta1:
            time.sleep(1)
            cores(f"A resposta '{c}' está incorreta!", 31)
            time.sleep(1)
        if c == Resposta1:
            time.sleep(1)
            cores("Resposta Correta!", 32)
            time.sleep(1)
            print("Preparando próxima pergunta. . .")
            break
    except ValueError:
        time.sleep(1)
        cores("A resposta não pode conter números quebrados nem letras!",31)
        time.sleep(1)

# \\--\\--\\ Pergunta 3 \\--\\--\\

while True:
    try:
        time.sleep(1)
        print(" ")
        cores("3) Qual o seu filme favorito?", 33)

        ff = (input())

        if ff == "":
            time.sleep(1)
            cores("Insira o nome de um filme!", 31)
            time.sleep(1)
        if ff != "":
            time.sleep(1)
            cores(f"Ótima escolha, '{ff}' é realmente um bom filme!", 32)
            time.sleep(1)
            print("Preparando próxima pergunta. . .")
            print(" ")
            break
    except ValueError:
        time.sleep(1)
        print("Insira uma resposta válida!"), time.sleep(1)

# \\--\\--\\ Pergunta 4 \\--\\--\\

time.sleep(1)
cores("4) Passando para uma pergunta um pouco mais pessoal, como você está se sentindo?", 33)

while True:
    try:

        time.sleep(1)
        print('''Digite a opção que melhor se encaixa a sua situação atual:
        [1] Estou me sentindo bem!
        [2] Estou me sentindo mal...'''), time.sleep(1)

        e1 = 1
        e2 = 2

        e = int(input())
        
        if e != e1 and e != e2:
            time.sleep(1)
            cores(f"Escolha entre [{e1}] e [{e2}]!", 31)
            print(" ")
        if e == e1:
            cores("Que bom!", 32), time.sleep(1)
            print(" ")
            break
        if e == e2:
            cores("Nem tão bom. . .", 31), time.sleep(1)
            print(" ")
            break
    except ValueError:
        cores(f"Escolha entre [{e1}] e [{e2}]!", 31), time.sleep(1)
        print(" ")