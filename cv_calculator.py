import tkinter as tk
import pyglet
from tkinter import PhotoImage, ttk, messagebox

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
        self.__cr.set("0")
        self.__cdmg = tk.StringVar() # Input Crit DMG
        self.__cdmg.set("0")
        self.__cv = 0.0 # Default Value
        self.__is_circlet = tk.BooleanVar() # Assuring the artifact is a Crit Circlet or no
        
        self.master.resizable(False, False)
        self.master.title("Genshin Impact Crit Value Calculator")
        
        w = 824
        h = 409
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = int((ws/2) - (w/2))
        y = int((hs/2) - (h/2))
        
        self.master.geometry(f"{w}x{h}+{x}+{y}")
        
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
            command=self.generate_cv,
            compound=tk.RIGHT,
            width=10,
            cursor="hand2"
        )
        
        self.cv_label = tk.Label(
            self.interface_frame,
            text=f"Your Artifact's Crit Value : {self.__cv}",
            font=("HYWenHei-85W", 11)
        )
        
        self.cv_rank = tk.Label(
            self.interface_frame,
            text="No Upgrades",
            foreground="dark grey",
            font=("HYWenHei-85W", 15)
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
        self.generate_btn.pack(side=tk.TOP, pady=(5, 25), padx=50)
        self.cv_label.pack(side=tk.TOP, pady=(5, 0), padx=50)
        self.cv_rank.pack(side=tk.TOP, pady=(5, 0), padx=50)
        
        # Pack the Frame
        self.interface_frame.pack(side=tk.RIGHT)
        
        self.cr_field.focus() # Auto Focusing Keyboard (?) to input Crit Rate
    
    def generate_rank(self):
        # NOTE: I'm not pretty sure for the Crit Circlet yet..
        self.__rank = "Impossible!"
        self.__color_rank = "dark red"
        
        __rank_tier = {
            0 : ["No Upgrades", "dark grey"],
            10 : ["Average", "#deb63e"],
            20 : ["Decent", "#7d7765"],
            30 : ["Very Good", "#336134"],
            40 : ["Jewel", "#abd6ac"],
            50 : ["Unicorn?!", "#b856ae"]
        }
        
        __range = 5 if self.__is_circlet.get() else 10
        __circlet_doubled = 2 if self.__is_circlet.get() else 1
        __start_comp = 0
        
        for i in range(6):
            if __start_comp <= self.__cv < (__start_comp + __range):
                self.__rank = __rank_tier[__start_comp*__circlet_doubled][0]
                self.__color_rank = __rank_tier[__start_comp*__circlet_doubled][1]
                break
            __start_comp += __range
        
        self.cv_rank['text'] = self.__rank
        self.cv_rank['foreground'] = self.__color_rank
            
    
    def generate_cv(self):
        try:
            __crit_rate = float(self.__cr.get())
            __crit_dmg = float(self.__cdmg.get())
            
            # Highest CR possible is 23.4% and 46.8% for CDMG. Negative Crit is also not possible.
            if not(0 <= __crit_rate <= 23.4) or not(0 <= __crit_dmg <= 46.8):
                raise Exception
            
            self.__cv = __crit_rate*2 + __crit_dmg
            
            self.cv_label["text"] = f"Your Artifact's Crit Value : {self.__cv}"
            self.generate_rank()
        except ValueError: # User input is not a number.
            if "%" in self.__cr.get() or "%" in self.__cdmg.get():
                tk.messagebox.showwarning(
                    title="Unable to Calculate CV",
                    message="Didn't we told you to not use the '%'..."
                )
            else:
                tk.messagebox.showwarning(
                    title="Unable to Calculate CV",
                    message="Please input your crit substats properly."
                )
        except:
            tk.messagebox.showwarning(
                title="Unable to Calculate CV",
                message="Your crit substats don't seem right..\n(Take notes that crit main stats are not sub stats)."
            )



if __name__ == "__main__":
    app = CVCalculator()
    app.master.mainloop()
    