import tkinter as tk
import random as rd

#-----------creation de la fenetre-------------#
root=tk.Tk()
root.geometry("720x480")
root.title("Menu Puissance 4")
root.attributes("-fullscreen", True)
root.bind("<Escape>", lambda event: root.destroy())
#----------------------------------------------#
#--organisation de la geometrie de la fenetre--#
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

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
def affichage(self):
    aff=tk.Label(root, text="Appuie sur le boutton ci-dessus pour connaitre les règles !",
                 font=("haelvetica", 15), fg="green" )
    aff.grid(row=11, column=1)
    return
tour="jaune"
def Jeu_normal():
    def fermer():
        game.destroy()
        return
    HEIGHT = 720 #Sera modifiable
    WIDTH = 1300 #Sera modifiable
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
    B7=tk.Button(game, text="quitter", font=("haelvetica",15), fg="black", 
                 bg="lightgrey", relief="ridge", padx=10, command=fermer)
    B7.pack(side=tk.BOTTOM)
    rayon_trou = (min((HEIGHT//dim_grille[0]),(WIDTH//dim_grille[1])))//2.5
    for i in range(dim_grille[1]):
        for j in range(dim_grille[0]):
            canva_jeu.create_oval(((i+0.5)*WIDTH//dim_grille[1]-rayon_trou,(j+0.5)*HEIGHT//dim_grille[0]-rayon_trou), 
                                  ((i+0.5)*WIDTH//dim_grille[1]+rayon_trou,(j+0.5)*HEIGHT//dim_grille[0]+rayon_trou), 
                                  fill = "#3394ff",  outline="#004fab", width= 0.1*rayon_trou)
    #-------------creation des jetons--------------#
    rayon_jeton = 1.8 * rayon_trou / 2.13
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
    rules=tk.Tk()
    rules.title("Règles du jeu")
    rules.rowconfigure(0, weight=1)
    rules.rowconfigure(1, weight=1)
    rules.rowconfigure(2, weight=1)
    rules.rowconfigure(3, weight=1)
    rules.rowconfigure(4, weight=1)
    rules.columnconfigure(0, weight=1)
    rules.columnconfigure(1, weight=1)
    rules.columnconfigure(2, weight=1)
    rules.attributes("-fullscreen", True)
    M2=tk.Label(rules, text="regles", font=("haelvetica", 20), fg="black")
    B5=tk.Button(rules, text="fermer les règles", font=("haelvetica",15), fg="black", 
                 bg="lightgrey", relief="ridge", padx=10, pady=5, command=fermer)
    B5.pack(side=tk.BOTTOM)
    M2.grid(row=0, column=1)
    return
##--------------------------------------------##
#----------------------------------------------#
#--------creation des widgets textuels---------#
M1=tk.Label(root, text="Bienvenue sur Puissance 4 !", fg="red",
                  font=("Broadway", 45))

M1.grid(column=1, row=2)
#----------------------------------------------#
#--------creation des widget boutons-----------#
B1=tk.Button(root, text="Normal game", font=('haelvetica', 20), bg="lightgrey",
             fg="grey", relief="ridge", padx=10, pady=5, command=Jeu_normal)
B2=tk.Button(root, text="Sandbox", font=('haelvetica', 20), bg="lightgrey", 
             fg="grey", relief="ridge", padx=37, pady=5, command=Jeu_sandbox)
B3=tk.Button(root, text="Options", font=('haelvetica', 20), bg="lightgrey", 
             fg="grey", relief="ridge", padx=42, pady=5, command=settings)
B4=tk.Button(root, text="Rules", font=('haelvetica', 20), bg="lightgrey", 
             fg="grey", relief="ridge", padx=54, pady=5, command=rules)

B1.grid(row=7, column=1)
B2.grid(row=8, column=1)
B3.grid(row=9, column=1)
B4.grid(row=10, column=1)
#----------------------------------------------#
#-------------creation des pop-up--------------#
B4.bind("<Motion>", affichage)
#----------------------------------------------#
root.mainloop()

