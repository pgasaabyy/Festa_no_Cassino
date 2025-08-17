# Importando bibliotecas
import random   # para sortear símbolos aleatórios
import os       # para limpar a tela do terminal
import time     # para dar pausas

# Lista de símbolos do caça-níquel
symbols = ["🍒", "🍋", "🔔", "⭐", "🍀", "💎"]

# Função que limpa a tela do terminal
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")  
    # "cls" é usado no Windows e clear nos demais SO

# Função principal do jogo
def slot_machine():
    limpar_tela()  # limpa a tela antes de começar
    print("🎰 Bem-vindo à Festa no Cassino! 🎰\n")  # mensagem de boas-vindas
    saldo = 100  # dinheiro inicial

    # Loop principal do jogo (vai rodar até o jogador sair ou perder tudo)
    while True:
        print(f"Seu saldo atual: ${saldo}")  # mostra saldo atual
        aposta = input("Quanto deseja apostar? (ou digite 'sair'): ")  # pede a aposta

        # Se o jogador digitar "sair", o jogo acaba
        if aposta.lower() == "sair":
            print("Obrigado por jogar! Seu saldo final é:", saldo)
            break  # encerra o loop (fim do jogo)

        # Verifica se o que o usuário digitou é um número
        if not aposta.isdigit():
            print("Digite um número válido!")  # se não for número, avisa
            continue  # volta pro início do loop

        # Converte a aposta de texto (string) para número inteiro
        aposta = int(aposta)

        # Impede apostas inválidas (maiores que o saldo ou menores que 1)
        if aposta > saldo or aposta <= 0:
            print("Aposta inválida!")
            continue  # volta pro início do loop

        # Mostra mensagem de roleta girando
        print("\nGirando...")
        time.sleep(2)  # espera 2 segundos para dar efeito de suspense

        # Sorteia 5 símbolos aleatórios da lista
        resultado = [random.choice(symbols) for _ in range(5)]
        print(" | ".join(resultado))  # mostra o resultado

        # Verifica condições de vitória
        if resultado.count(resultado[0]) == 5:
            # Se os 5 forem iguais → JACKPOT
            ganho = aposta * 10
            saldo += ganho
            print(f"🎉 JACKPOT! Você ganhou ${ganho} 🎉\n")
        elif any(resultado.count(s) == 4 for s in resultado):
            # Se 4 iguais
            ganho = aposta * 7
            saldo += ganho
            print(f"✨ Quase Jackpot! Você ganhou ${ganho}! ✨\n")
        elif any(resultado.count(s) == 3 for s in resultado):
            # Se 3 iguais
            ganho = aposta * 5
            saldo += ganho
            print(f"✨ Você ganhou ${ganho}! ✨\n")
        elif any(resultado.count(s) == 2 for s in resultado):
            # Se 2 iguais
            ganho = aposta * 2
            saldo += ganho
            print(f"✨ Você ganhou ${ganho}! ✨\n")
        else:
            # Se nenhum for igual
            saldo -= aposta
            print("😢 Você perdeu...\n")

        # Se o saldo zerar ou ficar negativo, o jogo acaba
        if saldo <= 0:
            print("💀 Você ficou sem saldo! Jogo encerrado.")
            break  # sai do loop

        # Espera o jogador apertar ENTER para continuar
        input("Pressione ENTER para continuar...")
        limpar_tela()  # limpa a tela antes da próxima rodada

# Chama a função principal para iniciar o jogo
slot_machine()
