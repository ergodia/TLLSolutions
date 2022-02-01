import os
import pandas as pd

from codes.analyze.simulated_annealing_dis import simulated_annealing_score, simulated_annealing_score_ot
from codes.analyze.traveling_salesman_dis import traveling_salesman_score
from pathlib import Path

PATH = Path(os.path.dirname(os.path.realpath(__file__)))

def main():
    max_score = {}
    datasheets = ["nationaal", "holland"]
  
    for datasheet in datasheets:
        max_score[f"{datasheet} SA max_score"] = simulated_annealing_score(100, 100, 20, datasheet)
        simulated_annealing_score_ot(5000, 20, datasheet)
        max_score[f"{datasheet} TS max_score"] = traveling_salesman_score(1000, datasheet)

    with open(PATH / "data" / "experiment" / "scores.txt", "w") as file:
        for key, value in max_score.items():
            file.write(f"{key}: {value}\n")

if __name__ == "__main__":
    main()