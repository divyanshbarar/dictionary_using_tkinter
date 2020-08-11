from tkinter import *

from PyDictionary import PyDictionary

root=Tk()
root.title("DICTIONARY BY PYTHON ")
txt=Text(root)
txt.configure(bg="yellow")
txt.grid(row=3,column=0,columnspan=2)
root.geometry("500x450")
def search():
    word=e.get()
    dictionary=PyDictionary(word)
    meaning=dictionary.printMeanings()
    st=str(meaning)

    txt.insert(END,"/n"+st)


e=Entry(root,font=("times",25,"bold"),justify=CENTER)
e.grid(row=0,column=0)
bttn_srch=Button(root,text="SEARCH",command=search)
bttn_srch.grid(row=1,column=0)




root.mainloop()