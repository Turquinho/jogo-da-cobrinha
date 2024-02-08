import pygame
import random

pygame.init()
pygame.display.set_caption("Jogo da Cobrinha Python")

#Tela
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)

# Parametros cobrinha
tamanhoQuadrado = 10
velocidadeAtualizacao = 15

def gerarComida():
    comidaX = round(random.randrange(0, largura - tamanhoQuadrado) / float(tamanhoQuadrado)) * float(tamanhoQuadrado)
    comidaY = round(random.randrange(0, altura - tamanhoQuadrado)/ float(tamanhoQuadrado)) * float(tamanhoQuadrado)
    return comidaX, comidaY

def desenharComida(tamanho, comidaX, comidaY):
    pygame.draw.rect(tela, branco, [comidaX, comidaY, tamanho, tamanho])

def desenharCobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, verde, [pixel[0], pixel[1], tamanho, tamanho])

def desenharPontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 30)
    texto = fonte.render(f'Pontos: {pontuacao}', True, vermelho)
    tela.blit(texto, [4, 4])

def selecionarVelocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidadeX = 0
        velocidadeY = tamanhoQuadrado
    elif tecla == pygame.K_UP:
        velocidadeX = 0
        velocidadeY = -tamanhoQuadrado
    elif tecla == pygame.K_RIGHT:
        velocidadeX = tamanhoQuadrado
        velocidadeY = 0
    elif tecla == pygame.K_LEFT:
        velocidadeX = -tamanhoQuadrado
        velocidadeY = 0
    return velocidadeX, velocidadeY


def rodarJogo():
    fimJogo = False

    x = largura / 2
    y = altura / 2

    velocidadeX = 0
    velocidadeY = 0

    tamanhoCobra = 1
    pixels = []

    comidaX, comidaY = gerarComida()

    while not fimJogo:
        tela.fill(preto)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fimJogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidadeX, velocidadeY = selecionarVelocidade(evento.key)
        
   

        #Desenho comida
        desenharComida(tamanhoQuadrado, comidaX, comidaY)

        #atualizar a posição da cobra
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fimJogo = True

        x += velocidadeX
        y += velocidadeY

        #Desenho cobra
        pixels.append([x, y])
        if len(pixels) > tamanhoCobra:
            del pixels[0]
         #Atualizar posição da cobra
        

        # Se a cobra bater no própio corpo
        for pixel in pixels[:-1]:       # Tira a cabeça da análise
            if pixel == [x, y]:
                fimJogo = True
        
        desenharCobra(tamanhoQuadrado, pixels)
        desenharPontuacao(tamanhoCobra - 1)



        #atualização da tela
        pygame.display.update()

        # Criar uma nova comida
        if x == comidaX and y == comidaY:
            tamanhoCobra +=1
            comidaX, comidaY = gerarComida()
        

        relogio.tick(velocidadeAtualizacao)

rodarJogo()
# Criar lógica de terminar o jogo - Cobra bateu na parede, ou a cobra bateu na própria cobra

# Interações do usuário - fechou a tela, teclas do teclado com movimentação