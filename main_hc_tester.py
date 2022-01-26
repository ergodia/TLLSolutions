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
from codes.algorithms.rail_hill_climber import Hill_Climber_Rail


PATH = Path(os.path.dirname(os.path.realpath(__file__)))


def main():
    graph = Graph(PATH / "data" / "StationsHolland.csv", PATH / "data" / "ConnectiesHolland.csv")
    
    Hill_Climber_Rail(graph.stations, PATH / "data" / "Holland_Output" / "output.csv", 120)


if __name__ == "__main__":
    main()