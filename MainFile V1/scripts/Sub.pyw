from tkinter import *

def Sub():
            top=Tk()
            top.geometry("400x400")
            top.title("Substitution Cypher")
            def sub(character):
                replace=textbox2.get("1.0","end-1c")
                input=textbox.get("1.0","end-1c")
                array=[]
                if len(replace)>1 or replace=="":
                    textbox2.delete("1.0",END)
                    textbox2.insert(INSERT,"Input for subsitution cypher can only be one character")
                    return None
                for i in range(len(input)):
                    array+=input[i:i+1]
                    if array[i].lower()==character:
                        array[i]=replace
                input=""
                for i in range(len(array)):
                    input+=array[i]

                textbox2.delete("1.0",END)
                output.delete("1.0",END)
                output.insert(INSERT,input)

            label=Label(top,text="Substitution").pack(expand=1)
            labelT=Label(top,text="Input Cypher").pack(expand=1)
            textbox=Text(top,height=5)
            textbox.pack(expand=1)
            labelT2=Label(top,text="Input what you are substituting").pack(expand=1)
            textbox2=Text(top,height=1,width=10)
            textbox2.pack(expand=1)
            buttonframe=Frame(top)
            buttonframe.columnconfigure(0, weight=1)
            buttonframe.columnconfigure(1, weight=1)
            buttonframe.columnconfigure(2, weight=1)
            buttonframe.columnconfigure(3, weight=1)
            buttonframe.columnconfigure(4, weight=1)
            buttonframe.columnconfigure(5, weight=1)
            buttonframe.columnconfigure(6, weight=1)
            buttonframe.columnconfigure(7, weight=1)
            buttonframe.columnconfigure(8, weight=1)
            buttonframe.columnconfigure(9, weight=1)
            buttonframe.columnconfigure(10, weight=1)
            buttonframe.columnconfigure(11, weight=1)
            buttonframe.columnconfigure(12, weight=1)

            btna=Button(buttonframe,text="a",font=("Arial",10),command=lambda:sub("a"))
            btna.grid(row=0,column=0,sticky=W+E)
            btnb=Button(buttonframe,text="b",font=("Arial",10),command=lambda:sub("b"))
            btnb.grid(row=0,column=1,sticky=W+E)
            btnc=Button(buttonframe,text="c",font=("Arial",10),command=lambda:sub("c"))
            btnc.grid(row=0,column=2,sticky=W+E)
            btnd=Button(buttonframe,text="d",font=("Arial",10),command=lambda:sub("d"))
            btnd.grid(row=0,column=3,sticky=W+E)
            btne=Button(buttonframe,text="e",font=("Arial",10),command=lambda:sub("e"))
            btne.grid(row=0,column=4,sticky=W+E)
            btnf=Button(buttonframe,text="f",font=("Arial",10),command=lambda:sub("f"))
            btnf.grid(row=0,column=5,sticky=W+E)
            btng=Button(buttonframe,text="g",font=("Arial",10),command=lambda:sub("g"))
            btng.grid(row=0,column=6,sticky=W+E)
            btnh=Button(buttonframe,text="h",font=("Arial",10),command=lambda:sub("h"))
            btnh.grid(row=0,column=7,sticky=W+E)
            btni=Button(buttonframe,text="i",font=("Arial",10),command=lambda:sub("i"))
            btni.grid(row=0,column=8,sticky=W+E)
            btnj=Button(buttonframe,text="j",font=("Arial",10),command=lambda:sub("j"))
            btnj.grid(row=0,column=9,sticky=W+E)
            btnk=Button(buttonframe,text="k",font=("Arial",10),command=lambda:sub("k"))
            btnk.grid(row=0,column=10,sticky=W+E)
            btnl=Button(buttonframe,text="l",font=("Arial",10),command=lambda:sub("l"))
            btnl.grid(row=0,column=11,sticky=W+E)
            btnm=Button(buttonframe,text="m",font=("Arial",10),command=lambda:sub("m"))
            btnm.grid(row=0,column=12,sticky=W+E)
            btnn=Button(buttonframe,text="n",font=("Arial",10),command=lambda:sub("n"))
            btnn.grid(row=1,column=0,sticky=W+E)
            btno=Button(buttonframe,text="o",font=("Arial",10),command=lambda:sub("o"))
            btno.grid(row=1,column=1,sticky=W+E)
            btnp=Button(buttonframe,text="p",font=("Arial",10),command=lambda:sub("p"))
            btnp.grid(row=1,column=2,sticky=W+E)
            btnq=Button(buttonframe,text="q",font=("Arial",10),command=lambda:sub("q"))
            btnq.grid(row=1,column=3,sticky=W+E)
            btnr=Button(buttonframe,text="r",font=("Arial",10),command=lambda:sub("r"))
            btnr.grid(row=1,column=4,sticky=W+E)
            btns=Button(buttonframe,text="s",font=("Arial",10),command=lambda:sub("s"))
            btns.grid(row=1,column=5,sticky=W+E)
            btnt=Button(buttonframe,text="t",font=("Arial",10),command=lambda:sub("t"))
            btnt.grid(row=1,column=6,sticky=W+E)
            btnu=Button(buttonframe,text="u",font=("Arial",10),command=lambda:sub("u"))
            btnu.grid(row=1,column=7,sticky=W+E)
            btnv=Button(buttonframe,text="v",font=("Arial",10),command=lambda:sub("v"))
            btnv.grid(row=1,column=8,sticky=W+E)
            btnw=Button(buttonframe,text="w",font=("Arial",10),command=lambda:sub("w"))
            btnw.grid(row=1,column=9,sticky=W+E)
            btnx=Button(buttonframe,text="x",font=("Arial",10),command=lambda:sub("x"))
            btnx.grid(row=1,column=10,sticky=W+E)
            btny=Button(buttonframe,text="y",font=("Arial",10),command=lambda:sub("y"))
            btny.grid(row=1,column=11,sticky=W+E)
            btnz=Button(buttonframe,text="z",font=("Arial",10),command=lambda:sub("z"))
            btnz.grid(row=1,column=12,sticky=W+E)
            buttonframe.pack()
            labelO=Label(top,text="Output").pack(expand=1)
            output=Text(top,height=5)
            output.pack(expand=1)
        
            top.mainloop()

Sub()




