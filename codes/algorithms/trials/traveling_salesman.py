import copy
import random


class Traveling_Salesman():
    def __init__(self, graph, maximum_trajects, maximum_time):
        self._graph = copy.deepcopy(graph)
        self._stations = self._graph.stations
        self._maximum_trajects = maximum_trajects
        self._maximum_time = maximum_time
        self._already_visited = set()
        self._trajects = {}


    def run(self):
        """
        Runs the traveling salesman algortithm with the given information
        """
        
        # initialize the initial values for this algorithm
        total_traject_time = 0
        
        # create the needed amount of trajects
        for traject in range(self._maximum_trajects):
            # pick a random starting point from all the stations
            station_pointer = self.starting_point(self._stations)

            # if there is not suitable starting point anymore then stop the loop
            # because no suitable trajects can be made anymore
            if station_pointer == None:
                break

            # begin with the start of a new traject and add it to the already visited
            self._trajects[f"train {traject}"] = [station_pointer]
            self._already_visited.add(station_pointer)

            # create the connections of the traject
            while True:    
                # retrieve the closest station and the travel time 
                closest_station = self.closest_station(station_pointer)
                
                # check if the added travel time doesn't exceed the maximum traject time
                # if this is true then the traject is finished so we go to the next
                # herefore we need to set the total_traject_time back to 0
                # the same will be done if there isn't a suitable connection anymore
                if closest_station == None or total_traject_time + closest_station["travel_time"] > self._maximum_time:
                    total_traject_time = 0
                    break
                
                # add the station to the traject
                self.add_station(traject, closest_station["name"])

                # add the travel time to the total_traject_time
                total_traject_time += closest_station["travel_time"]
                
                # delete the previous station from the dict
                # and set the current pointer to the closest station
                del self._stations[station_pointer]
                station_pointer = closest_station["name"]

        # return the trajects
        return self._trajects


    def add_station(self, traject, station):
        """
        Adds a station to the given traject and already visited.
        """
        
        self._trajects[f"train {traject}"].append(station)
        self._already_visited.add(station)


    def starting_point(self, stations):
        """
        Pick a random starting point for a new traject
        if there are any connections available.
        """

        # pick a random starting point
        starting_point = random.choice(list(stations))

        # check if the station has connections to stations already visited
        self.check_visited(self._stations[starting_point].connections)

        # check if there are any connections available
        if self._stations[starting_point].connections:
            return starting_point

        # if there are no connections then return the first available station with connections
        for station in list(stations):
            if self._stations[station].connections:
                return station

        # return None if there are no suitable starting point
        return None


    def closest_station(self, station):
        """
        Returns the closest connected station of the current station and the travel time between them.
        """

        # retrieve all the connections of a station
        connections = self._stations[station].connections

        # check if there are any station connections that are already visited
        connections = self.check_visited(connections)

        # check if there are any available connections
        # if not return None, delete the station and pretend we already visited the station
        if not connections:
            del self._stations[station]
            self._already_visited.add(station)
            
            return None
        
        # retrieve the closest connected station
        closest_station = min(connections, key=connections.get)

        # retrieve the travel time between the two stations
        travel_time = connections[closest_station]

        return {"name": closest_station, "travel_time": travel_time}
 

    def check_visited(self, connections):
        """
        Checks if there are any connections to stations that already have been visted.
        Will delete any if this is true.
        """

        for connection in list(connections):
            if connection in self._already_visited:
                del connections[connection]

        return connections
