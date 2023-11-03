import time
import csv
import random

def apresentar_questao(pergunta, resposta_correta):
    print(pergunta)
    resposta_jogador = input("Sua resposta: ")
    if resposta_jogador == resposta_correta:
        return True
    else:
        print("--------------------\n")
        print(f"Resposta INCORRETA! A resposta correta é {resposta_correta}.")
        return False

def jogo_de_matematica(questoes, tempo_por_questao):
    acertos = 0
    tempo_por_questao = 2
    for pergunta, resposta_correta in questoes:
        print("\n--------------------")
        if apresentar_questao(pergunta, resposta_correta):
            acertos += 1
            print("--------------------\n")
            print(f"Resposta CORRETA! Você acertou {acertos} por enquanto!")
        time.sleep(tempo_por_questao)
        
def ler_questoes_arquivo(nome_arquivo):
    questoes = []
    with open(nome_arquivo, newline='', encoding='utf-8') as arquivo:
        leitor_csv = list(csv.reader(arquivo, delimiter=';'))
        random.shuffle(leitor_csv)
        for linha in leitor_csv:
            pergunta, resposta = linha
            questoes.append((pergunta, resposta))
    return questoes

def inicio():
    print("Bem-vindo!")
    time.sleep(0.5)
    start = input("Vamos começar? (s/n): ")
    
    if start.lower() == 's':
        questoes = ler_questoes_arquivo("jogo\questoes.csv")
        numero_de_questoes = len(questoes)
        jogo_de_matematica(questoes, numero_de_questoes)
    else:
        print("Até mais!")

if __name__ == "__main__":
    inicio()