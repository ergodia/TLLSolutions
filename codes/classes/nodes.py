class Stations():
    def __init__(self, name, longitude, latitude):
        self._name = name
        self._connections = {}
        self._coordinates = {
            "longitude": longitude,
            "latitude": latitude
        }
        self._number_connections = 0


    def add_connection(self, des_station, distance):
        """
        Adds a possible destination with the traveling time to the connections dictionary
        """

        self._connections[des_station] = distance

    
    def calc_num_connections(self):
        self._number_connections = len(self._connections)

    
    def __repr__(self):
        return f"{self._connections} - {self._number_connections}"
