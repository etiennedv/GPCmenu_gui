import tkinter as tk
from PIL import ImageTk

def load_frame1():
    frame1.pack_propagate(False)

    # frame1 widgets
    logo_img = ImageTk.PhotoImage(file="GPClogo.jpg")
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_color)
    logo_widget.image = logo_img
    logo_widget.pack()

    tk.Label(
        frame1, 
        text="GPC Pull Sheet Generator",
        bg=bg_color,
        fg="black",
        font=("TkMenuFont", 14)
        ).pack()

    button1 = tk.Button(
        frame1,
        text="Create Pull Sheet",
        font=("TkHeadingFont", 20),
        bg="#28393a",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:load_frame2()
        ).pack(pady=100)

    button2 = tk.Button(
        frame1,
        text="Add Menu",
        font=("TkHeadingFont", 20),
        bg="#28393a",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:load_frame2()
        ).pack(pady=100) 
      
def load_frame2():
    print("Test")


#initialize app
root = tk.Tk()
root.title("GPC Menu")

bg_color = "#fffafa"
#root.eval("tk::PlaceWindow . center")
x = (root.winfo_screenwidth()-1000)//2
y = int(root.winfo_screenheight()*0.1)
root.geometry('1000x800+' + str(x) + '+' + str(y))

frame1 = tk.Frame(root, width=1000, height=800, bg=bg_color)
frame2 = tk.Frame(root, bg=bg_color)

for frame in (frame1, frame2):
    frame.grid(row=0, column=0)

load_frame1()

# run app
root.mainloop()
