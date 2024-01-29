import tkinter as tk
import pyglet
from tkinter import PhotoImage

pyglet.font.add_file('src/gi_font.ttf') # Adding Genshin Font

class CVCalculator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        
        self.__img = PhotoImage(file="src/info.png")
        
        self.__cr = tk.StringVar() # Input Crit Rate
        self.__cdmg = tk.StringVar() # Input Crit DMG
        self.__is_circlet = tk.BooleanVar() # Assuring the artifact is a Crit Circlet or no
        
        self.master.resizable(False, False)
        self.master.title("Genshin Impact Crit Value Calculator")
        self.master.iconbitmap("src/paimon.ico") # Not really necessary but ok
        
        self.app_interface()
        
    def app_interface(self):
        self.app_frame = tk.Frame(self)
        self.infographic(self.app_frame)
        self.input_crit(self.app_frame)
        self.app_frame.pack(padx=5, pady=5)
    
    def infographic(self, frame):
        tk.Label(frame, image=self.__img).pack(side=tk.LEFT, padx=(0, 17))
        
    def input_crit(self, frame):
        self.input_frame = tk.Frame(frame)
        
        self.cr_label = tk.Label(
            self.input_frame,
            text="Input the Artifact's Crit Rate",
            font=("HYWenHei-85W", 12)
        )
        
        self.cdmg_label = tk.Label(
            self.input_frame,
            text="Input the Artifact's Crit DMG",
            font=("HYWenHei-85W", 12)
        )
        
        self.cr_field = tk.Entry(
            self.input_frame,
            textvariable=self.__cr,
            width=20,
            justify="center"
        )
        
        self.cdmg_field = tk.Entry(
            self.input_frame,
            textvariable=self.__cdmg,
            width=20,
            justify="center"
        )
        
        self.circlet = tk.Checkbutton(
            self.input_frame,
            text="Crit Circlet",
            variable=self.__is_circlet,
            font=("HYWenHei-85W", 10)
        )
        
        self.cr_label.pack(side=tk.TOP, pady=(0, 5), padx=100)
        self.cr_field.pack(side=tk.TOP, pady=(0, 25), padx=100)
        self.cdmg_label.pack(side=tk.TOP, pady=(0, 5), padx=100)
        self.cdmg_field.pack(side=tk.TOP, pady=(0, 25), padx=100)
        self.circlet.pack(side=tk.TOP, pady=(7, 20), padx=100)
        
        self.input_frame.pack(side=tk.RIGHT)
        

if __name__ == "__main__":
    app = CVCalculator()
    app.master.mainloop()