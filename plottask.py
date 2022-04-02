##Task to plot graph using matplotlib
##Author JP Quinn


import matplotlib.pyplot as plt
import numpy as np

x = [0,4]

f = (x)=x
g = (x)=np.power(x,2)
h = (x)=np.power(x,3) ##https://numpy.org/doc/stable/reference/generated/numpy.power.html


fig, axs = plt.subplots(3)  ##https://matplotlib.org/devdocs/gallery/subplots_axes_and_figures/subplots_demo.html
##plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

axs[0].plot(f)
axs[0].set_title("(x)=x")

axs[1].plot(g)
axs[1].set_title("(x)=x^2")

axs[2].plot(h)
axs[2].set_title("(x)=x^3")

##plt.plot(f)
##plt.plot(g)
##plt.plot(h)

plt.show()






