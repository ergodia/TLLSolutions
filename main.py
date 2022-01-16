"""
TLL Solutions
main.py
"""

import os

from pathlib import Path
from codes.classes.connections import Connections
from codes.classes.stations import Stations
from codes.trials.graph import holland_graph
from codes.classes.graph import Graph


PATH = Path(os.path.dirname(os.path.realpath(__file__)))


def main():
    # TODO Moet misschien via een terminal ARGV worden gedaan zodat je daar kan aangeven welke bestanden moeten worden gebruikt. (Tim)
    #connections = Connections(PATH / "data" / "ConnectiesHolland.csv")
    stations = Stations(PATH / "data" / "StationsHolland.csv")

    # show of the holland graph
    #holland_graph(PATH, stations)

    # shapefile reader TESTER
    #shapfile_reader(PATH)

    # line graphs test
    data = {}
    data["train 1"] = stations.data_from_stations(["Alkmaar", "Schiphol Airport", "Gouda"])
    data["train 2"] = stations.data_from_stations(["Amsterdam Zuid", "Amsterdam Sloterdijk", "Haarlem", "Beverwijk"])

    holland_graph(PATH, data, stations.bbox_limits())

    print(Graph(PATH / "data" / "StationsHolland.csv", PATH / "data" / "ConnectiesHolland.csv"))


if __name__ == "__main__":
    main()
