import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D

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
        style.use('ggplot')
        self.fig = plt.figure(figsize=(4, 2.5), dpi=100)
        self.ani = None

    def set_projection(self, proj):
        self.ax1 = self.fig.add_subplot(111, projection=proj)

    def make_appear(self, data_holder, xfield, yfield, zfield=None):
        if self.ani != None:
            self.ani.event_source.stop()
            self.ax1.clear()
        self.plotcanvas = FigureCanvasTkAgg(self.fig, self.master)
        self.plotcanvas.get_tk_widget().grid(column=self.column, row=self.row, padx=self.padx, pady=self.pady)
        self.ani = animation.FuncAnimation(self.fig, animate, interval=1000, blit=False, 
                    fargs=(self, data_holder, xfield, yfield, zfield), repeat=False)

def animate(i, obj, data_holder, xfield, yfield, zfield=None):
    data_dict = data_holder.get_data_dict()
    xs = data_dict[xfield]
    ys = data_dict[yfield]
    zs = []
    obj.ax1.clear()
    if zfield != None:
        zs = data_dict[zfield]
        obj.ax1.plot(xs, ys, zs)
    else:
        obj.ax1.plot(xs, ys, zs)

