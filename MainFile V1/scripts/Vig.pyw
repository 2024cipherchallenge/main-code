from tkinter import *
def Vigerene():
            #can u add logic in the function vig
            def vig():
                pass

            top=Tk()
            top.geometry("400x400")
            top.title("Substitution Cypher")
            LabelT=Label(top,text="Input Cypher").pack()
            textbox=Text(top,height=5)
            textbox.pack()
            LabelT2=Label(top,text="Input word").pack()
            textbox2=Text(top,height=1)
            textbox2.pack()
            btn_vigerene=Button(top,text="Vigerene Cypher",command=vig)
            btn_vigerene.pack()
            LabelO=Label(top,text="Output").pack()
            output=Text(top,height=5)
            output.pack()
            top.mainloop()

Vigerene()
