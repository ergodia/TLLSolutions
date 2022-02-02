"""
TTL Solutions
simualted_annealing_dis.py

Houses the two experiments for the simulated annealing algorithm.
simulated_annealing_score() gives the highest score over a couple of iterations and produces a barplot
with the frequencies of each score.

simulated_annealing_score_ot() produces a lineplot with all the scores of the accepted networks over time.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set_theme()

from ..algorithms.simulated_annealing import Simulated_Annealing_Rail
from ..classes.network import Network
from ..classes.graph import Graph
from ..calculations.line_quality import load_connections
from pathlib import Path


PATH = Path(os.path.dirname(os.path.realpath(__file__))).parents[1]
sns.set_theme(style="whitegrid", palette="hls")


def simulated_annealing_score(iterations, algorithm_iterations, temperature, datasheet, experiment):
    """
    Generates the highest score and graph over a couple of simulated annealing iterations.
    """

    # load the needed files and classes
    stations_file, connections_file, network_file = data_files(datasheet)
    score_connections = load_connections(connections_file)

    graph = Graph(stations_file, connections_file)
    base_network = Network(network_file, graph.stations)

    # define the max_traject and max_length based on the datasheet.
    if datasheet == "holland":
        max_traject = 7
        max_length = 120
    else:
        max_traject = 20
        max_length = 180

    scores = {}

    # go through the algorithm with the given iteration count
    for iteration in range(iterations):
        network, score = Simulated_Annealing_Rail(base_network, max_length, max_traject, algorithm_iterations, temperature, score_connections).run(False)

        # count the scores
        if score in scores:
            scores[score] += 1
        else:
            scores[score] = 1

    # create the graph
    data = pd.Series(scores)
    ax = data.plot.bar(x="score", y="amount")
    plt.savefig(PATH / "data" / "experiment" / experiment / f"sa_{datasheet}", bbox_inches="tight", dpi=150)
    plt.clf()

    return max(scores, key=scores.get)


def simulated_annealing_score_ot(algorithm_iterations, temperature, datasheet, experiment):
    """
    Runs the simulated annaealing algorithm 1 time and gives the accepted scores over time.
    """

    # load the needed files and classes
    stations_file, connections_file, network_file = data_files(datasheet)
    score_connections = load_connections(connections_file)

    graph = Graph(stations_file, connections_file)
    base_network = Network(network_file, graph.stations)

    # define the max_traject and max_length based on the datasheet.
    if datasheet == "holland":
        max_traject = 7
        max_length = 120
    else:
        max_traject = 20
        max_length = 180

    # calculate the scores over time with one iteration
    scores = Simulated_Annealing_Rail(base_network, max_length, max_traject, algorithm_iterations, temperature, score_connections).run(True)

    # create the graph
    data = pd.Series(scores)
    ax = data.plot.line(x="iteration", y="score")
    plt.savefig(PATH / "data" / "experiment" / experiment / f"sa_overtime_{datasheet}", bbox_inches="tight", dpi=150)
    plt.clf()


def data_files(datasheet):
    """
    Returns the datafiles based on the datasheet needed.
    """

    if datasheet == "holland":
        return (PATH / "data" / "StationsHolland.csv",
                PATH / "data" / "ConnectiesHolland.csv",
                PATH / "data" / "holland_output" / "output_TS_holland.csv")

    elif datasheet == "nationaal":
        return (PATH / "data" / "StationsNationaal.csv",
                PATH / "data" / "ConnectiesNationaal.csv",
                PATH / "data" / "nationaal_output" / "output_TS_nationaal.csv")
