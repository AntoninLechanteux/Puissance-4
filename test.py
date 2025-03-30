import tkinter as tk

root=tk.Tk()
root.geometry("720x480")
root.attributes("-fullscreen", True)
root.config(bg="#3394ff")
root.bind("<Escape>", lambda event: root.destroy())

T1=tk.Label(text="Puissance", foreground="white", bg="#3394ff", font=("System", 50))
T1.place(x=580, y=360)

y=360
dy=0
ymax=15
dt =20
t=100


def bas():
    global y,dy,ymax,dt
    if dy < ymax:
        T1.place(x=580, y=y-ymax+dy)
        T1.config(fg="#bb261f")
        dy += 1
        root.after(40, bas)
    else:
        dy=0
        root.after(50, haut)
    return

def haut():
    global y,dy,ymax,dt
    if dy < ymax:
        T1.place(x=580, y=y-dy)
        T1.config(fg="#e7ba00")
        dy += 1
        root.after(40, haut)
    else :
        dy = 0
        root.after(50, bas)
    return


def animation():
    global y,dy,ymax,dt
    root.after(100, haut)
    

root.after(0, animation)
root.mainloop()


