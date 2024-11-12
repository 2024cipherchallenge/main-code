from tkinter import *
class Cypher_Tools:
    def __init__(self):
        win=Tk()
        win.geometry("400x400")
        win.title("CypherTools")

        Grid.rowconfigure(win,0, weight=1)
        Grid.columnconfigure(win,0,weight=1)
        Grid.rowconfigure(win,1,weight=1)
        Grid.columnconfigure(win,1,weight=1)


        btn_Ceasure=Button(win,text="Ceasure Cypher")
        btn_Ceasure.grid(row=0,column=0,sticky="NEWS")
        btn_Vigenere=Button(win,text="Vigenere Cypher")
        btn_Vigenere.grid(row=0,column=1,sticky="NEWS")
        btn_Substitution=Button(win,text="Substitution Cypher")
        btn_Substitution.grid(row=1,column=0,sticky="NEWS")
        btn_Tools=Button(win,text="Tools")
        btn_Tools.grid(row=1,column=1,sticky="NEWS")

        win.mainloop()

Cypher_Tools()

