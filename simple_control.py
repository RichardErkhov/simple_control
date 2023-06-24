import keyboard, time
import pyautogui
__version__ = "0.0.1"
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
def typing(text: str, length: float, raw:bool = False) -> None:
    #if raw just write whatever we are given
    #else, we preprocess the text before typing
    if raw:
        dt = length/len(text)
        for i in text:
            click_button(button = i, 
                         length = dt)
    else:
        typing_auto_preprocess(text = text, 
                               length = length)

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
    ellipsis

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

#delay between clicks in seconds
def double_click(left:bool = True, delay:float = 0.05):
    mouse_press(left = left)
    time.sleep(delay)
    mouse_press(left = left)

def typing_auto_preprocess(text: str, length: float):
    dt = length / len(text)
    for char in text:
        if char == ' ':
            #chars.append('space')
            click_button(button = 'space', 
                         length = dt)
        #check if capital
        elif char == char.upper():
            click_button(button =f'shift+{char.lower()}',
                         length = dt)
        elif char == '':
            pass
        else:
            click_button(button = char, 
                         length = dt)
                        

def test3():
    time.sleep(2)
    typing_auto_preprocess('NeVer GoNNa Give you Up', 2)
