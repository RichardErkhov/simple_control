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
#type using click_button
def typing(text: str, length: float) -> None:
    dt = length/len(text)
    for i in text:
        click_button(i, dt)

def mouse_press(left: bool) -> None:
    #click left or right mouse button
    ellipsis

def mouse_hold(left: bool, length: float) -> None:
    #hold left or right mouse button
    ellipsis

def mouse_drag(left: bool, length: float) -> None:
    #hold left or right mouse button and move the mouse
    ellpsis