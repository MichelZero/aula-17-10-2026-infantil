import random

print("=== JOGO DA ADIVINHAÇÃO ===")
print("Tente adivinhar o número entre 1 e 100.\n")

# O computador escolhe um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)
tentativas = 0
acertou = False

# Laço de repetição que continua rodando até o usuário acertar
while not acertou:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1
    
    # Estruturas condicionais para dar as dicas
    if palpite < numero_secreto:
        print("O número secreto é maior!\n")
    elif palpite > numero_secreto:
        print("O número secreto é menor!\n")
    else:
        acertou = True
        print(f"Parabéns! Você acertou o número secreto ({numero_secreto}) em {tentativas} tentativas!")
