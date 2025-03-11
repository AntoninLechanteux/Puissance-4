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
#----------------------------------------------#
#--------creation des widgets textuels---------#
M1=tk.Label(root, text="Bienvenue sur Puissance 4 !", fg="red",
                  font="Broadway")

M1.grid(column=1, row=0)
#----------------------------------------------#
#--------creation des widget boutons-----------#
B1=tk.Button(root, text="Normal game", font="Arial",
                   bg="lightgrey", fg="grey", relief="raised", padx=5, pady=5)
B2=tk.Button(root, text="Sandbox", font="Arial",
                   bg="lightgrey", fg="grey", relief="raised", padx=5, pady=5)
B3=tk.Button(root, text="Options", font="Arial",
                   bg="lightgrey", fg="grey", relief="raised", padx=5, pady=5)
B4=tk.Button(root, text="Rules", font="Arial",
                   bg="lightgrey", fg="grey", relief="raised", padx=5, pady=5)

B1.grid(column=1, row=2)
B2.grid(column=1, row=3)
B3.grid(column=1, row=4)
B4.grid(column=1, row=5)
#----------------------------------------------#


root.mainloop()
