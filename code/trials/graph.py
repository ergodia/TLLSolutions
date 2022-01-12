import matplotlib.pyplot as plt


def holland_graph(path, stations):
    stations = stations

    data = stations.data()

    ruh_map = plt.imread(path / "data" / "holland.png")
    fig, ax = plt.subplots()

    BBox = (data.y.min(),   data.y.max(),      
         data.x.min(), data.x.max())

    ax.scatter(data.y, data.x, zorder=1, alpha= 0.2, c='b', s=30, linewidths=4)
    ax.set_xlim(BBox[0],BBox[1])
    ax.set_ylim(BBox[2],BBox[3])
    ax.imshow(ruh_map, zorder=0, extent = BBox, aspect= 'equal')

    plt.show()