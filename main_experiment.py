"""
TLL Solutions
main_experiment.py

Runs experiments with all available combinations of the parameters an writes
the results to specific maps for each combination inside data/experiment.
"""

import os
import itertools
import time

from codes.analyze.simulated_annealing_dis import simulated_annealing_score, simulated_annealing_score_ot
from codes.analyze.traveling_salesman_dis import traveling_salesman_score
from pathlib import Path

PATH = Path(os.path.dirname(os.path.realpath(__file__)))


def main():
    # definition of the parameters
    all_combinations = get_all_combinations()

    # define all the dictionaries for the best score
    best_scores = {"holland SA max_score": 0, "nationaal SA max_score": 0, "holland TS max_score": 0, "nationaal TS max_score": 0}
    best_experiment = {"holland SA max_score": None, "nationaal SA max_score": None, "holland TS max_score": None, "nationaal TS max_score": None}

    for combination in all_combinations:
        # create the experiment name
        experiment = '-'.join((str(item) for item in combination))

        # create a map in the experiment folder if it doesn't exists
        path = PATH / "data" / "experiment" / experiment
        exists = os.path.exists(path)

        if not exists:
            os.makedirs(path)

        print(f"Running {experiment}")

        # unpack the tuple
        temperature, max_algorithm_iterations, sa_iterations, ts_iterations = combination

        # run the experiment
        max_scores = experiments(temperature, max_algorithm_iterations, sa_iterations, ts_iterations, experiment)

        # check if the score has been improved
        for score in max_scores:
            if max_scores[score] > best_scores[score]:
                best_scores[score] = max_scores[score]
                best_experiment[score] = experiment

    # write the best scores into a text file
    with open(PATH / "data" / "experiment" / "best_scores.txt", "w") as file:
        for key, value in best_scores.items():
            file.write(f"{key}: {value} / {best_experiment[score]}\n")


def get_all_combinations():
    """
    Returns the combination of all parameters in the experiment
    """

    temperature = [1, 10, 20, 100, 1000, 10000, 100000]
    max_algorithm_iterations = [10, 20, 30, 50, 100]
    sa_iterations = [1, 10, 100]
    ts_iterations = [10, 100, 1000]

    all_combinations = list(itertools.product(*[temperature, max_algorithm_iterations, sa_iterations, ts_iterations]))

    return all_combinations


def experiments(temperature, max_algorithm_iterations, sa_iterations, ts_iterations, experiment):
    """
    Executes one experiment with the defined parameters.
    """

    max_score = {}
    timings = {}
    datasheets = ["nationaal", "holland"]

    for datasheet in datasheets:
        # execute the simulated annealing algorithm
        sa_time_begin = time.time()
        max_score[f"{datasheet} SA max_score"] = simulated_annealing_score(sa_iterations, max_algorithm_iterations, temperature, datasheet, experiment)
        sa_time_end = time.time()

        simulated_annealing_score_ot(sa_iterations, temperature, datasheet, experiment)

        # calculate the traveling salesman algorithm
        ts_time_begin = time.time()
        max_score[f"{datasheet} TS max_score"] = traveling_salesman_score(ts_iterations, datasheet, experiment)
        ts_time_end = time.time()

        # calculate the timings of the algorithms
        timings[f"{datasheet} SA timing"] = sa_time_end - sa_time_begin
        timings[f"{datasheet} TS timing"] = ts_time_end - ts_time_begin

    # write the information to the text file
    with open(PATH / "data" / "experiment" / experiment / "scores.txt", "w") as file:
        for key, value in max_score.items():
            file.write(f"{key}: {value}\n")
        for key, value in timings.items():
            file.write(f"{key}: {value}\n")

    return max_score


if __name__ == "__main__":
    main()
