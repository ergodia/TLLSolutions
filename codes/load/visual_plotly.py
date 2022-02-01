import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns; sns.set_theme()
import numpy as np
import plotly.graph_objects as go
from matplotlib.animation import FuncAnimation
from IPython import display

def holland_graph(path, stations_dict: dict, bbox):
    # load the map into the graph
    # map = plt.imread(path / "data" / "holland.png")
    map = plt.imread(path / "data" / "Kaart_NL_grijs.png")

    # traject = pd.read_csv(path / "data" / "StationsNationaal.csv" )
    # # traject = traject[:-1]
    # traject.set_index(['stations'])
    # ex_traject = traject.explode('stations')

    # print(traject)
    #print(ex_traject)
    x = np.linspace(0, 2*np.pi, 100)
  
    fig, ax = plt.subplots(figsize=(17, 20))  
    ax.set_xlim(bbox[0], bbox[1])
    ax.set_ylim(bbox[2], bbox[3])
    lines = plt.plot([])
    line = lines[0]

    # animation function
    def animate(frame):
        # update plot
        y = np.sin(x + 2*np.pi * frame/100)
        line.set_data((x, y))
   
    
    # colors form seaborn
    line_colors = sns.color_palette("husl", 20)
    colors = iter(line_colors)
    
    # plot line and markers
    for key in stations_dict:
        ax.plot(stations_dict[key].y,
            stations_dict[key].x,
            zorder=1,
            linewidth=5,
            color=next(colors),
            marker="o",
            markersize=12,
            markeredgewidth=4,
            markerfacecolor='w',
            label=key)
 
    
    # plt.text(3, 4.5, 'This')
    # #https://queirozf.com/entries/add-labels-and-text-to-matplotlib-plots-annotation-examples
    # # for x, y in zip(traject['y'], traject['x']):
    # #     station=traject['station'] 
    # ax.annotate('station', # this is the text
    #     (52,6), # these are the coordinates to position the label
    #     textcoords="offset points", # how to position the text
    #     xytext=(0,15), # distance from text to points (x,y)
    #     ha='center',
    #     fontsize=10,
    #     bbox=dict(boxstyle="round", fc="w", alpha=0.5)) # horizontal alignment can be left



    # print(plt.style.available)
    
    ax.imshow(map, zorder=0, extent = bbox, aspect="auto") # kaart inladen order(onder boven)
    #fig.set_size_inches(10, 40, forward=True) #kaart formaat

    # show legend 
    ax.legend(loc=2, prop={'size': 15})
    
    plt.axis("off")
    plt.title("Holland Graph", fontsize=60)
    
    # fig.savefig(path / "data" / "holland_graph.png", bbox_inches="tight", dpi=350)
    fig.savefig(path / "data" / "Animatie_graph.png", bbox_inches="tight", dpi=150)

    anim = FuncAnimation(fig, animate, frames=100, interval=20)
    video = anim.to_html5_video()
    html = display.HTML(video)
    display.display(html)
    plt.close()

    plt.show()

# https://matplotlib.org/basemap/users/examples.html
# https://plotly.com/python/lines-on-maps/
