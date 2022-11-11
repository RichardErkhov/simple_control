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

def move_mouse_to(x: int, y: int, length: float, mode: int=0) -> None:
    '''
modes:
0 - using move_mouse()
1 - randomised move_mouse() #indev
2 - teleport mouse to location
    '''
    if mode == 0:
        current_position = get_mouse_position()
        target = x - current_position[0], y - current_position[1]
        move_mouse(target[0], target[1], length)
    elif mode == 1:
        pass
    elif mode == 2:
        pass
    else:
        pass
#type using click_button
def typing(text: str, length: float) -> None:
    dt = length/len(text)
    for i in text:
        click_button(i, dt)

def mouse_press(left: bool = True) -> None:
    #click left or right mouse button
    key = 'LEFT'
    if left == False:
        key = 'RIGHT'
    pos = get_mouse_position()
    pyautogui.click(x = pos[0], 
                    y = pos[1], 
                    button = key)

def mouse_hold(left: bool, length: float) -> None:
    #hold left or right mouse button
    ellipsis

def mouse_drag(left: bool, length: float) -> None:
    #hold left or right mouse button and move the mouse
    ellpsis

def get_mouse_position() -> [int, int]:
    #return current mouse position
    pos = pyautogui.position()
    return [pos[0], pos[1]]

def get_keys_pressed():
    return keyboard.read_key()

def is_key_pressed(key) -> bool:
    return keyboard.is_pressed(key)

def test1():
    time.sleep(1)
    click_button('a', 0.02)
    move_mouse(100, 100, 0.2)
    print(get_mouse_position())
    time.sleep(1)
    print(get_keys_pressed())
    print(is_key_pressed('a'))

def test2():
    move_mouse_to(100, 100, 1)

if __name__ == "__main__": 
    test2()