import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
import numpy as np
import plotly.graph_objects as go
from matplotlib.colors import hsv_to_rgb


def holland_graph(path, stations_dict: dict, bbox):
    # load the map into the graph
    # map = plt.imread(path / "data" / "holland.png")
    map = plt.imread(path / "data" / "Kaart_NL_grijs.png")

    traject = pd.read_csv(path / "data" / "StationsNationaal.csv" )
    # traject = traject[:-1]
    # traject.set_index(['stations'])
    # ex_traject = traject.explode('stations')

    
    

    # print(traject)
    #print(ex_traject)

    fig, ax = plt.subplots(figsize=(17, 20))  
    # colors
    line_colors = ['#55efc4', '#2ecc71', '#02836a', '#d1ad73', '#f8a200', '#ffd44d', '#fce800', '#ffc9bc', '#9f1a5a', '#d63031', '#fd79a8', '#d980fa', '#6c5ce7', '#a29bfe', '#acf5ff', '#74b9ff', '#0984e3', '#006691', '#b2bec3', '#707070', '#000000']
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

        print('stations_dict[key]:',stations_dict[key].index)
    
    
    # plt.text(3, 4.5, 'This')

    #https://queirozf.com/entries/add-labels-and-text-to-matplotlib-plots-annotation-examples
    # for x, y in zip(traject['y'], traject['x']):
    #     station=traject['station'] 
    ax.annotate('station', # this is the text
        (52,6), # these are the coordinates to position the label
        textcoords="offset points", # how to position the text
        xytext=(0,15), # distance from text to points (x,y)
        ha='center',
        fontsize=10,
        bbox=dict(boxstyle="round", fc="w", alpha=0.5)) # horizontal alignment can be left



        
    # # #https://queirozf.com/entries/add-labels-and-text-to-matplotlib-plots-annotation-examples
    # for x,y in zip(stations_dict[key].y,stations_dict[key].x):
    #     stations=stations_dict[key].index
    #     a = set()
    #     for i in stations:
    #         # print(i)
    #         # if i in a:
    #         #     pass
    #         # else:
    #             ax.annotate(i, # this is the text
    #                 (x,y), # these are the coordinates to position the label
    #                 textcoords="offset points", # how to position the text
    #                 xytext=(0,15), # distance from text to points (x,y)
    #                 ha='center',
    #                 fontsize=10,
    #                 bbox=dict(boxstyle="round", fc="w", alpha=0.5)) # horizontal alignment can be left
    #             a.add(i)
                # print(i)
    
    # print(a)
    # print(stations_dict)

    
    #print(stations_dict)

    # Plek waarin lijnen geplot moeten worden
    ax.set_xlim(bbox[0], bbox[1])
    ax.set_ylim(bbox[2], bbox[3])
    
    ax.imshow(map, zorder=0, extent = bbox, aspect="auto") # kaart inladen order(onder boven)
    #fig.set_size_inches(10, 40, forward=True) #kaart formaat

    # show legend 
    ax.legend(loc=2, prop={'size': 15})
    
    plt.annotate('joi', (52, 4.7), fontsize=60)
    # plt.text(52, 4.7, 'This')
    # x = 5.0
    # y = 3.0
    # ax.annotate(stations_dict[key].index[0], x, y)

    plt.axis("off")
    plt.title("Holland Graph", fontsize=60)
    
    # fig.savefig(path / "data" / "holland_graph.png", bbox_inches="tight", dpi=350)
    fig.savefig(path / "data" / "Kaart_NL_grijs_graph.png", bbox_inches="tight", dpi=150)


# https://matplotlib.org/basemap/users/examples.html
# https://plotly.com/python/lines-on-maps/