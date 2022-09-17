import keyboard, time
import pyautogui
#just type a letter that is given
def click_button(button: str, length: float) -> None:
    keyboard.press(button)
    time.sleep(length/2)
    keyboard.release(button)
    time.sleep(length/2)
#move the mouse relative to it's starting point
def move_mouse(x: int, y: int, length: float) -> None:
    pyautogui.move(x,y,length)
