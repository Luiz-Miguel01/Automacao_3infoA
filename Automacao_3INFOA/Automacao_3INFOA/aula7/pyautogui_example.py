"""Exemplo mínimo de uso do PyAutoGUI

Salva uma captura de tela em 'screenshot_example.png' e move o cursor brevemente.
Use apenas em um ambiente seguro — o script moverá o mouse.
"""
import time
import pyautogui

def main():
    print("Tela:", pyautogui.size())
    # Evita falha automática quando cursor está em canto
    pyautogui.FAILSAFE = False

    # Move o mouse para o centro da tela (sem bloquear totalmente)
    w, h = pyautogui.size()
    cx, cy = w // 2, h // 2
    print(f"Movendo o mouse para ({cx}, {cy})")
    pyautogui.moveTo(cx, cy, duration=0.5)

    # Pequena pausa para você ver
    time.sleep(0.5)

    # Captura de tela e salva
    out = 'screenshot_example.png'
    print(f"Salvando captura de tela em {out}...")
    img = pyautogui.screenshot()
    img.save(out)
    print("Pronto.")

if __name__ == '__main__':
    main()
