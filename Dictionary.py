from tkinter import*
root=Tk()
root.title("Dictionary")
root.geometry("600x400")

label_mutable = Label(root)
label_immutable = Label(root)
label_tkinter = Label(root)

dictionary = { "Mutable": "Values can be changed just like list",
               "Immutable": "Values can not be changed just like tuples",
               "Tkinter": "It is the GUI library of python"} 

def mutable():
    label_mutable['text'] = dictionary["Mutable"]
    
def immutable():
    label_immutable['text'] = dictionary["Immutable"]
    
def tkinter():
    label_tkinter['text'] = dictionary["Tkinter"]
    
button_mutable = Button(root, text="Meaning of Mutable", command=mutable)
button_mutable.place(relx=0.5, rely=0.2, anchor=CENTER)

label_mutable.place(relx=0.5, rely=0.3, anchor=CENTER)

button_immutable = Button(root, text="Meaning of Immutable", command=immutable)
button_immutable.place(relx=0.5, rely=0.4, anchor=CENTER)

label_immutable.place(relx=0.5, rely=0.5, anchor=CENTER)

button_tkinter = Button(root, text="Meaning of Tkinter", command=tkinter)
button_tkinter.place(relx=0.5, rely=0.6, anchor=CENTER)

label_tkinter.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()


