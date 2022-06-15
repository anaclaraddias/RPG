
import random as aleatorio
import os
import time

os.system("clear")

print("\n RPG \n")

vidaP = 10
vidaM = 20
ataqueM = 3

ataque_MAX_ma = 15
ataque_MAX_gue = 10

while True:

    personagem = int(input("\n Escolha entre ser um mago (digite 1) ou um guerreiro (digite 2)\n --> "))

    if personagem == 1:

        print(f"\n Seu personagem: Mago")
        print(f" Sua vida e: {vidaP}")

        poder = aleatorio.randint(7,ataque_MAX_ma)

        print(f" Sua barra de poder: {poder}")

        break

    elif personagem == 2:

        print(f"\n Seu personagem: Guerreiro")
        print(f" Sua vida e: {vidaP}")

        poder = aleatorio.randint(5,ataque_MAX_gue)

        print(f" Sua barra de poder: {poder}")

        break

    else:

        continue


while True: 

    while True:

        time.sleep(1.2)

        print("\n--------------------------------------------")
        print("\n SEU TURNO")

        acao = int(input("\n Escolha o que voce quer fazer: \n\n - Atacar (digite 1)\n - Defender (digite 2)\n - curar (digite 3)\n - Descansar (digite 4) \n\n --> "))

        if poder > 1:

            if acao == 1:

                print("\n Voce escolheu atacar")

                if personagem == 1:

                    dano = aleatorio.randint(0,8)
                    poder = poder - 2

                else: 

                    dano = aleatorio.randint(3,10)
                    poder = poder - 2

                print(f"\n O dano causado e de: {dano}")
                print(f" E seu poder agora e: {poder}")

                break

            elif acao == 2:

                print("\n Voce escolheu defender")

                #cancela 1 de ataque do inimigo (turno do monstro - ataque)

                if personagem == 1:

                    poder = poder - 1

                print("\n Voce bloqueou 1 de dano do inimigo")
        
                if personagem == 1:

                    print(" Mas tambem perdeu poder de ataque")
                    print(f" Seu poder agora e: {poder}")

                break

            elif acao == 3:

                print("\n Voce escolheu curar")

                if personagem == 1:

                    vidaP = vidaP + 2

                else:

                    vidaP = vidaP + 1

                print(f"\n Sua vida agora e: {vidaP}")

                break

            elif acao == 4:

                print("\n Voce escolheu descansar")

                quantdes = aleatorio.randint(1,5)

                poder = poder + quantdes

                print(f"\n Seu poder agora e: {poder}")

                break

            else: 

                continue

        else:

            if acao == 3:

                print("\n Voce escolheu curar")

                if personagem == 1:

                    vidaP = vidaP + 2

                else:

                    vidaP = vidaP + 1

                print(f"\n Sua vida agora e: {vidaP}")

                break

            elif acao == 4:

                print("\n Voce escolheu descansar")

                quantdes = aleatorio.randint(1,5)

                poder = poder + quantdes

                print(f"\n Seu poder agora e: {poder}")

                break

            else:

                print("\n -----> Voce nao tem poder suficiente, tente descansar <-----")

            
    #turno do monstro
    #Para atacar, o monstro em seu turno escolhe aleatoriamente entre atacar dando 3 de dano ou se defender  

    acaoM = aleatorio.randint(1,2)

    time.sleep(1.35)

    print("\n--------------------------------------------")
    print("\n TURNO DO MONSTRO")

    if acaoM == 1:

        #monstro ataca
        print("\n O monstro te ataca")

        if acao == 2:

            vidaP = vidaP - (ataqueM - 1)
        
        else:

            vidaP = vidaP - ataqueM

        if acao == 1:

            vidaM = vidaM - dano

            print(f"\n A vida do monstro agora e: {vidaM}")

        print(f" Sua vida agora e: {vidaP}")


    else:

        #monstro defende
        print("\n O monstro defende")

        if acao == 1:

            dano = 0

            vidaM = vidaM - dano

            print(f"\n A vida do monstro e: {vidaM}")


    if vidaP <= 0:

        time.sleep(1)

        print("\n--------------------------------------------")
        print("\n-------> GAME OVER <-------\n")

        while True:

            fim = int(input("Voce quer sair do jogo (digite 1) ou quer tentar de novo (digite 2)? "))

            if fim == 1:

                break

            elif fim == 2:

                break

            else: 

                continue
        
        if fim == 1:

            break

        else: 

            vidaP = 10 
            vidaM = 20

            while True:

                personagem = int(input("\n Escolha entre ser um mago (digite 1) ou um guerreiro (digite 2) --> "))

                if personagem == 1:

                    print(f"\n Seu personagem: Mago")
                    print(f" Sua vida e: {vidaP}")

                    poder = aleatorio.randint(7,ataque_MAX_ma)

                    print(f" Sua barra de poder: {poder}")

                    break

                elif personagem == 2:

                    print(f"\n Seu personagem: Guerreiro")
                    print(f" Sua vida e: {vidaP}")

                    poder = aleatorio.randint(5,ataque_MAX_gue)

                    print(f" Sua barra de poder: {poder}")

                    break

                else:

                    continue

            continue


    
    if vidaM <= 0:

        time.sleep(1)

        print("\n --> O monstro morreu <-- \n")

        while True:

            resposta = int(input(" Voce quer sair do jogo (digite 1) ou continuar (digite 2)? "))

            if resposta == 1:

                break

            elif resposta == 2:


                break

            else: 

                continue
    
        if resposta == 1:

            break

        else: 

            #repor vida 

            vidaP = 10
            vidaM = 10
            ataqueM = ataqueM + 3

            if personagem == 1:

                ataque_MAX_ma = ataque_MAX_ma + 3

            else:

                ataque_MAX_gue = ataque_MAX_gue + 3

            vidaP = vidaP + 5



            continue


#Caso o usuário após matar um monstro queira continuar jogando
#toda a sua vida é recuperada e o próximo monstro gerado terá 10 de vida e 3 de ataque a mais que o último e o jogador ganhará mais 3 de probabilidade de ataque e mais 5 de vida

