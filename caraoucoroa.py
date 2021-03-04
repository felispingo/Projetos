#importando módulo para pegar número aleatório
import random

#continuar jogando, por padrão é 1 (True)
cj = 1

#pontuação (por padrão, 0)
carap1 = coroap1 = carap2 = coroap2 = vp1 = vp2 = cdp = 0

#definindo os players
p1 = input("Nome do player 1: ")
p2 = input("Nome do player 2: ")

#enquanto continuar jogando = 1 (True)
while cj == 1:
    #pula linha - questões estéticas
    print()

    #escolhendo número aleatório entre 0 e 1
    #obs: se for menor do que 0.5, será coroa; se for maior, cara; e se for exatamente 0.5, empate
    r = random.random()

    #pergunta se continua jogando, se dar enter assume-se que sim
    cj = int(input("Continuar jogando? (0/1) ") or '1')

    #se continuar jogando
    if cj == 1:

        #cara ou coroa (1 ou 2), se dar enter assume-se cara
        cc = int(input("Qual a aposta do p1? (Cara = 1, Coroa = 2): ") or '1')

        #se apostar cara e der cara
        if cc == 1 and r > 0.5:

            #ipmrime resultado
            print("Cara")

            #soma 1 ao placar (cara) do p1
            carap1 = carap1 + 1

        #se apostar cara e der coroa
        elif cc == 1 and r < 0.5:

            #imprime resultado
            print("Coroa")

            #soma 1 ao placar (coroa) do p2
            coroap2 = coroap2 + 1

        #se apostar coroa e der cara
        if cc == 2 and r > 0.5:

            #imprime resultado
            print("Cara")

            #adiciona 1 ao placar (cara) do p2
            carap2 = carap2 + 1
        elif cc == 2 and r < 0.5:

            #imprime resultado
            print("Coroa")

            #adiciona 1 ao placar (coroa) do p1
            coroap1 = coroap1 + 1

        #se a moeda cair em pé
        if r == 0.5:

            #imprime resultado
            print("Então... caiu de pé: é empate")

            #adiciona 1 na variavel caiu de pe (cdp)
            cdp += 1
            
    #se não continuar jogando
    else:
        #avisa que o jogo acabou
        print("O jogo acabou .-.")

        #pula linha
        print()

        #soma cara e coroa de cada jogador para dar o placar final
        vp1 = carap1 + coroap1
        vp2 = carap2 + coroap2

#imprime o placar e quantas vezes cada jogador acertou cada coisa
print(p1,"acertou cara",carap1,"vezes e coroa",coroap1,"vezes!")
print("Somando um total de",vp1,"pontos")
print()

print(p2,"acertou cara",carap2,"vezes e coroa",coroap2,"vezes!")
print("Somando um total de",vp2,"pontos")
print()

#imprime, se ocorreu, quantas vezes a moeda caiu de pé
if cdp > 0:
    print("Incrivelmente, a moeda caiu de pé",cdp,"vez.")

#imprime quem ganhou, ou se deu empate
if vp1 > vp2:
    print(p1,"venceu!")
elif vp2 > vp1:
    print(p2,"venceu!")
else:
    print(p1,"empatou com",p2)

#declara e imprime duração do jogo (ddj)
ddj = vp1 + vp2
print("A moeda foi lançada",ddj,"vezes")
print()
if ddj > 50 and ddj < 99.5:
    print("Ta maluco?")
elif ddj > 99.5 and ddj < 499.5:
    print("Não tem nada melhor para fazer não?")
elif ddj > 499.5:
    print("Sério, vai fazer outra coisa")
else:
    print("Obrigado por jogar : )")
