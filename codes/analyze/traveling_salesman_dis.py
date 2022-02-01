import os
import pandas as pd
import matplotlib.pyplot as plt
import collections
import seaborn as sns; sns.set_theme()

from ..algorithms.traveling_salesman_rail import Traveling_Salesman_Rail
from ..classes.graph import Graph
from ..calculations.line_quality import K, load_connections
from pathlib import Path
from progress.spinner import Spinner

PATH = Path(os.path.dirname(os.path.realpath(__file__))).parents[1]
sns.set_theme(style="whitegrid", palette="hls")


def traveling_salesman_score(iterations, datasheet):
    stations_file, connections_file = data_files(datasheet)
    score_connections = load_connections(connections_file)

    graph = Graph(stations_file, connections_file)
    
    scores = {}
    
    spinner = Spinner(f"Running Traveling Salesman {datasheet}")
    for iteration in range(iterations):
        trajects, check = Traveling_Salesman_Rail(graph, 20, 180).run()

        score = round(K(score_connections, trajects), 2)
        
        if score in scores:
            scores[score] += 1
        else:
            scores[score] = 1
        spinner.next()
    
    scores = dict(collections.OrderedDict(sorted(scores.items())))

    data = pd.Series(scores)
    ax = data.plot.bar(x="score", y="amount")
    plt.savefig(PATH / "data" / "experiment" / f"ts_{datasheet}", bbox_inches="tight", dpi=150)
    plt.close()

    return max(scores, key=scores.get)


def data_files(datasheet):
    """
    Returns the datafiles based on the datasheet needed.
    """
    
    if datasheet == "holland":
        return (PATH / "data" / "StationsHolland.csv", PATH / "data" / "ConnectiesHolland.csv")

    elif datasheet == "nationaal":
        return (PATH / "data" / "StationsNationaal.csv", PATH / "data" / "ConnectiesNationaal.csv")
    