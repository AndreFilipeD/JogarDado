import random
import pygame
from pygame.locals import *
from sys import exit

pygame.init()

# Configurações de tela do projeto
pygame.display.set_caption('Jogar Dados Python - André')
tempo = pygame.time.Clock()
telalargura = 640
telaaltura = 480
fps = 60
# Configurações base do dado
dlargura = 100
daltura = 100
dx = telaaltura/4
dy = (telaaltura / 2)-(daltura/2)
dz = 10
# variaves do projeto
cont = 0

ndado = random.randint(1, 6)
throw = False
speed = 0

power = 0
bounce = 0
secbounce = 0
bouncemax = 0
angle = 0
stop = 0
result = ndado

neverlaunch = True

fonte = pygame.font.SysFont('arial', 40, True, True)
# Texto contador e informativo || Parametros fonte: Tipo de texto, tamanho do texto, negrito, italico

tela = pygame.display.set_mode((telalargura, telaaltura))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if not throw and stop == 0:
                    throw = True
                    power = random.randint(5, 10)
                    angle = random.randint(-1, 2)
                    secbounce = bounce = bouncemax = power
                    cont = 0
                    stop = 1
                    if neverlaunch:
                        neverlaunch = False
                elif stop == 2:
                    # throw = False
                    dx = telaaltura / 4
                    dy = (telaaltura / 2) - (daltura / 2)
                    throw = True
                    power = random.randint(5, 10)
                    angle = random.randint(-1, 2)
                    secbounce = bounce = bouncemax = power
                    cont = 0
                    stop = 1
# botões de controle
    '''if pygame.key.get_pressed()[K_a]:
        if ndado >= 6:
            ndado = 1
        else:
            ndado += 1'''

# Objetos visuais do projeto
    if throw:
        pygame.draw.rect(tela, (145, 120, 110), (dx-15, dy-15, dlargura, daltura))
    pygame.draw.rect(tela, (255, 255, 255), (dx, dy, dlargura, daltura))
    # Dado e sua sombra, quando ele for jogado.
    ultres = f'Ultimo resultado {result}'
    if stop == 0 and neverlaunch:
        mensagem = f'Aperte espaço para lançar'
    elif stop == 1:
        mensagem = f''
    else:
        mensagem = f'espaço para lançar denovo'
    textoa = fonte.render(ultres, False, (255, 255, 255))
    textob = fonte.render(mensagem, False, (255, 255, 255))
    # Texto informativo

    if throw and stop == 1:
        dx += ((power*5)-cont)/3
        dy += angle
        cont += 1
        if bounce > 0:
            daltura -= bounce
            dlargura -= bounce
            bounce -= 1
            ndado = random.randint(1, 6)
            # dado caindo
        elif secbounce > 0:
            daltura += secbounce
            dlargura += secbounce
            secbounce -= 1
            ndado = random.randint(1, 6)
            # dado subindo
        else:
            bouncemax -= 2
            bounce = secbounce = bouncemax
        if cont >= power * 5:
            stop = 2
            result = ndado
            # Final do arremeço, aguardando ser lançado pela variavel stop

    # Faces do dado de 1 a 6 renderizado usando metodo circle.
    if ndado == 1:
        pygame.draw.circle(tela, (0, 0, 0), (dx+dlargura/2, dy+daltura/2), ((daltura+dlargura)/16))
    elif ndado == 2:
        pygame.draw.circle(tela, (0, 0, 0), (dx + dlargura / 4, dy + daltura / 4), ((daltura + dlargura) / 16))
        pygame.draw.circle(tela, (0, 0, 0), (dx + dlargura * 0.75, dy + daltura * 0.75), ((daltura + dlargura) / 16))
    elif ndado == 3:
        pygame.draw.circle(tela, (0, 0, 0), (dx + dlargura / 2, dy + daltura / 2), ((daltura + dlargura) / 16))
        pygame.draw.circle(tela, (0, 0, 0), (dx + dlargura / 4, dy + daltura / 4), ((daltura + dlargura) / 16))
        pygame.draw.circle(tela, (0, 0, 0), (dx + dlargura * 0.75, dy + daltura * 0.75), ((daltura + dlargura) / 16))
    elif ndado == 4:
        pygame.draw.circle(tela, (0, 0, 0), (dx + dlargura / 4, dy + daltura * 0.75), ((daltura + dlargura) / 16))
        pygame.draw.circle(tela, (0, 0, 0), (dx + dlargura * 0.75, dy + daltura / 4), ((daltura + dlargura) / 16))
        pygame.draw.circle(tela, (0, 0, 0), (dx + dlargura / 4, dy + daltura / 4), ((daltura + dlargura) / 16))
        pygame.draw.circle(tela, (0, 0, 0), (dx + dlargura * 0.75, dy + daltura * 0.75), ((daltura + dlargura) / 16))
    elif ndado == 5:
        pygame.draw.circle(tela, (0, 0, 0), (dx + dlargura / 4, dy + daltura * 0.75), ((daltura + dlargura) / 16))
        pygame.draw.circle(tela, (0, 0, 0), (dx + dlargura * 0.75, dy + daltura / 4), ((daltura + dlargura) / 16))
        pygame.draw.circle(tela, (0, 0, 0), (dx + dlargura / 4, dy + daltura / 4), ((daltura + dlargura) / 16))
        pygame.draw.circle(tela, (0, 0, 0), (dx + dlargura * 0.75, dy + daltura * 0.75), ((daltura + dlargura) / 16))
        pygame.draw.circle(tela, (0, 0, 0), (dx + dlargura / 2, dy + daltura / 2), ((daltura + dlargura) / 16))
    elif ndado == 6:
        pygame.draw.circle(tela, (0, 0, 0), (dx + dlargura / 4, dy + daltura * 0.75), ((daltura + dlargura) / 22))
        pygame.draw.circle(tela, (0, 0, 0), (dx + dlargura * 0.75, dy + daltura / 4), ((daltura + dlargura) / 22))
        pygame.draw.circle(tela, (0, 0, 0), (dx + dlargura / 4, dy + daltura / 4), ((daltura + dlargura) / 22))
        pygame.draw.circle(tela, (0, 0, 0), (dx + dlargura * 0.75, dy + daltura * 0.75), ((daltura + dlargura) / 22))
        pygame.draw.circle(tela, (0, 0, 0), (dx + dlargura / 4, dy + daltura/2), ((daltura + dlargura) / 22))
        pygame.draw.circle(tela, (0, 0, 0), (dx + dlargura * 0.75, dy + daltura/2), ((daltura + dlargura) / 22))
# Renderizando a tela e textos
    pygame.display.update()
    tempo.tick(fps)
    tela.fill((195, 170, 150))
    tela.blit(textoa, (150, 40))
    tela.blit(textob, (70, 400))
