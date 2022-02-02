"""
TLL Solutions
visualize_graph.py

Uses a given network to create a visual graph with all the trajects
on a Dutch map.
"""

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()


def holland_graph(path, stations_dict: dict, bbox, output, algorithm):
    """
    Visualizes the map of the Netherlands and plots trajects.
    """

    # load the map into the graph
    map = plt.imread(path / "data" / "background_graph.png")

    # set size of plot
    fig, ax = plt.subplots(figsize=(17, 20))
    ax.set_xlim(bbox[0], bbox[1])
    ax.set_ylim(bbox[2], bbox[3])

    # load colors from color palette and choose different colors
    line_colors = sns.color_palette("hls", 20)
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
                markerfacecolor='#9B9B9B',
                label=key)

    # show map and legend
    ax.imshow(map, zorder=0, extent=bbox, aspect="auto")
    ax.legend(loc=2, prop={'size': 15}, fancybox=True, framealpha=0.5)

    # plot image without axes
    plt.axis("off")

    # save image
    fig.savefig(path / "data" / output / f"graph_{algorithm}.png", bbox_inches="tight", dpi=150, transparent=True)
