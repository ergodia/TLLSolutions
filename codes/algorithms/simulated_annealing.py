from operator import index
import random
import copy


class Simulated_Annealing_Rail():
    def __init__(self, network, maximum_track_time, maximum_trajects, iterations):
        """
        Initialize the needed data.
        """

        self._best_network = copy.deepcopy(network)
        self._working_network = copy.deepcopy(network)
        self._accepted_network = copy.deepcopy(network)
        self._maximum_track_time = maximum_track_time
        self._maximum_trajects = maximum_trajects

    def run(self):
        """
        Runs the simulated annealing algortithm with the given information.
        """

        # change the solution
        self.change_solution()

        # check if the maximum_traject number is not exceeded
        # if len(self._working_network.trajects) > self._maximum_trajects:
        #     self._working_network = copy.deepcopy(self._accepted_network)
        #     continue

        # reindex trajects
        self.reindex_trajects()

        return self._working_network.trajects

    def reindex_trajects(self):
        """
        Deletes empty trajects and reindexes the trajects.
        """

        # get the empty trajects
        empty_trajects = [traject for traject in self._working_network.trajects
                          if not self._working_network.trajects[traject]]

        # delete the empty trajects
        for traject in empty_trajects:
            del self._working_network.trajects[traject]

        # reindex the trajects
        self._working_network.trajects = {f"train {(index + 1)}" :self._working_network.trajects[traject]
                                          for index, traject in enumerate(self._working_network.trajects)}

        # update the traject information
        self._working_network.create_stations_set()
        self._working_network.calc_init_length_duration()

    def change_solution(self):
        """
        Changes the solution until we have a new solution.
        """

        # choose the shortest traject TESTING
        original_traject_number = min(self._working_network.trajects_duration, key=self._working_network.trajects_duration.get)
        traject_to_implement = copy.deepcopy(self._working_network.trajects[original_traject_number])

        # rearrange the tracks and store the sliced_out portion and set it aside
        sliced_out = self.rearrange_tracks(original_traject_number, traject_to_implement, full_traject=True)
        original_traject_number = None

        # keep rearranging until we don't have any sliced out bits anymore
        tries = 0

        self.process_slices(original_traject_number, sliced_out, tries)

        # retrieve a traject that is too long
        sliced_out, original_traject_number = self._working_network.make_traject_to_spec(self._maximum_track_time)

        # keep rearranging until the traject are all within time
        tries = 0

        self.trajects_in_time(original_traject_number, sliced_out, tries)

    def process_slices(self, original_traject_number, sliced_out, tries):
        """
        Processes slices.
        This may be done for 100 times.
        """

        while sliced_out != None:
            sliced_out = self.rearrange_tracks(original_traject_number, sliced_out, full_traject=False)
            tries += 1

            if tries == 100:
                sliced_out = self.place_sliced_element(sliced_out)

    def trajects_in_time(self, original_traject_number, sliced_out, tries):
        """
        Makes sure that all trajects are within time.
        This may be done for 100 times.
        """
        
        while sliced_out != None:
            sliced_out = self.rearrange_tracks(original_traject_number, sliced_out, full_traject=False)
            original_traject_number = None
            tries += 1

            # place the sliced out traject in its own traject after 100 iterations
            if tries == 100:
                sliced_out = self.place_sliced_element(sliced_out)

            # check if there are more trajects not in time
            if sliced_out == None:
                sliced_out, original_traject_number = self._working_network.make_traject_to_spec(self._maximum_track_time)

    def rearrange_tracks(self, original_traject_number, traject_to_implement, full_traject):
        """
        Rearanges the tracks and return the bit, if any, that has been
        sliced out.
        """
        
        # get the station_pointer (station which will be the head) and implement_traject (traject where the ) for the sliced_out bit
        station_pointer, implement_traject = self.get_implement_traject(traject_to_implement, original_traject_number, full_traject)
        
        # remove the implement_traject from the traject_no_check since it could be used again
        self._working_network.trajects_no_check.discard(implement_traject)

        # check if the traject to be implemented can be implemented
        if station_pointer != None and implement_traject != None:
            traject_to_implement = self.implement_trajects(traject_to_implement, station_pointer, implement_traject)
            
            # update the information
            self.update_traject(original_traject_number, implement_traject)
        else:
            traject_to_implement = self.place_sliced_element(traject_to_implement)

        return traject_to_implement

    def place_sliced_element(self, traject_to_implement):
        """
        Places sliced element in an empty traject.
        """
        
        # retrieve the first best empty traject
        empty_trajects = [traject for traject in self._working_network.trajects 
                          if self._working_network.trajects[traject] == []]

        if not empty_trajects:
            empty_traject = f"train {(len(self._working_network.trajects)) + 1}"
        else:
            empty_traject = empty_trajects[0]

        # store the traject to implement in the empty traject an set it inside the trajects which can't be implemented
        self._working_network.trajects[empty_traject] = traject_to_implement
        self._working_network.trajects_no_check.add(empty_traject)

        # update the information
        self.update_traject(None, empty_traject)

        # set traject_to_implement to None
        traject_to_implement = None
        
        return traject_to_implement

    def update_traject(self, original_traject_number, implement_traject):
        """
        Updates the given trajects information.
        """
        
        # clear the original traject if this is used and update the traject_duration/length and stations_set
        if original_traject_number != None:
            self._working_network.update_stations_set(original_traject_number)
            self._working_network.calc_duration(original_traject_number, update=True)
        
        # update the traject_duration/length and update the stations_set of the implement traject
        self._working_network.update_stations_set(implement_traject)
        self._working_network.calc_duration(implement_traject, update=True)

    def get_implement_traject(self, traject_to_implement, original_traject_number, full_traject):
        """
        Retrieves a traject where the given traject can be implemented.
        """
        
        # get the tracks where the station_pointer is present
        # if not found then take a look at the other side
        # choose which side will be searched first by choosing to reverse the list or not
        to_reverse = random.choice([True, False])
        
        # 0 means the beginning of the traject and -1 the end of the traject
        sides = [0, -1]

        # reverse the list if to_reverse is True
        if to_reverse is True:
            sides.reverse()

        for side in sides:
            # get the station at a side
            station_pointer = traject_to_implement[side]
            
            # check in which trajects the station is also present
            station_pressence = [traject for traject in self._working_network.stations_traject 
                                if station_pointer in self._working_network.stations_traject[traject]]
            
            # remove the originaltraject from the list if that is given
            if original_traject_number:
                station_pressence.remove(original_traject_number)

            # check if the station_pressence is empty and continue if so
            if not station_pressence:
                continue
            
            # choose a random traject from the trajact where the station is present
            implement_traject = random.choice(station_pressence)

            # clear the original traject if this is used
            if original_traject_number != None and full_traject == True:
                self._working_network.trajects[original_traject_number].clear()
      
            return station_pointer, implement_traject

        # return None if there is no suitable traject
        return None, None

    def implement_trajects(self, old_traject, station_pointer, implement_traject):
        """
        Implements trajects in other trajects. 
        Chooces randomly between before or after a chosen traject.
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
            left_over = self._working_network.trajects[implement_traject][index + 1:]
            
            # add the new bid to the traject
            self._working_network.trajects[implement_traject] = old_traject + left_over
        else:
            # check if the traject is in the right orientation
            if old_traject[0] != station_pointer:
                old_traject.reverse()
            
            # slice a bit out to make place for the new bit
            sliced_out = self._working_network.trajects[implement_traject][index:]
            left_over = self._working_network.trajects[implement_traject][:index]
            
            # add the new bid to the traject
            self._working_network.trajects[implement_traject] = left_over + old_traject

        # check if the sliced out bit is only one station
        # this indicates a begin or end station and doesn't have to be stored
        # in that case return None

        if len(sliced_out) == 1:
            return None
        else:
            return sliced_out
