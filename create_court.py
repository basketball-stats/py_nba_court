import matplotlib as mpl

def create_court(ax, color):
    ax.plot([-220, -220], [0, 140], linewidth=2, color=color) # 3PT STRAIGHT LINE
    ax.plot([220, 220], [0, 140], linewidth=2, color=color) # 3PT STRAIGHT LINE
    ## Draw the circle as if it was an ellipse. 
    ## Second element: half of rim inner radius
    ## Third element of center is: 7 to 10 so that 3pt straight line match 140
    ax.add_artist(mpl.patches.Arc((0, 40+7.5//2+7), 237.5*2, 237.5*2, theta1=22, theta2=158, 
                                  facecolor='none', edgecolor=color, lw=2)) # 3PT ARC
    ax.plot([-80, -80], [0, 190], linewidth=2, color=color) # PAINT SIDE
    ax.plot([80, 80], [0, 190], linewidth=2, color=color) # PAINT SIDE
    ##ax.plot([-60, -60], [0, 190], linewidth=2, color=color) # inner lines in paint
    ##ax.plot([60, 60], [0, 190], linewidth=2, color=color) # inner lines in paint
    ax.plot([-80, 80], [190, 190], linewidth=2, color=color)
    ax.add_artist(mpl.patches.Circle((0, 190), 60, facecolor='none', edgecolor=color, lw=2)) # FT CIRCLE
    ax.add_artist(mpl.patches.Circle((0, 55), 7.5, facecolor='none', edgecolor=color, lw=2)) # RIM
    ax.plot([-30, 30], [40, 40], linewidth=2, color=color) # BACKBOARD
    ax.add_artist(mpl.patches.Arc((0, 470), 60*2, 60*2, theta1=0, theta2=360,facecolor='none',edgecolor=color,lw=2)) # CENTER CIRCLE
    ax.add_artist(mpl.patches.Arc((0, 55), 40*2, 40*2, theta1=0, theta2=180, facecolor='none', edgecolor=color, lw=2)) # PAINT CIRCLE
    ax.set_xlim(-250, 250)
    ax.set_ylim(0, 470)
    ax.set_xticks([])
    ax.set_yticks([])
    #colors = {'2PT Field Goal':'tab:red', '3PT Field Goal':'tab:green'}
    mpl.rcParams['font.family'] = 'Arial'
    mpl.rcParams['font.size'] = 18
    mpl.rcParams['axes.linewidth'] = 2
    return ax
