from tkinter import *
import os
import subprocess
class Cypher_Tools:
    def __init__(self):
        win=Tk()
        win.geometry("300x300") # Resized so buttons fit nicely
        win.title("CypherTools")

        frame=Frame(win)
        frame.grid(row=0,column=0,sticky=N+E+W+S)
        for rows in range(4):
            Grid.rowconfigure(frame,rows,weight=1)
            for column in range(8):
                Grid.columnconfigure(frame,column,weight=1)

        def run_Ceasure():
            # 3 options, try all and pick your fav:
            
            #os.system("CypherTools.py")

            #subprocess.run(["python", "CypherTools.py"])
            
            #with open("CypherTools.py") as file:
                #exec(file.read())

            pass
            

        
        btn_Ceasure=Button(   # Laying out buttons like this makes it much easier to see what they are doing, and edit individual aspects of them
            frame,
            text="Ceasure Cypher",
            width=20,
            height=10,
            command=lambda: run_Ceasure()
            #font = "Helvetica 20" # - If you want to make it look nice...
            )
        btn_Ceasure.grid(row=0,column=0,columnspan=4,rowspan=2,sticky=N+E+W+S)  #grid method is shite. Pack is bad aswell, "place" method is best IMO
        
        btn_Vigenere=Button(frame,text="Vigenere Cypher",width=20,height=10)
        btn_Vigenere.grid(row=2,column=0,rowspan=2,columnspan=4,sticky=N+E+W+S)
        
        btn_Substitution=Button(frame,text="Substitution Cypher",width=20,height=10)
        btn_Substitution.grid(row=0,column=4,rowspan=2,columnspan=4,sticky=N+E+W+S)
        
        btn_Tools=Button(frame,text="Tools",width=20,height=10)
        btn_Tools.grid(row=2,column=4,rowspan=2,columnspan=4,sticky=N+E+W+S)

        win.mainloop()

Cypher_Tools()
