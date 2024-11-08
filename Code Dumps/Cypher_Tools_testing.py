from tkinter import *
class Cypher_Tools:
    def __init__(self):
        win=Tk()
        win.geometry("400x400")
        win.title("CypherTools")

        frame=Frame(win)
        frame.grid(row=0,column=0,sticky=N+E+W+S)
        for rows in range(4):
            Grid.rowconfigure(frame,rows,weight=1)
            for column in range(8):
                Grid.columnconfigure(frame,column,weight=1)

        btn_Ceasure=Button(frame,text="Ceasure Cypher",width=20,height=20)
        btn_Ceasure.grid(row=0,column=0,columnspan=4,rowspan=2,sticky=N+E+W+S)
        btn_Vigenere=Button(frame,text="Vigenere Cypher",width=20,height=20)
        btn_Vigenere.grid(row=2,column=0,rowspan=2,columnspan=4,sticky=N+E+W+S)
        btn_Substitution=Button(frame,text="Substitution Cypher",width=20,height=20)
        btn_Substitution.grid(row=0,column=4,rowspan=2,columnspan=4,sticky=N+E+W+S)
        btn_Tools=Button(frame,text="Tools",width=20,height=20)
        btn_Tools.grid(row=2,column=4,rowspan=2,columnspan=4,sticky=N+E+W+S)

        win.mainloop()

Cypher_Tools()