import random
import copy
import math

from ..trials.line_quality import K
from progress.bar import Bar


class Simulated_Annealing_Rail():
    def __init__(self, network, maximum_track_time, maximum_trajects, iterations, start_temperature, connections):
        """
        Initialize the needed data.
        """

        self._best_network = copy.deepcopy(network)
        self._working_network = copy.deepcopy(network)
        self._accepted_network = copy.deepcopy(network)
        self._no_starting_traject = set()
        self._maximum_track_time = maximum_track_time
        self._maximum_trajects = maximum_trajects
        self._start_temperature = start_temperature
        self._current_temperature = start_temperature
        self._iterations = iterations
        self._all_connections = connections

    def run(self):
        """
        Runs the simulated annealing algortithm with the given information.
        """

        # start the bar progress bar
        bar = Bar("Progress Algortithm", max=self._iterations)

        # go through the given iterations
        for iteration in range(self._iterations):
            # change the solution
            self.change_solution()

            # check if the maximum_traject number is not exceeded
            # in that case just treat it as a worser case
            if len(self._working_network.trajects) > self._maximum_trajects:
                self._working_network = copy.deepcopy(self._accepted_network)
                self.update_temperature()

                # go to the next iteration
                bar.next()
                continue

            # update the score
            self.update_score()

            # reindex trajects
            self.reindex_trajects()

            # check the solution
            self.check_solution()

            # go to the next iteration
            bar.next()

        bar.finish()

        # return the best network
        return self._best_network.trajects, self._best_network.score

    def check_solution(self):
        """
        Checks and accepts better solutions than the current solution.
        """

        old_score = self._accepted_network.score
        new_score = self._working_network.score

        # calculate the probability of accepting the new network
        delta = old_score - new_score
    
        # check if the delta is equal to 0
        # this will be treated as a small deterioration so the delta will be equal to 1
        if delta == 0:
            delta = 1

        probability = math.exp(-delta / self._current_temperature)

        # check if the new network will be accepted on a random chance
        if random.random() < probability:
            self._accepted_network = copy.deepcopy(self._working_network)
        else:
            self._working_network = copy.deepcopy(self._accepted_network)

        # check if the accepted_network score is higher than the best network
        if self._accepted_network.score > self._best_network.score:
            self._best_network = copy.deepcopy(self._accepted_network)
        
        # update the temperature
        self.update_temperature()


    def update_score(self):
        """
        Updates the score of the working network.
        """

        self._working_network.score = K(self._all_connections, self._working_network.trajects)


    def update_temperature(self):
        """
        Updates the temperature which will define the chance that
        a solution will be accepted.
        """

        self._current_temperature = self._current_temperature - (self._start_temperature / self._iterations)

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

        # update all the traject information
        self._working_network.create_stations_set()
        self._working_network.calc_init_length_duration()

    def change_solution(self):
        """
        Changes the solution until we have a new solution.
        """

        # choose the shortest traject
        original_traject_number, traject_to_implement = self.get_starting_traject()

        # rearrange the tracks and store the sliced_out portion with its traject where it came from and set it aside
        sliced_out, original_traject_number = self.rearrange_tracks(original_traject_number, traject_to_implement)

        # keep rearranging until we don't have any sliced out bits anymore
        tries = 0

        self.process_slices(original_traject_number, sliced_out, tries)

        # retrieve a traject that is too long
        sliced_out, original_traject_number = self._working_network.make_traject_to_spec(self._maximum_track_time)

        # keep rearranging until the traject are all within time
        tries = 0

        self.trajects_in_time(original_traject_number, sliced_out, tries)

    def get_starting_traject(self):
        """
        Returns the starting traject for the beginning of the change solution.
        """
        
        starting_traject = min((traject for traject in self._working_network.trajects_duration 
                               if traject not in self._no_starting_traject), 
                               key=self._working_network.trajects_duration.get)
        traject_to_implement = copy.deepcopy(self._working_network.trajects[starting_traject])
        
        # clear the traject that will be used
        self._working_network.trajects[starting_traject].clear()

        # update the traject information
        self.update_traject(None, starting_traject)

        return starting_traject, traject_to_implement

    def process_slices(self, original_traject_number, sliced_out, tries):
        """
        Processes slices.
        This may be done for 100 times.
        """

        while sliced_out != None:
            sliced_out, original_traject_number = self.rearrange_tracks(original_traject_number, sliced_out)
            tries += 1

            if tries == 100:
                sliced_out = self.place_sliced_element(sliced_out)

    def trajects_in_time(self, original_traject_number, sliced_out, tries):
        """
        Makes sure that all trajects are within time.
        This may be done for 100 times.
        """
        
        while sliced_out != None:
            sliced_out, original_traject_number = self.rearrange_tracks(original_traject_number, sliced_out)
            tries += 1

            # place the sliced out traject in its own traject after 100 iterations
            if tries == 100:
                sliced_out = self.place_sliced_element(sliced_out)

            # check if there are more trajects not in time
            if sliced_out == None:
                sliced_out, original_traject_number = self._working_network.make_traject_to_spec(self._maximum_track_time)
                if sliced_out != None:
                    tries = 0

    def rearrange_tracks(self, original_traject_number, traject_to_implement):
        """
        Rearanges the tracks and return the bit, if any, that has been
        sliced out.
        """
        
        # get the station_pointer (station which will be the head) and implement_traject for the sliced_out bit
        station_pointer, implement_traject = self.get_implement_traject(traject_to_implement, original_traject_number)

        # check if the traject to be implemented can be implemented
        if station_pointer != None and implement_traject != None:
            traject_to_implement, original_traject_number = self.implement_trajects(traject_to_implement, original_traject_number, station_pointer, implement_traject)
        else:
            traject_to_implement = self.place_sliced_element(traject_to_implement)

        return traject_to_implement, original_traject_number

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

        # store the traject to implement in the empty traject
        self._working_network.trajects[empty_traject] = traject_to_implement

        # update the information
        self.update_traject(None, empty_traject)

        # put this element in the set with trajects that must not be a starting traject
        self._no_starting_traject.add(empty_traject)

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

    def get_implement_traject(self, traject_to_implement, original_traject_number):
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
            station_pressence = {traject for traject in self._working_network.stations_traject 
                                if station_pointer in self._working_network.stations_traject[traject]}
            
            # discard the original traject from the list
            station_pressence.discard(original_traject_number)

            # check if the station_pressence is empty and continue if so
            if not station_pressence:
                continue
            
            # choose a random traject from the trajact where the station is present
            implement_traject = random.choice(list(station_pressence))

            # discard the implement_traject from the no starting traject set because
            # it can used again since it has more connections
            self._no_starting_traject.discard(implement_traject)
      
            return station_pointer, implement_traject

        # return None if there is no suitable traject
        return None, None

    def implement_trajects(self, old_traject, original_traject_number, station_pointer, implement_traject):
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

        # update the trajects
        self.update_traject(original_traject_number, implement_traject)

        # check if the sliced out bit is only one station
        # this indicates a begin or end station and doesn't have to be stored
        # in that case return None
        # if this is not the case then return the sliced out bit with the traject where it came from

        if len(sliced_out) == 1:
            return None, None
        else:
            return sliced_out, implement_traject
