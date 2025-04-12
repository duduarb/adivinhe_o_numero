from random import randint


def adivinhar_numero():

    num_secreto = randint(1, 10)
    tentativas = 0

    print('----ADIVINHE O NÚMERO SECRETO----')
    print('Estou pensando em um número de 1 a 10, tente adivinhá-lo.')


while True:
    tentativas += 1
    chute = int(input('Qual seu palpite? '))

    if chute == num_secreto:
        print(f'PARABÉNS! Você acertou! Eu estava pensando no número {chute}.')
    else:
        print('Você errou! Tente novamente.')


def jogar():
    print('Bem vindo ao jogo do número secreto')

    while True:
        adivinhar_numero()

        jogue_novamente = input('Quer jogar novamente? (s/n): ')
        if jogue_novamente.lower() != "s":
            print('Obrigado por jogar!')
            break


jogar()
