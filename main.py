import mouse
import keyboard
import time
import pyautogui  # for screen size

# --- Get screen resolution ---
screen_width, screen_height = pyautogui.size()

# Reference resolution
REF_WIDTH = 1920
REF_HEIGHT = 1080

def scale(x, y):
    new_x = int(x / REF_WIDTH * screen_width)
    new_y = int(y / REF_HEIGHT * screen_height)
    return new_x, new_y

def click(x, y):
    sx, sy = scale(x, y)
    mouse.move(sx, sy)
    mouse.click("left")

def drag(x1, y1, x2, y2):
    sx1, sy1 = scale(x1, y1)
    sx2, sy2 = scale(x2, y2)
    mouse.press()
    mouse.drag(sx1, sy1, sx2, sy2)
    mouse.release()

def row1():
    time.sleep(0.9)
    click(1207, 879)
    for i in range(0, 3):
        time.sleep(0.4)
        click(1104, 380 + (150 * i))
    time.sleep(0.4)
    click(1214, 888)

def row2():
    time.sleep(0.9)
    click(1207, 879)
    for i in range(0, 3):
        time.sleep(0.4)
        click(1259, 380 + (150 * i))
    time.sleep(0.4)
    click(1214, 888)

def addingredients():
    for i in range(0, 3):
        time.sleep(0.4)
        click(1401, 390 + (i * 150))

    time.sleep(0.4)
    click(1382, 885)
    time.sleep(0.4)
    click(1157, 556)
    time.sleep(0.4)
    click(1113, 702)
    time.sleep(0.7)
    click(1619, 203)
    time.sleep(0.4)
    click(1207, 879)

# --- Global flags ---
running = False
superrunning = True
count = 1

# --- Keyboard event handlers ---
def toggle_run(e=None):
    global running
    running = not running
    print(f"Running = {running}")

def stop_program(e=None):
    global superrunning
    superrunning = False
    print("Stopping program...")

# Hook key events
keyboard.on_press_key("s", toggle_run)
keyboard.on_press_key("a", toggle_run)
keyboard.on_press_key("esc", stop_program)

# --- Main Loop ---
while superrunning:
    if running:
        if count % 2 == 0:
            row1()
        else:
            row2()

        addingredients()
        count += 1
    else:
        time.sleep(0.1)

#1104, 379 base coffee
#1259, 379 hot coffee
#1107 537 milk
#1258 535 chocolate
#1105, 699 nuts
#1261, 699 spice
#1214, 888 next button

#1401 392 1st +
#1401, 545 second +
#1398, 713 third +
#1382, 885 multiple
#1157, 556 max
#1113 702 ok
#1619, 203 skip
#1207, 879 start
