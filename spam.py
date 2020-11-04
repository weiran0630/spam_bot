import pyautogui, time
import keyboard, pyperclip

if __name__ == "__main__":

    '''time.sleep(5)
    fp = open('鮫島事件.txt')
    text = fp.readlines()
    fp.close()

    for line in text:
        pyperclip.copy(line)
        pyautogui.hotkey('command', 'v')
        pyautogui.hotkey("enter")'''

    time.sleep(5)
    while True:
        if keyboard.is_pressed('q'):
            break
        pyautogui.hotkey('command', 'v')
        pyautogui.hotkey("enter")