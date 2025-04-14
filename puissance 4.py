import tkinter as tk
import random as rd
import inspect 
from win32api import GetSystemMetrics

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
#----------------------------------------------#


#----------------------------------------------#
#-----Création de la fenêtre de jeu normal-----#
couleur_jeton = "#ffd933" 
contour = "#e7ba00" 
tour = 'j'
cooldown = 0
cursor_grid = 0

def Jeu_normal():
    global tour
    hasard = rd.choice([0, 1])
    if hasard == 0:
        tour = "jaune"
    else:
        tour = "rouge"
    def fermer():
        game.destroy()
        return
        
    game=tk.Tk()
    game.title("Jeu mode normal")
    support_game = tk.Frame(game, bg="#3394ff", width = width_screen, height= width_screen)
    support_game.place(x=0, y=0)
    game.attributes("-fullscreen", True)
    game.bind("<Escape>", lambda event: game.destroy())
    game.config(bg = "white")
    
    #----------------------------------------------#
    #-------------Création de la grille------------#
    HEIGHT = 2*height_screen/3
    WIDTH = 2*width_screen/3
    canva_jeu = tk.Canvas(support_game, height=HEIGHT, width=WIDTH,bg="#005bff", borderwidth=0)
    canva_jeu.place(x=(width_screen-WIDTH)//2, y=(height_screen-HEIGHT)//2)
    B7=tk.Button(support_game, text="quitter", font=("System",15), fg="white", 
                 bg="#ff7262", relief="ridge", padx=20, command=fermer)
    B7.place(x=width_screen/2-45, y=height_screen-50)

    ligne = 6
    colonne = 7
    dim_grille = [ligne,colonne] #Fixe pour jeu normal
    grille = []
    for i in range(ligne):
        grille.append([0] * colonne)
    rayon_trou = (min((HEIGHT//dim_grille[0]),(WIDTH//dim_grille[1])))//2.5
    for i in range(dim_grille[1]):
        for j in range(dim_grille[0]):
            canva_jeu.create_oval(((i+0.5)*WIDTH//dim_grille[1]-rayon_trou,(j+0.5)*HEIGHT//dim_grille[0]-rayon_trou), 
                                  ((i+0.5)*WIDTH//dim_grille[1]+rayon_trou,(j+0.5)*HEIGHT//dim_grille[0]+rayon_trou), 
                                  fill = "#3394ff",  outline="#004fab", width= 0.1*rayon_trou)
            
    #----------------------------------------------#
    #-------------Création des jetons--------------#
    rayon_jeton = 1.8 * rayon_trou / 2.09 
    tour = 'j'
    diff_milieux_y = [i*HEIGHT//(ligne*2) for i in range(1,ligne*2,2)]
    diff_milieux_y.reverse()
    diff_milieux_x = [i*WIDTH//(colonne) for i in range(0,colonne+1)]

    #----------------------------------------------#
    #----------Fonctions de vérification-----------#
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

    #----------------------------------------------#
    #------------Animation des jetons--------------#
    def placer_jeton(event):
        global tour
        global couleur_jeton
        global contour
        global cooldown
        coords_trou = canva_jeu.coords(canva_jeu.find_closest(event.x, event.y))
        (milieu_x,milieu_y) = ((coords_trou[0]+coords_trou[2])//2, (coords_trou[1]+coords_trou[3])//2)
        if cooldown ==0 and cursor_grid == 1:
            cooldown = 1
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
                    game.after(200//ligne, lambda: canva_jeu.delete(jeton))  # supprime l'ancien cercle
                    game.after(200//ligne, lambda: animer_jeton(diff_milieux_y[diff_milieux_y.index(i)-1]))  # récursivité qui descend jusqu'à atteindre la limite
            
            def cooldown_switch():
                global cooldown
                cooldown=0            

            animer_jeton(diff_milieux_y[-1])
            root.after(300, cooldown_switch)
            verif()
            tour = "r" if tour == "j" else "j"
            couleur_jeton = "#ffd933" if tour == "j" else "#ff3b30"
            contour = "#e7ba00" if tour == "j" else "#bb261f"
            
        elif cooldown == 1 :
            return
        
    def cursor_in_grid(event):
        global cursor_grid
        cursor_grid = 1
    def cursor_not_in_grid(event):
        global cursor_grid
        cursor_grid = 0
    canva_jeu.bind('<Enter>', cursor_in_grid)#Vérifient si le curseur est dans la grille pour poser le jeton après un clic
    canva_jeu.bind('<Leave>', cursor_not_in_grid)       
    game.bind("<Button-1>", placer_jeton)#Pose un jeton si les conditions sont remplies
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
    sand_width = width_screen/3
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
    def jouer():
        #-----------creation de la grille-------------#
        HEIGHT = 720 
        WIDTH = 1295
        Bhome2=tk.Button(mod, text="Quitter", font=("System",15),
                 fg="white", bg="#ff7262", relief="ridge", padx=10, pady=5, command=fermer)
        wBhome2 = Bhome2.winfo_reqwidth()
        hBhome2 = Bhome2.winfo_reqheight()
        Bhome2.place(x=width_screen/2-wBhome2/2, y=height_screen-1.5*hBhome2)
        dim_grille=[7,11]
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
    Bplay = tk.Button(sand, text="Jouer",font=("System",15), fg="white", bg="#ff7262", relief="ridge", padx=10, pady=5, command=animation_panel)
    wBplay = Bplay.winfo_reqwidth()
    hBplay = Bplay.winfo_reqheight()
    Bplay.place(x=sand_width/1.2-wBplay/2, y=sand_height-1.5*hBplay)
    Mcol = tk.Label(sand, text=" nombre de colonnes :", fg="white",  bg= "#6db3fe", font=("System",15))
    wMcol = Mcol.winfo_reqwidth() 
    Mcol.place(x=sand_width/6-wMcol/2, y=sand_height/5-50)
    colonne = tk.Spinbox(sand, from_= 0, to = 100, fg="#6db3fe", width=8, borderwidth=3, relief="sunken", font=("System", 15))
    wcolonne = colonne.winfo_reqwidth()
    colonne.place(x=sand_width/6-wcolonne/2, y=sand_height/5)
    Mlig = tk.Label(sand, text="nombre de lignes :", fg="white",  bg= "#6db3fe", font=("System",15))
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
    joueur2 = tk.Label(sand, text="Joueur 2 :",border=0, background="#6db3fe", font=("System",15))
    wjoueur2 = joueur2.winfo_reqwidth()
    joueur2.place(x=sand_width/1.2-wjoueur2/2, y=sand_height/2)
    
    # ------------------- Configuration des listebox ------------------ #
    for item in nom_couleur: #Ajoute les couleurs disponibles a la listebox
        LBcolor.insert(tk.END,item)
    
    def color():
        for i in range(len(nom_couleur)):
            LBcolor.itemconfigure(i, background=couleur_centre[i])
    
    color()
    
    def print_selec():  #Impression sur l'ecran de la couleur choisie  
        if joueur1["text"] == "":
            joueur1["text"]= LBcolor.get(LBcolor.curselection())
            LBcolor.delete(LBcolor.curselection()) #suppression dans les choix pour pas se faire affronter les memes couleurs
        else:
            joueur2["text"] = LBcolor.get(LBcolor.curselection())
            LBcolor.delete(LBcolor.curselection())
        return   
    
    def annuler():  #réinsertion des couleurs choisies dans la liste des couleurs dispo et suppression des couleurs choisies
        if (joueur1["text"] != "" and joueur2["text"] != ""):
            LBcolor.insert(tk.END,joueur1["text"])
            LBcolor.itemconfigure(len(nom_couleur)-2,background=couleur_centre[nom_couleur.index(joueur1["text"])])
            joueur1["text"] = ""
            LBcolor.insert(tk.END,joueur2["text"]) 
            LBcolor.itemconfigure(len(nom_couleur)-1,background=couleur_centre[nom_couleur.index(joueur2["text"])])
            joueur2["text"] = ""
        if joueur1["text"] != "":
            LBcolor.insert(tk.END,joueur1["text"])
            LBcolor.itemconfigure(len(nom_couleur)-1,background=couleur_centre[nom_couleur.index(joueur1["text"])])
            joueur1["text"] = "" 
        return

    select = tk.Button(sand,text = "Selectionner", command=print_selec, font=("System", 15), fg="white", bg="#ff7262", relief="ridge")
    wselect = select.winfo_reqwidth()
    select.place(x=sand_width/6-wselect/2, y=sand_height/1.75)
    retour = tk.Button(sand, text= "Retour", command=annuler, font=("System", 15), fg="white", bg="#ff7262", relief="ridge")
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
             fg="white", relief="raised", padx=5, pady=15, command=Jeu_normal)
B2=tk.Button(support_button, text="PARTIE CUSTOM", font=('system', 20), bg="#ff7262", 
             fg="white", relief="raised", padx=14, pady=15, command=Jeu_sandbox)
B3=tk.Button(support_button, text="SAUVEGARDE", font=('system', 20), bg="#ff7262", 
             fg="white", relief="raised", padx=33, pady=15, command=settings)
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


#----------------------------------------------#
#-------------Effets graphiques fenêtre principale--------------#
##-------------------surbrillance boutton----------------------##
def bouton_touche1(event, self):
    B1.config(bg="#ff8e81")
def bouton_relache1(event, self):
    B1.config(bg="#ff7262")
def bouton_touche2(event, self):
    B2.config(bg="#ff8e81")
def bouton_relache2(event, self):
    B2.config(bg="#ff7262")
def bouton_touche3(event, self):
    B3.config(bg="#ff8e81")
def bouton_relache3(event, self):
    B3.config(bg="#ff7262")
def bouton_touche4(event, self):
    B4.config(bg="#ff8e81")
def bouton_relache4(event, self):
    B4.config(bg="#ff7262")
B1.bind("<Enter>", lambda event : bouton_touche1(event,B1))
B1.bind("<Leave>", lambda event : bouton_relache1(event,B1))
B2.bind("<Enter>", lambda event : bouton_touche2(event,B2))
B2.bind("<Leave>", lambda event : bouton_relache2(event,B2))
B3.bind("<Enter>", lambda event : bouton_touche3(event,B3))
B3.bind("<Leave>", lambda event : bouton_relache3(event,B3))
B4.bind("<Enter>", lambda event : bouton_touche4(event,B4))
B4.bind("<Leave>", lambda event : bouton_relache4(event,B4))
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


