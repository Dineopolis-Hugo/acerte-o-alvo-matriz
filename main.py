import random
import pygame
tempo = 30
LINHAS = 3
COLUNAS = 3
pontos = 0
alvo_total = 0


def matriz():
    matriz= [[000]*COLUNAS for i in range(LINHAS)]
    return matriz

def percorrerMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print([i],[j])
            #J = linha I = COLUNA

def escolheralvo():
    if tempo >15:
    #Máximo de alvos na matriz
         alvo_max = 1    

    elif tempo <= 15 and tempo > 0:
        alvo_max = 2
       
    else:
        alvo_max=0    
        
            
    alvo_total =sum(linha.count(1) for linha in matriz)
    #conta a quantidades de 1 na matriz e daí vê o total de alvos 
    while alvo_total < alvo_max:
        linha_escolhida = random.randint(0,2)
        Coluna_escolhida = random.randint(0,2)
        #Enquanto não estiver o maximo de alvo ele sorteia outro novo

        if matriz[linha_escolhida][Coluna_escolhida] == 0:
            matriz [linha_escolhida][Coluna_escolhida] = 1
            alvo_total+=1
        #Se a posição sorteada estiver vazia adiciona alvo, senão volta no while para escolher outra posição    
#MAIN
matriz = matriz()
escolheralvo()
pygame.init()

tela = pygame.display.set_mode((600, 600))
#tamanho tela
pygame.display.set_caption("Acerte o Alvo")
#titulo na janela


inicio = pygame.time.get_ticks()
rodando = True

while rodando:
    tempo = 30 - (pygame.time.get_ticks() - inicio) // 1000
    #Começa a baixar o tempo com ticks
    if tempo <= 0:
        rodando = False
    #Se o tempo acabar fecha

    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                x,y = evento.pos
                #evento.pos pega a posição do mouse na tela.
                coluna = x  // 200
                #x // 200 descobre a coluna clicada dividindo por 200 e retorna 0,1,2
                linha = y // 200
                print("linha ",linha ,"coluna ",coluna)

                if matriz[linha][coluna] == 1:
                    #se clicar no alvo ele volta a ser 0 na matriz e ganha pontos
                    print("ACERTOU")
                    matriz[linha][coluna]= 0
                    pontos+= 10
                    print("pontuação",pontos)

                    escolheralvo()
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill((255, 255, 255))

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            pygame.draw.rect(
                tela, (200, 0, 0),
                (j * 200, i * 200, 200, 200), 2
            )
            if matriz[i][j] == 1:
                pygame.draw.rect(tela,(200,0,0),(j * 200 ,i * 200,200,200 ))

    pygame.display.flip()
    #criar matriz

  

pygame.quit()