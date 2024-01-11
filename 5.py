from tkinter import *
from math import sin, cos, pi

after_id = ''

def draw_fc():
    global R, x0, y0
    R, x0, y0 = int(t1.get()), int(cvs['width'])//2, int(cvs['height'])//2
    cvs.create_oval(x0 - R, y0 - R, x0 + R, y0 + R, fill="white", width = 3)

def inp():
    global m
    m = True

def outp():
    global m
    m = False

def draw():
    global x0, dx, after_id, ln, a, b
    x0 = int(cvs["width"]) // 2
    y0 = int(cvs["height"]) // 2
    if m:
        xc, yc = x0 + (R - r) * cos(a), y0 - (R - r) * sin(a)
        xt1, yt1 = xc + d * cos(a - b), yc - d * sin(a - b)
        a += dx
        b = a * R / r
        xc, yc = x0 + (R - r) * cos(a), y0 - (R - r) * sin(a)
        xt2, yt2 = xc + d * cos(a - b), yc - d * sin(a - b)
        cvs.create_line(xt1, yt1, xt2, yt2)
        after_id = root.after(10, draw)
    else:
        xc, yc = x0 + (R + r) * cos(a), y0 - (R + r) * sin(a)
        xt1, yt1 = xc + d * cos(a + b), yc - d * sin(a + b)
        a += dx
        b = a * R / r
        xc, yc = x0 + (R + r) * cos(a), y0 - (R + r) * sin(a)
        xt2, yt2 = xc + d * cos(a + b), yc - d * sin(a + b)
        cvs.create_line(xt1, yt1, xt2, yt2)
        root.after(10, draw)

def stop_draw():
    root.after_cancel(after_id)

def continue_draw():
    root.after_cancel(after_id)
    draw()
    pass

def start_draw():
    global R, r, d, dx, x0, y0, crcl, a, b
    cvs.delete("all")
    root.after_cancel(after_id)
    a, b = 0, 0
    R, r, d, dx = t1.get(), t2.get(), t3.get(), t4.get()
    try:
        R = int(R)
        r = int(r)
        d = int(d)
        dx = int(dx) * pi / 180
        x0, y0 = int(cvs["width"]) // 2, int(cvs["height"]) // 2
        crcl = cvs.create_oval(x0 - R, y0 - R, x0 + R, y0 + R, fill="white", width = 3)
        cvs.create_oval(x0, y0, x0, y0)
    except:
        showwarning("Error!", "Input integers!")
    draw()

def close():
    root.destroy()

root = Tk()
root.title("Spirograph")

l1 = Label(root, text="Input R", font="Ubuntu, 16")
l2 = Label(root, text="Input r", font="Ubuntu, 16")
l3 = Label(root, text="Input d", font="Ubuntu, 16")
l4 = Label(root, text="Input Speed", font="Ubuntu, 16")
t1 = Entry(root, font = "Ubuntu, 16")
t2 = Entry(root, font = "Ubuntu, 16")
t3 = Entry(root, font = "Ubuntu, 16")
t4 = Entry(root, font = "Ubuntu, 16")
b1 = Button(root, text='Draw circle', font='Ubuntu, 16', command=draw_fc)
btn1 = Button(root, text="Start", font="Ubuntu, 16", command=start_draw)
btn2 = Button(root, text="Stop", font="Ubuntu, 16", command=stop_draw)
btn3 = Button(root, text="Continue", font="Ubuntu, 16", command=continue_draw)
btn4 = Button(root, text="Close", font="Ubuntu, 16", command=close)
btn5 = Button(root, text="Inside", font="Ubuntu, 16", command=inp)
btn6 = Button(root, text="Outside", font="Ubuntu, 16", command=outp)
cvs = Canvas(root, width=700, height=600, bg="#fff")

l1.grid(row=0, column=0, columnspan=2, sticky="ew")
l2.grid(row=2, column=0, columnspan=2, sticky="ew")
l3.grid(row=2, column=2, columnspan=2, sticky="ew")
l4.grid(row=4, column=0, columnspan=2, sticky="ew")
t1.grid(row=0, column=2, columnspan=2, sticky="ew")
t2.grid(row=3, column=0, columnspan=2, sticky="ew")
t3.grid(row=3, column=2, columnspan=2, sticky="ew")
t4.grid(row=4, column=2, columnspan=2, sticky="ew")
b1.grid(row=1, column=0, columnspan=4, sticky="ew")
btn1.grid(row=6, column=0, sticky="ew")
btn2.grid(row=6, column=1, sticky="ew")
btn3.grid(row=6, column=2, sticky="ew")
btn4.grid(row=6, column=3, sticky="ew")
btn5.grid(row=5, column=0, columnspan=2, sticky="ew")
btn6.grid(row=5, column=2, columnspan=2, sticky="ew")
cvs.grid(row=7, columnspan=4)

root.mainloop()