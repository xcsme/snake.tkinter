import tkinter
root=tkinter.Tk()
canvas=tkinter.Canvas(root,width=500,height=500)
canvas.pack()
image=tkinter.PhotoImage(file="smile.png")
canvas.create_image(50,50,anchor=tkinter.CENTER,image=image)
root.mainloop()