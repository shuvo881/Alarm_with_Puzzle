import random
import time
from tkinter import *
import alarm
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

number_of_clicks = 0
display_clicks = StringVar()
display_clicks.set("Number of Clicks \n" + "0")

game_state_string = StringVar()


def update_counter():
    global number_of_clicks, display_clicks
    display_clicks.set("Number of Clicks \n" + str(number_of_clicks))


def game_state_update(game_state):
    global game_state_string
    game_state_string.set(game_state)


# ============== Button ================
def shuffle():
    global number_of_clicks, display_clicks
    game_state_update("Start Game")
    alarm.p_play()
    nums = []
    for ii in range(12):
        ii += 1
        if ii == 12:
            nums.append("")
        else:
            nums.append(str(ii))

    for ix in range(len(btn_numbers)):
        for jy in range(len(btn_numbers[0])):
            num = random.choice(nums)
            btn_numbers[ix][jy].text_taken.set(num)
            nums.remove(num)


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


update_counter()
game_state_update("")

Label(right_frame_1, textvariable=display_clicks, font=('arial', 40)).place(x=0, y=10, width=480, height=160)

Button(right_frame_2, text="New Game", font=('arial', 40), bd=5, command=shuffle).place(x=0, y=10, width=480,
                                                                                        height=100)

Label(right_frame_3, textvariable=game_state_string, font=('arial', 40)).place(x=0, y=10, width=480, height=100)

btn_numbers = []

# pattern button
name = 0
for i in range(3):  # 3 is number of row
    btn_numbers_ = []
    for j in range(4):  # 4 is # column
        name += 1
        if name == 12:
            name = ""

        btn_numbers_.append(Button_(left_frame, str(name), x=j, y=i))
    btn_numbers.append(btn_numbers_)


def empty_spot_checker(y, x):
    print(WIN_STATUS)
    global btn_numbers, number_of_clicks

    if not btn_numbers[x][y].text_taken.get() == "":
        for i in range(-1, 2):
            new_x = x + i

            if not (new_x < 0 or len(btn_numbers) - 1 < new_x or i == 0):
                if btn_numbers[new_x][y].text_taken.get() == "":
                    text = btn_numbers[x][y].text_taken.get()
                    btn_numbers[x][y].text_taken.set(btn_numbers[new_x][y].text_taken.get())
                    btn_numbers[new_x][y].text_taken.set(text)
                    win_check()
                    break
        for j in range(-1, 2):
            new_y = y + j

            if not (new_y < 0 or len(btn_numbers[0]) - 1 < new_y or i == 0):
                if btn_numbers[x][new_y].text_taken.get() == "":
                    text = btn_numbers[x][y].text_taken.get()
                    btn_numbers[x][y].text_taken.set(btn_numbers[x][new_y].text_taken.get())
                    btn_numbers[x][new_y].text_taken.set(text)
                    win_check()
                    break
        number_of_clicks += 1
        update_counter()


global WIN_STATUS

WIN_STATUS = False


def win_check():
    global WIN_STATUS
    won = True  # Assume the player has won initially
    for y in range(len(btn_numbers)):
        for x in range(len(btn_numbers[y])):
            if btn_numbers[y][x].enter_value != btn_numbers[y][x].text_taken.get():
                won = False  # If any condition is not met, the player has not won
                break

    if won:
        game_state_update("You are winner!")
        WIN_STATUS = True
        alarm.p_stop()



print(WIN_STATUS)

root.mainloop()
