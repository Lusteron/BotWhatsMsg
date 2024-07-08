import webbrowser
import pyautogui
from time import sleep

telefones = []


with open('fones.txt','r') as arquivo:
    for linha in arquivo:
        telefones.append(linha.split('\n')[0])

mensagem_enviada = pyautogui.prompt(text='Informe sua mensagem: ')

for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(10)
    inicar = pyautogui.locateCenterOnScreen('iniciar.png')
    pyautogui.click(inicar, duration=2)
    sleep(5)
    msg = pyautogui.locateCenterOnScreen('mens.png')
    pyautogui.click(msg, duration=2)
    sleep(2)
    pyautogui.typewrite(mensagem_enviada)
    sleep(2)
    pyautogui.press('enter')
    sleep(300)