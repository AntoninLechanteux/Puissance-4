import tkinter as tk
import random as rd
import inspect 
from win32api import GetSystemMetrics

#---------Importe la resolution machine--------#

width_screen = GetSystemMetrics(0)
height_screen = GetSystemMetrics(1)

print(width_screen)
print(height_screen)

#-----------creation de la fenetre-------------#
root=tk.Tk()
root.title("Menu Puissance 4")
root.attributes("-fullscreen", True)
root.bind("<Escape>", lambda event: root.destroy())
root.config(bg="white")
#----------------------------------------------#
#--organisation de la geometrie de la fenetre--#

#----------------------------------------------#
#-------creation des fonctions à appeler-------#
tour="jaune"
def Jeu_normal():
    def fermer():
        game.destroy()
        return
    HEIGHT = 2*height_screen/3 #Sera modifiable
    WIDTH = 2*width_screen/3 #Sera modifiable
    game=tk.Tk()
    game.title("Jeu mode normal")
    support_game = tk.Frame(game, bg="#3394ff", width = width_screen, height= width_screen)
    support_game.place(x=0, y=0)
    game.attributes("-fullscreen", True)
    game.bind("<Escape>", lambda event: game.destroy())
    game.config(bg = "white")
    dim_grille = [6,7] #Sera modifiable
    canva_jeu = tk.Canvas(support_game, height=HEIGHT, width=WIDTH,bg="#005bff", borderwidth=0)
    canva_jeu.place(x=width_screen/2-WIDTH/2, y=50)
    B7=tk.Button(support_game, text="quitter", font=("System",15), fg="white", 
                 bg="#ff7262", relief="ridge", padx=20, command=fermer)
    B7.place(x=width_screen/2-45, y=height_screen-50)
    rayon_trou = (min((HEIGHT//dim_grille[0]),(WIDTH//dim_grille[1])))//2.5
    for i in range(dim_grille[1]):
        for j in range(dim_grille[0]):
            canva_jeu.create_oval(((i+0.5)*WIDTH//dim_grille[1]-rayon_trou,(j+0.5)*HEIGHT//dim_grille[0]-rayon_trou), 
                                  ((i+0.5)*WIDTH//dim_grille[1]+rayon_trou,(j+0.5)*HEIGHT//dim_grille[0]+rayon_trou), 
                                  fill = "#3394ff",  outline="#004fab", width= 0.1*rayon_trou)
#----------------------------------------------#
#-------------creation des jetons--------------#
    rayon_jeton = 1.8 * rayon_trou / 2.09  
    def placer_jeton(event):
        global tour
        coords_trou = canva_jeu.coords(canva_jeu.find_closest(event.x, event.y))
        (milieu_x,milieu_y) = ((coords_trou[0]+coords_trou[2])//2, 
                               (coords_trou[1]+coords_trou[3])//2)
        if tour == "jaune":
           canva_jeu.create_oval((milieu_x-rayon_jeton, milieu_y-rayon_jeton), 
                                 (milieu_x+rayon_jeton, milieu_y+rayon_jeton),  
                                 fill = "#ffd933",  outline = "#e7ba00", width = 0.25*rayon_jeton)
           tour = "rouge"
           return
        if tour == "rouge":
           canva_jeu.create_oval((milieu_x-rayon_jeton, milieu_y-rayon_jeton), 
                                 (milieu_x+rayon_jeton, milieu_y+rayon_jeton),  
                                 fill = "#ff3b30",  outline = "#bb261f", width = 0.25*rayon_jeton)
           tour = "jaune"
    game.bind("<Button-1>", placer_jeton)
    game.mainloop()
    return

def Jeu_sandbox():
    def fermer():
        sand.destroy()
        return
    sand=tk.Tk()
    sand.columnconfigure(0, weight=1)
    sand.columnconfigure(1, weight=1)
    sand.columnconfigure(2, weight=1)
    sand.columnconfigure(3, weight=1)
    sand.columnconfigure(4, weight=1)
    sand.columnconfigure(5, weight=1)
    sand.columnconfigure(6, weight=1)
    sand.rowconfigure(0, weight=1)
    sand.rowconfigure(1, weight=1)
    sand.rowconfigure(2, weight=1)
    sand.rowconfigure(3, weight=1)
    sand.rowconfigure(4, weight=1)
    sand.rowconfigure(5, weight=1)
    sand.rowconfigure(6, weight=1)
    sand.rowconfigure(7, weight=1)
    sand.rowconfigure(8, weight=1)
    
    sand.title("Jeu mode sandbox")
    sand.attributes("-fullscreen", True)
    sand.config(bg="#3394ff")
    global couleur_bordure
    global couleur_centre
    global nom_couleur
    couleur_centre = ["#04BBFF","#ff3b30","#ffd933","#67944C"]
    couleur_bordure = ["#0594D0","#bb261f","#e7ba00","#37633F"]
    nom_couleur = ["bleu","rouge","jaune", "vert"]
    selec_couleur = [couleur_centre,couleur_bordure,nom_couleur]
    
    def jouer():
        #-----------creation de la fenetre-------------#
        mod=tk.Tk()
        mod.geometry("720x480")
        mod.title("Menu Puissance 4")
        mod.attributes("-fullscreen", True)
        mod.config(bg = "#3394ff")
        #----------------------------------------------#

        #-----------creation de la grille-------------#
        HEIGHT = 720 
        WIDTH = 1295
        ligne = 11
        colonne = 7
        canva_jeu = tk.Canvas(mod, height=HEIGHT, width=WIDTH,bg="#005bff", borderwidth=0)
        canva_jeu.pack(expand=True)
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
            
    M1=tk.Label(sand, text="Configuations", fg="white",  bg= "#3394ff",
                font=("System",45))
    Bhome=tk.Button(sand, text="Retour au menu", font=("haelvetica",15),
                 fg="black", bg="lightgrey", relief="ridge", padx=10, pady=5, command=fermer)
    Bplay = tk.Button(sand, text="Jouer",font=("haelvetica",15),
                 fg="black", bg="lightgrey", relief="ridge", padx=10, pady=5, command=jouer)
    Mcol = tk.Label(sand, text="Colonne :", fg="white",  bg= "#3394ff",
                font=("System",45))
    colonne = tk.Spinbox(sand, from_= 0, to = 100, fg="#3394ff", width=8, borderwidth=3, relief="solid", font=("Arial", 45))
    Mlig = tk.Label(sand, text="Ligne :", fg="white",  bg= "#3394ff",
                font=("System",45))
    ligne = tk.Spinbox(sand, from_= 0, to = 100, fg="#3394ff", width=8, borderwidth=3, relief="solid", font=("Arial", 45))
    LBcolor = tk.Listbox(sand, height=3, width=13, selectbackground= "blue", font=("System",30))
    joueur1 = tk.Label(sand, text="",border=0, background="#3394ff", font=("System",45))
    joueur2 = tk.Label(sand, text="",border=0, background="#3394ff", font=("System",45))
   
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
                
    select = tk.Button(sand,text = "Selectionner", command=print_selec)
    retour = tk.Button(sand, text= "Retour", command=annuler)
    
    Bhome.grid(column=2, row=8)
    Bplay.grid(column=4, row= 8)
    M1.grid(column=3, row=0)
    Mcol.grid(column=1, row=2)
    colonne.grid(column=2, row=2)
    Mlig.grid(column=4, row=2)
    ligne.grid(column=5, row=2)
    LBcolor.grid(column=3, row=4)
    joueur1.grid(column=1, row=4)
    joueur2.grid(column=5, row=4)
    select.grid(column=2,row=5)
    retour.grid(column=4, row=5)
    
    sand.mainloop()
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
    HEIGHT=775
    WIDTH=400
    regles = "Le but du jeu est d'aligner 4 jetons de sa couleur horizontalement,\n verticalement ou diagonalement. \n \n Le jeu se joue à deux joueurs, chacun ayant une couleur de jeton différente. \n \n" \
    " Le premier joueur à aligner 4 jetons de sa couleur gagne la partie. \n \n Pour placer un jeton, il suffit de cliquer sur la case \ndans laquelle vous souhaitez le placer. \n \n Le jeu se termine lorsqu'un joueur a aligné 4 jetons ou lorsque la grille est pleine. "
    rules=tk.Tk()
    rules.title("Règles du jeu")
    rules.attributes("-fullscreen", True)
    rules.config(bg="#3394ff")
    support_rules = tk.Frame(rules, bg="#3394ff", width = width_screen, height= width_screen)
    support_rules.place(x=0, y=0)
    
    M2=tk.Label(support_rules, text="Voici les règles du jeu! ", font=("System", 35), fg="White", bg="#3394ff")
    M2.place(x=width_screen/2-225, y=25)
    M3=tk.Label(support_rules, text=regles, font=("System", 20), fg="white", bg="#3394ff", width=65)
    M3.place(x=width_screen/4-125, y=height_screen/4) 
    M4=tk.Label(support_rules, text='A VOUS DE JOUER !!', font=("System", 35), fg="white", bg="#3394ff", width=20)
    M4.place(x=width_screen/2-245, y=height_screen/1.25)    
    B5=tk.Button(support_rules, text="fermer les règles", font=("System",15), fg="white", 
                 bg="#ff7262", relief="ridge", command=fermer, padx=10, pady=5)
    B5.place(x=width_screen/2-50, y=height_screen-50)
    
    frame_gauche = tk.Frame(support_rules, height=HEIGHT, width=WIDTH/2, bg ="#3394ff")
    frame_droite = tk.Frame(support_rules, height=HEIGHT, width=WIDTH/2, bg ="#3394ff")
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
    M3.place(x=width_screen/4-170, y=height_screen/3)
    rules.after(20, animation1)
    return
#----------------------------------------------------------#
#---------------creation des widget menu-------------------#
HEIGHT=775
WIDTH=400
support_root = tk.Frame(root, bg="#3394ff", width = width_screen, height= width_screen)
support_root.place(x=0, y=0)

B1=tk.Button(support_root, text="PARTIE NORMALE", font=('system', 20), bg="#ff7262",
             fg="white", relief="raised", padx=5, pady=15, command=Jeu_normal)
B1.place(x=width_screen/2-125, y=height_screen/3.75)
B2=tk.Button(support_root, text="PARTIE CUSTOM", font=('system', 20), bg="#ff7262", 
             fg="white", relief="raised", padx=14, pady=15, command=Jeu_sandbox)
B2.place(x=width_screen/2-125, y=height_screen/3.75+100)
B3=tk.Button(support_root, text="SAUVEGARDE", font=('system', 20), bg="#ff7262", 
             fg="white", relief="raised", padx=34, pady=15, command=settings)
B3.place(x=width_screen/2-125, y=height_screen/3.75+200)
B4=tk.Button(support_root, text="REGLES", font=('system', 20), bg="#ff7262", 
             fg="white", relief="raised", padx=69, pady=15, command=rules)
B4.place(x=width_screen/2-125, y=height_screen/3.75+300)
M1=tk.Label(support_root, text="Bienvenue sur Puissance 4 !", fg="white",  bg= "#3394ff",
                  font=("System",45))
M1.place(x=width_screen/4, y=25)
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
##-------------------------------------------------------##
#---------------------------------------------------------#
root.mainloop()


