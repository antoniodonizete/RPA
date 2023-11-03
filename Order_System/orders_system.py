#OBJETIVO DA AUTOMAÇÃO 

# Este documento tem como objetivo especificar de forma 
# prática e objetiva todo o processo de preenchimento 
# do formulário RoboForm. 
import os
import sys
import csv
import pyautogui
import time
import subprocess

# Comando para abrir o arquivo, e 'r' (ler) (outros: w, d) e nome da variavel 
# que recebe os dados
# with open ('C:\user\anton\RPA\Order_System|Orders.csv', 'r') as arquivo: (se precisar caminho)


with open('Orders.csv', 'r') as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=',')
    for line in arquivo_csv:
        print(line)

tr = [r'C:\Users\anton\RPA\Exercicios\2 - Exercício Order System\TrainingOrderSystem.exe']
process = subprocess.Popen(tr)
time.sleep(2)
# Localize a caixa de texto na tela
# text_box = pyautogui.locateOnScreen('Staff Number')
pyautogui.write('AA')
time.sleep(1)
pyautogui.press('tab')
pyautogui.write('AA')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('1')
pyautogui.press('tab')
pyautogui.press('enter')

i = 0
for item in line:
    pyautogui.write(item[i])
    pyautogui.press('tab')
    i += 1
    pyautogui.press('1')

print('Finalizado')
# x = 154
# y = 72

# Obtenha as coordenadas da caixa de texto
# x, y = pyautogui.center(text_box)
# Clique na caixa de texto para selecioná-la
# pyautogui.click(154, 72)
# time.sleep(2)
# Digite um texto na caixa de texto
# pyautogui.typewrite('AA')
# process.wait()



