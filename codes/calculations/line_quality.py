"""
line_quality.py

- reads CSV file
- calculates the quality of the lines
"""

import pandas as pd
import matplotlib.pyplot as plt

def score_calculation(trajects, path, connection_file):
    connections = load_connections(connection_file)
    
    # create list to store dictionaries that contain possibility and quality
    dataframe_rows = []
    for traject in range(len(trajects)):    
        dataframe_rows.append({ 'possibility': (traject+1), 'quality': K(connections, trajects[traject]) })
        
    # create dataframe out of list with dictionaries and create barplot, save this barplot in barplot.png to look at data
    dataframe = pd.DataFrame(dataframe_rows)
    dataframe.plot.bar(x='possibility', y = 'quality', title="barplot quality per trainline possibility")
    plt.xticks(rotation='horizontal')
    plt.savefig(path / "data" / "barplot.png")
    
    return dataframe
    
        
def load_connections(file):
    connections = []

    with open(file) as cns_file:
        lines = cns_file.readlines()
        for line in lines:
            line = line.split(',')
            line_tuple = tuple(line)
            connections.append(line_tuple)

    # remove header in connections csv from list
    connections.pop(0)
    
    return connections

# K = p*10000 - (T*100 + Min): quality of train trajects
# The higher the score, the better!
# p is fraction of used connections, T is the total amount of trajects
# Min is the total duration (in minutes) of the trajects together
def K(connections, trajects):
    return p(connections, trajects)*10000 - (T(trajects)*100 + Min(connections, trajects))


def p(connections: list([str, str, int]), trajects: dict):
    count = 0
    
    for connection in connections:
        if connection_in_trajects(connection, trajects):
            count = count + 1
    
    total = len(connections)
    return count / total


def connection_in_trajects(connection: list([str, str, int]), trajects: dict):
    for traject in trajects.values():
        for i in range(len(traject)-1):
            if connection_equals_traject_part(connection, traject, i):
                return True
    return False
             

def Min(connections: list([str, str, int]), trajects: dict):
    total_minutes = 0
    
    for traject in trajects.values():
        for i in range(len(traject)-1):
            for connection in connections:
                if connection_equals_traject_part(connection, traject, i):
                    total_minutes = total_minutes + float(connection[2].strip())
    return total_minutes


def connection_equals_traject_part(connection, traject, i):
    return (traject[i] == connection[0] and traject[i+1] == connection[1]) or (traject[i] == connection[1] and traject[i+1] == connection[0])


def T(trajects:dict):
    return len(trajects)




        