import tkinter as tk
import pyglet
from tkinter import PhotoImage, ttk

pyglet.font.add_file('src/gi_font.ttf') # Adding Genshin Font

class CVCalculator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        
        self.__img = PhotoImage(file="src/info.png")
        self.__gi_font = ttk.Style()
        self.__gi_font.configure("Genshin.TButton", font=("HYWenHei-85W", 10))
        self.__gi_font.configure("Genshin.TCheckbutton", font=("HYWenHei-85W", 10))
        
        self.__cr = tk.StringVar() # Input Crit Rate
        self.__cdmg = tk.StringVar() # Input Crit DMG
        self.__is_circlet = tk.BooleanVar() # Assuring the artifact is a Crit Circlet or no
        
        self.master.resizable(False, False)
        self.master.title("Genshin Impact Crit Value Calculator")
        self.master.iconbitmap("src/paimon.ico") # Not really necessary but ok
        
        self.app_interface()
        
    # ===== Methods =====
    def app_interface(self):
        self.app_frame = ttk.Frame(self)
        self.infographic(self.app_frame)
        self.input_crit(self.app_frame)
        self.app_frame.pack(padx=7, pady=7)
    
    
    def infographic(self, frame):
        tk.Label(frame, image=self.__img).pack(side=tk.LEFT, padx=(0, 17))
    
    
    def input_crit(self, frame):
        self.interface_frame = ttk.Frame(frame)
        self.form_frame = ttk.Frame(self.interface_frame)
        self.cr_frame = ttk.Frame(self.form_frame)
        self.cdmg_frame = ttk.Frame(self.form_frame)
        self.__ganyu_icon = PhotoImage(file="src/ganyu.png")
        
        # === Widgets ===
        self.desc = tk.Label(
            self.interface_frame,
            text="Please input your crit substats without\nthe percentage (%) symbol.",
            font=("HYWenHei-85W", 11)
        )
        
        self.cr_label = tk.Label(
            self.cr_frame,
            text="Crit Rate Substat",
            font=("HYWenHei-85W", 10)
        )
        
        self.cdmg_label = tk.Label(
            self.cdmg_frame,
            text="Crit DMG Substat",
            font=("HYWenHei-85W", 10)
        )
        
        self.cr_field = ttk.Entry(
            self.cr_frame,
            textvariable=self.__cr,
            width=17,
            justify="center",
            
        )
        
        self.cdmg_field = ttk.Entry(
            self.cdmg_frame,
            textvariable=self.__cdmg,
            width=17,
            justify="center"
        )
        
        self.circlet = ttk.Checkbutton(
            self.interface_frame,
            text="Crit Circlet",
            variable=self.__is_circlet,
            style="Genshin.TCheckbutton"
        )
        
        self.generate_btn = ttk.Button(
            self.interface_frame,
            text="Calculate CV ",
            style="Genshin.TButton",
            image=self.__ganyu_icon,
            compound=tk.RIGHT,
            width=10,
            cursor="hand2"
        )
        
        # Pack for Input Form
        self.cr_label.pack(pady=5, padx=10)
        self.cdmg_label.pack(pady=5, padx=10)
        self.cr_field.pack(pady=(0, 10))
        self.cdmg_field.pack(pady=(0, 10))
        
        # Combine those frame in form frame
        self.cr_frame.pack(side=tk.LEFT, pady=(15, 0))
        self.cdmg_frame.pack(side=tk.LEFT, pady=(15, 0))
        
        # Pack for main interface frame
        self.desc.pack(side=tk.TOP, pady=(0, 5), padx=50)
        self.form_frame.pack(side=tk.TOP, pady=(0, 10))
        self.circlet.pack(side=tk.TOP, pady=(0, 15), padx=50)
        self.generate_btn.pack(side=tk.TOP, pady=(5, 20), padx=50)
        
        # Pack the Frame
        self.interface_frame.pack(side=tk.RIGHT)
        
        self.cr_field.focus()
    
    
    def generate_cv(self):
        # TODO: Changeable Label to display CV Range and Value.
        pass
    
    
    def calc_cv(self):
        try:
            crit_rate = float(self.__cr.get())
            crit_dmg = float(self.__cdmg.get())
        except ValueError:
            return False # Can't calculate Crit Value



if __name__ == "__main__":
    app = CVCalculator()
    app.master.mainloop()