import time
import pyautogui
import tkinter as tk
def screen_shot():
    time.sleep(2)
    img = pyautogui.screenshot()
    img.save('screenshot.png')
    img.show()

screen_shot()


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button( 
    frame,
    text='Take Screenshot',
    fg='red',
    command=screen_shot

)

button.pack(side='left')
close = tk.Button(
    frame, 
    text='QUIT', 
    fg='blue', 
    command= quit
)
close.pack(side='left')
root.mainloop()
