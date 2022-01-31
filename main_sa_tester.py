"""
TLL Solutions
main_hc_tester.py

This python file will essentially be used to test the "hill climber"
algorithm for the RAILNL problem
"""

import os
import pandas as pd

from pathlib import Path
from codes.calculations.line_quality import score_calculation, load_connections
from codes.classes.graph import Graph
from codes.classes.network import Network
from codes.algorithms.simulated_annealing import Simulated_Annealing_Rail


PATH = Path(os.path.dirname(os.path.realpath(__file__)))


def main():
    graph = Graph(PATH / "data" / "StationsNationaal.csv", PATH / "data" / "ConnectiesNationaal.csv")
    trajects = Network(PATH / "data" / "output_nat.csv", graph.stations)
    connections = load_connections(PATH / "data" / "ConnectiesNationaal.csv")
    
    trajects = Simulated_Annealing_Rail(trajects, 180, 20, 100000, 3000, connections).run()

    # calculate the quality of the trajects
    quality = score_calculation([trajects], PATH)
    
    # write the data to a csv file
    trajects = {traject:f"[{', '.join(trajects[traject])}]" for traject in trajects}

    output_data = pd.DataFrame.from_dict(trajects, orient="index")
    output_data.reset_index(level=0, inplace=True)
    output_data.columns = ["train", "stations"]
    output_data = output_data.append({"train":"score", "stations": quality["quality"][0]}, ignore_index=True)
    output_data.to_csv(PATH / "data" / "output_hc_5.csv", index=False)


if __name__ == "__main__":
    main()