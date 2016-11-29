from pynput.keyboard import Key, Listener
import time
import socket

s = socket.socket()
s.connect(("10.100.0.105", 9998))
print("Connected")

up = False
down = False
right = False
left = False

cam_up, cam_down, cam_left, cam_right = [False]*4

def on_press(key):
    global up, down, right, left, cam_up, cam_down, cam_right, cam_left, s
    key_str = '{0}'.format(key)[1]
    if key is Key.up:
        if not up:
            up = True
            print("forward speed")
            s.send(b"sf")
    elif key is Key.down:
        if not down:
            down = True
            print("backward speed")
            s.send(b"sb")
    elif key is Key.right:
        if not right:
            right = True
            print("turn right")
            s.send(b"sr")
    elif key is Key.left:
        if not left:
            left = True
            print("turn left")
            s.send(b"sl")


    # cam controls
    if key_str == "w":
        if not cam_up:
            cam_up = True
            print("cam up")
            s.send(b"cu")
    elif key_str == "s":
        if not cam_down:
            cam_down = True
            print("cam down")
            s.send(b"cd")
    elif key_str == "d":
        if not cam_right:
            cam_right = True
            print("cam right")
            s.send(b"cr")
    elif key_str == "a":
        if not cam_left:
            cam_left = True
            print("cam left")
            s.send(b"cl")

def on_release(key):
    global up, down, right, left, cam_up, cam_down, cam_left, cam_right, s
    key_str = '{0}'.format(key)[1]
    if key is Key.up:
        up = False
        print("stopped forward speed")
        s.send(b"pf")
    elif key is Key.down:
        down = False
        print("stopped backward speed")
        s.send(b"pb")
    elif key is Key.right:
        right = False
        print("stopped turn right")
        s.send(b"pr")
    elif key is Key.left:
        left = False
        print("stopped turn left")
        s.send(b"pl")

    # cam controls
    elif key_str == "w":
        cam_up = False
        print("stopped cam up")
        s.send(b"xu")
    elif key_str == "s":
        cam_down = False
        print("stopped cam down")
        s.send(b"xd")
    elif key_str == "d":
        cam_right = False
        print("stopped cam right")
        s.send(b"xr")
    elif key_str == "a":
        cam_left = False
        print("stopped cam left")
        s.send(b"xl")

    elif key is Key.esc:
        # Stop listener
        s.send(b"qq")
        return False

# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

s.close()
