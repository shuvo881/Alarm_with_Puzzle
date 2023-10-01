from tkinter import *


class Button_:
    def __init__(self, frame, text_, x, y):
        self.enter_value = text_
        self.text_taken = StringVar()
        self.text_taken.set(text_)
        self.x = x
        self.y = y
        self.btn_number = Button(frame, textvariable=self.text_taken, font=('arial', 80), bd=2,
                                 command=lambda i=self.x, j=self.y: empty_spot_checker(i, j))
        self.btn_number.place(x=self.x * 150, y=self.y * 150, width=150, height=150)
