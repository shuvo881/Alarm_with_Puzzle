import random
import time
from tkinter import *


# ======================== Frame Creation Start ===================================

root = Tk()
root.geometry('1350x750+0+0')
root.title('Puzzle Game')
root.configure(background='#59618A')

Tops = Frame(root, bg='#59618A', padx=2, width=1350, height=100, relief=RIDGE)
Tops.grid(row=0, column=0, )

# Label create
lbl_title = Label(Tops, font=('arial', 70, 'bold'),
                  text='Alarm with Puzzle Game',
                  bd=10,
                  bg='#59618A',
                  fg='Cornsilk',
                  justify=CENTER,
                  )
lbl_title.grid(row=0, column=0)

# main frame create
main_frame = Frame(root,
                   bg='#525FA0',
                   bd=10,
                   width=1350,
                   height=600,
                   relief=RIDGE
                   )
main_frame.grid(row=1, column=0, padx=20)

# left frame create
left_frame = Frame(main_frame,
                   bd=10,
                   width=650,
                   height=470,
                   pady=2,
                   relief=RIDGE
                   )
left_frame.pack(side=LEFT)

# right frame create
right_frame = Frame(main_frame,
                    bd=10,
                    width=500,
                    height=470,
                    padx=1,
                    pady=2,
                    relief=RIDGE
                    )
right_frame.pack(side=RIGHT)

# right1 frame create
right_frame_1 = Frame(right_frame,
                      bd=10,
                      width=540,
                      height=200,
                      padx=10,
                      pady=2,
                      relief=RIDGE
                      )
right_frame_1.grid(row=0, column=0)

# right2 frame create
right_frame_2 = Frame(right_frame,
                      bd=10,
                      width=540,
                      height=140,
                      padx=10,
                      pady=2,
                      relief=RIDGE
                      )
right_frame_2.grid(row=1, column=0)

# right2 frame create
right_frame_3 = Frame(right_frame,
                      bd=10,
                      width=540,
                      height=130,
                      padx=10,
                      pady=2,
                      relief=RIDGE
                      )
right_frame_3.grid(row=2, column=0)


# ======================== Frame Creation END ===================================

root.mainloop()
