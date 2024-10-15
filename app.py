import pyautogui
# posição algo = use 'mouseInfo()' no cmd para capturar as coordenadas do click
# fazer algo com essa posição = pyautogui.moveTo()
pyautogui.moveTo(1802,67, duration=1)
#movimentando para o lado esquerdo (numero negativo)
pyautogui.move(-1480,-15,duration=1)
pyautogui.click()
pyautogui.move(-12,duration=1)
pyautogui.click()