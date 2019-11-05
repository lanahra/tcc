import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

csv = pd.read_csv('full.csv')

datasets = (csv[['flows', 'h time', 'lower sol']], csv[['avg', 'into sol', 'lower sol']])
colors = ('#306ae6', '#49b347')
groups = ('Heuristic', 'Cover Model')

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_ylabel('Processing Time (Seconds)')
ax.set_xlabel('Number of Flows')

for data, color, group in zip(datasets, colors, groups):
    df = data.dropna()
    df = df.sort_values('flows')
    x, y, z = df.T.to_numpy()
    # y = (y - z) / y
    # y = y - z
    # permut = x.argsort()
    # x = x[permut]
    # y = y[permut]
    coefs = np.polyfit(x, y, 2)
    p = np.poly1d(coefs)
    ax.scatter(x, y, marker='s', c=color, label=group, zorder=3)
    ax.plot(x, p(x), '-', alpha=0.6, c=color)
    break

# plt.ylim(top=100, bottom=-5)
# plt.xlim(right=5000, left=-500)
plt.legend(loc=2)
plt.grid(linestyle='dotted', zorder=0)
# plt.show()
plt.savefig('fig/heuristic_flows_time.png')
