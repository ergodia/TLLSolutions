"""
TLL Solutions
main.py
"""

import os
import pandas as pd

from pathlib import Path
from codes.classes.stations import Stations
from codes.trials.graph import holland_graph
from codes.classes.graph import Graph
from codes.trials.line_quality import score_calculation
from codes.algorithms.traveling_salesman_rail import Traveling_Salesman_Rail
from codes.algorithms.trials.traveling_salesman import Traveling_Salesman


PATH = Path(os.path.dirname(os.path.realpath(__file__)))


def main():
    # load the stations for the creation of the graph
    stations = Stations(PATH / "data" / "StationsHolland.csv")

    # load everything inside a graph
    graph = Graph(PATH / "data" / "StationsHolland.csv", PATH / "data" / "ConnectiesHolland.csv")

    # calculate trajects with the help of an algorithm
    check = False

    while check == False:
        trajects, check = Traveling_Salesman(graph, 7, 120).run()

    # create a graph of all the trajects
    data = {train:stations.data_from_stations(trajects[train]) for train in trajects}
    holland_graph(PATH, data, stations.bbox_limits())
    
    # calculate the quality of the trajects
    quality = score_calculation([trajects], PATH)
    
    # write the data to a csv file
    trajects = {traject:f"[{', '.join(trajects[traject])}]" for traject in trajects}
    
    output_data = pd.DataFrame.from_dict(trajects, orient="index")
    output_data.reset_index(level=0, inplace=True)
    output_data.columns = ["train", "stations"]
    output_data = output_data.append({"train":"score", "stations": quality["quality"][0]}, ignore_index=True)
    output_data.to_csv(PATH / "data" / "output_baseline.csv", index=False)
    

if __name__ == "__main__":
    main()
