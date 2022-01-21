import copy
from os import stat
import random


class Traveling_Salesman_Rail():
    def __init__(self, graph, maximum_trajects, maximum_time):
        """
        Initialize the needed data.
        """
        
        self._graph = copy.deepcopy(graph)
        self._all_stations = self._graph.stations
        self._maximum_trajects = maximum_trajects
        self._maximum_time = maximum_time
        self._connections, self._more_connections_allowed = self.load_stations_connections()
        self._already_visited = set()
        self._trajects = {}


    def load_stations_connections(self):
        """
        Defines a dictionary with the number of connections of all stations and
        defines a dictionary with stations that can be visted more than one time, where
        the number of times visted can be defined.
        """

        # retrieve the number of connections from all the stations
        connections = {station:self._all_stations[station].number_connections for station in self._all_stations}

        # create a dictionary with all the stations that can be visted more than ones
        # this will be the case if the number of connections is more or equal to 3
        # also set the number of visitations to 0 for later purposes
        more_connections_allowed = {station for station in connections if connections[station] >= 3}

        return connections, more_connections_allowed

    
    def run(self):
        """
        Runs the traveling salesman algortithm with the given information
        """

        # try to make the maximum amount of trajects from 1 to the maximum
        for traject in range(1, self._maximum_trajects + 1):
            # initialize the total_traject_time for this new traject
            total_traject_time = 0
            
            # starts the traject with a starting point
            start_station = self.starting_point()

            # add the starting station to the traject
            station_pointer = self.add_station_traject(traject, start_station)

            while True:
                # retrieve the station the train will go next
                next_station = self.next_station(station_pointer)
                
                # check if the connection can be made within the timelimit of the traject
                # or to a station at all
                if next_station == None or total_traject_time + next_station["travel_time"] > self._maximum_time:
                    # stop the traject
                    break

                # add the station to the traject
                station_pointer = self.add_station_traject(traject, next_station["name"])

                # calculate the total_traject_time
                total_traject_time = total_traject_time + next_station["travel_time"]

        # return all the trajects after completetion
        return self._trajects

    
    def starting_point(self):
        """
        Picks a starting point for a new traject.
        This starting point must have preferably only one available connection
        but will take a station with the lowest amount of connections.
        """

        # get the lowest amount of connections from the connections dict
        lowest_amount = min(self._connections.values())

        # create a set with all the stations with the lowest value
        possibilities = [station for station in self._connections 
                         if self._connections[station] == lowest_amount]

        # pick a random starting point from the list of possibilities
        starting_station = random.choice(possibilities)

        return starting_station


    def next_station(self, current_station):
        """
        Returns the next suitable connected station from the current 
        station and the travel time between them.
        """

        # retrieve all the connections from the current station
        connections = self._all_stations[current_station].connections

        # check if the connections are all suitable
        connections = self.check_suitable_connections(connections)

        # return the closest station if there is a connection possible
        if connections == None:
            return None
        else:
            # retrieve the connection with the lowest distance
            next_station = min(connections, key=connections.get)
            
            # return the needed information
            return {
                "name": next_station,
                "travel_time": connections[next_station]
            }


    def check_suitable_connections(self, connections):
        """
        Checks if a connection is suitable given the following requirements:
            1: The station is not already visited.
            2: If the station is already visited, then it must be checked if it
               can be visited multiple times. But if there is a station that is not
               yet visited then this station will not be used because there is an option
               that has not yet been used.
        """

        # create a list with not yet visisted station within the given connections
        not_visited = {connection:connections[connection] for connection in list(connections) if connection not in self._already_visited}

        # create a list of stations that can be vistited multiple times
        multi_visit = {connection:connections[connection] for connection in list(connections) 
                       if connection in self._more_connections_allowed}
        
        # return the not_visited dictionary when not empty
        if not_visited:
            return not_visited
        # return the list of multi_visit_stations if there are any
        elif multi_visit:
            return multi_visit
        # return None if there aren't any suitable stations anymore
        else:
            return None


    def add_station_traject(self, traject, des_station):
        """
        Adds the given station to the given traject and will execute
        the following mutations:
            1: Adds the station to the already visited set.
            2: Check if the station is in the list of station that can
               be visited multiple times. If yes then the station counter goes one up.
               If the station has surpassed his maximum then the station will be deleted.
        """

        # add the station to the traject
        if f"train {traject}" in self._trajects:
            self._trajects[f"train {traject}"].append(des_station)
        else:
            self._trajects[f"train {traject}"] = [des_station]

        # add the station to the already visited set
        self._already_visited.add(des_station)
     
        # retract one from the maximum of possible connections for that station
        self._connections[des_station] = self._connections[des_station] - 1
        
        # delete the station if the remaining connection count is equal to zero
        if self._connections[des_station] == 0:
            del self._connections[des_station]

            # if the station is also a multi visit station then delete it from there as well
            if des_station in self._more_connections_allowed:
                self._more_connections_allowed.remove(des_station)

        # return the des_station to set it as the next station pointer
        return des_station
