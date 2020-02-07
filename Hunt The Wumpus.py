import pygame, random, time, os

os.chdir("assets")

def linhas(tela, cor, altura, largura, tamanho):
    x, y = 100, 100
    for i in range(0, tamanho + 1):
        pygame.draw.line(tela, cor,(x * i, 0), (x * i, largura), 3)
    for i in range(0, tamanho + 1):
        pygame.draw.line(tela, cor,(0, y * i), (altura, y * i), 3)

class Mapa(object):
    def __init__(self):
        self.terra = pygame.image.load("terra.png")
        self.grama = pygame.image.load("grama.png")
    
    def exibirMapa(self):
        for i in range(tamanho):
            for j in range(tamanho):
                x = 100 * i
                y = 100 * j
                k = [x, y]
                tela.blit(self.terra, (x, y))
                if x == 0 and y == 0 or k in jogador.mov:
                    tela.blit(self.grama, (x, y))

class Abismos(object):
    def __init__(self):
        self.local = []
        self.abismo = pygame.image.load("abismo.png")
        self.vento = pygame.image.load("vento.png")
    
    def gerar(self):
        quantidade = ((tamanho ** 2) * 0.15) - 1
        if quantidade < 2:
            quantidade = 2
        while len(self.local) <= quantidade:
            p = random.randrange(0, altura, 200)
            q = random.randrange(100, largura, 200)
            z = [p, q]
            if z not in self.local:
                self.local.append(z)
            
    def exibirAbismo(self):
        for i in self.local:
            if i in jogador.mov:
                tela.blit(self.abismo, (i[0], i[1]))
            
    def exibirVento(self):
        for i in self.local:
            posVento = [[i[0] + 100, i[1]], [i[0] - 100, i[1]], [i[0], i[1] + 100], [i[0], i[1] - 100]]
            for i in posVento:
                if i in jogador.mov:
                    tela.blit(self.vento, (i[0], i[1]))

class Wumpus(object):
    def __init__(self):
        self.status = "Vivo"
        self.wumpus = pygame.image.load("wumpus.png")
        self.pegadas = pygame.image.load("pegadas.png")
        self.pos = [random.randrange(100, altura, 100), random.randrange(100, largura, 100)]
                
    def exibirWumpus(self):
        if self.pos in jogador.mov and self.status == "Vivo":
            tela.blit(self.wumpus, (self.pos[0], self.pos[1]))
            
    def exibirPegadas(self):
        posPegadas = [[self.pos[0] + 100, self.pos[1]], [self.pos[0] - 100, self.pos[1]], [self.pos[0], self.pos[1] + 100], [self.pos[0], self.pos[1] - 100]]
        for i in posPegadas:
            if i in jogador.mov:
                tela.blit(self.pegadas, (i[0], i[1]))

class Ouro(object):
    def __init__(self):
        self.status = "Intacto"
        self.ouro = pygame.image.load("ouro.png")
        self.brilho = pygame.image.load("brilho.png")
        self.pos = [random.randrange(100, altura, 100), random.randrange(100, largura, 100)]

    def exibirOuro(self):
        global status, jogador
        if self.pos in jogador.mov:
            tela.blit(self.ouro, (self.pos[0], self.pos[1]))
            status.msg = "Você pegou o ouro!"
            if self.status == "Intacto":
                jogador.pontos += 1000
            self.status = "Coletado"

    def exibirBrilho(self):
        posBrilho = [[self.pos[0] + 100, self.pos[1]], [self.pos[0] - 100, self.pos[1]], [self.pos[0], self.pos[1] + 100], [self.pos[0], self.pos[1] - 100]]
        for i in posBrilho:
            if i in jogador.mov:
                tela.blit(self.brilho, (i[0], i[1]))

