import forca as fgame
import adivinhacao

def escolhe_jogo():
    print('*'*20)
    print('Escolha o seu jogo'.center(20,'*'))
    print('*'*20)


    print('(1) Forca\n(2) Adivinhação')

    jogo = int(input('Qual o jogo? '))

    if jogo==1:
        print('Jogando forca')
        fgame.jogar()
    elif jogo==2:
        print('Jogando adivinhação')
        adivinhacao.jogar()

if (__name__=="__main__"):
    escolhe_jogo()