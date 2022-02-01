import os
import pandas as pd
import matplotlib.pyplot as plt
import collections

from ..algorithms.traveling_salesman_rail import Traveling_Salesman_Rail
from ..classes.graph import Graph
from ..calculations.line_quality import K, load_connections
from pathlib import Path
from progress.spinner import Spinner

PATH = Path(os.path.dirname(os.path.realpath(__file__))).parents[1]
SCORE_CONNECTIONS = load_connections(PATH / "data" / "ConnectiesNationaal.csv")

def traveling_salesman_score(iterations):
    graph = Graph(PATH / "data" / "StationsNationaal.csv", PATH / "data" / "ConnectiesNationaal.csv")
    
    scores = {}
    
    spinner = Spinner('Running')
    for iteration in range(iterations):
        trajects, check = Traveling_Salesman_Rail(graph, 20, 180).run()

        score = round(K(SCORE_CONNECTIONS, trajects), 2)
        
        if score in scores:
            scores[score] += 1
        else:
            scores[score] = 1
        spinner.next()
    
    scores = dict(collections.OrderedDict(sorted(scores.items())))

    data = pd.Series(scores)
    ax = data.plot.bar(x="score", y="amount")
    plt.show()
    
    