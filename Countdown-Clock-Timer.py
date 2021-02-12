from tkinter import *
import time
from playsound import playsound

#
root = Tk()
root.title("Countdown clock and Timer")
root.geometry("400x300")
root.resizable(0, 0)
#
lb_frame = Frame(root, width=400, height=50, highlightbackground="black", highlightthickness=1)
lb_frame.pack(side=TOP)
#
lb = Label(lb_frame, text="Countdown Clock And Timer", font=('arial', 20, 'bold'), width=25).pack()
#
main_frame = Frame(root, width=400, height=300)
main_frame.pack()


#
def clock():
    current_time = time.strftime("%H:%M:%S")
    lb_time_current.config(text=current_time)
    lb_time_current.after(1000, clock)


Label(main_frame, text="Time Current: ", font=('arial', 20, 'bold'), bg="grey").place(x=30, y=20)
lb_time_current = Label(main_frame, text="", font=('arial', 20, 'bold'), bg="#00FF00")
lb_time_current.place(x=250, y=20)
clock()
#
Label(main_frame, text="Set The Time", font=("arial", 15), bg="grey").place(x=60, y=150)

hour = StringVar()
hour_input = Entry(main_frame, textvariable=hour, width=2, font=("arial", 15))
hour_input.place(x=250, y=150)
hour.set("0")

minute = StringVar()
minute_input = Entry(main_frame, textvariable=minute, width=2, font=("arial", 15))
minute_input.place(x=280, y=150)
minute.set("0")

seconds = StringVar()
seconds_input = Entry(main_frame, textvariable=seconds, width=2, font=("arial", 15))
seconds_input.place(x=310, y=150)
seconds.set("0")


#
def countdownt():
    times = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(seconds.get())
    while times > -1:
        mins, sec = (times // 60, times % 60)
        hrs = 0
        if mins > 60:
            hrs, mins = (times // 60, times % 60)
        hour.set(hrs)
        minute.set(mins)
        seconds.set(sec)
        root.update()
        time.sleep(1)
        if times == 0:
            playsound("Clock.mp3")
            hour.set("0")
            minute.set("0")
            seconds.set("0")
        times -= 1


#
Button(main_frame, text="Start", bg="#FF0000", font=("arial", 15), command=countdownt).place(x=185, y=200)

root.mainloop()
