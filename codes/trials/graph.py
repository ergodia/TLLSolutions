import matplotlib.pyplot as plt
import numpy as np


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

    fig, ax = plt.subplots(figsize=(32, 40))  

    for key in stations_dict:
        ax.plot(stations_dict[key].y, stations_dict[key].x, zorder=1, linewidth=6, marker="o",  markersize=20, label=key)

    #print(stations_dict['train 0'].index)

    # Plek waarin lijnen geplot moeten worden
    ax.set_xlim(bbox[0], bbox[1])
    ax.set_ylim(bbox[2], bbox[3])
    
    ax.imshow(map, zorder=0, extent = bbox, aspect="auto") # kaart inladen order(onder boven)
    #fig.set_size_inches(10, 40, forward=True) #kaart formaat

    # legenda weergave 
    # https://stackoverflow.com/questions/7125009/how-to-change-legend-size-with-matplotlib-pyplot
    ax.legend(loc=2, prop={'size': 30})


    plt.axis("off")
    plt.title("Holland Graph", fontsize=60)
    
    # fig.savefig(path / "data" / "holland_graph.png", bbox_inches="tight", dpi=350)
    fig.savefig(path / "data" / "Kaart_NL_grijs_graph.png", bbox_inches="tight", dpi=150)


# https://matplotlib.org/basemap/users/examples.html