import tkinter as tk
import random as rd

#-----------creation de la fenetre-------------#
root=tk.Tk()
root.geometry("720x480")
root.title("Menu Puissance 4")
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
    aff=tk.Label(root, text="Appuie sur le boutton ci-dessus pour connaitre es règles !", font=("haelvetica", 15), fg="lightgreen" )
    aff.grid(row=11, column=1)
    return
#----------------------------------------------#
#--------creation des widgets textuels---------#
M1=tk.Label(root, text="Bienvenue sur Puissance 4 !", fg="red",
                  font=("Broadway", 45))

M1.grid(column=1, row=2)
#----------------------------------------------#
#--------creation des widget boutons-----------#
B1=tk.Button(root, text="Normal game", font=('haelvetica', 20),
                   bg="lightgrey", fg="grey", relief="ridge", padx=10, pady=5)
B2=tk.Button(root, text="Sandbox", font=('haelvetica', 20),
                   bg="lightgrey", fg="grey", relief="ridge", padx=37, pady=5)
B3=tk.Button(root, text="Options", font=('haelvetica', 20),
                   bg="lightgrey", fg="grey", relief="ridge", padx=42, pady=5)
B4=tk.Button(root, text="Rules", font=('haelvetica', 20),
                   bg="lightgrey", fg="grey", relief="ridge", padx=54, pady=5)


B4.bind("<Button-3>", affichage)

B1.grid(row=7, column=1)
B2.grid(row=8, column=1)
B3.grid(row=9, column=1)
B4.grid(row=10, column=1)
#----------------------------------------------#


root.mainloop()
