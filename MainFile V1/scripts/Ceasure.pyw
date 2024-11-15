from tkinter import *
def Ceasure():
            top=Tk()
            top.geometry("400x400")
            top.title("Ceasure")
            def ceasureShift():
                input=textbox.get("1.0","end-1c")
                shift=int(var.get())
                punctuation=" .!,:;()?/1234567890"
                string1=""
                for character in input:
                    if character in punctuation:
                        character=character
                    elif ord(character)<=90:
                        character=chr(ord(character)+shift)
                        if ord(character)>90:
                            character=chr(ord(character)-26)
                    else:
                        character=chr(ord(character)+shift)
                        if ord(character)>122:
                            character=chr(ord(character)-26)
                    string1+=character
                output.delete("1.0",END)
                output.insert(INSERT,string1)

            label=Label(top,text="Ceasure").pack(expand=1)
            labelT=Label(top,text="Input").pack(expand=1)
            textbox=Text(top,height=5)
            textbox.pack(expand=1)
            var=StringVar()
            slider=Scale(top,variable=var,from_=0,to=25,orient=HORIZONTAL).pack(expand=1)
            labelO=Label(top,text="Output").pack(expand=1)
            output=Text(top,height=5)
            output.pack(expand=1)
            btnCeasure=Button(top,text="Ceasure Shift",command=ceasureShift).pack(expand=1)
            top.mainloop()
Ceasure()
