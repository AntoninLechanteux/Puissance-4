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
WIDTH = 1295 #Sera modifiable
dim_grille = [6,7] #jeu de base donc non modifiable
canva_jeu = tk.Canvas(root, height=HEIGHT, width=WIDTH,bg="#005bff", borderwidth=0)
canva_jeu.pack(expand=True)
rayon_trou = (min((HEIGHT//dim_grille[0]),(WIDTH//dim_grille[1])))//2.5
for i in range(dim_grille[1]):
    for j in range(dim_grille[0]):
        canva_jeu.create_oval(((i+0.5)*WIDTH//dim_grille[1]-rayon_trou,(j+0.5)*HEIGHT//dim_grille[0]-rayon_trou), ((i+0.5)*WIDTH//dim_grille[1]+rayon_trou,(j+0.5)*HEIGHT//dim_grille[0]+rayon_trou), fill = "#3394ff",  outline="#004fab", width= 0.1*rayon_trou)
#----------------------------------------------#

#-----------creation des jetons-------------#
tour = "j"
grille = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
diff_milieux_y = [660,540,420,300,180,60]
rayon_jeton = 1.8 * rayon_trou / 2.13


def verif(): #fonction qui prend en variable les coordonnees du jeton juste placé
    global win
    win = False
    ligne()
    colonne()
    diag_droit_gauche()
    diag_gauche_droit()
    if win == True:
        if tour == "j":
            print("omgomgomg jaune a gagné")
        elif tour == "r":
            print("omgomgomg rouge a gagné")
    return
    
def ligne(): #Fonction qui verifie si 4 jetons sont alignés en ligne
    global win
    for i in grille:
        for j in range(4):
            if i[j] != 0:
                if (i[j] == i[j+1] == i[j+2] == i[j+3]):
                    win = True
                    
def colonne(): #Fonction qui verifie si 4 jetons sont alignés en colonne
    global win
    for i in range(7):
        for j in range(3):
            if grille[j][i] != 0:    
                if (grille[j][i] == grille[j+1][i] == grille[j+2][i] == grille[j+3][i]):
                    win = True
                    
def diag_gauche_droit(): #fonction qui verifie si 4 jetons sont alignés en diagonale de la gauche en haut vers la droite en bas
    global win
    for i in range(5,2,-1):
        for j in range(4):
            if grille[i][j] != 0:
                if (grille[i][j] == grille[i-1][j+1] == grille[i-2][j+2] == grille[i-3][j+3]):
                    win = True
            
def diag_droit_gauche(): #fonction qui verifie si 4 jetons sont alignés en diagonale de la droite en haut vers la gauche en bas
    global win
    for i in range(6,2,-1):
        for j in range(5,2,-1):
            if grille[j][i]!= 0:
                if (grille[j][i] == grille[j-1][i-1] == grille[j-2][i-2] == grille[j-3][i-3]):
                    win = True
        
 

def placer_jeton(event):
    global tour
    global grille
    coords_trou = canva_jeu.coords(canva_jeu.find_closest(event.x, event.y))
    (milieu_x,milieu_y) = ((coords_trou[0]+coords_trou[2])//2, (coords_trou[1]+coords_trou[3])//2)
    if 0 <= milieu_x < 185: #Cas de la premiere colonne
        if all(i[0] == 0 for i in grille): #cas ou toutes les trous de la colonne sont nulles
            grille[0][0] = tour
            milieu_y = diff_milieux_y[0]
        elif grille[5][0] != 0:
            print("La premiere colonne est pleine") #Afficher quelque part sur l ecran que la colonne est pleine
            return
        else:
            for i in range(4,-1,-1): #on regarde du haut vers le bas
                if grille[i][0] != 0: #Et des qu'un trou est plein
                    grille[i+1][0] = tour #On remplit celui d'au dessus
                    milieu_y = diff_milieux_y[i+1]
                    break
    elif 185 <= milieu_x < 370: #Cas de la deuxieme colonne
        if all(i[1] == 0 for i in grille): 
            grille[0][1] = tour
            milieu_y = diff_milieux_y[0]
        elif grille[5][1] != 0:
            print("La deuxieme colonne est pleine") 
            return
        else:
            for i in range(4,-1,-1):
                if grille[i][1] != 0:
                    grille[i+1][1] = tour
                    milieu_y = diff_milieux_y[i+1]
                    break
    elif 370 <= milieu_x < 555: #Cas de la troisieme colonne
        if all(i[2] == 0 for i in grille): 
            grille[0][2] = tour
            milieu_y = diff_milieux_y[0]
        elif grille[5][2] != 0:
            print("La troisieme colonne est pleine") 
            return
        else:
            for i in range(4,-1,-1):
                if grille[i][2] != 0:
                    grille[i+1][2] = tour
                    milieu_y = diff_milieux_y[i+1]
                    break
    elif 555 <= milieu_x < 740: #Cas de la quatieme colonne
        if all(i[3] == 0 for i in grille): 
            grille[0][3] = tour
            milieu_y = diff_milieux_y[0]
        elif grille[5][3] != 0:
            print("La quatrieme colonne est pleine") 
            return
        else:
            for i in range(4,-1,-1):
                if grille[i][3] != 0:
                    grille[i+1][3] = tour
                    milieu_y = diff_milieux_y[i+1]
                    break
    elif 740 <= milieu_x < 925: #Cas de la cinquieme colonne
        if all(i[4] == 0 for i in grille): 
            grille[0][4] = tour
            milieu_y = diff_milieux_y[0]
        elif grille[5][4] != 0:
            print("La cinquieme colonne est pleine") 
            return
        else:
            for i in range(4,-1,-1):
                if grille[i][4] != 0:
                    grille[i+1][4] = tour
                    milieu_y = diff_milieux_y[i+1]
                    break
    elif 925 <= milieu_x < 1110: #Cas de la sizieme colonne
        if all(i[5] == 0 for i in grille): 
            grille[0][5] = tour
            milieu_y = diff_milieux_y[0]
        elif grille[5][5] != 0:
            print("La sizieme colonne est pleine") 
            return
        else:
            for i in range(4,-1,-1):
                if grille[i][5] != 0:
                    grille[i+1][5] = tour
                    milieu_y = diff_milieux_y[i+1]
                    break
    elif 1110 <= milieu_x <= 1295: #Cas de la septieme colonne
        if all(i[6] == 0 for i in grille): 
            grille[0][6] = tour
            milieu_y = diff_milieux_y[0]
        elif grille[5][6] != 0:
            print("La derniere colonne est pleine") 
            return
        else:
            for i in range(4,-1,-1):
                if grille[i][6] != 0:
                    grille[i+1][6] = tour
                    milieu_y = diff_milieux_y[i+1]
                    break
    if tour == "j":
        canva_jeu.create_oval((milieu_x-rayon_jeton,milieu_y-rayon_jeton), (milieu_x+rayon_jeton, milieu_y+rayon_jeton),  fill = "#ffd933",  outline = "#e7ba00", width = 0.25*rayon_jeton)
        verif()
        tour = "r"
        return
    if tour == "r":
        canva_jeu.create_oval((milieu_x-rayon_jeton,milieu_y-rayon_jeton), (milieu_x+rayon_jeton, milieu_y+rayon_jeton),  fill = "#ff3b30",  outline = "#bb261f", width = 0.25*rayon_jeton)
        verif()
        tour = "j"
        return
root.bind("<Button-1>", placer_jeton)

root.mainloop()
