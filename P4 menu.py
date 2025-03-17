import tkinter as tk
import random as rd

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

def Jeu_normal():
    game=tk.Tk()
    game.title("Jeu mode normal")
    game.attributes("-fullscreen", True)
    game.bind("<Escape>", lambda event: game.destroy())
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
    B6.grid(row=4, column=1)
##-----------Affichage des règles-------------##
def regle():
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
    B5=tk.Button(rules, text="fermer les règles", font=("haelvetica",15),
                 fg="black", bg="lightgrey", relief="ridge", padx=10, pady=5, command=fermer)
    B5.grid(row=4, column=1)
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
B1=tk.Button(root, text="Normal game", font=('haelvetica', 20),
                   bg="lightgrey", fg="grey", relief="ridge", padx=10, pady=5, command=Jeu_normal)
B2=tk.Button(root, text="Sandbox", font=('haelvetica', 20),
                   bg="lightgrey", fg="grey", relief="ridge", padx=37, pady=5, command=Jeu_sandbox)
B3=tk.Button(root, text="Options", font=('haelvetica', 20),
                   bg="lightgrey", fg="grey", relief="ridge", padx=42, pady=5, command=settings)
B4=tk.Button(root, text="Rules", font=('haelvetica', 20),
                   bg="lightgrey", fg="grey", relief="ridge", padx=54, pady=5, command=regle)

B1.grid(row=7, column=1)
B2.grid(row=8, column=1)
B3.grid(row=9, column=1)
B4.grid(row=10, column=1)
#----------------------------------------------#
#-------------creation des pop-up--------------#
B4.bind("<Motion>", affichage)
#----------------------------------------------#
root.mainloop()
