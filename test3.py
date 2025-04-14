import tkinter as tk
import random as rd

root=tk.Tk()
root.geometry("720x480")
root.attributes("-fullscreen", True)
root.config(bg="#3394ff")
def close():
    root.destroy()
    return

end_pos = -350
start_pos = 0
dpos=0
dt=5
dx=0
panel = tk.LabelFrame(root, bg="#6db3fe", width=350, height=864, relief="ridge")
B2 = tk.Button(panel, bg = "#ff7262", text = "terminer",fg = "white", relief="ridge", command=close )
wB2 = B2.winfo_reqwidth()
print(wB2)
B2.place(x=175-wB2, y=432)

def animation():
    global dpos
    panel.place(x=start_pos, y=0)
    if dpos < abs(end_pos):
        panel.place(x=start_pos-dpos, y=0)
        dpos += 1
        root.after(dt, animation)
    else:
        panel.place(x=end_pos, y=0)
        dpos=0
    return

B1 = tk.Button(root, text="lancer l'animation", bg="#ff7262", fg="white", relief="ridge", command=animation)
B1.place(x=720, y=360)

root.mainloop()