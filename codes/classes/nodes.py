class Stations():
    def __init__(self, name, longitude, latitude):
        self._name = name
        self._connections = {}
        self._coordinates = {
            "longitude": longitude,
            "latitude": latitude
        }


    def add_connection(self, des_station, distance):
        """
        Adds a possible destination with the traveling time to the connections dictionary
        """

        self._coordinates[des_station] = distance

    
    def __str__(self):
        return f"{self._name} - {self._connections}"
