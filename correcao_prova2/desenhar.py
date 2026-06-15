import pyautogui
import time

#Abrir o paint
pyautogui.press('win')
pyautogui.write('Paint')
pyautogui.press('Enter')
time.sleep(1)

#Maximizar o Paint
pyautogui.hotkey('alt', 'space')
time.sleep(1)
pyautogui.press('x')
time.sleep(1)

#Posicionar o Mouse no Centro da Tela
largura, altura = pyautogui.size()
x_centro = largura/2
y_centro = altura/2
pyautogui.moveTo(x_centro, y_centro)

#faz o desenho utilizando
#coordenadas relativas
pyautogui.dragRel(0,100)
pyautogui.dragRel(100,0)
pyautogui.dragRel(0,-100)
pyautogui.dragRel(-100,0)

#mover sem arrastar
pyautogui.moveRel(50, -150)
pyautogui.dragRel(100,150)
pyautogui.dragRel(-200,0)
pyautogui.dragRel(100,-150)

#localizar botões no Paint
xy_balde = pyautogui.locateCenterOnScreen(
    "correcao_prova2\\balde.png",
    confidence=0.98,
    grayscale=False)

xy_verde = pyautogui.locateCenterOnScreen(
    "correcao_prova2\\verde.png",
    confidence=0.98,
    grayscale=False)

xy_marron = pyautogui.locateCenterOnScreen(
    "correcao_prova2\\marron.png",
    confidence=0.98,
    grayscale=False)

#Clica no balde
pyautogui.click(xy_balde)
pyautogui.click(xy_marron)

#clica no caule
pyautogui.moveTo(x_centro, y_centro)
pyautogui.moveRel(10, 10)
pyautogui.click(clicks=2)

#clica no verde
pyautogui.click(xy_verde)

#clica nas folhas
pyautogui.moveTo(x_centro, y_centro)
pyautogui.moveRel(10, -10)
pyautogui.click(clicks=2)

#Salvar
pyautogui.hotkey('ctrl', 's')
time.sleep(2)
pyautogui.write("C:\\Users\\07298764624\\Desktop\\Automacao_3INFOA\\correcao_prova2\\arvore.png")
pyautogui.press('enter')
