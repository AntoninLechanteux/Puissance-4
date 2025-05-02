import tkinter as tk
import random as rd
import inspect 
from win32api import GetSystemMetrics
import pygame
from tkinter import ttk
#---------Importe la resolution machine--------#
width_screen = GetSystemMetrics(0)
height_screen = GetSystemMetrics(1)
#----------------------------------------------#



#----------------------------------------------#
#------Création de la fenêtre principale-------#
root=tk.Tk()
root.title("Menu Puissance 4")
root.attributes("-fullscreen", True)
root.bind("<Escape>", lambda event: root.destroy())
root.config(bg="white")
pygame.mixer.init()
#----------------------------------------------#


#----------------------------------------------#
#------Création de la fenêtre jeu normal-------#
def Jeu_normal(valeur_ligne, valeur_colonne, valeur_alignement, valeur_manche, 
               valeur_compteur_manche_J1, valeur_compteur_manche_J2, valeur_premier_joueur,
               valeur_tour, valeur_couleur_centre, valeur_couleur_bordure, valeur_grille):
    
    game = tk.Tk()
    game.title("Jeu mode normal")
    support_game = tk.Frame(game, bg="#3394ff", width=width_screen, height=width_screen)
    support_game.place(x=0, y=0)
    game.attributes("-fullscreen", True)
    game.bind("<Escape>", lambda: game.destroy())
    game.config(bg="white")

    HEIGHT = 2 * height_screen / 3
    WIDTH = 2 * width_screen / 3

    canva_jeu = tk.Canvas(support_game, height=HEIGHT, width=WIDTH, bg="#005bff")
    canva_jeu.place(x=(width_screen - WIDTH) // 8, y=(height_screen - HEIGHT) // 2)
    

    def quitter():
        global compteur_manche_J1
        global compteur_manche_J2
        compteur_manche_J1 = 0
        compteur_manche_J2 = 0
        game.destroy()
        return

    def sauvegarder_partie():
        global sauvegarde
        if (compteur_manche_J1 < valeur_manche and compteur_manche_J2 < valeur_manche):
            sauvegarde = {}
            sauvegarde['valeur_ligne'] = valeur_ligne
            sauvegarde['valeur_colonne'] = valeur_colonne
            sauvegarde['valeur_alignement'] = valeur_alignement
            sauvegarde['valeur_manche'] = valeur_manche
            sauvegarde['valeur_compteur_manche_J1'] = compteur_manche_J1
            sauvegarde['valeur_compteur_manche_J2'] = compteur_manche_J2
            sauvegarde['valeur_premier_joueur'] = premier_joueur
            sauvegarde['valeur_tour'] = valeur_tour
            sauvegarde['valeur_couleur_centre'] = valeur_couleur_centre
            sauvegarde['valeur_couleur_bordure'] = valeur_couleur_bordure
            sauvegarde["valeur_grille"] = grille.copy()
        else:
            texte_fin_de_partie = tk.Label(support_game, text= 'La partie est déjà terminée', font=("System", 35),
                                                    fg='white', bg='#3394ff')
            texte_fin_de_partie.place(x=(width_screen - texte_fin_de_partie.winfo_reqwidth())//2,
                                      y=8.7*height_screen//10)

    def sauvegarde_manche_fct():
        global sauvegarde_manche
        if (compteur_manche_J1 < valeur_manche and compteur_manche_J2 < valeur_manche):
            sauvegarde_manche = {}
            sauvegarde_manche['valeur_ligne'] = valeur_ligne
            sauvegarde_manche['valeur_colonne'] = valeur_colonne
            sauvegarde_manche['valeur_alignement'] = valeur_alignement
            sauvegarde_manche['valeur_manche'] = valeur_manche
            sauvegarde_manche['valeur_compteur_manche_J1'] = compteur_manche_J1
            sauvegarde_manche['valeur_compteur_manche_J2'] = compteur_manche_J2
            sauvegarde_manche['valeur_premier_joueur'] = premier_joueur
            sauvegarde_manche['valeur_tour'] = valeur_tour
            sauvegarde_manche['valeur_couleur_centre'] = valeur_couleur_centre
            sauvegarde_manche['valeur_couleur_bordure'] = valeur_couleur_bordure
            sauvegarde_manche["valeur_grille"] = []

    def relancer_partie():
        sauvegarde_manche_fct()
        game.destroy()
        return

    def player_switch(): #Après la chute du jeton, l'autre joueur peut jouer
                global tour
                global couleur_centre
                global couleur_bordure
                global cooldown
                if win == False:
                    cooldown=0   
                tour = valeur_tour[1] if tour == valeur_tour[0] else valeur_tour[0] 
                couleur_centre = valeur_couleur_centre[0] if tour == valeur_tour[0] else valeur_couleur_centre[1]
                couleur_bordure = valeur_couleur_bordure[0] if tour == valeur_tour[0] else valeur_couleur_bordure[1] 
                titre_jeu = tk.Label(support_game, text="Bienvenue sur Puissance 4 !", fg=valeur_couleur_centre[valeur_tour.index(tour)], 
                                     bg="#3394ff",font=("System", 45), padx=0)
                titre_jeu.place(x=(width_screen - titre_jeu.winfo_reqwidth()) // 2, y=10)

    def annuler():
        global liste_coups
        global tour
        if win == False and liste_coups != []:
            canva_jeu.create_oval((liste_coups[-1][0] - rayon_trou, liste_coups[-1][1] - rayon_trou),
                                 (liste_coups[-1][0] + rayon_trou, liste_coups[-1][1] + rayon_trou),
                                 fill = "#3394ff",outline = "#004fab", width = 0.1 * rayon_trou)
            (grille[diff_milieux_y.index(liste_coups[-1][1])][diff_milieux_x.index(liste_coups[-1][0])]) = 0
            player_switch()
            liste_coups.pop()


    global compteur_manche_J1
    global compteur_manche_J2
    global liste_coups

    compteur_manche_J1 = valeur_compteur_manche_J1
    compteur_manche_J2 = valeur_compteur_manche_J2
    liste_coups = []

    affichage_score = tk.Canvas(support_game, height=HEIGHT // 2, width=width_screen // 5,
                                bg="black", highlightbackground='#b10000')
    affichage_score.place(x=(41 * width_screen // 48) - affichage_score.winfo_reqwidth() // 2,
                          y=(height_screen - HEIGHT) // 2)

    affichage_score.create_line((0, affichage_score.winfo_reqheight() // 3.4),
                                (affichage_score.winfo_reqwidth(), affichage_score.winfo_reqheight() // 3.4),
                                fill='#b10000', width=2)
    affichage_score.create_line((0, affichage_score.winfo_reqheight() // 2),
                                (affichage_score.winfo_reqwidth(), affichage_score.winfo_reqheight() // 2),
                                fill='#b10000', width=2)
    affichage_score.create_line((affichage_score.winfo_reqwidth() // 2, affichage_score.winfo_reqheight() // 3.4),
                                (affichage_score.winfo_reqwidth() // 2, affichage_score.winfo_reqheight()),
                                fill='#b10000', width=2)

    score = tk.Label(support_game, text='SCORE', font=("System", 35),
                     fg='#b10000', bg='black')
    score.place(x=(41 * width_screen // 48) - affichage_score.winfo_reqwidth() // 2 +(affichage_score.winfo_reqwidth() - score.winfo_reqwidth()) // 2,
                y=((height_screen - HEIGHT) // 2) + 2)

    J1 = tk.Label(support_game, text='J1', font=("System", 20),
                  fg='#b10000', bg='black')
    J1.place(x=(41 * width_screen // 48) - affichage_score.winfo_reqwidth() // 2 +(affichage_score.winfo_reqwidth() // 2 - J1.winfo_reqwidth()) // 2,
             y=(height_screen - HEIGHT) // 2 + affichage_score.winfo_reqheight() // 3)

    J2 = tk.Label(support_game, text='J2', font=("System", 20),
                  fg='#b10000', bg='black')
    J2.place(x=(41 * width_screen // 48) - affichage_score.winfo_reqwidth() // 2 +(3 * affichage_score.winfo_reqwidth() // 2 - J2.winfo_reqwidth()) // 2,
             y=(height_screen - HEIGHT) // 2 + affichage_score.winfo_reqheight() // 3)

    score_J1 = tk.Label(support_game, text=compteur_manche_J1, font=("System", 45),
                        fg='#b10000', bg='black')
    score_J1.place(x=(41 * width_screen // 48) - affichage_score.winfo_reqwidth() // 2 +(affichage_score.winfo_reqwidth() // 2 - score_J1.winfo_reqwidth()) // 2,
                   y=(height_screen - HEIGHT) // 2 + affichage_score.winfo_reqheight() // 1.65)

    score_J2 = tk.Label(support_game, text=compteur_manche_J2, font=("System", 45),
                        fg='#b10000', bg='black')
    score_J2.place(x=(41 * width_screen // 48) - affichage_score.winfo_reqwidth() // 2 +(3 * affichage_score.winfo_reqwidth() // 2 - score_J2.winfo_reqwidth()) // 2,
                   y=(height_screen - HEIGHT) // 2 + affichage_score.winfo_reqheight() // 1.65)

    bouton_quitter = tk.Button(support_game, text="Quitter", font=("System", 15), fg="white",
                               bg="#ff7262", relief="raised", padx=32, command=quitter)
    bouton_quitter.place(x=(41 * width_screen // 48) - bouton_quitter.winfo_reqwidth() // 2,
                         y=7.5 * height_screen / 10)
    bouton_quitter.bind("<Enter>", lambda event : bouton_touche(event,bouton_quitter))
    bouton_quitter.bind("<Leave>", lambda event : bouton_relache(event,bouton_quitter))

    bouton_sauvegarder = tk.Button(support_game, text="Sauvegarder", font=("System", 15), fg="white",
                                           bg="#ff7262", relief="raised", padx=8, command=sauvegarder_partie)
    bouton_sauvegarder.place(x=(41 * width_screen // 48) - bouton_sauvegarder.winfo_reqwidth() // 2,
                             y=6.5 * height_screen / 10)
    bouton_sauvegarder.bind("<Enter>", lambda event : bouton_touche(event,bouton_sauvegarder))
    bouton_sauvegarder.bind("<Leave>", lambda event : bouton_relache(event,bouton_sauvegarder))
    
    bouton_annuler = tk.Button(support_game, text="Annuler", font=("System", 15), fg="white",
                                           bg="#ff7262", relief="raised", padx=29, command=annuler)
    bouton_annuler.place(x=(41 * width_screen // 48) - bouton_annuler.winfo_reqwidth() // 2,
                             y=5.5 * height_screen / 10)
    bouton_annuler.bind("<Enter>", lambda event : bouton_touche(event,bouton_annuler))
    bouton_annuler.bind("<Leave>", lambda event : bouton_relache(event,bouton_annuler))

    #----------------------------------------------#
    #-------------Création de la grille------------#
    global sauvegarde
    global cooldown

    cooldown = 0  # Empêche de jouer pendant que le jeton précédent tombe ou en cas de victoire
    ligne = valeur_ligne
    colonne = valeur_colonne
    grille = valeur_grille

    if grille == []:  # Vérifie si il y a déjà une grille (si on utilise la sauvegarde) pour en créer une vide sinon
        for i in range(ligne):
            grille.append([0] * colonne)

    rayon_trou = (min((HEIGHT // ligne), (WIDTH // colonne))) // 2.5

    for i in range(colonne):  # Crée l'affichage de la grille sans jetons
        for j in range(ligne):
            canva_jeu.create_oval(((i + 0.5) * WIDTH // colonne - rayon_trou,
                                   (j + 0.5) * HEIGHT // ligne - rayon_trou),
                                   ((i + 0.5) * WIDTH // colonne + rayon_trou,
                                    (j + 0.5) * HEIGHT // ligne + rayon_trou),
                                    fill = "#3394ff",outline = "#004fab",
                                    width = 0.1 * rayon_trou)

    
    #----------------------------------------------#
    #-------------Création des jetons--------------#
    global tour
    global couleur_centre
    global couleur_bordure
    global premier_joueur

    if valeur_compteur_manche_J1 == 0 and valeur_compteur_manche_J2 == 0:  # Vérifie si le tour est prédéfini par la sauvegarde pour restituer ou non l'ordre de jeu de la partie
        tour = rd.choice(valeur_tour)
        premier_joueur = tour  # Pour la gestion des scores
    else :
        premier_joueur = valeur_premier_joueur

    couleur_centre = valeur_couleur_centre[0] if tour == valeur_tour[0] else valeur_couleur_centre[1]  # Détermine le skin associé au tour
    couleur_bordure = valeur_couleur_bordure[0] if tour == valeur_tour[0] else valeur_couleur_bordure[1]  # Détermine le skin associé au tour

    rayon_jeton = 1.8 * rayon_trou / 2.09
    diff_milieux_y = [i * HEIGHT // (ligne * 2) for i in range(1, ligne * 2, 2)]
    diff_milieux_y.reverse()
    diff_milieux_x = [i * WIDTH // (colonne * 2) for i in range(1, (colonne + 1) * 2, 2)]

    if grille[0] != [0] * colonne:  # Réaffiche les jetons si on a activé la sauvegarde
        for i in range(ligne):
            for j in range(colonne):
                if grille[i][j] == valeur_tour[0]:
                    canva_jeu.create_oval((diff_milieux_x[j]-rayon_jeton, diff_milieux_y[i]-rayon_jeton),
                                            (diff_milieux_x[j]+rayon_jeton, diff_milieux_y[i]+rayon_jeton),
                                            fill=valeur_couleur_centre[0],outline=valeur_couleur_bordure[0],width=0.25 * rayon_jeton)
                if grille[i][j] == valeur_tour[1]:
                    canva_jeu.create_oval((diff_milieux_x[j]-rayon_jeton, diff_milieux_y[i]-rayon_jeton),
                                            (diff_milieux_x[j]+rayon_jeton, diff_milieux_y[i]+rayon_jeton),
                                            fill=valeur_couleur_centre[1],outline=valeur_couleur_bordure[1],width=0.25 * rayon_jeton)
                        
    #----------------------------------------------#
    #----------Fonctions de vérification-----------#
    def verif(): #Fonction qui vérifie si 4 jetons sont allignés
        global win
        global compteur_manche_J1
        global compteur_manche_J2
        global sauvegarde
        global cooldown

        win = False
        verif_ligne()
        verif_colonne()
        verif_diag_gauche_droite()
        verif_diag_droite_gauche()

        if win == True:
            if tour == premier_joueur :
                compteur_manche_J1 += 1  
            else :
                compteur_manche_J2 += 1 

            if (compteur_manche_J1 < valeur_manche and compteur_manche_J2 < valeur_manche) :
                texte_fin_de_partie = tk.Label(support_game, text= f"{tour} marque 1 point", font=("System", 35),
                                                fg='white', bg='#3394ff')
                texte_fin_de_partie.place(x=(width_screen - texte_fin_de_partie.winfo_reqwidth())//2,
                                            y=8.7*height_screen//10)
                
                root.after(2000,relancer_partie)
                root.after(2000, lambda : Jeu_normal(sauvegarde_manche['valeur_ligne'], sauvegarde_manche['valeur_colonne'],
                                                    sauvegarde_manche['valeur_alignement'], sauvegarde_manche['valeur_manche'],
                                                    sauvegarde_manche['valeur_compteur_manche_J1'],sauvegarde_manche['valeur_compteur_manche_J2'], sauvegarde_manche['valeur_premier_joueur'],
                                                    sauvegarde_manche['valeur_tour'],sauvegarde_manche['valeur_couleur_centre'], 
                                                    sauvegarde_manche['valeur_couleur_bordure'],sauvegarde_manche['valeur_grille']))
                
            elif (compteur_manche_J1 == valeur_manche or compteur_manche_J2 == valeur_manche)  :
                sauvegarde = {}
                score_J1 = tk.Label(support_game, text=compteur_manche_J1, font=("System",45), fg = '#b10000', bg ='black')
                score_J1.place(x = (41*width_screen//48) - affichage_score.winfo_reqwidth()//2 + (affichage_score.winfo_reqwidth()//2-score_J1.winfo_reqwidth())//2,
                               y =(height_screen-HEIGHT)//2 + affichage_score.winfo_reqheight()//1.65)
                
                score_J2 = tk.Label(support_game, text=compteur_manche_J2, font=("System",45), fg = '#b10000', bg ='black')
                score_J2.place(x = (41*width_screen//48) - affichage_score.winfo_reqwidth()//2 + (3*affichage_score.winfo_reqwidth()//2-score_J2.winfo_reqwidth())//2,
                               y =(height_screen-HEIGHT)//2 + affichage_score.winfo_reqheight()//1.65)
                
                texte_fin_de_partie = tk.Label(support_game, text= f"{tour} remporte la partie", font=("System", 35),
                                                fg='white', bg='#3394ff')
                texte_fin_de_partie.place(x=(width_screen - texte_fin_de_partie.winfo_reqwidth())//2,
                                            y=8.7*height_screen//10)

    def verif_ligne(): #Fonction qui verifie si 4 jetons sont alignés en ligne
        global win
        for i in grille:
            for j in range(valeur_colonne - (valeur_alignement - 1)):#Vérifie l'alignement jusqu'au dernier jeton pertinent à contrôler
                if i[j] != 0:
                    if all(i[j+k] == i[j] for k in range(1,valeur_alignement)):# Vérifie si les jetons d'après prennent la même valeur
                        win = True
                          
    def verif_colonne(): #Fonction qui verifie si 4 jetons sont alignés en colonne
        global win
        for i in range(valeur_ligne - (valeur_alignement - 1)):
            for j in range(valeur_colonne): #Vérifie l'alignement jusqu'au dernier jeton pertinent à contrôler
                if grille[i][j] != 0:    
                    if all(grille[i][j] == grille[i+k][j] for k in range(1,valeur_alignement)):# Vérifie si les jetons d'après prennent la même valeur
                            win = True
                        
    def verif_diag_gauche_droite(): #fonction qui verifie si 4 jetons sont alignés en diagonale de la gauche en haut vers la droite en bas
            global win
            for i in range(valeur_alignement - 1, valeur_ligne):
                for j in range(valeur_colonne - (valeur_alignement - 1)):#Vérifie l'alignement jusqu'au dernier jeton pertinent à contrôler
                    if grille[i][j] != 0:    
                            if all(grille[i][j] == grille[i-k][j+k] for k in range(1,valeur_alignement)):# Vérifie si les jetons d'après prennent la même valeur
                                    win = True
                    
    def verif_diag_droite_gauche(): #fonction qui verifie si 4 jetons sont alignés en diagonale de la droite en haut vers la gauche en bas
            global win
            for i in range(valeur_alignement - 1, valeur_ligne):
                for j in range(valeur_alignement - 1, valeur_colonne):#Vérifie l'alignement jusqu'au dernier jeton pertinent à contrôler
                    if grille[i][j] != 0:    
                            if all(grille[i][j] == grille[i-k][j-k] for k in range(1,valeur_alignement)):# Vérifie si les jetons d'après prennent la même valeur
                                    win = True

    
    #----------------------------------------------#
    #------------Animation des jetons--------------#
    def placer_jeton(event):
        global tour
        global couleur_centre
        global couleur_bordure
        global cooldown
        global liste_coups

        coords_trou = canva_jeu.coords(canva_jeu.find_closest(event.x, event.y))  # Détermine la position du trou le plus proche

        (milieu_x, milieu_y) = ((coords_trou[0] + coords_trou[2]) // 2,
                                (coords_trou[1] + coords_trou[3]) // 2)  # Trouve le centre du trou le plus proche

        if cooldown == 0 and cursor_grid == True:
            cooldown = 1
            for i in range(colonne):  # Pour chaque colonne
                if diff_milieux_x[i] <= milieu_x < diff_milieux_x[i + 1]:  # Si la coordonnée x se trouve dans la ieme colonne, on entre dans la boucle
                    if all(j[i] == 0 for j in grille):  # cas ou toutes les trous de la colonne sont nulles
                        grille[0][i] = tour  # on place la couleur en bas de la grille virtuelle
                        milieu_y = diff_milieux_y[0]  # on place le jeton tout en bas dans le canva
                        break  # break pour eviter de faire tourner la boucle inutilement
                    elif grille[ligne - 1][i] != 0:  # On verifie si
                        print(f"La {i+1} ème colonne est pleine")  # Afficher quelque part sur l écran que la colonne est pleine
                        return
                    else:
                        for t in range(ligne - 1, -1, -1):  # on regarde du haut vers le bas
                            if grille[t][i] != 0:  # et des qu'un trou est plein
                                grille[t + 1][i] = tour  # on remplit celui d'au dessus
                                milieu_y = diff_milieux_y[t + 1]
                                break
            liste_coups.append([milieu_x, milieu_y])

            
            def animer_jeton(i): #Animation de chute   
                if i == milieu_y:#Repasse le contour en bleu si il était en surbrillance avant de poser le jeton
                    jeton_2 = jeton = canva_jeu.find_closest(milieu_x, milieu_y)
                    canva_jeu.itemconfigure(jeton_2, outline = '#004fab')
                    if (compteur_manche_J1 < valeur_manche) and (compteur_manche_J2 < valeur_manche):
                        root.after(100,player_switch)

                jeton = canva_jeu.create_oval((milieu_x - rayon_jeton, i - rayon_jeton),(milieu_x + rayon_jeton, i + rayon_jeton),fill=couleur_centre,
                                              outline=couleur_bordure,width=0.25 * rayon_jeton)
                if i <milieu_y:
                    game.after(200//ligne, lambda: canva_jeu.delete(jeton))  # Supprime l'ancien cercle
                    game.after(200//ligne, lambda: animer_jeton(diff_milieux_y[diff_milieux_y.index(i)-1]))  # Récursivité qui descend jusqu'à atteindre la limite
                
            
            animer_jeton(diff_milieux_y[-1])
            pygame.mixer.music.load("Hit Marker sound effect.mp3")
            pygame.mixer.music.play(loops=0)
            verif()

        elif cooldown == 1 or cursor_grid == False:
            return
    
    game.bind("<Button-1>", placer_jeton)#Pose un jeton si les conditions sont remplies    

    #----------------------------------------------#
    #----------Effets graphiques grille------------#
    def surbrillance_contour(event):  # Cercles blancs pour indiquer dans quelle colonne on va jouer
        global grille_bleue  # Evite de superposer des cercles bleus à l'infini
        global grille_blanche # Evite de superposer des cercles blancs à l'infini
        grille_bleue = False
        grille_blanche = False

        x = event.x
        y = event.y
        overlapping = canva_jeu.find_overlapping(x - 1, y - (HEIGHT // (2 * ligne)), x + 1, y + (HEIGHT // (2 * ligne)))

        if len(overlapping) != 0:
            coords_overlapping = canva_jeu.coords(overlapping[-1])

        # Si on ne touche aucun jeton, tout repasse en bleu
        if len(overlapping) == 0 and grille_bleue == False:
            for i in range(colonne):  
                for j in range(ligne):
                    if grille[j][i] == 0:
                        jeton = canva_jeu.find_closest(diff_milieux_x[i], diff_milieux_y[j])
                        canva_jeu.itemconfigure(jeton, outline = '#004fab')
            grille_bleue = True
            grille_blanche = False

        if len(overlapping) != 0 and grille_blanche == False:
            coords_trou_x = (coords_overlapping[0] + coords_overlapping[2]) // 2
            for i in range(colonne):  
                if diff_milieux_x[i] <= coords_trou_x < diff_milieux_x[i + 1]:  # On vérifie si le jeton survolé est dans celle-ci
                    for j in range(ligne):  # Et pour chaque jeton de la colonne
                        if grille[j][i] == 0:  # On passe le contour des trous en blanc
                            jeton = canva_jeu.find_closest(diff_milieux_x[i], diff_milieux_y[j])
                            canva_jeu.itemconfigure(jeton, outline = "white")
            grille_bleue = False
            grille_blanche = True

    titre_jeu = tk.Label(support_game, text="Bienvenue sur Puissance 4 !", fg=valeur_couleur_centre[valeur_tour.index(tour)], 
                        bg="#3394ff",font=("System", 45), padx=0)
    titre_jeu.place(x=(width_screen - titre_jeu.winfo_reqwidth()) // 2, y=10)
    
    def cursor_in_grid(event):
        global cursor_grid
        cursor_grid = True

    def cursor_not_in_grid(event):
        global cursor_grid
        cursor_grid = False

    canva_jeu.bind("<Motion>", surbrillance_contour)
    canva_jeu.bind('<Enter>', cursor_in_grid)  # Vérifient si le curseur est dans la grille pour poser le jeton après un clic
    canva_jeu.bind('<Leave>', cursor_not_in_grid)       

    game.mainloop()
    return

#----------------------------------------------#


#----------------------------------------------#
#-----Création de la fenêtre de jeu Sandbox----#
def Jeu_sandbox():
    def fermer():
        mod.destroy()
        return
#-----------creation de la fenetre-------------#
    mod=tk.Tk()
    mod.geometry("720x480")
    mod.attributes("-fullscreen", True)
    mod.config(bg = "#3394ff")
    mod.title("Jeu mode sandbox")
#----------------------------------------------#
    sand_height = height_screen
    sand_width = width_screen
    sand = tk.LabelFrame(mod, height=sand_height, width=sand_width, bg="#6db3fe", relief="ridge")
    sand.place(x=0, y=0)
    global dpos
    global Lerror1
    global Lerror2
    global Lerror3

    end_pos = -sand_width
    start_pos = 0
    dpos = 0
    dt = 3
    
    #Definition des emplacements les parametres choisis rendent la partie injouable 
    Lerror1 = tk.Label(sand,text= "", font=("System",17), bg="#6db3fe", fg="white")
    Lerror1.place(x=width_screen/2,y=7*height_screen/9)
    
    Lerror2 = tk.Label(sand, text="", font=("System",17), bg="#6db3fe", fg="white")
    Lerror2.place(x = width_screen/2, y=8*height_screen/10)
    
    Lerror3 = tk.Label(sand, text = "", font=("System",17), bg="#6db3fe", fg="white", width=30)
    Lerror3.place(x=width_screen/2,y=6*height_screen/9)
    
    
    def animation_panel():
        global Lerror1
        global Lerror2
        global Lerror3
        if (int(colonne.get()) == 0) or (int(ligne.get()) == 0) or (Choix_joueur1["text"]=="") or (Choix_joueur2["text"]=="") or (int(SBalignement.get())== 0) and (int(SBmanche.get())== 0):
            Lerror1["text"] = "Un parametre est nul, veuillez modifier sa valeur"
            WLerror1 = Lerror1.winfo_reqwidth()
            Lerror1.place(x=width_screen/2-WLerror1/2,y=7*height_screen/9)
        else:
            Lerror1["text"] = ""
            Lerror1.place(x=width_screen/2,y=7*height_screen/9)
            if int(colonne.get()) == 1 or int(ligne.get()) == 1:
                Lerror2["text"] = "Cette grille est injouable, veuillez ajuster sa taille."
                WLerror2 = Lerror2.winfo_reqwidth()
                Lerror2.place(x=width_screen/2- WLerror2/2,y=8*height_screen/10)
            else:
                Lerror2["text"] = ""
                Lerror2.place(x = width_screen/2, y=8*height_screen/10)
                if (int(SBalignement.get()) >= int(colonne.get())) or (int(SBalignement.get()) >= int(ligne.get())):
                    Lerror3["text"] = "Vous ne pouvez pas aligner autant de \n jetons dans une si petite grille."
                    WLerror3 = Lerror3.winfo_reqwidth()
                    Lerror3.place(x=width_screen/2- WLerror3/2,y=6*height_screen/9)
                else:
                    Lerror3["text"] = ""
                    Lerror3.place(x=width_screen/2,y=6*height_screen/9)
                    global dpos
                    sand.place(x=start_pos, y=0)
                    if dpos < abs(end_pos):
                        sand.place(x=start_pos-dpos, y=0)
                        dpos += 1
                        root.after(dt, animation_panel)
                    else:
                        sand.place(x=end_pos, y=0)
                        dpos = 0

                        def lancer_jeu():
                            # Récupération des données avant destruction de mod
                            lignes = int(ligne.get())
                            colonnes = int(colonne.get())
                            alignement = int(SBalignement.get())
                            manches = int(SBmanche.get())
                            joueur1 = Choix_joueur1["text"]
                            joueur2 = Choix_joueur2["text"]
                            couleur_centre_j1 = couleurs_centre[nom_couleur.index(joueur1)]
                            couleur_centre_j2 = couleurs_centre[nom_couleur.index(joueur2)]
                            couleur_bordure_j1 = couleurs_bordure[nom_couleur.index(joueur1)]
                            couleur_bordure_j2 = couleurs_bordure[nom_couleur.index(joueur2)]

                            mod.destroy()

                            # Maintenant qu'on a toutes les infos, on peut lancer Jeu_normal
                            Jeu_normal(
                                lignes, colonnes, alignement, manches, 0, 0, "",
                                [joueur1, joueur2],
                                [couleur_centre_j1, couleur_centre_j2],
                                [couleur_bordure_j1, couleur_bordure_j2],
                                [])


                        mod.after(1, lancer_jeu)

            
         
    #Boutons en bas de l'écran
    M1=tk.Label(sand, text="Configuations", bg="#ff7262", fg="white", font=("System",30), relief="raised", padx=14, pady=15)
    wM1 = M1.winfo_reqwidth()
    hM1 = M1.winfo_reqheight()
    M1.place(x=sand_width/2-wM1/2, y=0.5*hM1)
    
    Bhome=tk.Button(sand, text="Quitter", font=("System",15),
                 fg="white", bg="#ff7262", relief="ridge", padx=10, pady=5, command=fermer)
    wBhome = Bhome.winfo_reqwidth()
    hBhome = Bhome.winfo_reqheight()
    Bhome.place(x=sand_width/6-wBhome/2, y=sand_height-1.5*hBhome)
    
    Bplay = tk.Button(sand, text="Jouer",font=("System",15), fg="white", bg="#ff7262", relief="ridge", padx=10, pady=5, 
                      command= animation_panel) #Bouton play
    wBplay = Bplay.winfo_reqwidth()
    hBplay = Bplay.winfo_reqheight()
    Bplay.place(x=sand_width/1.2-wBplay/2, y=sand_height-1.5*hBplay)
    
    Cita = tk.Label(sand, text='"La stratégie commence ici" - Luca Picciotto',bg="#ff7262", fg="white", font=("System",23,"underline"), relief="raised", padx=10, pady=10)
    wCita = Cita.winfo_reqwidth()
    hCita = Cita.winfo_reqheight()
    Cita.place(x=sand_width/2 - wCita/2, y = sand_height - 1.5*hCita)
    
    #Spinbox a gauche de l'écran
    Mcol = tk.Label(sand, text=" Nombre de colonne :", fg="white",  bg= "#6db3fe", font=("System",22))
    wMcol = Mcol.winfo_reqwidth() 
    Mcol.place(x=sand_width/5-wMcol/2, y=sand_height/5-50)
    colonne = tk.Spinbox(sand, from_= 1, to = 100,
            validate='all', fg="#6db3fe", width=8, borderwidth=3, relief="sunken", font=("System", 15))
    wcolonne = colonne.winfo_reqwidth()
    colonne.place(x=sand_width/5-wcolonne/2, y=sand_height/5)
    
    Mlig = tk.Label(sand, text="Nombre de ligne :", fg="white",  bg= "#6db3fe", font=("System",22))
    wMlig = Mlig.winfo_reqwidth()
    Mlig.place(x=sand_width/5-wMlig/2, y=2*sand_height/5-50)
    ligne = tk.Spinbox(sand, from_= 1, to = 100,
            validate='all', fg="#3394ff", width=8, borderwidth=3, relief="sunken", font=("System", 15))
    wligne = ligne.winfo_reqwidth()
    ligne.place(x=sand_width/5-wligne/2, y=2*sand_height/5)  
    
    alignement = tk.Label(sand,text = "Nombre de jeton à aligner: ", fg="white",  bg= "#6db3fe", font=("System",22))
    walignement = alignement.winfo_reqwidth()
    alignement.place(x=sand_width/5 - walignement/2, y=3*sand_height/5-50)
    SBalignement = tk.Spinbox(sand, from_= 1, to = 100, fg="#6db3fe", width=8, borderwidth=3, relief="sunken", font=("System", 15))
    wSBalignement = SBalignement.winfo_reqwidth()
    SBalignement.place(x=sand_width/5 - wSBalignement/2, y=3*sand_height/5)
    
    manche = tk.Label(sand,text = "Nombre de manche: ", fg="white",  bg= "#6db3fe", font=("System",22))
    wmanche = manche.winfo_reqwidth()
    manche.place(x=sand_width/5 - wmanche/2, y=4*sand_height/5-50)
    SBmanche = tk.Spinbox(sand, from_= 1, to = 100, fg="#6db3fe", width=8, borderwidth=3, relief="sunken", font=("System", 15))
    wSBmanche = SBmanche.winfo_reqwidth()
    SBmanche.place(x=sand_width/5 - wSBmanche/2, y=4*sand_height/5)
    
    #Choix des couleurs + affichage 
    LBcolor = tk.Listbox(sand, height=5, width=23, selectbackground= "blue", font=("System",15))
    wLBcolor = LBcolor.winfo_reqwidth()
    LBcolor.place(x=4*sand_width/5-wLBcolor/2, y=2*sand_height/8)
    sbar = ttk.Scrollbar(sand, command=LBcolor.yview)
    sbar.place(x=4*sand_width/5 + wLBcolor/2, y=2*sand_height/8, height = LBcolor.winfo_reqheight())
    LBcolor.config(yscrollcommand=sbar.set)
    joueur1 = tk.Label(sand, text="Joueur 1 :",border=0, background="#6db3fe", fg = "white", font=("System",20))
    wjoueur1 = joueur1.winfo_reqwidth()
    joueur1.place(x=4*sand_width/5-wjoueur1/2-35, y=4*sand_height/8)
    Choix_joueur1 = tk.Label(sand,text = "",border=0, background="#6db3fe", font=("System",20), fg = "white")
    wChoix_joueur1 = Choix_joueur1.winfo_reqwidth()
    Choix_joueur1.place(x=4*sand_width/5-wChoix_joueur1/2+35, y=4*sand_height/8)
    joueur2 = tk.Label(sand, text="Joueur 2 :",border=0, background="#6db3fe", font=("System",20), fg = "white")
    wjoueur2 = joueur2.winfo_reqwidth()
    joueur2.place(x=4*sand_width/5-wjoueur2/2-35, y=5*sand_height/8)
    Choix_joueur2 = tk.Label(sand,text = "",border=0, background="#6db3fe", font=("System",20), fg = "white")
    wChoix_joueur2 = Choix_joueur2.winfo_reqwidth()
    Choix_joueur2.place(x=4*sand_width/5-wChoix_joueur2/2+35,y=5*sand_height/8)
    
    #Rendu au centre de la page
    rendu = tk.Canvas(sand, bg="#005bff", height=height_screen/7, width=width_screen/7)
    hrendu = rendu.winfo_reqheight()
    wrendu= rendu.winfo_reqwidth()
    rendu.place(x=sand_width/2-wrendu/2, y=sand_height/2-hrendu/2)
    
    
    def maj(*args):
        rendu.delete("all")  #On efface l'ancien dessin
        nb_col = int(colonne.get())
        nb_lig = int(ligne.get())
        #Dimensions fixes du Canvas
        canvas_width = width_screen / 7
        canvas_height = height_screen / 7

        #Rayon des trous en fonction du nombre de lignes et colonnes
        rayon_trou = min(canvas_width / nb_col, canvas_height / nb_lig) / 2.5

        for i in range(nb_col):
            for j in range(nb_lig):
                x_center = (i + 0.5) * (canvas_width / nb_col)
                y_center = (j + 0.5) * (canvas_height / nb_lig)
                rendu.create_oval(x_center - rayon_trou, y_center - rayon_trou, x_center + rayon_trou, y_center + rayon_trou, fill="#3394ff",
                    outline="#004fab", width=0.1 * rayon_trou)
        return
    
    #Lier les variables aux changements
    def maj_spinbox(event):
        sand.after_idle(maj)

    colonne.bind("<KeyRelease>", maj_spinbox)
    colonne.bind("<ButtonRelease-1>", maj_spinbox)

    ligne.bind("<KeyRelease>", maj_spinbox)
    ligne.bind("<ButtonRelease-1>", maj_spinbox)
    #Première mise à jour de l'affichage
    maj()
    
    
    # ------------------- Configuration des listebox ------------------ #
    for item in nom_couleur: #Ajoute les couleurs disponibles a la listebox
        LBcolor.insert(tk.END,item)
    
    def color():
        for i in range(len(nom_couleur)):
            LBcolor.itemconfigure(i, background=couleurs_centre[i])
    
    color()
    
    def print_selec():  #Impression sur l'ecran de la couleur choisie  
        if Choix_joueur1["text"] == "":
            Choix_joueur1["text"]= LBcolor.get(LBcolor.curselection())
            LBcolor.delete(LBcolor.curselection()) #suppression dans les choix pour pas se faire affronter les memes couleurs
        elif Choix_joueur1["text"] != "" and Choix_joueur2["text"] == "":
            Choix_joueur2["text"] = LBcolor.get(LBcolor.curselection())
            LBcolor.delete(LBcolor.curselection())
        return   
    
    def annuler():  #réinsertion des couleurs choisies dans la liste des couleurs dispo et suppression des couleurs choisies
        if (Choix_joueur1["text"] != "" and Choix_joueur2["text"] != ""):
            LBcolor.insert(tk.END,Choix_joueur1["text"])
            LBcolor.itemconfigure(len(nom_couleur)-2,background=couleurs_centre[nom_couleur.index(Choix_joueur1["text"])])
            Choix_joueur1["text"] = ""
            LBcolor.insert(tk.END,Choix_joueur2["text"]) 
            LBcolor.itemconfigure(len(nom_couleur)-1,background=couleurs_centre[nom_couleur.index(Choix_joueur2["text"])])
            Choix_joueur2["text"] = ""
        elif Choix_joueur1["text"] != "":
            LBcolor.insert(tk.END,Choix_joueur1["text"])
            LBcolor.itemconfigure(len(nom_couleur)-1,background=couleurs_centre[nom_couleur.index(Choix_joueur1["text"])])
            Choix_joueur1["text"] = "" 
        return
    
    #Boutons de selection/suppression des couleurs
    select = tk.Button(sand,text = "Selectionner", command=print_selec, font=("System", 15), fg="white", bg="#ff7262", relief="ridge")
    wselect = select.winfo_reqwidth()
    select.place(x=4*sand_width/5-wselect/2+52, y=3*sand_height/8)
    retour = tk.Button(sand, text= "Annuler", command=annuler, font=("System", 15), fg="white", bg="#ff7262", relief="ridge")
    wretour = retour.winfo_reqwidth()
    retour.place(x=4*sand_width/5-wretour/2-52, y=3*sand_height/8)

    mod.mainloop()
    return

def settings():
    def fermer():
        option.destroy()
        return
    option=tk.Tk()
    option.columnconfigure(0, weight=1)
    option.columnconfigure(1, weight=1)
    option.columnconfigure(2, weight=1)
    option.rowconfigure(0, weight=1)
    option.rowconfigure(1, weight=1)
    option.rowconfigure(2, weight=1)
    option.rowconfigure(3, weight=1)
    option.rowconfigure(4, weight=1)
    option.title("option du jeu")
    option.attributes("-fullscreen", True)
    B6=tk.Button(option, text="Valider et quitter", font=("haelvetica",15),
                 fg="black", bg="lightgrey", relief="ridge", padx=10, pady=5, command=fermer)
    B6.pack(side=tk.BOTTOM)
#-----------------Affichage des règles-----------------#
index = 0
text = ""
def rules():
    def fermer():
        rules.destroy()
        return
    global index,text
    HEIGHT=0.9*height_screen
    WIDTH=200
    regles = "Le but du jeu est d'aligner 4 jetons de sa couleur horizontalement,\n verticalement ou diagonalement. \n \n Le jeu se joue à deux joueurs, chacun ayant une couleur de jeton différente. \n \n" \
    " Le premier joueur à aligner 4 jetons de sa couleur gagne la partie. \n \n Pour placer un jeton, il suffit de cliquer sur la case \ndans laquelle vous souhaitez le placer. \n \n Le jeu se termine lorsqu'un joueur a aligné 4 jetons ou lorsque la grille est pleine. "
    rules=tk.Tk()
    rules.title("Règles du jeu")
    rules.attributes("-fullscreen", True)
    rules.config(bg="#3394ff")
    support_rules = tk.Frame(rules, bg="#3394ff", width = width_screen, height= width_screen)
    support_rules.place(x=0, y=0)
    
    M2=tk.Label(support_rules, text="Voici les règles du jeu! ", font=("System", 35), fg="White", bg="#3394ff")
    wM2 = M2.winfo_reqwidth()
    hM2 = M2.winfo_reqheight()
    M2.place(x=width_screen/2-wM2/2, y=0.2*hM2)
    M3=tk.Label(support_rules, text=regles, font=("System", 20), fg="white", bg="#3394ff", width=65)
    wM3 = M3.winfo_reqwidth()
    hM3 = M3.winfo_reqheight()
    M3.place(x=width_screen/2-wM3/2, y=height_screen/4-hM3/2) 
    B5=tk.Button(support_rules, text="Quitter", font=("System",15), fg="white", 
                 bg="#ff7262", relief="ridge", command=fermer, padx=10, pady=5)
    wB5 = B5.winfo_reqwidth()
    hB5 = B5.winfo_reqheight()
    B5.place(x=width_screen/2-wB5/2, y=height_screen-1.5*hB5)
    
    frame_gauche = tk.Frame(support_rules, height=HEIGHT, width=WIDTH, bg ="#3394ff")
    hframe_gauche = frame_gauche.winfo_reqheight()
    frame_droite = tk.Frame(support_rules, height=HEIGHT, width=WIDTH, bg ="#3394ff")
    wframe_droite = frame_droite.winfo_reqwidth()
    hframe_droite = frame_droite.winfo_reqheight()
    jeton_gauche_1 = tk.Canvas(frame_gauche, height=200, width=200, bg ='#3394ff', highlightthickness=0)
    jeton_gauche_1_counter = 1
    jeton_gauche_2 = tk.Canvas(frame_gauche, height=200, width=200, bg ='#3394ff', highlightthickness=0)
    jeton_gauche_2_counter = 0
    jeton_droite_1 = tk.Canvas(frame_droite, height=200, width=200, bg ='#3394ff', highlightthickness=0)
    jeton_droite_1_counter = 0
    jeton_droite_2 = tk.Canvas(frame_droite, height=200, width=200, bg ='#3394ff', highlightthickness=0)
    jeton_droite_2_counter = 1

    hjeton = jeton_gauche_1.winfo_reqheight()
    wjeton = jeton_gauche_1.winfo_reqwidth()
    jeton_gauche_1.place(x=WIDTH/2-wjeton/2, y=0)
    jeton_gauche_2.place(x=WIDTH/2-wjeton/2, y=HEIGHT-hjeton)
    jeton_gauche_1.create_oval((25,25),(175,175), fill="#ffd933", outline = "#e7ba00", width = 25 )
    jeton_gauche_2.create_oval((25,25),(175,175), fill="#ff3b30", outline = "#bb261f", width = 25  )
    jeton_droite_1.place(x=WIDTH/2-wjeton/2, y=0)
    jeton_droite_2.place(x=WIDTH/2-wjeton/2, y=HEIGHT-hjeton)
    jeton_droite_1.create_oval((25,25),(175,175), fill="#ff3b30", outline = "#bb261f", width = 25 )
    jeton_droite_2.create_oval((25,25),(175,175), fill="#ffd933", outline = "#e7ba00", width = 25  )
    frame_gauche.place(x=0, y=height_screen/2-hframe_gauche/2)
    frame_droite.place(x=width_screen-wframe_droite, y=height_screen/2-hframe_droite/2)
    Tg=tk.Label(frame_gauche, text="P\nU\nI\nS\nS\nA\nN\nC\nE\n-\n4", font=("System", 17), fg="White", bg="#3394ff")
    Td=tk.Label(frame_droite, text="P\nU\nI\nS\nS\nA\nN\nC\nE\n-\n4", font=("System",17), fg="White", bg="#3394ff")
    hT = Tg.winfo_reqheight()
    wT = Tg.winfo_reqwidth()
    Tg.place(x=WIDTH/2-wT/2, y=HEIGHT/2-hT/2)
    Td.place(x=WIDTH/2-wT/2, y=HEIGHT/2-hT/2)

    jeton_gauche_1.bind('<ButtonPress-1>',lambda event : animation_clic(event, jeton_gauche_1))
    jeton_gauche_1.bind('<ButtonRelease-1>', lambda event : animation_relache(event, jeton_gauche_1))
    jeton_gauche_2.bind('<ButtonPress-1>',lambda event : animation_clic(event, jeton_gauche_2))
    jeton_gauche_2.bind('<ButtonRelease-1>', lambda event : animation_relache(event, jeton_gauche_2))
    jeton_droite_1.bind('<ButtonPress-1>',lambda event : animation_clic(event, jeton_droite_1))
    jeton_droite_1.bind('<ButtonRelease-1>', lambda event : animation_relache(event, jeton_droite_1))
    jeton_droite_2.bind('<ButtonPress-1>',lambda event : animation_clic(event, jeton_droite_2))
    jeton_droite_2.bind('<ButtonRelease-1>', lambda event : animation_relache(event, jeton_droite_2))
        
    def animation2():
        M4=tk.Label(support_rules, text='A VOUS DE JOUER !!', font=("System", 35), fg="white", bg="#3394ff", width=20)
        wM4 = M4.winfo_reqwidth()
        M4.place(x=width_screen/2-wM4/2, y=height_screen/1.5)    
        return

    def animation1():
        global index,text
        if index >= len(regles):
            index =- 1
            text = ""
            M3.config(text=regles)
        else:
            text = [text[i] for i in range(len(text)-2)]
            text = ''.join(text)
            text = text + regles[index] + " I"
            M3.config(text=text)
            index += 1
            rules.after(50, animation1)
    M3.place(x=width_screen/2-wM3/2, y=height_screen/2-hM3/1.5)
    rules.after(20, animation1)
    rules.after(29000, animation2)
    return
#----------------------------------------------------------#
#---------------creation des widget menu-------------------#
HEIGHT=0.9*height_screen
WIDTH=200
support_root = tk.Frame(root, bg="#3394ff", width = width_screen, height= width_screen)
support_button = tk.Frame(support_root, bg="#3394ff")

B1=tk.Button(support_button, text="PARTIE NORMALE", font=('system', 20), bg="#ff7262",
             fg="white", relief="raised", padx=5, pady=15, command= (lambda : Jeu_normal(valeur_ligne=6, valeur_colonne=7,valeur_alignement = 4, valeur_manche = 2, 
                                                                                        valeur_compteur_manche_J1 = 0,valeur_compteur_manche_J2 = 0,valeur_premier_joueur = '',
                                                                                        valeur_tour=['Jaune','Rouge'], valeur_couleur_centre=['#ffd933', '#ff3b30'],
                                                                                        valeur_couleur_bordure=['#e7ba00', '#bb261f'],valeur_grille=[])))
B2=tk.Button(support_button, text="PARTIE CUSTOM", font=('system', 20), bg="#ff7262", 
             fg="white", relief="raised", padx=14, pady=15, command=Jeu_sandbox)
B3=tk.Button(support_button, text="SAUVEGARDE", font=('system', 20), bg="#ff7262", 
             fg="white", relief="raised", padx=33, pady=15, command= (lambda : Jeu_normal(sauvegarde['valeur_ligne'], sauvegarde['valeur_colonne'],
                                                                                        sauvegarde['valeur_alignement'], sauvegarde['valeur_manche'],
                                                                                        sauvegarde['valeur_compteur_manche_J1'],sauvegarde['valeur_compteur_manche_J2'], sauvegarde['valeur_premier_joueur'],
                                                                                        sauvegarde['valeur_tour'],sauvegarde['valeur_couleur_centre'], 
                                                                                        sauvegarde['valeur_couleur_bordure'],sauvegarde['valeur_grille'])))
B4=tk.Button(support_button, text="REGLES", font=('system', 20), bg="#ff7262", 
             fg="white", relief="raised", padx=69, pady=15, command=rules)
M1=tk.Label(support_root, text="Bienvenue sur Puissance 4 !", fg="white",  bg= "#3394ff",
                  font=("System",45))
wB1 = B1.winfo_reqwidth()
hB1 = B1.winfo_reqheight()
wM1 = M1.winfo_reqwidth()
hM1 = M1.winfo_reqheight()
support_button.config(width=wB1, height=360)
dy = 8
support_button.place(x=width_screen/2-wB1/2, y=height_screen/2-hB1*2)
B1.place(x=0, y=0)
B2.place(x=0, y=hB1+dy)
B3.place(x=0, y=2*hB1+2*dy)
B4.place(x=0, y=3*hB1+3*dy)
M1.place(x=width_screen/2-wM1/2, y=0.2*hM1)
support_root.place(x=0, y=0)


citations = ['"La défaite est temporaire, le puissance 4 est éternel."', '"Ne jamais mettre tous ses jetons dans la même grille."',
             '"Si il y a jeton, il y a match."', '"Je pense, donc j aligne."', '"Respire. Pose. Aligne."', 
             '"Laisse la victoire venir à toi."', '"Un jeton de perdu, 4 de retouvés"', '"Un jeton peut en cacher un autre"',
             '"N aligne pas, atomise."', '"Il est venu, il a vu, il a aligné."', '"Quand il joue, même le vent retient son souffle."',
             '"Tes jetons sont là. Les miens sont partout."','"Main hésitante, jeton vagabond"']

Lcita = tk.Label(root, text= rd.choice(citations)+ " - Luca", bg="#3394ff", fg="white",
                 font=("System",18,"underline"), padx=2, pady=10)

def changer_citation(event, self):
    self.config(text = rd.choice(citations)+ " - Luca")
    Lcita.place(x=width_screen/2-Lcita.winfo_reqwidth()/2, y=6*height_screen/7-Lcita.winfo_reqheight()/2)

Lcita.bind("<Button-1>",lambda event : changer_citation(event,Lcita))
Lcita.place(x=width_screen/2-Lcita.winfo_reqwidth()/2, y=6*height_screen/7-Lcita.winfo_reqheight()/2)


#---------------------------------------------------------------#
#-------------Effets graphiques fenêtre principale--------------#
##-------------------surbrillance boutton----------------------##
def bouton_touche(event, self):
    self.config(bg="#ff8e81")
def bouton_relache(event, self):
    self.config(bg="#ff7262")
B1.bind("<Enter>", lambda event : bouton_touche(event,B1))
B1.bind("<Leave>", lambda event : bouton_relache(event,B1))
B2.bind("<Enter>", lambda event : bouton_touche(event,B2))
B2.bind("<Leave>", lambda event : bouton_relache(event,B2))
B3.bind("<Enter>", lambda event : bouton_touche(event,B3))
B3.bind("<Leave>", lambda event : bouton_relache(event,B3))
B4.bind("<Enter>", lambda event : bouton_touche(event,B4))
B4.bind("<Leave>", lambda event : bouton_relache(event,B4))
##------------------------------------------------------------##

##-------------------animation jeton coté---------------------##
global couleur_bordure
global couleur_centre
global nom_couleur

frame_gauche = tk.Frame(support_root,height=HEIGHT, width=WIDTH, bg ="#3394ff")
frame_droite = tk.Frame(support_root,height=HEIGHT, width=WIDTH, bg ="#3394ff")
wframe = frame_gauche.winfo_reqwidth()
hframe = frame_gauche.winfo_reqheight()
frame_gauche.place(x=0, y=height_screen/2-hframe/2)
frame_droite.place(x=width_screen-wframe, y=height_screen/2-hframe/2)


couleurs_centre = ["#04BBFF","#ff3b30","#ffd933","#67944C","#ABA0F9","#A76844","#038A91","#FFEBD8","#676B4A","#FFB8CE","#CE8F8A", "#CBEFB6", "#FF5EFA", "#FE9063", "#5D1F31"]
couleurs_bordure = ["#0594D0","#bb261f","#e7ba00","#37633F","#7C80FC","#9F5540","#06708E","#FFD5BA","#585944","#FE94B4","#805050", "#A0C6A9", "#FF7AD1", "#EA5863", "#4A192E"]
nom_couleur = ["BLEU","ROUGE","JAUNE","VERT","LAVANDE","MARRON","CANARD","BEIGE","OLIVE","ROSE","TERRACOTTA","VERT PALE", "ROSE BONBON", "SAUMON", "POURPRE"]

jeton_gauche_1 = tk.Canvas(frame_gauche, height=200, width=200, bg ='#3394ff', highlightthickness=0)
jeton_gauche_2 = tk.Canvas(frame_gauche, height=200, width=200, bg ='#3394ff', highlightthickness=0)
jeton_droite_1 = tk.Canvas(frame_droite, height=200, width=200, bg ='#3394ff', highlightthickness=0)
jeton_droite_2 = tk.Canvas(frame_droite, height=200, width=200, bg ='#3394ff', highlightthickness=0)

jeton_gauche_1.create_oval((25,25),(175,175), fill="#ffd933", outline = "#e7ba00", width = 25 )
jeton_gauche_2.create_oval((25,25),(175,175), fill="#ff3b30", outline = "#bb261f", width = 25  )
jeton_droite_1.create_oval((25,25),(175,175), fill="#ff3b30", outline = "#bb261f", width = 25 )
jeton_droite_2.create_oval((25,25),(175,175), fill="#ffd933", outline = "#e7ba00", width = 25  )

wjeton = jeton_gauche_1.winfo_reqwidth()
hjeton = jeton_gauche_1.winfo_reqheight()
jeton_gauche_1.place(x=WIDTH/2-wjeton/2, y=0)
jeton_gauche_2.place(x=WIDTH/2-wjeton/2, y=HEIGHT-hjeton)
jeton_droite_1.place(x=WIDTH/2-wjeton/2, y=0)
jeton_droite_2.place(x=WIDTH/2-wjeton/2, y=HEIGHT-hjeton)

def animation_clic(event, self):
    overlapping = self.find_overlapping(event.x , event.y , event.x+1, event.y+1)
    if len(overlapping) != 0:
        self.coords(overlapping,(40,40),(160,160))
def animation_relache(event, self):
    overlapping = self.find_overlapping(event.x , event.y , event.x+1, event.y+1)
    if len(overlapping) != 0:
        i = rd.randint(0, len(couleurs_bordure)-1)
        self.coords(overlapping,(25,25),(175,175))
        self.itemconfigure(overlapping[0],fill=couleurs_centre[i], outline=couleurs_bordure[i])

jeton_gauche_1.bind('<ButtonPress-1>',lambda event : animation_clic(event, jeton_gauche_1))
jeton_gauche_1.bind('<ButtonRelease-1>', lambda event : animation_relache(event, jeton_gauche_1))
jeton_gauche_2.bind('<ButtonPress-1>',lambda event : animation_clic(event, jeton_gauche_2))
jeton_gauche_2.bind('<ButtonRelease-1>', lambda event : animation_relache(event, jeton_gauche_2))
jeton_droite_1.bind('<ButtonPress-1>',lambda event : animation_clic(event, jeton_droite_1))
jeton_droite_1.bind('<ButtonRelease-1>', lambda event : animation_relache(event, jeton_droite_1))
jeton_droite_2.bind('<ButtonPress-1>',lambda event : animation_clic(event, jeton_droite_2))
jeton_droite_2.bind('<ButtonRelease-1>', lambda event : animation_relache(event, jeton_droite_2))

##-------------------------------------------------------##
Tg=tk.Label(frame_gauche, text="P\nU\nI\nS\nS\nA\nN\nC\nE\n-\n4", font=("System", 17), fg="White", bg="#3394ff")
Td=tk.Label(frame_droite, text="P\nU\nI\nS\nS\nA\nN\nC\nE\n-\n4", font=("System", 17), fg="White", bg="#3394ff")
wT = Tg.winfo_reqwidth()
hT= Tg.winfo_reqheight()
Tg.place(x=WIDTH/2-wT/2, y=HEIGHT/2-hT/2)
Td.place(x=WIDTH/2-wT/2, y=HEIGHT/2-hT/2)


#---------------------------------------------------------#
root.mainloop()
