import csv

class Network():
    def __init__(self, trajects_csv, stations):
        self.stations = stations
        self.score, self.trajects = self.load_trajects(trajects_csv)
        self.stations_traject = self.create_stations_set()
        self.trajects_length = {}
        self.trajects_duration = {}
        self.calc_init_length_duration()

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
        return {traject: set(self.trajects[traject]) for traject in self.trajects}

    def calc_init_length_duration(self):
        """
        Calculates the length and duration of each traject for the given file.
        #### KAN ZIJN DAT TRAJECT LENGTH NIET GEBRUIKT WORDT, VERWIJDER DIT DAN!!! ####
        """

        for traject in self.trajects:
            self.calc_length_duration(traject, update=False)

    def update_stations_set(self, traject):
        """
        Updates a given traject in the stations_traject set.
        """

        self.stations_traject[traject] = set(self.trajects[traject])

    def calc_length_duration(self, traject, update):
        """
        Calculates the length and duration of a given traject.
        It purges the trajects set if Update is True which indicates that
        the traject needs to be updated.
        """

        if update == True:
            self.trajects_length[traject].clear()
            self.trajects_duration[traject].clear()

        # calculate the length of each traject
        self.trajects_length[traject] = len(self.trajects[traject])

        # calculate the duration of each traject
        for index in range(len(self.trajects[traject][:-1])):
            station1 = self.trajects[traject][index]
            station2 = self.trajects[traject][index + 1]

            if traject in self.trajects_duration:
                self.trajects_duration[traject] += self.stations[station1].connections[station2]
            else:
                self.trajects_duration[traject] = self.stations[station1].connections[station2]
