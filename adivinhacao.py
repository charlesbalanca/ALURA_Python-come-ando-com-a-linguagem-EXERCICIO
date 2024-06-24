import random

def jogar():
    print('*'*24)
    print('Jogo adivinhe o número'.center(24,'*'))
    print('*'*24)

    numero_secreto=random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print('Qual nível de dificuldade?')
    print('(1) Fácil\n(2) Médio\n(3) Difícil\n')

    nivel = int(input('Defina o nível: '))
    if nivel ==1:
        total_de_tentativas = 20
        print('Você definiu fácil')
    elif nivel==2:
        total_de_tentativas = 10
        print('Você definiu médio')
    else:
        total_de_tentativas = 5
        print('Você definiu díficil')

    for rodada in range (1, total_de_tentativas + 1):
        print('Tentativa {} de {}'.format(rodada,total_de_tentativas))
        #mostrar número secreto aleátorio para testar
        print(numero_secreto)
        chute_str = input('Digite um número entre 1 e 100: ')
        print('Você digitou ', chute_str)
        chute = int(chute_str)

        if chute < 1 or chute >100:
            print('Você deve digitar um número entre 1 e 100!')
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if acertou:
            print('Você acertou! e fez {} pontos'.format(pontos))
            break
        else:
            if maior:
                print('Você errou! O seu chute foi maior do que o número secreto')
            elif menor:
                print('Você errou! O seu chute foi menor do que o número secreto')
            pontos_perdidos = abs(numero_secreto-chute)
            pontos = pontos-pontos_perdidos

    print('Fim do jogo')


if (__name__=="__main__"):
    jogar()