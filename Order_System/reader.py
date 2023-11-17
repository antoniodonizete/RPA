import csv

# import pandas as pd

# df = pd.read_csv('Orders.csv', skiprows=1)

# for index, row in df.iterrows():
#     print(row)

# Lendo arquivo CSV e iniciando preenchimento dos campos
counter = 0
with open('Orders.csv', 'r') as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=',')
    for line in arquivo_csv:
        if counter > 0:
            print('linhaaa:', line[0], line[1])
        counter+=1
        # for i in line:
        #     print(i)
#         # pyautogui.write(line[i])
        #     time.sleep(1)
        #     pyautogui.press('tab')
    # line += 1,