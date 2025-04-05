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
ligne = 11
colonne = 7
dim_grille = [ligne,colonne] #jeu de base donc non modifiable
grille = []
for i in range(ligne):
    grille.append([0] * colonne)
canva_jeu = tk.Canvas(root, height=HEIGHT, width=WIDTH,bg="#005bff", borderwidth=0)
canva_jeu.pack(expand=True)
rayon_trou = (min((HEIGHT//dim_grille[0]),(WIDTH//dim_grille[1])))//2.5
for i in range(dim_grille[1]):
    for j in range(dim_grille[0]):
        canva_jeu.create_oval(((i+0.5)*WIDTH//dim_grille[1]-rayon_trou,(j+0.5)*HEIGHT//dim_grille[0]-rayon_trou), ((i+0.5)*WIDTH//dim_grille[1]+rayon_trou,(j+0.5)*HEIGHT//dim_grille[0]+rayon_trou), fill = "#3394ff",  outline="#004fab", width= 0.1*rayon_trou)
#----------------------------------------------#

#-----------creation des jetons-------------#

diff_milieux_y = [i*HEIGHT//(ligne*2) for i in range(1,ligne*2,2)]
diff_milieux_y.reverse()
diff_milieux_x = [i*WIDTH//(colonne) for i in range(0,colonne+1)]
rayon_jeton = 1.8 * rayon_trou / 2.13



def verif(): #fonction qui prend en variable les coordonnees du jeton juste placé
    global win
    win = False
    ligne_fct()
    colonne_fct()
    diag_droit_gauche_fct()
    diag_gauche_droit_fct()
    if win == True:
        if tour == "j":
            print("omgomgomg jaune a gagné")
        elif tour == "r":
            print("omgomgomg rouge a gagné")
    return
    
def ligne_fct(): #Fonction qui verifie si 4 jetons sont alignés en ligne
    global win
    for i in grille:
        for j in range(4):
            if i[j] != 0:
                if (i[j] == i[j+1] == i[j+2] == i[j+3]):
                    win = True
                    
def colonne_fct(): #Fonction qui verifie si 4 jetons sont alignés en colonne
    global win
    for i in range(7):
        for j in range(3):
            if grille[j][i] != 0:    
                if (grille[j][i] == grille[j+1][i] == grille[j+2][i] == grille[j+3][i]):
                    win = True
                    
def diag_gauche_droit_fct(): #fonction qui verifie si 4 jetons sont alignés en diagonale de la gauche en haut vers la droite en bas
    global win
    for i in range(5,2,-1):
        for j in range(4):
            if grille[i][j] != 0:
                if (grille[i][j] == grille[i-1][j+1] == grille[i-2][j+2] == grille[i-3][j+3]):
                    win = True
            
def diag_droit_gauche_fct(): #fonction qui verifie si 4 jetons sont alignés en diagonale de la droite en haut vers la gauche en bas
    global win
    for i in range(6,2,-1):
        for j in range(5,2,-1):
            if grille[j][i]!= 0:
                if (grille[j][i] == grille[j-1][i-1] == grille[j-2][i-2] == grille[j-3][i-3]):
                    win = True
        
 
tour = "j"
couleur_jeton = "#ffd933" 
contour = "#e7ba00" 

def placer_jeton(event):
    global tour
    global grille
    global couleur_jeton
    global contour
    coords_trou = canva_jeu.coords(canva_jeu.find_closest(event.x, event.y))
    (milieu_x,milieu_y) = ((coords_trou[0]+coords_trou[2])//2, (coords_trou[1]+coords_trou[3])//2)
    
    for i in range(colonne):   #pour chaque colonne
        if diff_milieux_x[i] <= milieu_x < diff_milieux_x[i+1]: #Si la coordonnée x se trouve dans la ieme colonne, on entre dans la boucle
            if all(j[i] == 0 for j in grille): #cas ou toutes les trous de la colonne sont nulles
                grille[0][i] = tour #on place la couleur en bas de la grille virtuelle
                milieu_y = diff_milieux_y[0] #on place le jeton tout en bas dans le canva
                break #break pour eviter de faire tourner la boucle inutilement 
            elif grille[ligne-1][i] != 0: #On verifie si 
                print(f"La {i+1} ème colonne est pleine") #Afficher quelque part sur l écran que la colonne est pleine
                return
            else:
                for t in range(ligne-1,-1,-1): #on regarde du haut vers le bas
                    if grille[t][i] != 0: #et des qu'un trou est plein
                        grille[t+1][i] = tour #on remplit celui d'au dessus
                        milieu_y = diff_milieux_y[t+1]
                        break

    def animer_jeton(i):        
        jeton = canva_jeu.create_oval((milieu_x - rayon_jeton, i - rayon_jeton),(milieu_x + rayon_jeton, i + rayon_jeton),fill=couleur_jeton,outline=contour,width=0.25 * rayon_jeton)
        if i <milieu_y:
            root.after(200//ligne, lambda: canva_jeu.delete(jeton))  # supprime l'ancien cercle
            root.after(200//ligne, lambda: animer_jeton(diff_milieux_y[diff_milieux_y.index(i)-1]))  # récursivité qui descend jusqu'à atteindre la limite²

    animer_jeton(diff_milieux_y[-1])
    tour = "r" if tour == "j" else "j"
    couleur_jeton = "#ffd933" if tour == "j" else "#ff3b30"
    contour = "#e7ba00" if tour == "j" else "#bb261f"

root.bind("<Button-1>", placer_jeton)

root.mainloop()

