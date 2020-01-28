import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GraphWindow(tk.Frame):
    def __init__(self, name, bg_color, text_color, column, row, padx, pady):
        super().__init__()
        self.name = name
        self.bg_color = bg_color
        self.text_color = text_color
        self.padx = padx
        self.pady = pady
        self.column = column
        self.row = row
        self.init_graph_ui()
    
    def init_graph_ui(self):
        self.debug_label = tk.Label(self.master, text=self.name)
        self.debug_label.configure(bg=self.bg_color, fg=self.text_color)
        self.xar = []
        self.yar = []
        style.use('ggplot')
        self.fig = plt.figure(figsize=(4, 2.5), dpi=100)
        self.ax1 = self.fig.add_subplot(111)
        #self.ax1.set_ylim(0, 100)
        self.line, = self.ax1.plot(self.xar, self.yar, 'r', marker='o')
        self.ani = None

    def make_appear(self, data_holder, xfield, yfield):
        if self.ani != None:
            self.ani.event_source.stop()
        self.plotcanvas = FigureCanvasTkAgg(self.fig, self.master)
        self.plotcanvas.get_tk_widget().grid(column=self.column, row=self.row, padx=self.padx, pady=self.pady)
        self.ani = animation.FuncAnimation(self.fig, animate, interval=1000, blit=False, 
                    fargs=(self, data_holder, xfield, yfield), repeat=False)

# def animate(i, obj):
#     obj.yar.append(99-i)
#     obj.xar.append(i)
#     obj.line.set_data(obj.xar, obj.yar)
#     obj.ax1.set_xlim(0, i+1)

def animate(i, obj, data_holder, xfield, yfield):
    data_dict = data_holder.get_data_dict()
    xs = data_dict[xfield]
    ys = data_dict[yfield]
    obj.ax1.clear()
    obj.ax1.plot(xs, ys)