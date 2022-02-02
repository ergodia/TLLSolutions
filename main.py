"""
TLL Solutions
main.py
"""

import os
import argparse
import pandas as pd
import copy

from pathlib import Path
from progress.bar import Bar
from codes.help_classes.network import Network
from codes.help_classes.stations import Stations
from codes.help_classes.graph import Graph
from codes.calculations.line_quality import score_calculation, K, load_connections
from codes.help_functions.visualise_graph import holland_graph
from codes.help_classes.graph import Graph
from codes.calculations.line_quality import score_calculation
from codes.algorithms.traveling_salesman_rail import Traveling_Salesman_Rail
from codes.algorithms.simulated_annealing import Simulated_Annealing_Rail


PATH = Path(os.path.dirname(os.path.realpath(__file__)))
SCORE_CONNECTIONS = load_connections(PATH / "data" / "ConnectiesNationaal.csv")


def main(algorithm, datasheet, max_trajects, max_length, iterations):
    stations_file, connections_file, network_file, output = load_data(datasheet)

    # load the stations for the creation of the graph
    stations = Stations(stations_file)

    # load everything inside a graph
    graph = Graph(stations_file, connections_file)
    
    # load everything in a network
    network = Network(network_file, graph.stations)

    # calculate trajects with the help of an algorithm
    if algorithm == "TS":
        trajects = traveling_salesman(graph, max_trajects, max_length, iterations)
    elif algorithm == "SA":
        trajects = simulated_annealing(network, max_trajects, max_length, 5000, 200, iterations)
    else:
        print("No suitable algorithm given, please state TS: Traveling Salesman or SA: Simulated Annealing")
        exit()

    # create a graph of all the trajects
    data = {train:stations.data_from_stations(trajects[train]) for train in trajects}
    holland_graph(PATH, data, stations.bbox_limits(), output, algorithm)
    
    # calculate the quality of the trajects
    quality = score_calculation([trajects], PATH, connections_file)
    
    # write the data to a csv file
    trajects = {traject:f"[{', '.join(trajects[traject])}]" for traject in trajects}
    
    output_csv = output / f"output_{algorithm}_{datasheet}.csv"
    output_data = pd.DataFrame.from_dict(trajects, orient="index")
    output_data.reset_index(level=0, inplace=True)
    output_data.columns = ["train", "stations"]
    output_data = output_data.append({"train":"score", "stations": quality["quality"][0]}, ignore_index=True)
    output_data.to_csv(output_csv, index=False)


def load_data(datasheet):
    """
    Loads the data from the datasheet in the needed classes.
    """

    if datasheet == "holland":
        return (PATH / "data" / "StationsHolland.csv", 
                PATH / "data" / "ConnectiesHolland.csv", 
                PATH / "data" / "holland_output" / "output_TS_holland.csv",
                PATH / "data" / "holland_output")

    elif datasheet == "nationaal":
        return (PATH / "data" / "StationsNationaal.csv", 
                PATH / "data" / "ConnectiesNationaal.csv", 
                PATH / "data" / "nationaal_output" / "output_TS_nationaal.csv",
                PATH / "data" / "nationaal_output")


def traveling_salesman(graph, max_trajects, max_length, iterations):
    """
    Runs the traveling_salesman algorithm an amount of times and will return the best score.
    """
    
    best_score = 0 
    
    # start the bar progress bar
    bar = Bar("Progress Traveling_Salesman", max=iterations)

    # run the algorithm for an amount of iterations and only save the best network
    for iteration in range(iterations):
        trajects, check = Traveling_Salesman_Rail(graph, max_trajects, max_length).run()

        # if the solution is not correct then just continue
        if check == False:
            # go to the next iteration
            bar.next()
            continue

        # calculate score for the network
        score = K(SCORE_CONNECTIONS, trajects)

        # save the network if the score is higher
        if score > best_score:
            best_network = copy.deepcopy(trajects)
            best_score = score
        
        # go to the next iteration
        bar.next()

    bar.finish()
        
    return best_network


def simulated_annealing(network, max_trajects, max_length, max_algorithm_iterations, temperature, iterations):
    """
    Runs the Simulated_Annealing algorithm an amount of times and will return the best score.
    """

    best_score = 0
    base_network = copy.deepcopy(network)
    
    # start the bar progress bar
    bar = Bar("Progress Simulated Annealing", max=iterations)

    # run the algorithm for an amount of iterations and only save the best network
    for iteration in range(iterations):
        network, score = Simulated_Annealing_Rail(base_network, max_length, max_trajects, max_algorithm_iterations, temperature, SCORE_CONNECTIONS).run(False)

        # save the network if the score is higher
        if score > best_score:
            best_network = copy.deepcopy(network)
            best_score = score
        
        # go to the next iteration
        bar.next()

    bar.finish()
        
    return best_network


if __name__ == "__main__":
    # Set-up parsing command line arguments
    parser = argparse.ArgumentParser(description = "Run different algorithms for the RAILNL problem")

    # Adding arguments
    parser.add_argument("-a", "--algorithm", type=str, default = "TS", help="Algorithm TS = Traveling Salesman, SA = Simulated Annealing")
    parser.add_argument("-d", "--datasheet", type=str, default = "nationaal", help="Dataset (holland/nationaal)")
    parser.add_argument("-tra", "--max_trajects", type=int, default = 20, help="Max Trajects")
    parser.add_argument("-len", "--max_length", type=int, default = 180, help="Max Length of each traject")
    parser.add_argument("-i", "--iterations", type=int, default = 5000, help="Amount of iterations to run the algorithm")
    
    # Read arguments from command line
    args = parser.parse_args()

    # Run main with provide arguments
    main(args.algorithm, args.datasheet, args.max_trajects, args.max_length, args.iterations)
