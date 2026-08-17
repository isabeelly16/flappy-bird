import pygame
from scripts.cano import Cano
from scripts.jogador import Jogador
from scripts.interfaces import Texto
from scripts.interfaces import Botao

class Partida:
    def __init__(self, tela):
        self.tela = tela
        self.jogador = Jogador(tela, 100, 100)
        self.cano = Cano(tela)
        self.estado = "menu"


    def atualizar(self):
        self.estado = "menu"
        self.titulo.desenhar()

        return self.estado
    
class Menu:
    def __init__(self,tela):
        self.tela = tela
        self.titulo = Texto(tela,"FlappyBird",100,20,(255,255,255),50)
    
    def atualizar(self):
        self.estado = "menu"
        self.titulo.desenhar()

        return self.estado
    
class Menu:
    def __init__(self,tela):
        self.tela = tela
        self.titulo = Texto(tela,"FlappyBird",100,20)
        