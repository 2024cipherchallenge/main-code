from tkinter import *
class CypherTools:
    def  __init__ (self):
        def CeasureShift():
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
            textbox.delete("1.0",END)
            textbox.insert(INSERT,string1)

        def sub(character):
           
            replace=textbox2.get("1.0","end-1c")
            input=textbox.get("1.0","end-1c")
            array=[]
            if len(replace)>1:
                textbox2.delete("1.0",END)
                textbox2.insert(INSERT,"Input for subsitution cypher can only be one character")
                return None
            for i in range(len(input)):
                array+=input[i:i+1]
                if array[i]==character:
                    array[i]=replace
            input=""
            for i in range(len(array)):
                input+=array[i]
            textbox.delete("1.0",END)
            textbox2.delete("1.0",END)
            textbox.insert(INSERT,input)

        def frequency():
            input=textbox.get("1.0","end-1c")
            input=input.lower()
            textbox3.delete("1.0",END)
            counta=0
            countb=0
            countc=0
            countd=0
            counte=0
            countd=0
            countf=0
            countg=0
            counth=0
            counti=0
            countj=0
            countk=0
            countl=0
            countm=0
            countn=0
            counto=0
            countp=0
            countq=0
            countr=0
            counts=0
            countt=0
            countu=0
            countv=0
            countw=0
            countx=0
            county=0
            countz=0
            for chr in input:
                if chr=="a":
                    counta+=1
                elif chr=="b":
                    countb+=1
                elif chr=="c":
                    countc+=1
                elif chr=="d":
                    countd+=1
                elif chr=="e":
                    counte+=1
                elif chr=="f":
                    countf+=1
                elif chr=="g":
                    countg+=1
                elif chr=="h":
                    counth+=1
                elif chr=="i":
                    counti+=1
                elif chr=="j":
                    countj+=1
                elif chr=="k":
                    countk+=1
                elif chr=="l":
                    countl+=1
                elif chr=="m":
                    countm+=1
                elif chr=="n":
                    countn+=1
                elif chr=="o":
                    counto+=1
                elif chr=="p":
                    countp+=1
                elif chr=="q":
                    countq+=1
                elif chr=="r":
                    countr+=1
                elif chr=="s":
                    counts+=1
                elif chr=="t":
                    countt+=1
                elif chr=="u":
                    countu+=1
                elif chr=="v":
                    countv+=1
                elif chr=="w":
                    countw+=1
                elif chr=="x":
                    countx+=1
                elif chr=="y":
                    county+=1
                elif chr=="z":
                    countz+=1
                else:
                    chr=chr
            string1=("a: "+str(counta)+"b: "+str(countb)+"c: "+str(countc)+"d: "+str(countd)+"e: "+str(counte)+"f: "+str(countf)+"g: "+str(countg)+"\n"+"i: "+str(counti)+"j: "+str(countj)+"k: "+str(countk)+"l: "+str(countl)+"m: "+str(countm)+"n: "+str(countn)+"\n"+"o: "+str(counto)+"p: "+str(countp)+"q: "+str(countq)+"t: "+str(countt)+"\n"+"u: "+str(countu)+"v: "+str(countv)+"w: "+str(countw)+"x: "+str(countx)+"y: "+str(county)+"z: "+str(countz))
            textbox3.insert(INSERT,string1)
            
        window=Tk()
        window.geometry("800x500")
        window.title("CypherTools")
        label=Label(window,text="CypherTools",font=("Arial",12))
        label.pack(padx=20,pady=20)
        label3=Label(window,text="Input Text",font=("Arial",12))
        textbox=Text(window,height=5,font=("Arial",12))
        label3.pack()
        textbox.pack(padx=20,pady=20)
        label1=Label(window,text="Substitution Cypher",font=("Arial",12))
        label2=Label(window,text="Letter Frequency",font=("Arial",12))
        textbox2=Text(window,height=1,font=("Arial",12))
        textbox3=Text(window,height=3,font=("Arial",12))
        label1.pack()
        textbox2.pack()
        label2.pack()
        textbox3.pack()
        var=StringVar()
        slider=Scale(window,variable=var,from_=0,to=25,orient=HORIZONTAL)
        slider.pack()
        btn=Button(window,text="CeasureShift",command=CeasureShift)
        btn.pack()
        btnfrequency=Button(window,text="Letter Frequency",command=frequency)
        btnfrequency.pack()
        buttonframe=Frame(window)
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
       
        window.mainloop()
    

CypherTools()

