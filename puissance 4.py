import tkinter as tk
import random as rd
import inspect 

#-----------creation de la fenetre-------------#
root=tk.Tk()
root.geometry("720x480")
root.title("Menu Puissance 4")
root.attributes("-fullscreen", True)
root.bind("<Escape>", lambda event: root.destroy())
root.config(bg="#3394ff")
#----------------------------------------------#
#--organisation de la geometrie de la fenetre--#
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)


root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.rowconfigure(6, weight=1)
root.rowconfigure(7, weight=1)
root.rowconfigure(8, weight=1)
root.rowconfigure(9, weight=1)
root.rowconfigure(10, weight=1)
root.rowconfigure(11, weight=1)
root.rowconfigure(12, weight=1)
root.rowconfigure(13, weight=1)
root.rowconfigure(14, weight=1)
root.rowconfigure(15, weight=1)
#----------------------------------------------#
#-------creation des fonctions à appeler-------#
tour="jaune"
def Jeu_normal():
    def fermer():
        game.destroy()
        return
    HEIGHT = 480 #Sera modifiable
    WIDTH = 700 #Sera modifiable
    game=tk.Tk()
    game.title("Jeu mode normal")
    game.rowconfigure(0, weight=1)
    game.rowconfigure(1, weight=1)
    game.rowconfigure(2, weight=1)
    game.rowconfigure(3, weight=1)
    game.rowconfigure(4, weight=1)
    game.rowconfigure(5, weight=1)
    game.rowconfigure(6, weight=1)
    game.rowconfigure(7, weight=1)
    game.rowconfigure(8, weight=1)
    game.rowconfigure(9, weight=1)
    game.rowconfigure(10, weight=1)
    game.columnconfigure(0, weight=1)
    game.attributes("-fullscreen", True)
    game.bind("<Escape>", lambda event: game.destroy())
    game.config(bg = "#3394ff")
    dim_grille = [6,7] #Sera modifiable
    canva_jeu = tk.Canvas(game, height=HEIGHT, width=WIDTH,bg="#005bff", borderwidth=0)
    canva_jeu.pack(expand=True)
    B7=tk.Button(game, text="quitter", font=("System",15), fg="white", 
                 bg="#ff7262", relief="ridge", padx=10, command=fermer)
    B7.pack(side=tk.BOTTOM)
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
    sand=tk.Tk()
    sand.title("Jeu mode sandbox")
    sand.attributes("-fullscreen", True)
    sand.bind("<Escape>", lambda event: sand.destroy())
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
##-----------Affichage des règles-------------##
def rules():
    def fermer():
        rules.destroy()
        return
    HEIGHT=800
    WIDTH=1280
    regles = "Le but du jeu est d'aligner 4 jetons de sa couleur horizontalement, verticalement ou diagonalement. \n \n Le jeu se joue à deux joueurs, chacun ayant une couleur de jeton différente. \n \n" \
    " Le premier joueur à aligner 4 jetons de sa couleur gagne la partie. \n \n Pour placer un jeton, il suffit de cliquer sur la case dans laquelle vous souhaitez le placer. \n \n Le jeu se termine lorsqu'un joueur a aligné 4 jetons ou lorsque la grille est pleine. "
    rules=tk.Tk()
    rules.title("Règles du jeu")
    rules.attributes("-fullscreen", True)
    rules.config(bg="#3394ff")
    rules.rowconfigure(0, weight=1)
    rules.rowconfigure(1, weight=1)
    rules.rowconfigure(2, weight=1)
    rules.rowconfigure(3, weight=1)
    rules.rowconfigure(4, weight=1)
    rules.columnconfigure(0, weight=1)
    rules.columnconfigure(1, weight=1)
    rules.columnconfigure(2, weight=1)
    rules.columnconfigure(3, weight=1)
    rules.columnconfigure(4, weight=1)
    
    M2=tk.Label(rules, text="Voici les règles du jeu! ", font=("System", 35), fg="black", bg="#3394ff")
    M3=tk.Label(rules, text=regles, font=("haelvetica", 15), fg="black", bg="#3394ff", width=90, pady=10, padx=10)
    M4=tk.Label(rules, text='A VOUS DE JOUER !!', font=("haelvetica", 35), fg="black", bg="#3394ff", width=60)
    B5=tk.Button(rules, text="fermer les règles", font=("System",15), fg="white", 
                 bg="#ff7262", relief="ridge", command=fermer, padx=10, pady=5)
    
    B5.grid(row=4, column=1,) # columnspan=4)
    M2.grid(row=0, column=1,) #columnspan=4)
    M4.grid(row=3, column=1,) #padx=10)    
    M3.grid(row=2, column=1,) #padx=10)
    canva_rules = tk.Canvas(rules, height=HEIGHT, width=WIDTH/2,bg="#3394ff", borderwidth=0)
    canva_rules2 = tk.Canvas(rules, height=HEIGHT, width=WIDTH/2,bg="#3394ff", borderwidth=0)
    canva_rules.create_oval((25,25),(175,175), fill="#ffd933", outline = "#e7ba00", width = 25 )
    canva_rules.create_oval((25,625),(175,775), fill="#ff3b30", outline = "#bb261f", width = 25 )
    canva_rules2.create_oval((25,25),(175,175), fill="#ff3b30", outline = "#bb261f", width = 25 )
    canva_rules2.create_oval((25,625),(175,775), fill="#ffd933", outline = "#e7ba00", width = 25 )
    T1=tk.Label(canva_rules, text="P\nU\nI\nS\nS\nA\nN\nC\nE\n\n4", font=("System", 30), fg="black", bg="#3394ff")
    T2=tk.Label(canva_rules2, text="P\nU\nI\nS\nS\nA\nN\nC\nE\n\n4", font=("System", 30), fg="black", bg="#3394ff")
    T1.place(x=85, y=200)
    T2.place(x=85, y=200)


    canva_rules2.grid(row=0, column=4, rowspan=5, )
    canva_rules.grid(row=0, column=0, rowspan=5, )
    return
