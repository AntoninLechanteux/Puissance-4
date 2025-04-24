import tkinter as tk
import random as rd
import inspect 
from win32api import GetSystemMetrics
import pygame
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

    global compteur_manche_J1
    global compteur_manche_J2

    compteur_manche_J1 = valeur_compteur_manche_J1
    compteur_manche_J2 = valeur_compteur_manche_J2


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
                                           bg="#ff7262", relief="raised", padx=29)
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
    sand_width = width_screen/2
    sand = tk.LabelFrame(mod, height=sand_height, width=sand_width, bg="#6db3fe", relief="ridge")
    sand.place(x=0, y=0)
    global couleur_bordure
    global couleur_centre
    global nom_couleur
    global dpos
    couleur_centre = ["#04BBFF","#ff3b30","#ffd933","#67944C"]
    couleur_bordure = ["#0594D0","#bb261f","#e7ba00","#37633F"]
    nom_couleur = ["bleu","rouge","jaune", "vert"]
    selec_couleur = [couleur_centre,couleur_bordure,nom_couleur]

    end_pos = -sand_width
    start_pos = 0
    dpos = 0
    dt = 3
    
    def animation_panel():
        if (int(colonne.get()) != 0) and (int(ligne.get())!= 0) and (Choix_joueur1["text"]!="") and (Choix_joueur2["text"]!=""):
            global dpos
            sand.place(x=start_pos, y=0)
            if dpos < abs(end_pos):
                sand.place(x=start_pos-dpos, y=0)
                dpos += 1
                root.after(dt, animation_panel)
            else:
                sand.place(x=end_pos, y=0)
                dpos=0
                mod.after(1000, jouer)
            return
        else:
            print("les conditions ne sont pas respectées")
    def jouer():
        #-----------creation de la grille-------------#
        HEIGHT = 720 
        WIDTH = 1295
        Bhome2=tk.Button(mod, text="Quitter", font=("System",15),
                 fg="white", bg="#ff7262", relief="ridge", padx=10, pady=5, command=fermer)
        wBhome2 = Bhome2.winfo_reqwidth()
        hBhome2 = Bhome2.winfo_reqheight()
        Bhome2.place(x=width_screen/2-wBhome2/2, y=height_screen-1.5*hBhome2)
        dim_grille=[int(ligne.get()),int(colonne.get())]
        canva_jeu = tk.Canvas(mod, height=HEIGHT, width=WIDTH,bg="#005bff", highlightthickness=0)
        canva_jeu.place(x=width_screen/2-WIDTH/2, y=0.1*HEIGHT)
        rayon_trou = (min((HEIGHT//dim_grille[0]),(WIDTH//dim_grille[1])))//2.5
        for i in range(dim_grille[1]):
            for j in range(dim_grille[0]):
                canva_jeu.create_oval(((i+0.5)*WIDTH//dim_grille[1]-rayon_trou,(j+0.5)*HEIGHT//dim_grille[0]-rayon_trou), ((i+0.5)*WIDTH//dim_grille[1]+rayon_trou,(j+0.5)*HEIGHT//dim_grille[0]+rayon_trou), fill = "#3394ff",  outline="#004fab", width= 0.1*rayon_trou)
        global tour_mod
        tour_mod = "j"
        rayon_jeton = 1.8 * rayon_trou / 2.13

        #Creation de la grille en tant que liste
        global grille_mod
        grille_mod = []
        for i in range(int(ligne.get())):
            grille_mod.append([0] * int(colonne.get()))
            
        #Creation des milieux x et y
        diff_milieux_y_mod = [i*HEIGHT/(int(ligne.get())*2) for i in range(1,int(ligne.get())*2,2)]
        diff_milieux_y_mod.reverse()
        diff_milieux_x_mod = [i*WIDTH/(int(colonne.get())) for i in range(0,int(colonne.get())+1)]
        
        def verif(): #Fonction qui verif si 4 jetons sont alignés+ qui dit qui a win
            global win
            win = False
            ligne_fct()
            colonne_fct()
            diag_droit_gauche()
            diag_gauche_droit()
            if win == True:
                if tour_mod == "j":
                    print("omgomgomg jaune a gagné")
                elif tour_mod == "r":
                    print("omgomgomg rouge a gagné")
            return
        
        def ligne_fct(): #Fonction qui verifie si 4 jetons sont alignés en ligne
            global win
            for i in grille_mod:
                for j in range(int(colonne.get())-3):
                    if i[j] != 0:
                        if (i[j] == i[j+1] == i[j+2] == i[j+3]):
                            win = True
        def colonne_fct(): #Fonction qui verifie si 4 jetons sont alignés en colonne
            global win
            for i in range(int(colonne.get())):
                for j in range(int(ligne.get())-3):
                   if grille_mod[j][i] != 0:    
                        if (grille_mod[j][i] == grille_mod[j+1][i] == grille_mod[j+2][i] == grille_mod[j+3][i]):
                            win = True
        def diag_gauche_droit(): #fonction qui verifie si 4 jetons sont alignés en diagonale de la gauche en haut vers la droite en bas
            global win
            for i in range(int(ligne.get())-1,2,-1):
                for j in range(int(colonne.get())-3):
                    if grille_mod[i][j] != 0:
                        if (grille_mod[i][j] == grille_mod[i-1][j+1] == grille_mod[i-2][j+2] == grille_mod[i-3][j+3]):
                            win = True
        def diag_droit_gauche(): #fonction qui verifie si 4 jetons sont alignés en diagonale de la droite en haut vers la gauche en bas
            global win
            for i in range(int(colonne.get())-1,2,-1):
                for j in range(int(ligne.get())-1,2,-1):
                    if grille_mod[j][i]!= 0:
                        if (grille_mod[j][i] == grille_mod[j-1][i-1] == grille_mod[j-2][i-2] == grille_mod[j-3][i-3]):
                            win = True

        def placer_jeton_mod(event):
            global tour_mod
            global grille_mod
            coords_trou = canva_jeu.coords(canva_jeu.find_closest(event.x, event.y))
            (milieu_x_mod,milieu_y_mod) = ((coords_trou[0]+coords_trou[2])//2, (coords_trou[1]+coords_trou[3])//2)
            for i in range(int(colonne.get())):   #pour chaque colonne
                if diff_milieux_x_mod[i] <= milieu_x_mod < diff_milieux_x_mod[i+1]: #Si la coordonnée x se trouve dans la ieme colonne, on entre dans la boucle
                    if all(j[i] == 0 for j in grille_mod): #cas ou toutes les trous de la colonne sont vides
                        grille_mod[0][i] = tour_mod #on place la couleur en bas de la grille virtuelle
                        milieu_y_mod = diff_milieux_y_mod[0] #on place le jeton tout en bas dans le canva
                        break #break pour eviter de faire tourner la boucle inutilement 
                    elif grille_mod[int(ligne.get())-1][i] != 0: #Si la colonne est pleine
                        if i == 0:
                            print(f"La {i+1} ere colonne est pleine") #Afficher quelque part sur l écran que la 1ere colonne est pleine
                        else:
                            print(f"La {i+1} eme colonne est pleine") #Afficher quelque part sur l écran que la i-eme colonne est pleine
                        return
                    else:
                        for t in range(int(ligne.get())-1,-1,-1): #on regarde du haut vers le bas
                            if grille_mod[t][i] != 0: #et des qu'un trou est plein
                                grille_mod[t+1][i] = tour_mod #on remplit celui d'au dessus
                                milieu_y_mod = diff_milieux_y_mod[t+1] #Placement visuel
                                break #Break pour eviter de faire tourner la boucle inutilement
    
            if tour_mod == "j":
                canva_jeu.create_oval((milieu_x_mod-rayon_jeton,milieu_y_mod-rayon_jeton), (milieu_x_mod+rayon_jeton, milieu_y_mod+rayon_jeton),
                                      fill = "#ffd933",  outline = "#e7ba00", width = 0.25*rayon_jeton) #Placement visuel sur le canva
                verif() #Verifie s'il a gagné
                tour_mod = "r" #Tour suivant 
                return
            elif tour_mod == "r":
                canva_jeu.create_oval((milieu_x_mod-rayon_jeton,milieu_y_mod-rayon_jeton), (milieu_x_mod+rayon_jeton, milieu_y_mod+rayon_jeton),
                                      fill = "#ff3b30",  outline = "#bb261f", width = 0.25*rayon_jeton)
                verif()
                tour_mod = "j" #tour suivant 
                return
        mod.bind("<Button-1>", placer_jeton_mod)

    M1=tk.Label(sand, text="Configuations", fg="white",  bg= "#6db3fe", font=("System",30))
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
    Mcol = tk.Label(sand, text=" Nombre de colonne :", fg="white",  bg= "#6db3fe", font=("System",22))
    wMcol = Mcol.winfo_reqwidth() 
    Mcol.place(x=sand_width/6-wMcol/2, y=sand_height/5-50)
    colonne = tk.Spinbox(sand, from_= 0, to = 100, fg="#6db3fe", width=8, borderwidth=3, relief="sunken", font=("System", 15))
    wcolonne = colonne.winfo_reqwidth()
    colonne.place(x=sand_width/6-wcolonne/2, y=sand_height/5)
    Mlig = tk.Label(sand, text="Nombre de ligne :", fg="white",  bg= "#6db3fe", font=("System",22))
    wMlig = Mlig.winfo_reqwidth()
    Mlig.place(x=sand_width/1.2-wMlig/2, y=sand_height/5-50)
    ligne = tk.Spinbox(sand, from_= 0, to = 100, fg="#3394ff", width=8, borderwidth=3, relief="sunken", font=("System", 15))
    wligne = ligne.winfo_reqwidth()
    ligne.place(x=sand_width/1.2-wligne/2, y=sand_height/5)  
    LBcolor = tk.Listbox(sand, height=3, width=13, selectbackground= "blue", font=("System",15))
    wLBcolor = LBcolor.winfo_reqwidth()
    LBcolor.place(x=sand_width/2-wLBcolor/2, y=sand_height/2-50)
    joueur1 = tk.Label(sand, text="Joueur 1 :",border=0, background="#6db3fe", font=("System",15))
    wjoueur1 = joueur1.winfo_reqwidth()
    joueur1.place(x=sand_width/6-wjoueur1/2, y=sand_height/2)
    Choix_joueur1 = tk.Label(sand,text = "",border=0, background="#6db3fe", font=("System",15))
    wChoix_joueur1 = Choix_joueur1.winfo_reqwidth()
    Choix_joueur1.place(x=sand_width/6-wChoix_joueur1/1.3, y=sand_height/1.89)
    joueur2 = tk.Label(sand, text="Joueur 2 :",border=0, background="#6db3fe", font=("System",15))
    wjoueur2 = joueur2.winfo_reqwidth()
    joueur2.place(x=sand_width/1.2-wjoueur2/2, y=sand_height/2)
    Choix_joueur2 = tk.Label(sand,text = "",border=0, background="#6db3fe", font=("System",15))
    wChoix_joueur2 = Choix_joueur2.winfo_reqwidth()
    Choix_joueur2.place(x=sand_width/1.2-wChoix_joueur2/2,y=sand_height/1.89)

    # ------------------- Configuration des listebox ------------------ #
    for item in nom_couleur: #Ajoute les couleurs disponibles a la listebox
        LBcolor.insert(tk.END,item)
    
    def color():
        for i in range(len(nom_couleur)):
            LBcolor.itemconfigure(i, background=couleur_centre[i])
    
    color()
    
    def print_selec():  #Impression sur l'ecran de la couleur choisie  
        if Choix_joueur1["text"] == "":
            Choix_joueur1["text"]= LBcolor.get(LBcolor.curselection())
            LBcolor.delete(LBcolor.curselection()) #suppression dans les choix pour pas se faire affronter les memes couleurs
        else:
            Choix_joueur2["text"] = LBcolor.get(LBcolor.curselection())
            LBcolor.delete(LBcolor.curselection())
        return   
    
    def annuler():  #réinsertion des couleurs choisies dans la liste des couleurs dispo et suppression des couleurs choisies
        if (Choix_joueur1["text"] != "" and Choix_joueur2["text"] != ""):
            LBcolor.insert(tk.END,Choix_joueur1["text"])
            LBcolor.itemconfigure(len(nom_couleur)-2,background=couleur_centre[nom_couleur.index(Choix_joueur1["text"])])
            Choix_joueur1["text"] = ""
            LBcolor.insert(tk.END,Choix_joueur2["text"]) 
            LBcolor.itemconfigure(len(nom_couleur)-1,background=couleur_centre[nom_couleur.index(Choix_joueur2["text"])])
            Choix_joueur2["text"] = ""
        elif Choix_joueur1["text"] != "":
            LBcolor.insert(tk.END,Choix_joueur1["text"])
            LBcolor.itemconfigure(len(nom_couleur)-1,background=couleur_centre[nom_couleur.index(Choix_joueur1["text"])])
            Choix_joueur1["text"] = "" 
        return

    select = tk.Button(sand,text = "Selectionner", command=print_selec, font=("System", 15), fg="white", bg="#ff7262", relief="ridge")
    wselect = select.winfo_reqwidth()
    select.place(x=sand_width/6-wselect/2, y=sand_height/1.75)
    retour = tk.Button(sand, text= "Annuler", command=annuler, font=("System", 15), fg="white", bg="#ff7262", relief="ridge")
    wretour = retour.winfo_reqwidth()
    retour.place(x=sand_width/1.2-wretour/2, y=sand_height/1.75)

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
    Tg=tk.Label(frame_gauche, text="P\nU\nI\nS\nS\nA\nN\nC\nE\n-\n4", font=("System", 20), fg="White", bg="#3394ff")
    Td=tk.Label(frame_droite, text="P\nU\nI\nS\nS\nA\nN\nC\nE\n-\n4", font=("System", 20), fg="White", bg="#3394ff")
    hT = Tg.winfo_reqheight()
    wT = Tg.winfo_reqwidth()
    Tg.place(x=WIDTH/2-wT/2, y=HEIGHT/2-hT/2)
    Td.place(x=WIDTH/2-wT/2, y=HEIGHT/2-hT/2)

    jeton_gauche_1.bind('<ButtonPress-1>',lambda event : animation_clic(event, jeton_gauche_1, jeton_gauche_1_counter))
    jeton_gauche_1.bind('<ButtonRelease-1>', lambda event : animation_relache_jg1(event, jeton_gauche_1, jeton_gauche_1_counter))
    jeton_gauche_2.bind('<ButtonPress-1>',lambda event : animation_clic(event, jeton_gauche_2, jeton_gauche_2_counter))
    jeton_gauche_2.bind('<ButtonRelease-1>', lambda event : animation_relache_jg2(event, jeton_gauche_2, jeton_gauche_2_counter))
    jeton_droite_1.bind('<ButtonPress-1>',lambda event : animation_clic(event, jeton_droite_1, jeton_droite_1_counter))
    jeton_droite_1.bind('<ButtonRelease-1>', lambda event : animation_relache_jd1(event, jeton_droite_1, jeton_droite_1_counter))
    jeton_droite_2.bind('<ButtonPress-1>',lambda event : animation_clic(event, jeton_droite_2, jeton_droite_2_counter))
    jeton_droite_2.bind('<ButtonRelease-1>', lambda event : animation_relache_jd2(event, jeton_droite_2, jeton_droite_2_counter))
        
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

frame_gauche = tk.Frame(support_root,height=HEIGHT, width=WIDTH, bg ="#3394ff")
frame_droite = tk.Frame(support_root,height=HEIGHT, width=WIDTH, bg ="#3394ff")
wframe = frame_gauche.winfo_reqwidth()
hframe = frame_gauche.winfo_reqheight()
jeton_gauche_1 = tk.Canvas(frame_gauche, height=200, width=200, bg ='#3394ff', highlightthickness=0)
jeton_gauche_1_counter = 1
jeton_gauche_2 = tk.Canvas(frame_gauche, height=200, width=200, bg ='#3394ff', highlightthickness=0)
jeton_gauche_2_counter = 0
jeton_droite_1 = tk.Canvas(frame_droite, height=200, width=200, bg ='#3394ff', highlightthickness=0)
jeton_droite_1_counter = 0
jeton_droite_2 = tk.Canvas(frame_droite, height=200, width=200, bg ='#3394ff', highlightthickness=0)
jeton_droite_2_counter = 1

wjeton = jeton_gauche_1.winfo_reqwidth()
hjeton = jeton_gauche_1.winfo_reqheight()
jeton_gauche_1.place(x=WIDTH/2-wjeton/2, y=0)
jeton_gauche_2.place(x=WIDTH/2-wjeton/2, y=HEIGHT-hjeton)
jeton_gauche_1.create_oval((25,25),(175,175), fill="#ffd933", outline = "#e7ba00", width = 25 )
jeton_gauche_2.create_oval((25,25),(175,175), fill="#ff3b30", outline = "#bb261f", width = 25  )
jeton_droite_1.place(x=WIDTH/2-wjeton/2, y=0)
jeton_droite_2.place(x=WIDTH/2-wjeton/2, y=HEIGHT-hjeton)
jeton_droite_1.create_oval((25,25),(175,175), fill="#ff3b30", outline = "#bb261f", width = 25 )
jeton_droite_2.create_oval((25,25),(175,175), fill="#ffd933", outline = "#e7ba00", width = 25  )
frame_gauche.place(x=0, y=height_screen/2-hframe/2)
frame_droite.place(x=width_screen-wframe, y=height_screen/2-hframe/2)
Tg=tk.Label(frame_gauche, text="P\nU\nI\nS\nS\nA\nN\nC\nE\n-\n4", font=("System", 20), fg="White", bg="#3394ff")
Td=tk.Label(frame_droite, text="P\nU\nI\nS\nS\nA\nN\nC\nE\n-\n4", font=("System", 20), fg="White", bg="#3394ff")
wT = Tg.winfo_reqwidth()
hT= Tg.winfo_reqheight()
Tg.place(x=WIDTH/2-wT/2, y=HEIGHT/2-hT/2)
Td.place(x=WIDTH/2-wT/2, y=HEIGHT/2-hT/2)

jeton_gauche_1.bind('<ButtonPress-1>',lambda event : animation_clic(event, jeton_gauche_1, jeton_gauche_1_counter))
jeton_gauche_1.bind('<ButtonRelease-1>', lambda event : animation_relache_jg1(event, jeton_gauche_1, jeton_gauche_1_counter))
jeton_gauche_2.bind('<ButtonPress-1>',lambda event : animation_clic(event, jeton_gauche_2, jeton_gauche_2_counter))
jeton_gauche_2.bind('<ButtonRelease-1>', lambda event : animation_relache_jg2(event, jeton_gauche_2, jeton_gauche_2_counter))
jeton_droite_1.bind('<ButtonPress-1>',lambda event : animation_clic(event, jeton_droite_1, jeton_droite_1_counter))
jeton_droite_1.bind('<ButtonRelease-1>', lambda event : animation_relache_jd1(event, jeton_droite_1, jeton_droite_1_counter))
jeton_droite_2.bind('<ButtonPress-1>',lambda event : animation_clic(event, jeton_droite_2, jeton_droite_2_counter))
jeton_droite_2.bind('<ButtonRelease-1>', lambda event : animation_relache_jd2(event, jeton_droite_2, jeton_droite_2_counter))
##-------------------------------------------------------##
#---------------------------------------------------------#
root.mainloop()


