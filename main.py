from tkinter import*

window = Tk()
window.title("Hubbo - Menu")
window.geometry("600x500")
window.minsize(600, 500)
window.maxsize(600, 500)
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.configure(bg="#303030")

hubbo = Label(window, text="Hubbo", font=(
    "Consolas", 40, "bold"), bg="#303030", fg="lightgrey")

games = Button(window, text="Minigames", font=("Consolas", 17, "bold"),
               bg="grey", fg="lightgrey", activebackground="darkgrey",
               activeforeground="grey", width=9, height=1)

settings = Button(window, text="Settings", font=("Consolas", 17, "bold"),
                  bg="grey", fg="lightgrey", activebackground="darkgrey",
                  activeforeground="grey", width=9, height=1)


test = Label(window, text= "Hello", font=("Consolas", 40, "bold"))

settings.pack()
games.pack()
hubbo.pack()

games.place(x=220, y=130)
settings.place(x=220, y=180)
hubbo.place(x=210, y=10)

window.mainloop()