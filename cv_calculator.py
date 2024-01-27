import tkinter as tk
from tkinter import PhotoImage

class CVCalculator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        
        self.__img = PhotoImage(file="src/info.png")
        
        self.master.resizable(False, False)
        self.master.title("Genshin Impact Crit Value Calculator")
        self.master.iconbitmap("src/paimon.ico") # Not really necessary but ok
        
        self.app_interface()
        
    def app_interface(self):
        self.app_frame = tk.Frame(self)
        self.infographic(self.app_frame)
        self.app_frame.pack(padx=5, pady=5)
    
    def infographic(self, frame):
        tk.Label(frame, image=self.__img).pack(side=tk.LEFT, padx=(0, 30))
        
    def calculate(self, frame, side):
        #TODO: Interface to input crit rate & dmg
        pass
        

if __name__ == "__main__":
    app = CVCalculator()
    app.master.mainloop()