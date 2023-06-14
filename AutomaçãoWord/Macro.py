#Abrir bloco de Word
import pyautogui
import pyperclip


#Abrir Word
pyautogui.position(x=118, y=1062)
pyautogui.click(x=118, y=1062)
pyautogui.write('Bloco de Notas')
pyautogui.doubleClick()
pyautogui.press('enter')
pyautogui.position(x=997, y=202)
pyautogui.click(x=997, y=202)

msg = 'A cólera é um cavalo fogoso; se lhe largamos o freio, o seu ardor exagerado em breve a deixa esgotada.'
pyperclip.copy(msg)

pyautogui.hotkey('Ctrl', 'V')