class Flecha(object):
    def __init__(self):
        self.imagem = pygame.image.load("flecha.png")
        self.flecha = self.imagem
        self.tiro = []
        self.quantidade = 1
        self.alcance = 1000
    
    def calcularTiro(self):
        global status
        if self.quantidade > 0:
            self.quantidade -= 1
            self.tiro = []
            
            if jogador.olhar == "Baixo":
                for i in range(jogador.mov[-1][1], jogador.mov[-1][1] + self.alcance, 100):
                    posTiro = [jogador.mov[-1][0], i]
                    acerto = self.verificarTiro(posTiro)
                    if acerto == 0:
                        self.tiro.append(posTiro)
                    else:
                        break
            
            if jogador.olhar == "Direita":
                for i in range(jogador.mov[-1][0], jogador.mov[-1][0] + self.alcance, 100):
                    posTiro = [i, jogador.mov[-1][1]]
                    acerto = self.verificarTiro(posTiro)
                    if acerto == 0:
                        self.tiro.append(posTiro)
                    else:
                        break
            
            if jogador.olhar == "Esquerda":
                for i in range(jogador.mov[-1][0], jogador.mov[-1][0] - self.alcance, -100):
                    posTiro = [i, jogador.mov[-1][1]]
                    acerto = self.verificarTiro(posTiro)
                    if acerto == 0:
                        self.tiro.append(posTiro)
                    else:
                        break
            
            if jogador.olhar == "Cima":
                for i in range(jogador.mov[-1][1], jogador.mov[-1][1] - self.alcance, -100):
                    posTiro = [jogador.mov[-1][0], i]
                    acerto = self.verificarTiro(posTiro)
                    if acerto == 0:
                        self.tiro.append(posTiro)
                    else:
                        break
            
            self.exibirTiro()
            jogador.mudarImagem()
            
        else:
            status.msg = "Você não possui uma flecha para atirar!"
            tela.blit(jogador.jogador, (x, y))
            pygame.display.update()
        
    def exibirTiro(self):     
        for i in self.tiro:
            time.sleep(0.01)
            mapa.exibirMapa()
            ouro.exibirBrilho()
            ouro.exibirOuro()
            abismo.exibirVento()
            abismo.exibirAbismo()
            wumpus.exibirWumpus()
            wumpus.exibirPegadas()
            tela.blit(jogador.jogador, (x, y))
            tela.blit(self.flecha, (i[0], i[1]))
            status.todos()
            pygame.display.update()
            
    def verificarTiro(self, posTiro):
        global status, wumpus, jogador
        if posTiro == wumpus.pos and wumpus.status == "Vivo":
            wumpus.status = "Morto"
            jogador.pontos += 10000
            status.msg = "Sua flecha acertou o Wumpus!"
            pygame.display.update()
            return 1
        else:
            return 0
        
        if posTiro in abismo.local:
            status.msg = "Sua flecha caiu no abismo!"
            status.todos()
            pygame.display.update()
            return 1
        else:
            return 0
         
