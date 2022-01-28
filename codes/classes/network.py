import csv
import copy
import random


class Network():
    def __init__(self, trajects_csv, stations):
        self.stations = stations
        self.score, self.trajects = self.load_trajects(trajects_csv)
        self.stations_traject = set()
        self.create_stations_set()
        self.trajects_duration = {}
        self.calc_init_length_duration()
        self.trajects_no_check = set()

    def load_trajects(self, trajects_csv):
        """
        Loads the trajects of a good solution with all the available connections
        into a dictionary with lists and sets from a csv file.
        """

        # read the csv file with the trajects
        with open(trajects_csv, "r") as file:
            reader = csv.DictReader(file)

            trajects = {row["train"]: list(row["stations"].strip("'[]'").split(", ")) for row in reader}

        # return the trajects, the initial score and the stations per trajects
        return float(trajects.pop("score")[0]), trajects

    def create_stations_set(self):
        self.stations_traject = {traject: set(self.trajects[traject]) for traject in self.trajects}

    def calc_init_length_duration(self):
        """
        Calculates the length and duration of each traject for the given file.
        """

        self.trajects_duration = {}

        for traject in self.trajects:
            self.calc_duration(traject, update=False)

    def update_stations_set(self, traject):
        """
        Updates a given traject in the stations_traject set.
        """

        self.stations_traject[traject] = set(self.trajects[traject])

    def calc_duration(self, traject, update):
        """
        Calculates the duration of a given traject.
        It purges the trajects set if Update is True which indicates that
        the traject needs to be updated.
        """

        # set the numbers back to 0 if they will be updated
        if update == True:
            self.trajects_duration[traject] = 0

        # calculate the duration of each traject
        for index in range(len(self.trajects[traject][:-1])):
            station1 = self.trajects[traject][index]
            station2 = self.trajects[traject][index + 1]

            if traject in self.trajects_duration:
                self.trajects_duration[traject] += self.stations[station1].connections[station2]
            else:
                self.trajects_duration[traject] = self.stations[station1].connections[station2]

    def make_traject_to_spec(self, maximum_traject_length):
        """
        Slices out a bit from the first traject which is to long from a 
        random side. It stores the new traject and returns the sliced out bit
        """

        # get the first traject which is too long
        traject_numbers = [traject for traject in self.trajects_duration 
                             if self.trajects_duration[traject] > maximum_traject_length]

        # return None if all trajects are to spec
        if not traject_numbers:
            return None, None

        # retrieve the first traject which is too long
        traject_number = traject_numbers[0]

        # copy the traject
        traject = copy.deepcopy(self.trajects[traject_number])

        # chooce between the front and back of the traject
        side = random.choice(("front", "back"))

        # reverse the traject if it needs to go from the back
        if side == "back":
            traject.reverse()

        # retrieve the end index for a suitable traject
        traject_duration = 0
        
        for index in range(len(traject[:-1])):
            station1 = traject[index]
            station2 = traject[index + 1]

            traject_duration += self.stations[station1].connections[station2]

            if traject_duration > maximum_traject_length:
                end_index = index

        # create the new traject
        self.trajects[traject_number] = traject[:end_index]

        # return the sliced out portion
        return traject[end_index:], traject_number
