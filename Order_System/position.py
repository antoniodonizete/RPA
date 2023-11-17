import pyautogui

x, y = pyautogui.position()

# Imprima as coordenadas do mouse
print(f'x: {x}, y: {y}')


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