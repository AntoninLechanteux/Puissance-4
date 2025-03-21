import tkinter as tk
from math import floor

#-----------creation de la fenetre-------------#
root=tk.Tk()
root.geometry("720x480")
root.title("Menu Puissance 4")
root.attributes("-fullscreen", True)
root.bind("<Escape>", lambda event: root.destroy())
root.config(bg = "#3394ff")
#----------------------------------------------#

#-----------creation de la grille-------------#
HEIGHT = 720 
WIDTH = 1295 
ligne = int(input("Nombre de ligne: "))
colonne = int(input("Nombre de colonne: "))
dim_grille = [ligne,colonne] 
canva_jeu = tk.Canvas(root, height=HEIGHT, width=WIDTH,bg="#005bff", borderwidth=0)
canva_jeu.pack(expand=True)
rayon_trou = (min((HEIGHT//dim_grille[0]),(WIDTH//dim_grille[1])))//2.5
for i in range(dim_grille[1]):
    for j in range(dim_grille[0]):
        canva_jeu.create_oval(((i+0.5)*WIDTH//dim_grille[1]-rayon_trou,(j+0.5)*HEIGHT//dim_grille[0]-rayon_trou), ((i+0.5)*WIDTH//dim_grille[1]+rayon_trou,(j+0.5)*HEIGHT//dim_grille[0]+rayon_trou), fill = "#3394ff",  outline="#004fab", width= 0.1*rayon_trou)
#----------------------------------------------#

#-----------creation des jetons-------------#
tour = "j"
rayon_jeton = 1.8 * rayon_trou / 2.13

#Creation de la grille en tant que liste
grille = []
for i in range(ligne):
    grille.append([0] * colonne)

#Creation des milieux x et y
diff_milieux_y_mod = [i*HEIGHT/(ligne*2) for i in range(1,ligne*2,2)]
diff_milieux_y_mod.reverse()
diff_milieux_x_mod = [i*WIDTH/(colonne) for i in range(0,colonne+1)]

def verif(): #fonction qui prend en variable les coordonnees du jeton juste placé
    global win
    win = False
    ligne_fct()
    colonne_fct()
    diag_droit_gauche()
    diag_gauche_droit()
    if win == True:
        if tour == "j":
            print("omgomgomg jaune a gagné")
        elif tour == "r":
            print("omgomgomg rouge a gagné")
    return

def ligne_fct(): #Fonction qui verifie si 4 jetons sont alignés en ligne
    global win
    for i in grille:
        for j in range(colonne-3):
            if i[j] != 0:
                if (i[j] == i[j+1] == i[j+2] == i[j+3]):
                    win = True

def colonne_fct(): #Fonction qui verifie si 4 jetons sont alignés en colonne
    global win
    for i in range(colonne):
        for j in range(ligne-3):
            if grille[j][i] != 0:    
                if (grille[j][i] == grille[j+1][i] == grille[j+2][i] == grille[j+3][i]):
                    win = True

def diag_gauche_droit(): #fonction qui verifie si 4 jetons sont alignés en diagonale de la gauche en haut vers la droite en bas
    global win
    for i in range(ligne-1,2,-1):
        for j in range(colonne-3):
            if grille[i][j] != 0:
                if (grille[i][j] == grille[i-1][j+1] == grille[i-2][j+2] == grille[i-3][j+3]):
                    win = True

def diag_droit_gauche(): #fonction qui verifie si 4 jetons sont alignés en diagonale de la droite en haut vers la gauche en bas
    global win
    for i in range(colonne-1,2,-1):
        for j in range(ligne-1,2,-1):
            if grille[j][i]!= 0:
                if (grille[j][i] == grille[j-1][i-1] == grille[j-2][i-2] == grille[j-3][i-3]):
                    win = True

def placer_jeton(event):
    global tour
    global grille
    coords_trou = canva_jeu.coords(canva_jeu.find_closest(event.x, event.y))
    (milieu_x_mod,milieu_y_mod) = ((coords_trou[0]+coords_trou[2])//2, (coords_trou[1]+coords_trou[3])//2)
    for i in range(colonne):
        if diff_milieux_x_mod[i] <= milieu_x_mod < diff_milieux_x_mod[i+1]:
            if all(j[i] == 0 for j in grille): #cas ou toutes les trous de la colonne sont nulles
                grille[0][i] = tour
                milieu_y_mod = diff_milieux_y_mod[0]
                break
            elif grille[ligne-1][i] != 0:
                print(f"La {i} eme colonne est pleine") #Afficher quelque part sur l ecran que la colonne est pleine
                return
            else:
                for t in range(ligne-1,-1,-1): #on regarde du haut vers le bas
                    if grille[t][i] != 0: #Et des qu'un trou est plein
                        grille[t+1][i] = tour #On remplit celui d'au dessus
                        milieu_y_mod = diff_milieux_y_mod[t+1]
                        break
    
    if tour == "j":
        canva_jeu.create_oval((milieu_x_mod-rayon_jeton,milieu_y_mod-rayon_jeton), (milieu_x_mod+rayon_jeton, milieu_y_mod+rayon_jeton),  fill = "#ffd933",  outline = "#e7ba00", width = 0.25*rayon_jeton)
        verif()
        tour = "r"
        return
    if tour == "r":
        canva_jeu.create_oval((milieu_x_mod-rayon_jeton,milieu_y_mod-rayon_jeton), (milieu_x_mod+rayon_jeton, milieu_y_mod+rayon_jeton),  fill = "#ff3b30",  outline = "#bb261f", width = 0.25*rayon_jeton)
        verif()
        tour = "j"
        return
root.bind("<Button-1>", placer_jeton)

root.mainloop()