from tkinter import *
import os
import subprocess
def Launcher():


        def Ceasure():
            win.destroy()
            #os.system("Ceasure.py")
            #subprocess.run(["python", "Ceasure.py"])
            with open("Ceasure.pyw") as file:
                exec(file.read())

        def Vig():
            win.destroy()
            #os.system("Vig.pyw")
            with open("Vig.pyw") as file:
                exec(file.read())
        def Sub():
            win.destroy()
            #os.system("Sub.pyw")
            with open("Sub.pyw") as file:
                exec(file.read())
        def Tools():
            win.destroy()
            #os.system("Tools.pyw")
            with open("Tools.pyw") as file:
                exec(file.read())

    
        win=Tk()
        win.geometry("400x400")
        win.title("CypherTools")

        cols=2
        rows=2

        for i in range (cols):
            Grid.columnconfigure(win,i,weight=1)
        for i in range(rows):
            Grid.rowconfigure(win,i,weight=1)

        btn_Ceasure=Button(win,text="Ceasure Cypher",command=Ceasure)
        btn_Ceasure.grid(row=0,column=0,sticky="NEWS")
        btn_Vigenere=Button(win,text="Vigenere Cypher",command=Vig)
        btn_Vigenere.grid(row=0,column=1,sticky="NEWS")
        btn_Substitution=Button(win,text="Substitution Cypher",command=Sub)
        btn_Substitution.grid(row=1,column=0,sticky="NEWS")
        btn_Tools=Button(win,text="Tools",command=Tools)
        btn_Tools.grid(row=1,column=1,sticky="NEWS")

        win.mainloop()

Launcher()


# split into seperate files
