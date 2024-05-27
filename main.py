from tkinter import *

timer_running = False
current_timer_id = None
intervals = 40 # For color grading

# ----------------Functions--------------------#

# Check if key is pressed
def on_key_press(event):
    global timer_running
    reset_timer()
    print(f"Key pressed: {event.char}")


def start_timer():
    global timer_running
    timer_running = True
    count_down_and_color_grade(intervals)  # Start the countdown


def reset_timer():
    global current_timer_id, timer_running
    if current_timer_id:
        window.after_cancel(current_timer_id)
    start_timer()


def count_down_and_color_grade(intervals):
    global timer_running, current_timer_id
    if intervals >= 0:
        red_intensity = int(255 - (intervals / 40) * 255)
        text_color = f'#{red_intensity:02x}{red_intensity:02x}{red_intensity:02x}'

        text_box.config(foreground=text_color)
        current_timer_id = window.after(200, count_down_and_color_grade, intervals - 1)
    else:
        timer_running = False
        text_box.delete('1.0', END)


# GUI Setup
window = Tk()
window.title("Disappearing Text")
window.config(padx=50, pady=50, bg="#f0f0f0")


frame = Frame(window, bg="#ffffff", bd=2, relief="groove")
frame.grid(row=0, column=0, pady=20)

text_box = Text(frame, width=40, height=15, font=("Helvetica", 14), wrap=WORD, bg="#ecf0f1", fg="#2d3436", padx=10,
                pady=10, highlightthickness=0, bd=2, relief="flat", borderwidth=2, insertborderwidth=2, insertwidth=2)
text_box.pack()
text_box.bind("<Key>", on_key_press)


window.after(0, start_timer)

window.mainloop()
