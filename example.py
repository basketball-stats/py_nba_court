import os
from create_court import create_court
import matplotlib.pyplot as plt

def create_court():
    fig = plt.figure(figsize=(4, 3.76))
    ax = fig.add_axes([0, 0, 1, 1])
    ax = create_court(ax, 'black')
    plt.savefig(os.path.join('./', 'empty_halfcourt.png'))

create_court()
