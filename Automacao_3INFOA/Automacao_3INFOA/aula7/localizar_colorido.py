import pyautogui

xy = pyautogui.locateCenterOnScreen ('aula7\\colorido.png',confidence=0.99, grayscale=False)
pyautogui.click(xy, duration=1)