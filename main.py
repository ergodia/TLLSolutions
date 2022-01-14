"""
TLL Solutions
main.py
"""

# add the paths to the different python files used for this script
import os, sys

from pathlib import Path

PATH = Path(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(os.path.join(PATH, "code"))
sys.path.append(os.path.join(PATH, "code", "classes"))
sys.path.append(os.path.join(PATH, "code", "trials"))


# import of the needed fuctions
from connections import Connections
from stations import Stations
from graph import holland_graph


def main():
    # TODO Moet misschien via een terminal ARGV worden gedaan zodat je daar kan aangeven welke bestanden moeten worden gebruikt. (Tim)
    connections = Connections(PATH / "data" / "ConnectiesHolland.csv")
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


if __name__ == "__main__":
    main()
