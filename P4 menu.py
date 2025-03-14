import tkinter as tk
import random as rd

#-----------creation de la fenetre-------------#
root=tk.Tk()
root.geometry("720x480")
root.title("Menu Puissance 4")
root.attributes("-fullscreen", True)
root.bind("<Escape>", lambda event: root.destroy())
#----------------------------------------------#

#-----------creation de la grille-------------#
HEIGHT = 600
WIDTH = 700
dim_grille = [6,7] #Sera modifiable
canva_jeu = tk.Canvas(root, height=HEIGHT, width=WIDTH,bg="#005bff")
canva_jeu.pack(expand=True)
for i in range(dim_grille[1]):
    for j in range(dim_grille[0]):
        diametre = 100
        canva_jeu.create_oval(((i*WIDTH)//dim_grille[1],(j*HEIGHT)/dim_grille[0]),  ((i*WIDTH)//dim_grille[1] + diametre,(j*HEIGHT)/dim_grille[0] + diametre),  fill = "#3394ff",  outline="#004fab", width=5)
#----------------------------------------------#

#-----------creation des jetons-------------#
tour = "jaune"
def placer_jeton(event):
    global tour
    if tour == "jaune":
        canva_jeu.create_oval((event.x-40,event.y-40), (event.x+40, event.y+40),  fill = "#ffd933",  outline = "#e7ba00", width = 10)
        tour = "rouge"
        return
    if tour == "rouge":
        canva_jeu.create_oval((event.x-40,event.y-40), (event.x+40, event.y+40),  fill = "#ff3b30",  outline = "#bb261f", width = 10)
        tour = "jaune"
root.bind("<Button-1>", placer_jeton)
root.mainloop()

