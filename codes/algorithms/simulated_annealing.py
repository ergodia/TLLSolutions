import random
import copy


class Simulated_Annealing_Rail():
    def __init__(self, network, maximum_time):
        """
        Initialize the needed data.
        """

        self._best_network = copy.deepcopy(network)
        self._working_network = copy.deepcopy(network)
        self._accepted_network = copy.deepcopy(network)

    def run(self):
        """
        Runs the simulated annealing algortithm with the given information.
        """

        # choose the shortest traject
        traject_pointer = min(self._working_network.trajects_duration, key=self._working_network.trajects_duration.get)

        traject = self._working_network.trajects[traject_pointer]
        station_pointer = random.choice([traject[0], traject[-1]])

        # check in which trajects the station is also present
        station_pressence = [traject for traject in self._working_network.stations_traject 
                             if station_pointer in self._working_network.stations_traject[traject]]
        station_pressence.remove(traject_pointer)

        # choose a random traject from the trajact where the station is present
        new_traject = random.choice(station_pressence)

        # get the index number of the station_pointer in the new_traject
        index = self._working_network.trajects[new_traject].index(station_pointer)
        
        # rearrange the tracks and store the sliced_out portion and set it aside
        sliced_out = self.rearrange_tracks(traject, station_pointer, new_traject, index)
        self._working_network.trajects[traject_pointer].clear()

        print(sliced_out)

    def rearrange_tracks(self, traject, station_pointer, new_traject, index):
        """
        Rearranges the trajects. Chooces randomly between before or after a chosen traject.
        """
        
        # chooce between before or after the station
        side = random.choice(("before", "after"))

        if side == "before":
            # check if the traject is in the right orientation
            if traject[-1] != station_pointer:
                traject.reverse()
            
            # slice a bit out to make place for the new bit
            sliced_out = self._working_network.trajects[new_traject][:index + 1]
            
            # add the new bid to the traject
            self._working_network.trajects[new_traject] = traject + self._working_network.trajects[new_traject][index + 1:]
        else:
            # check if the traject is in the right orientation
            if traject[0] != station_pointer:
                traject.reverse()
            
            # slice a bit out to make place for the new bit
            sliced_out = self._working_network.trajects[new_traject][index:]
            
            # add the new bid to the traject
            self._working_network.trajects[new_traject] = self._working_network.trajects[new_traject][:index] + traject

        # check if the sliced out bit is only one station
        # this indicates a begin or end station and doesn't have to be stored
        # in that case return None

        if len(sliced_out) == 1:
            return None
        else:
            return sliced_out