class Jogador(object):
    def __init__(self):
        self.status = "Vivo"
        self.pontos = 0
        self.mov = [[0, 0]]
        self.imagem = pygame.image.load("jogadorComFlecha.png")
        self.jogador = self.imagem
        self.olhar = "Direita"

    def mudarImagem(self):
        if flecha.quantidade <= 0:
            self.imagem = pygame.image.load("jogadorSemFlecha.png")

    def moverCima(self):
        global x, y, flecha
        if self.status == "Vivo":
            y -= 100
            k = [x, y]
            self.olhar = "Cima"
            self.mov.append(k)
            self.jogador = pygame.transform.rotate(self.imagem, 90)
            flecha.flecha = pygame.transform.rotate(flecha.imagem, 90)
    
    def moverBaixo(self):
        global x, y, flecha
        if self.status == "Vivo":
            y += 100
            k = [x, y]
            self.olhar = "Baixo"
            self.mov.append(k)
            self.jogador = pygame.transform.rotate(self.imagem, -90)
            flecha.flecha = pygame.transform.rotate(flecha.imagem, -90)

    def moverDireita(self):
        global x, y, flecha
        if self.status == "Vivo":
            x += 100
            k = [x, y]
            self.olhar = "Direita"
            self.mov.append(k)
            self.jogador = self.imagem
            flecha.flecha = flecha.imagem
        
    def moverEsquerda(self):
        global x, y, flecha
        if self.status == "Vivo":
            x -= 100
            k = [x, y]
            self.olhar = "Esquerda"
            self.mov.append(k)
            self.jogador = pygame.transform.flip(self.imagem, True, False)
            flecha.flecha = pygame.transform.flip(flecha.imagem, True, False)
    
    def salvarDados(self):
        arq = open("pontos.txt", "r")
        conteudo = arq.readlines()
        string = str(self.pontos) + " " + str(len(self.mov)) + "\n"
        conteudo.append(string)
        arq = open("pontos.txt", "w")
        arq.writelines(conteudo)
        arq.close()
        
    def morte(self):
        global status
        for i in self.mov:
            if i == wumpus.pos and wumpus.status == "Vivo":
                status.msg = "Você foi morto pelo Wumpus!"
                if self.status == "Vivo":
                    self.pontos -= 10000
                    self.status = "Morto"
                    status.todos()
                    pygame.display.update()
                    aviso = status.aviso()
                    if aviso == 1:
                        return 1

            if i in abismo.local:
                status.msg = "Você caiu no abismo!"
                if self.status == "Vivo":
                    self.pontos -= 10000
                    self.status = "Morto"
                    status.todos()
                    pygame.display.update()
                    aviso = status.aviso()
                    if aviso == 1:
                        return 1
                    
    def vitoria(self):
        global status
        if wumpus.status == "Morto" and ouro.status == "Coletado" and self.mov[-1] == [0, 0]:
            self.pontos += 100
            status.msg = "Você venceu o jogo!"
            status.todos()
            pygame.display.update()
            self.salvarDados()
            vitoria = status.vitoria()
            if vitoria == 1:
                return 1
        
        if self.mov[-1] == [0, 0] and ouro.status == "Coletado":
            self.pontos += 100
            status.msg = "Você venceu o jogo!"
            status.todos()
            pygame.display.update()
            self.salvarDados()
            vitoria = status.vitoria()
            if vitoria == 1:
                return 1

