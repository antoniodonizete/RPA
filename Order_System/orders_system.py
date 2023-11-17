# - OBJETIVO DA AUTOMAÇÃO -
# Este documento tem como objetivo especificar de forma 
# prática e objetiva todo o processo de preenchimento 
# do formulário RoboForm. 

import os
import sys
import csv
import pyautogui
import time
import subprocess

# Comando para abrir o arquivo TrainingOrderSystem.exe
tr = [r'C:\Users\anton\RPA\Exercicios\2 - Exercício Order System\TrainingOrderSystem.exe']
process = subprocess.Popen(tr)
time.sleep(2)

# Exibe alerta de início na tela para o usuário
# pyautogui.alert("Iniciando RPA!")
# pyautogui.PAUSE = 0.7

# Iniciando preenchimento login
pyautogui.write('AA')
time.sleep(1)
pyautogui.press('tab')
pyautogui.write('AA')
pyautogui.press('enter')
time.sleep(1)

# Selecionando opção desejada
pyautogui.write('1')
pyautogui.press('tab')
pyautogui.press('enter')

# Lendo arquivo CSV e iniciando preenchimento dos campos
counter = 0

with open('Orders.csv', 'r') as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=',')
    print('ok 1')
    print(arquivo_csv)
    for line in arquivo_csv:
        print('testeee')
        if counter > 0:
            print('ok 2')
            pyautogui.write(line[0])
            pyautogui.press('tab')
            pyautogui.write(line[1])
            pyautogui.press('tab')
            pyautogui.write(line[2])
            pyautogui.press('tab')
            pyautogui.write(line[3])
            pyautogui.press('tab')
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.press('enter')
            print('linhaaa:', line[0], line[1])
            pyautogui.press('enter')
        counter+=1
        print('próximo item')
    
        

        # for i in line:
        #     pyautogui.write(line[i])
        #     time.sleep(1)
        #     pyautogui.press('tab')
        #     print(i)
    # i += 1
    # pyautogui.press('1')

pyautogui.press('ALT + F4')
print('Finalizado')