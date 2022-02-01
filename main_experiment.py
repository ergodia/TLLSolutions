<<<<<<< HEAD
from codes.analyze.simulated_annealing_dis import simulated_annealing_score, simulated_annealing_score_ot

def main():
    # simulated_annealing_score(100, 100, 20)
    simulated_annealing_score_ot(50000, 20)
=======
from codes.analyze.simulated_annealing_dis import simulated_annealing_score
from codes.analyze.traveling_salesman_dis import traveling_salesman_score

def main():
    simulated_annealing_score(100, 100, 20)
    traveling_salesman_score(100, 100, 20)
>>>>>>> cc8f35113e6a2dd4b9ea71bfa85d0218b2c36023

if __name__ == "__main__":
    main()