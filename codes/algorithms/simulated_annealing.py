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

        # change the solution
        self.change_solution()


    def change_solution(self):
        """
        Changes the solution until no slices are left.
        """

        # choose the shortest traject TESTING
        original_traject_number = min(self._working_network.trajects_duration, key=self._working_network.trajects_duration.get)
        traject_to_implement = copy.deepcopy(self._working_network.trajects[original_traject_number])

        # get a traject where the original_traject can be implemented
        station_pointer, implement_traject = self.get_implement_traject(traject_to_implement, original_traject_number)

        # rearrange the tracks and store the sliced_out portion and set it aside
        sliced_out = self.rearrange_tracks(traject_to_implement, station_pointer, implement_traject)
        

        print(sliced_out)

    def get_implement_traject(self, traject_to_implement, original_traject_number):
        """
        Retrieves a traject where the given traject can be implemented.
        """

        # chooce the beginning or the end of the traject
        station_pointer = random.choice([traject_to_implement[0], traject_to_implement[-1]])

        # check in which trajects the station is also present
        station_pressence = [traject for traject in self._working_network.stations_traject 
                             if station_pointer in self._working_network.stations_traject[traject]]
        
        # remove the originaltraject from the list if that is given
        if original_traject_number:
            station_pressence.remove(original_traject_number)

        # choose a random traject from the trajact where the station is present
        implement_traject = random.choice(station_pressence)
      
        return station_pointer, implement_traject

    def rearrange_tracks(self, old_traject, station_pointer, implement_traject):
        """
        Rearranges the trajects. Chooces randomly between before or after a chosen traject.
        """
        
        # get the index number of the station_pointer in the implement_traject
        index = self._working_network.trajects[implement_traject].index(station_pointer)

        # chooce between before or after the station
        side = random.choice(("before", "after"))

        if side == "before":
            # check if the traject is in the right orientation
            if old_traject[-1] != station_pointer:
                old_traject.reverse()
            
            # slice a bit out to make place for the new bit
            sliced_out = self._working_network.trajects[implement_traject][:index + 1]
            
            # add the new bid to the traject
            self._working_network.trajects[implement_traject] = old_traject + self._working_network.trajects[implement_traject][index + 1:]
        else:
            # check if the traject is in the right orientation
            if old_traject[0] != station_pointer:
                old_traject.reverse()
            
            # slice a bit out to make place for the new bit
            sliced_out = self._working_network.trajects[implement_traject][index:]
            
            # add the new bid to the traject
            self._working_network.trajects[implement_traject] = self._working_network.trajects[implement_traject][:index] + old_traject

        # check if the sliced out bit is only one station
        # this indicates a begin or end station and doesn't have to be stored
        # in that case return None

        if len(sliced_out) == 1:
            return None
        else:
            return sliced_out
