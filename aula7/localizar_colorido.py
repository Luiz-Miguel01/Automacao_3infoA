import pyautogui

xy =  pyautogui.locateCenterOnScreen(
    "aula7\\vermelho.png",
    confidence=0.95,
    grayscale=False
)
pyautogui.click(xy, duration=1)