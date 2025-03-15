import tkinter as tk
import random as rd

#-----------creation de la fenetre-------------#
root=tk.Tk()
root.geometry("720x480")
root.title("Menu Puissance 4")
root.attributes("-fullscreen", True)
root.bind("<Escape>", lambda event: root.destroy())
root.config(bg = "#3394ff")
#----------------------------------------------#

#-----------creation de la grille-------------#
HEIGHT = 720 #Sera modifiable
WIDTH = 1300 #Sera modifiable
dim_grille = [10,10] #Sera modifiable
canva_jeu = tk.Canvas(root, height=HEIGHT, width=WIDTH,bg="#005bff", borderwidth=0)
canva_jeu.pack(expand=True)
rayon_trou = (min((HEIGHT//dim_grille[0]),(WIDTH//dim_grille[1])))//2.5
for i in range(dim_grille[1]):
    for j in range(dim_grille[0]):
        canva_jeu.create_oval(((i+0.5)*WIDTH//dim_grille[1]-rayon_trou,(j+0.5)*HEIGHT//dim_grille[0]-rayon_trou), ((i+0.5)*WIDTH//dim_grille[1]+rayon_trou,(j+0.5)*HEIGHT//dim_grille[0]+rayon_trou), fill = "#3394ff",  outline="#004fab", width= 0.1*rayon_trou)
#----------------------------------------------#

#-----------creation des jetons-------------#
tour = "jaune"
rayon_jeton = 1.8 * rayon_trou / 2.17
def placer_jeton(event):
    global tour
    coords_trou = canva_jeu.coords(canva_jeu.find_closest(event.x, event.y))
    (milieu_x,milieu_y) = ((coords_trou[0]+coords_trou[2])//2, (coords_trou[1]+coords_trou[3])//2)
    if tour == "jaune":
        canva_jeu.create_oval((event.x-rayon_jeton,event.y-rayon_jeton), (event.x+rayon_jeton, event.y+rayon_jeton),  fill = "#ffd933",  outline = "#e7ba00", width = 0.25*rayon_jeton)
        tour = "rouge"
        return
    if tour == "rouge":
        canva_jeu.create_oval((event.x-rayon_jeton,event.y-rayon_jeton), (event.x+rayon_jeton, event.y+rayon_jeton),  fill = "#ff3b30",  outline = "#bb261f", width = 0.25*rayon_jeton)
        tour = "jaune"
root.bind("<Button-1>", placer_jeton)
root.mainloop()

