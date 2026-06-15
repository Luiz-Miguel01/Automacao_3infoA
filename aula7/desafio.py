import pyautogui

while True:
    try:
        xyz =  pyautogui.locateAllOnScreen(
            "aula7\\circulo_vermelho.png",
            confidence=0.95,
            grayscale=False, region=[0,91,684,718]
        )

        for b in xyz:
            c = pyautogui.center(b)
            pyautogui.click(c)
    except:
        print("Ainda noa localizei")
