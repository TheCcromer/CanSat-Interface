import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import csv

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

def animate(i):
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
    
    xs = data_dict['MISSION TIME']
    ys = data_dict['ALTITUDE']
    ax1.clear()
    ax1.plot(xs, ys)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()