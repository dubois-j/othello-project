import matplotlib.pyplot as plt
import time
import numpy as np

x = [1,2,3]
y = [1,2,3]
y1=[4,5,6]
y2=[7,5,3]


# You probably won't need this if you're embedding things in a tkinter plot...
plt.ion()

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
line1= ax.scatter(x,y,c=['k','k','k'],s=45, marker='X',linestyle='')
print("Premier graph")

ax.set_ylim(-0.5,7.5)
ax.set_xlim(-0.5,7.5)
ax.set_facecolor("darkolivegreen")

ax.set_yticks([7,6,5,4,3,2,1,0],['1','2','3','4','5','6','7','8'])
ax.set_xticks([0,1,2,3,4,5,6,7],['A','B','C','D','E','F','G','H'])
ax.tick_params(axis="x", bottom=True, top=True, labelbottom=True, labeltop=True)
ax.tick_params(axis="y", right=True, left=True, labelright=True, labelleft=True)



for i in [-0.5,0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5]:
    ax.axvline(i,color='k')
    ax.axhline(i,color='k')

#ax.add_patch(plt.Circle((0,0), 0.4, color='k'))
fig.canvas.draw()
fig.canvas.flush_events()
time.sleep(1)

for phase in [y1,y2]:
    line1.set_aa(phase)
    #line1.set_xdata(x)
    line1.set_color(['r','r','k'])
    fig.canvas.draw()
    fig.canvas.flush_events()
    arg=input("Mon vieux fait qqch: ")


# x=[1,2,3]
# y1=[4,9,12]
# y2=[8,5,3]

# plt.ion()
# fig=plt.figure()
# ax=fig.add_subplot(111)

# line1, =ax.plot(x,y1)

# for y in [y1,y2]:
#     line1.set_ydata(y1)
#     fig.canvas.draw()

#     argu=input("Wesh tape qqch, ca a pas d'importance")
#     fig.canvas.flush_events()
#     time.sleep(5)
#     