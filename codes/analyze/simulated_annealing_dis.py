import os
import pandas as pd
import matplotlib.pyplot as plt

from ..algorithms.simulated_annealing import Simulated_Annealing_Rail
from ..classes.network import Network
from ..classes.graph import Graph
from ..calculations.line_quality import K, load_connections
from pathlib import Path
from progress.spinner import Spinner


PATH = Path(os.path.dirname(os.path.realpath(__file__))).parents[1]
SCORE_CONNECTIONS = load_connections(PATH / "data" / "ConnectiesNationaal.csv")

def simulated_annealing_score(iterations, algorithm_iterations, temperature):
    graph = Graph(PATH / "data" / "StationsNationaal.csv", PATH / "data" / "ConnectiesNationaal.csv")
    base_network = Network(PATH / "data" / "output_nat.csv", graph.stations)

    scores = {}

        
    spinner = Spinner('Running')
    for iteration in range(iterations):
        network, score = Simulated_Annealing_Rail(base_network, 180, 20, algorithm_iterations, temperature, SCORE_CONNECTIONS).run(False)

        if score in scores:
            scores[score] += 1
        else:
            scores[score] = 1
        spinner.next()

    
    data = pd.Series(scores)
    ax = data.plot.bar(x="score", y="amount")
    plt.show()


def simulated_annealing_score_ot(algorithm_iterations, temperature):
    graph = Graph(PATH / "data" / "StationsNationaal.csv", PATH / "data" / "ConnectiesNationaal.csv")
    base_network = Network(PATH / "data" / "output_nat.csv", graph.stations)

    scores = Simulated_Annealing_Rail(base_network, 180, 20, algorithm_iterations, temperature, SCORE_CONNECTIONS).run(True)

    data = pd.Series(scores)

    ax = data.plot.line(x="iteration", y="score")
    plt.show()