import csv

class Network():
    def __init__(self, trajects_csv, stations):
        self.stations = stations
        self.score, self.trajects = self.load_trajects(trajects_csv)
        self.stations_traject = self.create_stations_set()
        self.trajects_length, self.trajects_duration = self.calc_length_duration()

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

    def calc_length_duration(self):
        """
        Calculates the length and duration of each traject for the given file.
        #### KAN ZIJN DAT TRAJECT LENGTH NIET GEBRUIKT WORDT, VERWIJDER DIT DAN!!! ####
        """

        traject_duration = {}
        traject_length = {}

        for traject in self.trajects:
            # calculate the length of each traject
            traject_length[traject] = len(self.trajects[traject])

            # calculate the duration of each traject
            for index in range(len(self.trajects[traject][:-1])):
                station1 = self.trajects[traject][index]
                station2 = self.trajects[traject][index + 1]

                if traject in traject_duration:
                    traject_duration[traject] += self.stations[station1].connections[station2]
                else:
                    traject_duration[traject] = self.stations[station1].connections[station2]

        # return the calculated values
        return traject_length, traject_duration

    def update(self):
        """
        Updates the stations_traject set, trajects_length and trajects_duration of the network
        """

        self.create_stations_set()
        self.calc_length_duration()
