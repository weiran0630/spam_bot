import pyautogui, time
import keyboard, pyperclip

if __name__ == "__main__":

    # 讀取檔案每行洗版
    time.sleep(5)
    fp = open('鮫島事件.txt')
    text = fp.readlines()
    fp.close()

    for line in text:
        pyperclip.copy(line)
        pyautogui.hotkey('command', 'v')
        pyautogui.hotkey("enter")

    # 無限洗版剪貼板內容，按q停止
    '''time.sleep(5)
    while True:
        if keyboard.is_pressed('q'):
            break
        pyautogui.hotkey('command', 'v')
        pyautogui.hotkey("enter")'''