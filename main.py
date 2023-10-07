import random
from datetime import datetime
from tkinter import *
import alarm
import time

# ======================== Frame Creation Start ===================================


root = Tk()
root.geometry('1350x750+0+0')
root.title('Puzzle Game')
root.configure(background='#59618A')

alarm_time = StringVar()

Tops = Frame(root, bg='#59618A', padx=2, width=1350, height=100, relief=RIDGE)
Tops.grid(row=0, column=0, )

# Label create
lbl_title = Label(Tops, font=('arial', 40, 'bold'),
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
                   width=500,
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
                    padx=5,
                    pady=2,
                    relief=RIDGE
                    )
right_frame.pack(side=RIGHT)

# time frame
time_frame = Frame(right_frame,
                   bg='#525FA0',
                   bd=10,
                   width=140,
                   height=10,
                   relief=RIDGE
                   )
time_frame.grid(row=0, column=0)

# right1 frame create
right_frame_1 = Frame(right_frame,
                      bd=10,
                      width=540,
                      height=100,
                      pady=2,
                      relief=RIDGE
                      )
right_frame_1.grid(row=1, column=0)

# right2 frame create
right_frame_2 = Frame(right_frame,
                      bd=10,
                      width=540,
                      height=140,
                      padx=10,
                      pady=2,
                      relief=RIDGE
                      )
right_frame_2.grid(row=2, column=0)

# right2 frame create
right_frame_3 = Frame(right_frame,
                      bd=10,
                      width=540,
                      height=130,
                      padx=10,
                      pady=2,
                      relief=RIDGE
                      )
right_frame_3.grid(row=3, column=0)

# ======================== Frame Creation END ===================================

number_of_clicks = 0
display_clicks = StringVar()

game_state_string = StringVar()


def update_counter():
    global number_of_clicks, display_clicks
    display_clicks.set("Number of Clicks: " + str(number_of_clicks))


def game_state_update(game_state):
    global game_state_string
    game_state_string.set(game_state)


# ============== Button ================
def shuffle():
    try:
        hr, mint = map(int, alarm_time.get().split(':'))
    except:
        game_state_update("Time formate not match (HH:MM)")
        return
    game_state_update('Alarm set successful')
    while True:
        update_time()
        root.update()
        if hr == datetime.now().hour and mint == datetime.now().minute:
            break
        time.sleep(1)
    print("yes")
    global number_of_clicks, display_clicks
    game_state_update("Start game with alarm")
    alarm.p_play()
    nums = []
    for ii in range(9):
        ii += 1
        if ii == 9:
            nums.append("")
        else:
            nums.append(str(ii))

    # shafful butoon
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
game_state_update("Let's enter alarm time")

Label(right_frame_1, textvariable=display_clicks, font=('arial', 20)).place(x=0, y=10, width=500, height=70)

Entry(right_frame_2, textvariable=alarm_time, font=('comic sans', 18)).grid(row=0, column=0)
Button(right_frame_2, text="Set", font=('arial', 20), bd=5, command=shuffle).grid(row=0, column=1)

Label(right_frame_3, textvariable=game_state_string, font=('arial', 20)).place(x=0, y=10, width=480, height=100)

btn_numbers = []

# pattern button
name = 0
for i in range(3):  # 3 is number of row
    btn_numbers_ = []
    for j in range(3):  # 3 is # column
        name += 1
        if name == 9:
            name = ""

        btn_numbers_.append(Button_(left_frame, str(name), x=j, y=i))
    btn_numbers.append(btn_numbers_)


def empty_spot_checker(y, x):
    global btn_numbers, number_of_clicks

    if not btn_numbers[x][y].text_taken.get() == "":
        for i in range(-1, 2):  # -1,0,1
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


def win_check():
    won = True  # Assume the player has won initially
    for y in range(len(btn_numbers)):
        for x in range(len(btn_numbers[y])):
            if btn_numbers[y][x].enter_value != btn_numbers[y][x].text_taken.get():
                won = False  # If any condition is not met, the player has not won
                break

    if won:
        game_state_update("You are a winner!")
        WIN_STATUS = True
        alarm.p_stop()


def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.config(text=current_time)
    root.after(1000, update_time)  # Update every 1000 milliseconds (1 second)


time_label = Label(time_frame, font=("Helvetica", 20))
time_label.pack(padx=1, pady=1)
update_time()  # Start the time update loop
# shuffle()


root.mainloop()
