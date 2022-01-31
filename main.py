"""
TLL Solutions
main.py
"""

import os
import pandas as pd

from pathlib import Path
from codes.classes.stations import Stations
<<<<<<< HEAD
from codes.load.graph import holland_graph
=======
from codes.trials.graph import holland_graph
from codes.trials.graph import holland_animation
>>>>>>> 27d2938c64c7dec09f8692dbcda6e18326df7010
from codes.classes.graph import Graph
from codes.calculations.line_quality import score_calculation
from codes.algorithms.traveling_salesman_rail import Traveling_Salesman_Rail


PATH = Path(os.path.dirname(os.path.realpath(__file__)))


def main():
    # load the stations for the creation of the graph
    stations = Stations(PATH / "data" / "StationsNationaal.csv")

    # load everything inside a graph
    graph = Graph(PATH / "data" / "StationsNationaal.csv", PATH / "data" / "ConnectiesNationaal.csv")

    # calculate trajects with the help of an algorithm
    check = False

    while check == False:
        trajects, check = Traveling_Salesman_Rail(graph, 20, 180).run()

    # create a graph of all the trajects
    data = {train:stations.data_from_stations(trajects[train]) for train in trajects}
    holland_graph(PATH, data, stations.bbox_limits())
    holland_animation(PATH, data, stations.bbox_limits())
    
    # calculate the quality of the trajects
    quality = score_calculation([trajects], PATH)
    
    # write the data to a csv file
    trajects = {traject:f"[{', '.join(trajects[traject])}]" for traject in trajects}
    
    output_data = pd.DataFrame.from_dict(trajects, orient="index")
    output_data.reset_index(level=0, inplace=True)
    output_data.columns = ["train", "stations"]
    output_data = output_data.append({"train":"score", "stations": quality["quality"][0]}, ignore_index=True)
    output_data.to_csv(PATH / "data" / "output_nat.csv", index=False)
    

if __name__ == "__main__":
    main()
