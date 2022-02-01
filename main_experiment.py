from codes.analyze.simulated_annealing_dis import simulated_annealing_score, simulated_annealing_score_ot
from codes.analyze.traveling_salesman_dis import traveling_salesman_score

def main():
    # simulated_annealing_score(100, 100, 20)
    # simulated_annealing_score_ot(50000, 20)
    traveling_salesman_score(1000)

if __name__ == "__main__":
    main()