import tkinter as tk
from PIL import ImageTk, Image
from utils import  get_filepath

MAIN_BUTTON_LABELS = ('Tempeture', 'Pressure', 'Voltage', 'Air speed', 'Altitude', 'Trajectory')
BG_COLOR = '#0a1a38'
BUTTON_COLOR = '#ff7f50'
TEXT_COLOR = '#ffffff'
APPLICATION_NAME = "TuCan II Ground Station Software"
LOGO_PATH = f'{get_filepath()}/res/logo.jpeg'
PAD_X = 5
PAD_Y = 5

class Application(tk.Frame):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.master.title(APPLICATION_NAME)
        self.master.configure(bg=BG_COLOR)
        self.logo_img_PIL = Image.open(LOGO_PATH)
        self.logo_img_PIL = self.logo_img_PIL.resize((420, 320))
        self.logo_img = ImageTk.PhotoImage(self.logo_img_PIL)

        self.logo_label = tk.Label(root, image=self.logo_img)
        self.logo_label.configure(bg=BG_COLOR)
        self.logo_label.grid(column=1, row=1, ipadx=PAD_X, pady=PAD_Y)

        self.general_button = tk.Button(text="General")
        self.general_button.configure(bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.general_button.grid(column=1, row=2, ipadx=PAD_X, pady=PAD_Y)

        self.main_buttons = {}
        for i in range(len(MAIN_BUTTON_LABELS)):
            current_label = MAIN_BUTTON_LABELS[i]
            self.main_buttons[current_label] = (tk.Button(text=current_label))
            self.main_buttons[current_label].configure(bg=BUTTON_COLOR, fg=TEXT_COLOR)
            self.main_buttons[current_label].grid(column=(i%2) * 2, row=i%3, padx=PAD_X, pady=PAD_Y)
        
        self.exit_button = tk.Button(text="Exit", command=self._quit)
        self.exit_button.grid(column=2, row=5, padx=PAD_X, pady = PAD_Y)

    def _quit(self):
        self.master.quit()
        self.master.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = Application()
    root.mainloop()