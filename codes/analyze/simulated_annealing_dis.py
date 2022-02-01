import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set_theme()

from ..algorithms.simulated_annealing import Simulated_Annealing_Rail
from ..classes.network import Network
from ..classes.graph import Graph
from ..calculations.line_quality import K, load_connections
from pathlib import Path
from progress.spinner import Spinner


PATH = Path(os.path.dirname(os.path.realpath(__file__))).parents[1]
sns.set_theme(style="whitegrid", palette="hls")


def simulated_annealing_score(iterations, algorithm_iterations, temperature, datasheet):
    stations_file, connections_file, network_file = data_files(datasheet)
    score_connections = load_connections(connections_file)

    graph = Graph(stations_file, connections_file)
    base_network = Network(network_file, graph.stations)

    scores = {}
        
    spinner = Spinner('Running')
    for iteration in range(iterations):
        network, score = Simulated_Annealing_Rail(base_network, 180, 20, algorithm_iterations, temperature, score_connections).run(False)

        if score in scores:
            scores[score] += 1
        else:
            scores[score] = 1
        spinner.next()

    
    data = pd.Series(scores)
    ax = data.plot.bar(x="score", y="amount")
    plt.savefig(PATH / "data" / "experiment" / f"sa_{datasheet}", bbox_inches="tight", dpi=150)
    plt.close()

    return max(scores, key=scores.get)


def simulated_annealing_score_ot(algorithm_iterations, temperature, datasheet):
    """
    Runs the simulated annaealing algorithm 1 time and gives the accepted scores over time.
    """

    stations_file, connections_file, network_file = data_files(datasheet)
    score_connections = load_connections(connections_file)

    graph = Graph(stations_file, connections_file)
    base_network = Network(network_file, graph.stations)

    scores = Simulated_Annealing_Rail(base_network, 180, 20, algorithm_iterations, temperature, score_connections).run(True)

    data = pd.Series(scores)

    ax = data.plot.line(x="iteration", y="score")
    plt.savefig(PATH / "data" / "experiment" / f"sa_overtime_{datasheet}", bbox_inches="tight", dpi=150)
    plt.close()


def data_files(datasheet):
    """
    Returns the datafiles based on the datasheet needed.
    """
    
    if datasheet == "holland":
        return (PATH / "data" / "StationsHolland.csv", PATH / "data" / "ConnectiesHolland.csv", PATH / "data" / "output_hol.csv")

    elif datasheet == "nationaal":
        return (PATH / "data" / "StationsNationaal.csv", PATH / "data" / "ConnectiesNationaal.csv", PATH / "data" / "output_nat.csv")
