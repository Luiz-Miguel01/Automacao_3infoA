#importa a biblioteca(módulo) que controla o mouse e o teclado
import pyautogui 

#localiza as coordenadas de um elemento na tela, usando uma imagem de referência
xy = pyautogui.locateCenterOnScreen ('aula7\\8.png',confidence=0.9)
print(xy) #imprime as coordenadas encontradas
pyautogui.click(xy, duration=1)

xy = pyautogui.locateCenterOnScreen ('aula7\\botaox.png',confidence=0.9)
print(xy) #imprime as coordenadas encontradas
pyautogui.click(xy, duration=1)

xy = pyautogui.locateCenterOnScreen ('aula7\\botao3.png',confidence=0.9 )
print(xy) #imprime as coordenadas encontradas
pyautogui.click(xy, duration=1)

xy = pyautogui.locateCenterOnScreen ('aula7\\igual.png',confidence=0.9)
print(xy) #imprime as coordenadas encontradas
pyautogui.click(xy, duration=1)
