import tkinter as tk
from win32api import GetSystemMetrics

width_screen = GetSystemMetrics(0)
height_screen = GetSystemMetrics(1)
HEIGHT=775
WIDTH=400

root=tk.Tk()
root.geometry("720x480")
root.attributes("-fullscreen", True)
root.config(bg="#3394ff")
root.bind("<Escape>", lambda event: root.destroy()) 
support_root = tk.Frame(root, bg="#3394ff", width = width_screen, height= width_screen)
support_root.place(x=0, y=0)

def animation_clic(event, self, counter):
    self.create_oval((25,25),(175,175), fill="#3394ff", outline = "#3394ff", width = 25)
    if counter % 2 == 1 :
        self.create_oval((40,40),(160,160), fill="#ffd933", outline = "#e7ba00", width = 18)
    elif counter % 2 == 0 :
        self.create_oval((40,40),(160,160), fill="#ff3b30", outline = "#bb261f", width = 18)
        jeton_gauche_1_counter += 1
def animation_relache_jg1(event, self, counter):
    global jeton_gauche_1_counter
    jeton_gauche_1_counter += 1
    if counter % 2 == 0 :
        self.create_oval((25,25),(175,175), fill="#ffd933", outline = "#e7ba00", width = 25)
    elif counter % 2 == 1 :
        self.create_oval((25,25),(175,175), fill="#ff3b30", outline = "#bb261f", width = 25)
def animation_relache_jg2(event, self, counter):
    global jeton_gauche_2_counter
    jeton_gauche_2_counter += 1
    if counter % 2 == 0 :
        self.create_oval((25,25),(175,175), fill="#ffd933", outline = "#e7ba00", width = 25)
    elif counter % 2 == 1 :
        self.create_oval((25,25),(175,175), fill="#ff3b30", outline = "#bb261f", width = 25)
def animation_relache_jd1(event, self, counter):
    global jeton_droite_1_counter
    jeton_droite_1_counter += 1
    if counter % 2 == 0 :
        self.create_oval((25,25),(175,175), fill="#ffd933", outline = "#e7ba00", width = 25)
    elif counter % 2 == 1 :
        self.create_oval((25,25),(175,175), fill="#ff3b30", outline = "#bb261f", width = 25)
def animation_relache_jd2(event, self, counter):
    global jeton_droite_2_counter
    jeton_droite_2_counter += 1
    if counter % 2 == 0 :
        self.create_oval((25,25),(175,175), fill="#ffd933", outline = "#e7ba00", width = 25)
    elif counter % 2 == 1 :
        self.create_oval((25,25),(175,175), fill="#ff3b30", outline = "#bb261f", width = 25)

frame_gauche = tk.Frame(support_root,height=HEIGHT, width=WIDTH/2, bg ="#3394ff")
frame_droite = tk.Frame(support_root,height=HEIGHT, width=WIDTH/2, bg ="#3394ff")
jeton_gauche_1 = tk.Canvas(frame_gauche, height=200, width=200, bg ='#3394ff', highlightthickness=0)
jeton_gauche_1_counter = 1
jeton_gauche_2 = tk.Canvas(frame_gauche, height=200, width=200, bg ='#3394ff', highlightthickness=0)
jeton_gauche_2_counter = 0
jeton_droite_1 = tk.Canvas(frame_droite, height=200, width=200, bg ='#3394ff', highlightthickness=0)
jeton_droite_1_counter = 0
jeton_droite_2 = tk.Canvas(frame_droite, height=200, width=200, bg ='#3394ff', highlightthickness=0)
jeton_droite_2_counter = 1

jeton_gauche_1.place(x=0, y=0)
jeton_gauche_2.place(x=0, y=height_screen-289)
jeton_gauche_1.create_oval((25,25),(175,175), fill="#ffd933", outline = "#e7ba00", width = 25 )
jeton_gauche_2.create_oval((25,25),(175,175), fill="#ff3b30", outline = "#bb261f", width = 25  )
jeton_droite_1.place(x=0, y=0)
jeton_droite_2.place(x=0, y=height_screen-289)
jeton_droite_1.create_oval((25,25),(175,175), fill="#ff3b30", outline = "#bb261f", width = 25 )
jeton_droite_2.create_oval((25,25),(175,175), fill="#ffd933", outline = "#e7ba00", width = 25  )
frame_gauche.place(x=0, y=(height_screen-HEIGHT)/2)
frame_droite.place(x=width_screen-WIDTH/2, y=(height_screen-HEIGHT)/2)
Tg=tk.Label(frame_gauche, text="P\nU\nI\nS\nS\nA\nN\nC\nE\n-\n4", font=("System", 20), fg="White", bg="#3394ff")
Td=tk.Label(frame_droite, text="P\nU\nI\nS\nS\nA\nN\nC\nE\n-\n4", font=("System", 20), fg="White", bg="#3394ff")
Tg.place(x=85, y=210)
Td.place(x=85, y=210)

jeton_gauche_1.bind('<ButtonPress-1>',lambda event : animation_clic(event, jeton_gauche_1, jeton_gauche_1_counter))
jeton_gauche_1.bind('<ButtonRelease-1>', lambda event : animation_relache_jg1(event, jeton_gauche_1, jeton_gauche_1_counter))
jeton_gauche_2.bind('<ButtonPress-1>',lambda event : animation_clic(event, jeton_gauche_2, jeton_gauche_2_counter))
jeton_gauche_2.bind('<ButtonRelease-1>', lambda event : animation_relache_jg2(event, jeton_gauche_2, jeton_gauche_2_counter))
jeton_droite_1.bind('<ButtonPress-1>',lambda event : animation_clic(event, jeton_droite_1, jeton_droite_1_counter))
jeton_droite_1.bind('<ButtonRelease-1>', lambda event : animation_relache_jd1(event, jeton_droite_1, jeton_droite_1_counter))
jeton_droite_2.bind('<ButtonPress-1>',lambda event : animation_clic(event, jeton_droite_2, jeton_droite_2_counter))
jeton_droite_2.bind('<ButtonRelease-1>', lambda event : animation_relache_jd2(event, jeton_droite_2, jeton_droite_2_counter))

#----------------------------------------------#

root.mainloop()