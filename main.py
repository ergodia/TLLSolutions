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


# import of the needed fuctions
from connections import Connections
from stations import Stations


def main():
    # TODO Moet misschien via een terminal ARGV worden gedaan zodat je daar kan aangeven welke bestanden moeten worden gebruikt. (Tim)
    connections = Connections(PATH / "data" / "ConnectiesHolland.csv")
    stations = Stations(PATH / "data" / "StationsHolland.csv")

    # Test print code Wordt later verwijderd (Tim)
    print(connections.data())
    print(stations.data())


if __name__ == "__main__":
    main()