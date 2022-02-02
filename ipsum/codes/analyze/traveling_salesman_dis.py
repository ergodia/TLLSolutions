"""
TTL Solutions
simualted_annealing_dis.py

Houses the experiment for the traveling salesman algorithm.
It goes through the algorithm an amount of times and will return the
highest score and a bar plot with the frequency of all the scores observed.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import collections
import seaborn as sns; sns.set_theme()

from ..algorithms.traveling_salesman_rail import Traveling_Salesman_Rail
from ..help_classes.graph import Graph
from ..calculations.line_quality import K, load_connections
from pathlib import Path
from progress.spinner import Spinner

PATH = Path(os.path.dirname(os.path.realpath(__file__))).parents[1]
sns.set_theme(style="whitegrid", palette="hls")


def traveling_salesman_score(iterations, datasheet, experiment):
    # load the needed files and classes
    stations_file, connections_file = data_files(datasheet)
    score_connections = load_connections(connections_file)

    graph = Graph(stations_file, connections_file)

    # define the max_traject and max_length based on the datasheet
    if datasheet == "holland":
        max_traject = 7
        max_length = 120
    else:
        max_traject = 20
        max_length = 180

    # go through the algorithm with the given iteration count
    scores = {}

    spinner = Spinner(f"Running Traveling Salesman {datasheet}")
    for iteration in range(iterations):
        trajects, check = Traveling_Salesman_Rail(graph, max_traject, max_length).run()

        score = round(K(score_connections, trajects), 2)

        if score in scores:
            scores[score] += 1
        else:
            scores[score] = 1
        spinner.next()

    # order all the scores from small to large
    scores = dict(collections.OrderedDict(sorted(scores.items())))

    # create the graph
    data = pd.Series(scores)
    ax = data.plot.bar(x="score", y="amount")
    plt.savefig(PATH / "data" / "experiment" / experiment / f"ts_{datasheet}", bbox_inches="tight", dpi=150)
    plt.clf()

    return max(scores, key=scores.get)


def data_files(datasheet):
    """
    Returns the datafiles based on the datasheet needed.
    """

    if datasheet == "holland":
        return (PATH / "data" / "StationsHolland.csv",
                PATH / "data" / "ConnectiesHolland.csv")

    elif datasheet == "nationaal":
        return (PATH / "data" / "StationsNationaal.csv",
                PATH / "data" / "ConnectiesNationaal.csv")
