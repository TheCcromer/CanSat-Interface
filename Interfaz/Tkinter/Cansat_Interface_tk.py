import csv
import tkinter as tk
import threading
import time
from PIL import ImageTk, Image
from utils import  get_filepath
from graph_window import GraphWindow

MAIN_BUTTON_LABELS = ('Temperature', 'Pressure', 'Voltage', 'Air speed', 'Altitude', 'Trajectory')
BG_COLOR = '#0a1a38'
BUTTON_COLOR = '#ff7f50'
TEXT_COLOR = '#ffffff'
APPLICATION_NAME = "TuCan II Ground Station Software"
LOGO_PATH = f'{get_filepath()}/res/logo.jpeg'
DATA_PATH = f'{get_filepath()}/data.csv'
PAD_X = 5
PAD_Y = 5

def load_data():
    data_dict = {}
    try:
        with open(DATA_PATH, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for field in reader.fieldnames:
                data_dict[field] = []
            for row in reader:
                for field in reader.fieldnames:
                    try:
                        value = float(row[field])
                    except ValueError:
                        value = row[field]
                    data_dict[field].append(value)
    except IOError as err:
        #print(err)
        data_dict = None
    return data_dict

class Application(tk.Frame):
    def __init__(self):
        super().__init__()
        self.FUNCTION_NAMES = (self._graph_temp, self._graph_pres, self._graph_volt, self._graph_airsp, self._graph_alt, self._graph_traj)
        self.init_ui()

    def init_ui(self):
        self.data_lock = threading.Lock()
        self.data_dict = {}

        self.master.title(APPLICATION_NAME)
        self.master.configure(bg=BG_COLOR)
        
        self.logo_img_PIL = Image.open(LOGO_PATH)
        self.logo_img_PIL = self.logo_img_PIL.resize((420, 320))
        self.logo_img = ImageTk.PhotoImage(self.logo_img_PIL)

        self.logo_label = tk.Label(self.master, image=self.logo_img)
        self.logo_label.configure(bg=BG_COLOR)
        self.logo_label.grid(column=1, row=1, ipadx=PAD_X, pady=PAD_Y)

        self.general_button = tk.Button(text="General")
        self.general_button.configure(bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.general_button.grid(column=1, row=2, ipadx=PAD_X, pady=PAD_Y)

        self.main_buttons = {}
        for i in range(len(MAIN_BUTTON_LABELS)):
            current_label = MAIN_BUTTON_LABELS[i]
            self.main_buttons[current_label] = (tk.Button(text=current_label, command=self.FUNCTION_NAMES[i]))
            self.main_buttons[current_label].configure(bg=BUTTON_COLOR, fg=TEXT_COLOR)
            self.main_buttons[current_label].grid(column=(i%2) * 2, row=i%3, padx=PAD_X, pady=PAD_Y)
        
        self.exit_button = tk.Button(text="Exit", command=self._quit)
        self.exit_button.grid(column=2, row=5, padx=PAD_X, pady = PAD_Y)

        self.graph = GraphWindow("Temp", BG_COLOR, TEXT_COLOR, 1, 5, PAD_X, PAD_Y)

        self.exit_flag = False
        self.load_thread = threading.Thread(target=self._load_data)
        self.load_thread.start()

    def get_data_dict(self):
        with self.data_lock:
            return self.data_dict

    def _quit(self):
        self.exit_flag = True
        self.master.quit()
        self.master.destroy()
    
    def _graph_temp(self):
        self.graph.make_appear(self, 'MISSION TIME', 'TEMP')
    
    def _graph_pres(self):
        self.graph.make_appear(self, 'MISSION TIME', 'PRESSURE')

    def _graph_volt(self):
        self.graph.make_appear(self, 'MISSION TIME', 'VOLTAGE')    

    def _graph_airsp(self):
        self.graph.make_appear(self, 'MISSION TIME', 'AIR SPEED')

    def _graph_alt(self):
        self.graph.make_appear(self, 'MISSION TIME', 'ALTITUDE')

    def _graph_traj(self):
        print('3D')

    def _load_data(self):
        while not self.exit_flag:
            with self.data_lock:
                self.data_dict = load_data()
                #print('loaded')
            time.sleep(1.0)


if __name__ == '__main__':
    root = tk.Tk()
    app = Application()
    root.mainloop()