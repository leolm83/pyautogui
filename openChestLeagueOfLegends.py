import pyautogui, sys
from time import sleep

#Sim, isto é uma gambiarra para desencantar fragmentos de campeao no lol KJKKJKK

#(o jogo precisa estar aberto)
#seleciona aba do jogo
pyautogui.moveTo(960, 1055)
pyautogui.click()

#repete quantas vezes voce precisa
vezes = 2
for x in range(vezes):
    #posicao do primeiro fragmento(da esquerda p/ direita, cima p/ baixo)
    pyautogui.moveTo(90,267)
    pyautogui.click()
    #posicao do botao de desencantar
    pyautogui.moveTo(302,302)
    pyautogui.click()
    #posicao da confirmacao de desencantar
    pyautogui.moveTo(523,523)
    pyautogui.click()
    sleep(1.5)