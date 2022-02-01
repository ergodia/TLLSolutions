
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns; sns.set_theme()


def holland_graph(path, stations_dict: dict, bbox):
    # load the map into the graph
    map = plt.imread(path / "data" / "Kaart_NL_donkergrijs.png")

    fig, ax = plt.subplots(figsize=(17, 20))  
    ax.set_xlim(bbox[0], bbox[1])
    ax.set_ylim(bbox[2], bbox[3])

    # load colors from seaborn color palette
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
     
    ax.imshow(map, zorder=0, extent = bbox, aspect="auto") # kaart inladen order(onder boven)
    ax.legend(loc=2, prop={'size': 15}, fancybox=True, framealpha=0.5)
    
    plt.axis("off")
    # plt.title("Holland Graph", fontsize=60)
    
    # fig.savefig(path / "data" / "holland_graph.png", bbox_inches="tight", dpi=350)
    fig.savefig(path / "data" / "Kaart_NL_grijs_graph.png", bbox_inches="tight", dpi=150, transparent=True)

# def fun(i):
#     y = np.sin(i)
#     return y
 


# def holland_animation(path, stations_dict: dict, bbox):
#     map = plt.imread(path / "data" / "Kaart_NL_grijs.png")

#     fig, ax = plt.subplots(figsize=(17, 20))  
#     camera = Camera(fig)

#     ax.set_xlim(bbox[0], bbox[1])
#     ax.set_ylim(bbox[2], bbox[3])

#     # load colors from seaborn color palette
#     line_colors = sns.color_palette("husl", 20)
#     colors = iter(line_colors)
    
    
#     # ax.imshow(map, zorder=0, extent = bbox, aspect="auto") # kaart inladen order(onder boven)
   
#          # plot line and markers
#     for key in stations_dict:
#         ax.plot(stations_dict[key].y,
#             stations_dict[key].x,
#             zorder=1,
#             linewidth=5,
#             color=next(colors),
#             marker="o",
#             markersize=12,
#             markeredgewidth=4,
#             markerfacecolor='w',
#             label=key,
#             )
#         ax.imshow(map, zorder=0, extent = bbox, aspect="auto") # kaart inladen order(onder boven)
        
#         camera.snap()
    
#     animation = camera.animate(interval = 600, repeat = True)
  
    # # HTML(animation.to_html5_video)

    # # f = path / "data" / "Animatie_graph.mp4"
    # # writervideo = animation.FFMpegWriter(fps=60) 
    # # animation.save(f, writer=writervideo, bbox_inches="tight")

    # # animation.save(path / "data" / "Animatie_graph.mp4", bbox_inches="tight")
    
    # ax.legend(loc=2, prop={'size': 15})
    
    # plt.axis("off")
    # # plt.title("Holland Graph", fontsize=60)
    # plt.show()
    
    # # fig.savefig(path / "data" / "holland_graph.png", bbox_inches="tight", dpi=350)
    # # fig.savefig(path / "data" / "Animatie_graph.png", bbox_inches="tight", dpi=150, transparent=True)

   