##--------------------------------------------##
#----------------------------------------------#
#--------creation des widgets textuels---------#
M1=tk.Label(root, text="Bienvenue sur Puissance 4 !", fg="white",  bg= "#3394ff",
                  font=("System",45))

M1.grid(column=1, row=2, columnspan=3)
#----------------------------------------------#
#--------creation des widget boutons-----------#
B1=tk.Button(root, text="PARTIE NORMALE", font=('system', 20), bg="#ff7262",
             fg="white", relief="raised", padx=5, pady=15, command=Jeu_normal)
B2=tk.Button(root, text="PARTIE CUSTOM", font=('system', 20), bg="#ff7262", 
             fg="white", relief="raised", padx=14, pady=15, command=Jeu_sandbox)
B3=tk.Button(root, text="SAUVEGARDE", font=('system', 20), bg="#ff7262", 
             fg="white", relief="raised", padx=34, pady=15, command=settings)
B4=tk.Button(root, text="REGLES", font=('system', 20), bg="#ff7262", 
             fg="white", relief="raised", padx=69, pady=15, command=rules)

B1.grid(row=5, column=2)
B2.grid(row=7, column=2)
B3.grid(row=9, column=2)
B4.grid(row=11, column=2)
#----------------------------------------------#
#-------------Effets graphiques fenêtre principale--------------#
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

jeton_gauche_1 = tk.Canvas(root, height=200, width=200, bg ='#3394ff', highlightthickness=0)
jeton_gauche_1_counter = 1
jeton_gauche_2 = tk.Canvas(root, height=200, width=200, bg ='#3394ff', highlightthickness=0)
jeton_gauche_2_counter = 0
jeton_droite_1 = tk.Canvas(root, height=200, width=200, bg ='#3394ff', highlightthickness=0)
jeton_droite_1_counter = 0
jeton_droite_2 = tk.Canvas(root, height=200, width=200, bg ='#3394ff', highlightthickness=0)
jeton_droite_2_counter = 1

jeton_gauche_1.grid(row = 3, column=1, rowspan = 5)
jeton_gauche_2.grid(row = 9, column=1, rowspan = 5)
jeton_gauche_1.create_oval((25,25),(175,175), fill="#ffd933", outline = "#e7ba00", width = 25 )
jeton_gauche_2.create_oval((25,25),(175,175), fill="#ff3b30", outline = "#bb261f", width = 25  )
jeton_droite_1.grid(row = 3, column=3, rowspan = 5)
jeton_droite_2.grid(row = 9, column=3, rowspan = 5)
jeton_droite_1.create_oval((25,25),(175,175), fill="#ff3b30", outline = "#bb261f", width = 25 )
jeton_droite_2.create_oval((25,25),(175,175), fill="#ffd933", outline = "#e7ba00", width = 25  )

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


