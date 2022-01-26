import copy
import csv


class Hill_Climber_Rail():
    def __init__(self, stations, trajects, maximum_time):
        """
        Initialize the needed data.
        """

        self._stations = stations
        self._init_score, self._trajects = self.load_trajects(trajects)


    def load_trajects(self, trajects):
        """
        Loads the trajects of a good solution with all the available connections
        into a dictionary from a csv file.
        """

        # read the csv file with the trajects
        with open(trajects, "r") as file:
            reader = csv.DictReader(file)

            trajects = {row["train"]: list(row["stations"].strip("'[]'").split(", ")) for row in reader}

        # return the trajects and the initial score
        return float(trajects.pop("score")[0]), trajects
