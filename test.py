import tkinter as tk

root=tk.Tk()
root.geometry("720x480")
root.attributes("-fullscreen", True)
root.config(bg="#3394ff")
root.bind("<Escape>", lambda event: root.destroy())

T1=tk.Label(text="P", foreground="white", bg="#3394ff", font=("System", 50))
T1.place(x=580, y=360)
T2=tk.Label(text="u", foreground="white", bg="#3394ff", font=("System", 50))
T2.place(x=630, y=360)
T3=tk.Label(text="i", foreground="white", bg="#3394ff", font=("System", 50))
T3.place(x=680, y=360)
T4=tk.Label(text="s", foreground="white", bg="#3394ff", font=("System", 50))
T4.place(x=710, y=360)

y=360
dy=0
ymax=15
dt =20
t=100

def animer_T1():
    root.after(0, haut)
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

def animer_T2():
    root.after(0, haut)
    def bas():
        global y,dy,ymax,dt
        if dy < ymax:
            T2.place(x=580, y=y-ymax+dy)
            T2.config(fg="#bb261f")
            dy += 1
            root.after(40, bas)
        else:
            dy=0
            root.after(50, haut)
        return

    def haut():
        global y,dy,ymax,dt
        if dy < ymax:
            T2.place(x=580, y=y-dy)
            T2.config(fg="#e7ba00")
            dy += 1
            root.after(40, haut)
        else :
            dy = 0
            root.after(50, bas)
        return

def animation():
    global y,dy,ymax,dt
    root.after(100, animer_T1)
    

root.after(0, animation)
root.mainloop()


