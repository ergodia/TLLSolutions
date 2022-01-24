import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
import numpy as np
import plotly.graph_objects as go


# def holland_graph_1st(path, stations):
#     stations = stations

#     data = stations.data()

#     ruh_map = plt.imread(path / "data" / "holland.png")
#     fig, ax = plt.subplots()

#     BBox = (data.y.min(),   data.y.max(),      
#          data.x.min(), data.x.max())

#     ax.scatter(data.y, data.x, zorder=1, alpha= 0.2, c='b', s=30, linewidths=4)
#     ax.set_xlim(BBox[0],BBox[1])
#     ax.set_ylim(BBox[2],BBox[3])
#     ax.imshow(ruh_map, zorder=0, extent = BBox, aspect= 'equal')

#     plt.show()


def holland_graph(path, stations_dict: dict, bbox):
    # load the map into the graph
    # map = plt.imread(path / "data" / "holland.png")
    map = plt.imread(path / "data" / "Kaart_NL_grijs.png")

    fig, ax = plt.subplots(figsize=(17, 20))  

    # plot line and markers
    for key in stations_dict:
        ax.plot(stations_dict[key].y,
            stations_dict[key].x,
            zorder=1,
            linewidth=5,
            marker="o",
            markersize=17,
            markeredgewidth=4,
            markerfacecolor='w',
            label=key)

        print(stations_dict[key].index)
        
    #https://queirozf.com/entries/add-labels-and-text-to-matplotlib-plots-annotation-examples
    for x,y in zip(stations_dict[key].y,stations_dict[key].x):
        stations=stations_dict[key].index
        for i in stations:
            ax.annotate(i, # this is the text
                (x,y), # these are the coordinates to position the label
                textcoords="offset points", # how to position the text
                xytext=(0,15), # distance from text to points (x,y)
                ha='center',
                fontsize=10,
                bbox=dict(boxstyle="round", fc="w", alpha=0.5)) # horizontal alignment can be left

    #print(stations_dict[key].index)

    # Plek waarin lijnen geplot moeten worden
    ax.set_xlim(bbox[0], bbox[1])
    ax.set_ylim(bbox[2], bbox[3])
    
    ax.imshow(map, zorder=0, extent = bbox, aspect="auto") # kaart inladen order(onder boven)
    #fig.set_size_inches(10, 40, forward=True) #kaart formaat

    # show legend 
    ax.legend(loc=2, prop={'size': 30})
    
    # x = 5.0
    # y = 3.0
    # ax.annotate(stations_dict[key].index[0], x, y)

    plt.axis("off")
    plt.title("Holland Graph", fontsize=60)
    
    # fig.savefig(path / "data" / "holland_graph.png", bbox_inches="tight", dpi=350)
    fig.savefig(path / "data" / "Kaart_NL_grijs_graph.png", bbox_inches="tight", dpi=150)


# https://matplotlib.org/basemap/users/examples.html
# https://plotly.com/python/lines-on-maps/