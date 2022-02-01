from codes.analyze.simulated_annealing_dis import simulated_annealing_score
from codes.analyze.traveling_salesman_dis import traveling_salesman_score

def main():
    simulated_annealing_score(100, 100, 20)
    traveling_salesman_score(100, 100, 20)

if __name__ == "__main__":
    main()