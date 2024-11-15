from tkinter import *


def Tools():
            tools=Tk()
            tools.geometry("400x400")
            tools.title("Tools")
            def frequency():
                input=textbox.get("1.0","end-1c")
                input=input.lower()
                output.delete("1.0",END)
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
                output.insert(INSERT,string1)

            label=Label(tools,text="Tools")
            label.pack(expand=1)
            labelT=Label(tools,text="Input Text")
            labelT.pack(expand=1)
            textbox=Text(tools,height=5)
            textbox.pack(expand=1)
            labelO=Label(tools,text="Output")
            labelO.pack(expand=1)
            output=Text(tools,height=5)
            output.pack(expand=1)
            btnFrequency=Button(tools,text="Frequency Analaysis",command=frequency)
            btnFrequency.pack(expand=1)
            tools.mainloop()

Tools()
