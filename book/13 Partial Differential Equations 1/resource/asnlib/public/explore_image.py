# +
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from ipywidgets import interact
import ipywidgets as widgets

def explore_image(A, zname="$\phi$", xname="x", yname="y"):
    # Make a interactive plot of matrix A with an image plot on the left and an 
    # adjustable  line cut on the right
    # To keep things simple, we'll make it work only for square images

    plt.subplots(figsize=(9,3))
    lc_max = A.shape[1]-1
    lc = lc_max//2
    x = range(lc_max+1)
    plt.subplot(121)
    img = plt.imshow(A,cmap='RdBu_r', origin='bottom',aspect='equal')
    plt.xlabel(xname)
    plt.ylabel(yname)
    plt.colorbar().set_label(zname)
    line1, = plt.plot((0,lc_max),(lc,lc),c='w', ls=':')
    ax = plt.subplot(122)
    line2, = plt.plot(x,A[lc,:])
    data_max = np.max(A)
    data_min = np.min(A)
    plot_max = data_max + (data_max - data_min)*0.05
    plot_min = data_min - (data_max - data_min)*0.05
    plt.ylim(plot_min,plot_max)
    plt.axhline(0,ls=":",c="grey")
    plt.xlabel(xname)
    plt.ylabel(zname)
    plt.tight_layout()
    
    ngam = 100
    gamma_list = np.geomspace(0.1,10,ngam)
    
    def update_plot(lc=lc_max//2, hor=1, autoscale=0, color_tweak=ngam//2):
        gamma = gamma_list[color_tweak]
        if hor:
            line1.set_data((0,lc_max),(lc,lc))
            line2.set_data(x,A[lc,:])
            ax.set_xlabel(xname)
        else:
            line1.set_data((lc,lc),(0,lc_max))
            line2.set_data(x,A[:,lc])
            ax.set_xlabel(yname)
        if (autoscale):
            plt.autoscale(axis='both')
            ax.relim()
            ax.autoscale_view()
        else:
            ax.set_ylim(plot_min,plot_max)
        img.set_norm(norm=colors.PowerNorm(gamma=gamma, vmin=data_min, vmax=data_max))
        
    return interact(update_plot, lc=(0,lc_max,1), hor=(0,1,1), autoscale=(0,1,1),color_tweak=(0,ngam-1,1))
