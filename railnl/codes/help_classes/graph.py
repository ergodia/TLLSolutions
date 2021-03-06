"""
TLL Solutions
graph.py

- Graph class.
- Loads stations (see nodes.py) and connections into a graph.
- Calculates the number of connections per station.
"""

import csv
from .nodes import Stations


class Graph():
    def __init__(self, stations_csv, connections_csv):
        self.stations = self.load_stations(stations_csv)
        self.load_connections(connections_csv)
        self.calc_num_connections()

    def load_stations(self, stations_csv):
        """
        Loads all the stations in the csv file.
        """

        with open(stations_csv, "r") as file:
            reader = csv.DictReader(file)

            return {row["station"]: Stations(row["station"], row["y"], row["x"]) for row in reader}

    def load_connections(self, connections_csv):
        """
        Loads all the possible connections from the csv file with the connections.
        """

        with open(connections_csv, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                # add the connection to each node
                self.stations[row["station1"]].add_connection(row["station2"], float(row["distance"]))
                self.stations[row["station2"]].add_connection(row["station1"], float(row["distance"]))

    def calc_num_connections(self):
        """
        Calculates the number of connections for each station.
        """

        for station in self.stations:
            self.stations[station].calc_num_connections()

    def __str__(self):
        return f"{self.stations}"
