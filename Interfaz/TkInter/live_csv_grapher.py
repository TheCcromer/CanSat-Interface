import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from mpl_toolkits.mplot3d import Axes3D
import csv

style.use('fivethirtyeight')

fig = plt.figure()
#ax2d = fig.add_subplot(111)
ax3d = fig.add_subplot(111, projection='3d')

def load_data():
    data_dict = {}
    with open('data.csv', 'r', newline='') as f:
        reader = csv.DictReader(f)
        for field in reader.fieldnames:
            data_dict[field] = []
        for row in reader:
            for field in reader.fieldnames:
                try:
                    data_dict[field].append(float(row[field]))
                except ValueError:
                    pass
    return data_dict


def animate(i, xfield, yfield):
    ax2d = plt.figure().add_subplot(111)
    data_dict = load_data()
    xs = data_dict[xfield]
    ys = data_dict[yfield]
    #xs = data_dict['MISSION TIME']
    #ys = data_dict['ALTITUDE']
    ax2d.clear()
    ax2d.plot(xs, ys)

def animate3d(i, xfield, yfield, zfield):
    data_dict = load_data()
    xs = data_dict[xfield]
    ys = data_dict[yfield]
    zs = data_dict[zfield]
    ax3d.clear()
    ax3d.plot(xs, ys, zs)

if __name__ == '__main__':
    #ani = animation.FuncAnimation(fig, animate, interval=1000, fargs=('MISSION TIME', 'ALTITUDE'))
    ani2 = animation.FuncAnimation(fig, animate3d, interval=1000, fargs=('GPS LATITUDE', 'GPS LONGITUDE', 'GPS ALTITUDE'))
    plt.show()
