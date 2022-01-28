"""
TLL Solutions
main_hc_tester.py

This python file will essentially be used to test the "hill climber"
algorithm for the RAILNL problem
"""

import os
import pandas as pd

from pathlib import Path
from codes.trials.line_quality import score_calculation
from codes.classes.graph import Graph
from codes.classes.network import Network
from codes.algorithms.simulated_annealing import Simulated_Annealing_Rail


PATH = Path(os.path.dirname(os.path.realpath(__file__)))


def main():
    graph = Graph(PATH / "data" / "StationsHolland.csv", PATH / "data" / "ConnectiesHolland.csv")
    trajects = Network(PATH / "data" / "Holland_Output" / "output.csv", graph.stations)
    
    trajects = Simulated_Annealing_Rail(trajects, 120, 7, 500).run()

    # calculate the quality of the trajects
    quality = score_calculation([trajects], PATH)
    
    # write the data to a csv file
    trajects = {traject:f"[{', '.join(trajects[traject])}]" for traject in trajects}

    output_data = pd.DataFrame.from_dict(trajects, orient="index")
    output_data.reset_index(level=0, inplace=True)
    output_data.columns = ["train", "stations"]
    output_data = output_data.append({"train":"score", "stations": quality["quality"][0]}, ignore_index=True)
    output_data.to_csv(PATH / "data" / "output_hc_2.csv", index=False)


if __name__ == "__main__":
    main()