class Status(object):
    def __init__(self):
        self.fonte = pygame.font.SysFont(None, 30)
        self.fonteAviso = pygame.font.SysFont(None, 70)
        self.cor = cor["branco"]
        self.msg = "Bem vindo ao mundo de Wumpus"

    def quadro(self):
        pygame.draw.rect(tela, cor["cinza_escuro"], (0, altura - 100, largura, 100))
        pygame.draw.rect(tela, cor["preto"], (0, altura - 100, largura, 100), 3)
        pygame.draw.rect(tela, cor["branco"], (10, altura - 40, largura - 20, 30))
        pygame.draw.rect(tela, cor["preto"], (10, altura - 40, largura - 20, 30), 3)
    
    def pontos(self):
        string = self.fonte.render("Pontos: " + str(jogador.pontos), True, self.cor)
        tela.blit(string, (15, altura - 90))
    
    def olhar(self):
        texto = "Olhar: " + jogador.olhar
        string = self.fonte.render(texto, True, self.cor)
        tela.blit(string, (largura // 2 - 50, altura - 90))

    def wumpus(self):
        texto = "Wumpus: " + wumpus.status
        string = self.fonte.render(texto, True, self.cor)
        tela.blit(string, (largura // 2 - 50, altura - 70))

    def ouro(self):
        string = self.fonte.render("Ouro: " + ouro.status, True, self.cor)
        tela.blit(string, (15, altura - 70))
        
    def flechas(self):
        string = self.fonte.render("Flechas: " + str(flecha.quantidade), True, self.cor)
        tela.blit(string, (largura - 115, altura - 90))
        
    def info(self):
        string = self.fonte.render(self.msg, True, cor["preto"])
        tela.blit(string, (15, altura - 35))
    
    def todos(self):
        self.quadro()
        self.pontos()
        self.wumpus()
        self.info()
        self.ouro()
        self.olhar()
        self.flechas()
        
    def aviso(self):
        aviso = self.fonteAviso.render("Você morreu!", True, cor["preto"])
        reiniciar = self.fonte.render("Reiniciar", True, cor["preto"])
        sair = self.fonte.render("Sair", True, cor["preto"])
        posReiniciar = [largura // 2 - 125, altura // 2 - 50]
        posSair = [largura // 2 + 20, altura // 2 - 50]
        sairAviso = False
        
        while sairAviso != True:
            pygame.draw.rect(tela, (189, 196, 202), (largura // 2 - 170, altura // 2 - 150, 340, 160))
            pygame.draw.rect(tela, cor["preto"], (largura // 2 - 170, altura // 2 - 150, 340, 160), 3)
            mouse = pygame.mouse.get_pos()
            clique = pygame.mouse.get_pressed()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sairAviso = True
                    
            if posReiniciar[0] + 100 > mouse[0] > posReiniciar[0] and posReiniciar[1] + 40 > mouse[1] > posReiniciar[1]:
                pygame.draw.rect(tela, cor["verde"], (posReiniciar[0], posReiniciar[1], 100, 40))
                pygame.draw.rect(tela, cor["preto"], (posReiniciar[0], posReiniciar[1], 100, 40), 1)
                if clique[0] == 1:
                    inicializar()
            else:
                pygame.draw.rect(tela, cor["verde_escuro"], (posReiniciar[0], posReiniciar[1], 100, 40))
                pygame.draw.rect(tela, cor["preto"], (posReiniciar[0], posReiniciar[1], 100, 40), 1)
            
            if posSair[0] + 100 > mouse[0] > posSair[0] and posSair[1] + 40 > mouse[1] > posSair[1]:
                pygame.draw.rect(tela, cor["vermelho"], (posSair[0], posSair[1], 100, 40))
                pygame.draw.rect(tela, cor["preto"], (posSair[0], posSair[1], 100, 40), 1)
                if clique[0] == 1:
                    sairAviso = True
            else:
                pygame.draw.rect(tela, cor["vermelho_escuro"], (posSair[0], posSair[1], 100, 40))
                pygame.draw.rect(tela, cor["preto"], (posSair[0], posSair[1], 100, 40), 1)
            
            tela.blit(aviso, (largura // 2 - 155, altura // 2 - 120))
            tela.blit(reiniciar, (posReiniciar[0] + 5, posReiniciar[1] + 10))
            tela.blit(sair, (posSair[0] + 30, posSair[1] + 10))
            pygame.display.update()
        return 1
            
    def pausa(self):
        aviso = self.fonteAviso.render("Pausa", True, cor["preto"])
        reiniciar = self.fonte.render("Reiniciar", True, cor["preto"])
        continuar = self.fonte.render("Continuar", True, cor["preto"])
        sair = self.fonte.render("Sair", True, cor["preto"])
        posContinuar = [largura // 2 - 55, altura // 2 - 50]
        posReiniciar = [largura // 2 - 165, altura // 2 - 50]
        posSair = [largura // 2 + 65, altura // 2 - 50]
        sairPausa = False
        
        while sairPausa != True:
            pygame.draw.rect(tela, (189, 196, 202), (largura // 2 - 180, altura // 2 - 150, 360, 160))
            pygame.draw.rect(tela, cor["preto"], (largura // 2 - 180, altura // 2 - 150, 360, 160), 3)
            mouse = pygame.mouse.get_pos()
            clique = pygame.mouse.get_pressed()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sairPausa = True
                    return 1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        sairPausa = True
                    return 0
            
            if posContinuar[0] + 110 > mouse[0] > posContinuar[0] and posContinuar[1] + 40 > mouse[1] > posContinuar[1]:
                pygame.draw.rect(tela, cor["azul"], (posContinuar[0], posContinuar[1], 110, 40))
                pygame.draw.rect(tela, cor["preto"], (posContinuar[0], posContinuar[1], 110, 40), 1)
                if clique[0] == 1:
                    sairPausa = True
                    return 0
            else:
                pygame.draw.rect(tela, cor["azul_escuro"], (posContinuar[0], posContinuar[1], 110, 40))
                pygame.draw.rect(tela, cor["preto"], (posContinuar[0], posContinuar[1], 110, 40), 1)
            
            if posReiniciar[0] + 100 > mouse[0] > posReiniciar[0] and posReiniciar[1] + 40 > mouse[1] > posReiniciar[1]:
                pygame.draw.rect(tela, cor["verde"], (posReiniciar[0], posReiniciar[1], 100, 40))
                pygame.draw.rect(tela, cor["preto"], (posReiniciar[0], posReiniciar[1], 100, 40), 1)
                if clique[0] == 1:
                    inicializar()
            else:
                pygame.draw.rect(tela, cor["verde_escuro"], (posReiniciar[0], posReiniciar[1], 100, 40))
                pygame.draw.rect(tela, cor["preto"], (posReiniciar[0], posReiniciar[1], 100, 40), 1)
            
            if posSair[0] + 100 > mouse[0] > posSair[0] and posSair[1] + 40 > mouse[1] > posSair[1]:
                pygame.draw.rect(tela, cor["vermelho"], (posSair[0], posSair[1], 100, 40))
                pygame.draw.rect(tela, cor["preto"], (posSair[0], posSair[1], 100, 40), 1)
                if clique[0] == 1:
                    sairPausa = True
                    return 1
            else:
                pygame.draw.rect(tela, cor["vermelho_escuro"], (posSair[0], posSair[1], 100, 40))
                pygame.draw.rect(tela, cor["preto"], (posSair[0], posSair[1], 100, 40), 1)
            
            tela.blit(aviso, (largura // 2 - 70, altura // 2 - 120))
            tela.blit(continuar, (posContinuar[0] + 5, posContinuar[1] + 10))
            tela.blit(reiniciar, (posReiniciar[0] + 5, posReiniciar[1] + 10))
            tela.blit(sair, (posSair[0] + 30, posSair[1] + 10))
            pygame.display.update()
    
    def vitoria(self):
        aviso = self.fonteAviso.render("Você ganhou!", True, cor["preto"])
        pontos = self.fonte.render("Pontos: " + str(jogador.pontos), True, cor["preto"])
        movimentos = self.fonte.render("Movimentos: " + str(len(jogador.mov)), True, cor["preto"])
        wumpusStatus = self.fonte.render("Wumpus: " + wumpus.status, True, cor["preto"])
        ouroStatus = self.fonte.render("Ouro: " + ouro.status, True, cor["preto"])
        reiniciar = self.fonte.render("Reiniciar", True, cor["preto"])
        sair = self.fonte.render("Sair", True, cor["preto"])
        posReiniciar = [largura // 2 - 125, altura // 2 + 30]
        posSair = [largura // 2 + 20, altura // 2 + 30]
        sairVitoria = False
        
        while sairVitoria != True:
            pygame.draw.rect(tela, cor["cinza_claro"], (largura // 2 - 170, altura // 2 - 150, 340, 250))
            pygame.draw.rect(tela, cor["preto"], (largura // 2 - 170, altura // 2 - 150, 340, 250), 3)
            mouse = pygame.mouse.get_pos()
            clique = pygame.mouse.get_pressed()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sairVitoria = True
            
            if posReiniciar[0] + 100 > mouse[0] > posReiniciar[0] and posReiniciar[1] + 40 > mouse[1] > posReiniciar[1]:
                pygame.draw.rect(tela, cor["verde"], (posReiniciar[0], posReiniciar[1], 100, 40))
                pygame.draw.rect(tela, cor["preto"], (posReiniciar[0], posReiniciar[1], 100, 40), 1)
                if clique[0] == 1:
                    inicializar()
            else:
                pygame.draw.rect(tela, cor["verde_escuro"], (posReiniciar[0], posReiniciar[1], 100, 40))
                pygame.draw.rect(tela, cor["preto"], (posReiniciar[0], posReiniciar[1], 100, 40), 1)
            
            if posSair[0] + 100 > mouse[0] > posSair[0] and posSair[1] + 40 > mouse[1] > posSair[1]:
                pygame.draw.rect(tela, cor["vermelho"], (posSair[0], posSair[1], 100, 40))
                pygame.draw.rect(tela, cor["preto"], (posSair[0], posSair[1], 100, 40), 1)
                if clique[0] == 1:
                    sairVitoria = True
            else:
                pygame.draw.rect(tela, cor["vermelho_escuro"], (posSair[0], posSair[1], 100, 40))
                pygame.draw.rect(tela, cor["preto"], (posSair[0], posSair[1], 100, 40), 1)
            
            tela.blit(aviso, (largura // 2 - 160, altura // 2 - 120))
            tela.blit(pontos, (largura // 2 - 160, altura // 2 - 50))
            tela.blit(movimentos, (largura // 2 - 160, altura // 2 - 30))
            tela.blit(wumpusStatus, (largura // 2 + 5, altura // 2 - 50))
            tela.blit(ouroStatus, (largura // 2 + 5, altura // 2 - 30))
            tela.blit(reiniciar, (posReiniciar[0] + 5, posReiniciar[1] + 10))
            tela.blit(sair, (posSair[0] + 30, posSair[1] + 10))
            pygame.display.update()
        return 1

def config():
    global x, y, jogador, flecha, mapa, wumpus, ouro, abismo, status, sair
    x, y = 0, 0
    jogador = Jogador()
    flecha = Flecha()
    mapa = Mapa()
    wumpus = Wumpus()
    ouro = Ouro()
    abismo = Abismos()
    abismo.gerar()
    status = Status()
    sair = False
    return x, y, jogador, flecha, mapa, wumpus, ouro, abismo, status, sair

def game():
    global sair
    teclas = [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_f, pygame.K_p, pygame.K_DOWN, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT]
    while sair != True:        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            if event.type == pygame.KEYDOWN:
                if event.key not in teclas:
                    status.msg = "Tecla inválida!"
                else:
                    jogador.pontos -= 1
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        if y < (altura - 200):
                            jogador.moverBaixo()
                    
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        if y >= 100:
                            jogador.moverCima()
                    
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        if x < (largura - 100):
                            jogador.moverDireita()
                    
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        if x >= 100:
                            jogador.moverEsquerda()
                    
                    if event.key == pygame.K_f:
                        flecha.calcularTiro()
                    
                    if event.key == pygame.K_p:
                        jogador.pontos += 1
                        pausa = status.pausa()
                        if pausa == 1:
                            sair = True
        mapa.exibirMapa()
        ouro.exibirBrilho()
        ouro.exibirOuro()
        abismo.exibirVento()
        abismo.exibirAbismo()
        wumpus.exibirWumpus()
        wumpus.exibirPegadas()
        tela.blit(jogador.jogador, (x, y))
        status.todos()
        morte = jogador.morte()
        if morte == 1:
            sair = True
        vitoria = jogador.vitoria()
        if vitoria == 1:
            sair = True
        pygame.display.update()
    menu.fundo()

class Menu(object):
    def __init__(self):
        self.fonte = pygame.font.SysFont(None, 30)
        self.fontePrincipal = pygame.font.SysFont(None, 50)
        self.logo = pygame.image.load("logo.png")
        self.cor = cor["branco"]
        self.imagemFundo = pygame.image.load("terra.png")

    def fundo(self):
        for i in range(tamanho):
            for j in range(tamanho + 1):
                x = 100 * i
                y = 100 * j
                tela.blit(self.imagemFundo, (x, y))

    def recordes(self):
        recordes = self.fontePrincipal.render("Recordes", True, cor["preto"])
        posRet = [largura // 2 - 200, altura // 2 - 200]

        arq = open("pontos.txt", "r")
        dados = []
        for i in arq:
            k = i.split()
            g = [int(k[0]), int(k[1])]
            dados.append(g)
        arq.close()
        dados.sort()
        dados = dados[::-1]

        pontos0 = self.fonte.render("Pontos: " + str(dados[0][0]), True, cor["preto"])
        mov0 = self.fonte.render("Movimentos: " + str(dados[0][1]), True, cor["preto"])
        pontos1 = self.fonte.render("Pontos: " + str(dados[1][0]), True, cor["preto"])
        mov1 = self.fonte.render("Movimentos: " + str(dados[1][1]), True, cor["preto"])
        pontos2 = self.fonte.render("Pontos: " + str(dados[2][0]), True, cor["preto"])
        mov2 = self.fonte.render("Movimentos: " + str(dados[2][1]), True, cor["preto"])
        pontos3 = self.fonte.render("Pontos: " + str(dados[3][0]), True, cor["preto"])
        mov3 = self.fonte.render("Movimentos: " + str(dados[3][1]), True, cor["preto"])
        pontos4 = self.fonte.render("Pontos: " + str(dados[4][0]), True, cor["preto"])
        mov4 = self.fonte.render("Movimentos: " + str(dados[4][1]), True, cor["preto"])

        sair = False
        while sair != True:
            self.fundo()
            pygame.draw.rect(tela, (189, 196, 202), (posRet[0], posRet[1], 400, 400))
            pygame.draw.rect(tela, cor["preto"], (posRet[0], posRet[1], 400, 400), 3)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sair = True

            tela.blit(recordes, (posRet[0] + 120, posRet[1] + 30))
            tela.blit(pontos0, (posRet[0] + 40, posRet[1] + 100))
            tela.blit(mov0, (posRet[0] + 200, posRet[1] + 100))
            tela.blit(pontos1, (posRet[0] + 40, posRet[1] + 150))
            tela.blit(mov1, (posRet[0] + 200, posRet[1] + 150))
            tela.blit(pontos2, (posRet[0] + 40, posRet[1] + 200))
            tela.blit(mov2, (posRet[0] + 200, posRet[1] + 200))
            tela.blit(pontos3, (posRet[0] + 40, posRet[1] + 250))
            tela.blit(mov3, (posRet[0] + 200, posRet[1] + 250))
            tela.blit(pontos4, (posRet[0] + 40, posRet[1] + 300))
            tela.blit(mov4, (posRet[0] + 200, posRet[1] + 300))
            pygame.display.update()

    def menu(self):
        self.fundo()
        iniciar = self.fonte.render("Iniciar", True, cor["preto"])
        recordes = self.fonte.render("Recordes", True, cor["preto"])
        sair = self.fonte.render("Sair", True, cor["preto"])
        creditos = self.fonte.render("Criado por Pedro Lemos & Klaus Pereira", True, cor["preto"])
        posIniciar = [largura // 2 - 165, altura // 2 + 140]
        posRecordes = [largura // 2 - 55, altura // 2 + 140]
        posSair = [largura // 2 + 65, altura // 2 + 140]
        posCreditos = [largura // 2 - 215, altura // 2 + 200]
        sairMenu = False
        
        while sairMenu != True:
            tela.blit(self.logo, (largura // 2 - 200, altura // 2 - 250))
            mouse = pygame.mouse.get_pos()
            clique = pygame.mouse.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sairMenu = True
                    return 1
            
            if posRecordes[0] + 110 > mouse[0] > posRecordes[0] and posRecordes[1] + 40 > mouse[1] > posRecordes[1]:
                pygame.draw.rect(tela, cor["azul"], (posRecordes[0], posRecordes[1], 110, 40))
                pygame.draw.rect(tela, cor["preto"], (posRecordes[0], posRecordes[1], 110, 40), 1)
                if clique[0] == 1:
                    self.recordes()
                    self.fundo()
            else:
                pygame.draw.rect(tela, cor["azul_escuro"], (posRecordes[0], posRecordes[1], 110, 40))
                pygame.draw.rect(tela, cor["preto"], (posRecordes[0], posRecordes[1], 110, 40), 1)
            
            if posIniciar[0] + 100 > mouse[0] > posIniciar[0] and posIniciar[1] + 40 > mouse[1] > posIniciar[1]:
                pygame.draw.rect(tela, cor["verde"], (posIniciar[0], posIniciar[1], 100, 40))
                pygame.draw.rect(tela, cor["preto"], (posIniciar[0], posIniciar[1], 100, 40), 1)
                if clique[0] == 1:
                    inicializar()
            else:
                pygame.draw.rect(tela, cor["verde_escuro"], (posIniciar[0], posIniciar[1], 100, 40))
                pygame.draw.rect(tela, cor["preto"], (posIniciar[0], posIniciar[1], 100, 40), 1)
            
            if posSair[0] + 100 > mouse[0] > posSair[0] and posSair[1] + 40 > mouse[1] > posSair[1]:
                pygame.draw.rect(tela, cor["vermelho"], (posSair[0], posSair[1], 100, 40))
                pygame.draw.rect(tela, cor["preto"], (posSair[0], posSair[1], 100, 40), 1)
                if clique[0] == 1:
                    sairMenu = True
                    return 1
            else:
                pygame.draw.rect(tela, cor["vermelho_escuro"], (posSair[0], posSair[1], 100, 40))
                pygame.draw.rect(tela, cor["preto"], (posSair[0], posSair[1], 100, 40), 1)
            
            pygame.draw.rect(tela, cor["branco"], (posCreditos[0], posCreditos[1], 435, 40))
            tela.blit(creditos, (posCreditos[0] + 20, posCreditos[1] + 10))
            tela.blit(iniciar, (posIniciar[0] + 20, posIniciar[1] + 10))
            tela.blit(recordes, (posRecordes[0] + 10, posRecordes[1] + 10))
            tela.blit(sair, (posSair[0] + 30, posSair[1] + 10))
            pygame.display.update()

def inicializar():
    x, y, jogador, flecha, mapa, wumpus, ouro, abismo, status, sair = config()
    game()

cor = {"branco":(255, 255, 255), "preto":(0, 0, 0), "vermelho":(255, 0, 0), "verde":(0, 255, 0), "azul":(0, 255, 255), "azul_escuro":(0, 200, 200), "vermelho_escuro":(200, 0, 0), "verde_escuro":(0, 200, 0), "cinza":(124, 124, 124), "cinza_claro":(189, 196, 202), "cinza_escuro":(36, 36, 36)}
pygame.init()
tamanho = 6
altura = 100 * tamanho + 100
largura = 100 * tamanho
tela = pygame.display.set_mode([largura, altura])
pygame.display.set_caption("Hunt The Wumpus")
fps = pygame.time.Clock()
fps.tick(60)
menu = Menu()
sairMenu = False
pygame.mixer.init()
musica = pygame.mixer.music.load("musica.mp3")

while sairMenu != True:
    pygame.mixer.music.play()
    menu = menu.menu()
    if menu == 1:
        sairMenu = True
pygame.quit()
