"""
TLL Solutions
main_hc_tester.py

This python file will essentially be used to test the "hill climber"
algorithm for the RAILNL problem
"""

import os

from pathlib import Path
from codes.trials.line_quality import score_calculation
from codes.classes.graph import Graph
from codes.classes.network import Network
from codes.algorithms.simulated_annealing import Simulated_Annealing_Rail


PATH = Path(os.path.dirname(os.path.realpath(__file__)))


def main():
    graph = Graph(PATH / "data" / "StationsHolland.csv", PATH / "data" / "ConnectiesHolland.csv")
    trajects = Network(PATH / "data" / "Holland_Output" / "output.csv", graph.stations)
    Simulated_Annealing_Rail(trajects, 120).run()


if __name__ == "__main__":
    main()