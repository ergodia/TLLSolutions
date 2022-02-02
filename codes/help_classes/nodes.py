"""
nodes.py

- stations class
- adds connections
- calculates the number of connections
"""
class Stations():
    def __init__(self, name, longitude, latitude):
        self._name = name
        self.connections = {}
        self._coordinates = {
            "longitude": longitude,
            "latitude": latitude
        }
        self.number_connections = 0


    def add_connection(self, des_station, distance):
        """
        Adds a possible destination with the traveling time to the connections dictionary
        """

        self.connections[des_station] = distance

    
    def calc_num_connections(self):
        """
        Calculates the number of connections for the station.
        """
        
        self.number_connections = len(self.connections)

    
    def __repr__(self):
        return f"{self.connections} - {self.number_connections}"
