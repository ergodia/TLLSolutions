"""
TLL Solutions
stations.py
"""

import pandas as pd


class Stations():
    """
    
    """
    
    def __init__(self, input_csv):
        """
        Load the needed variable onto initialization. 
        """
        
        self._stations = self.load_stations(input_csv)

    
    def load_stations(self, input_csv):
        """
        The stations csv file will be loaded here into a dataframe.
        """
        
        return pd.read_csv(input_csv)

    
    def data(self):
        """
        Returns all the data in the dataframe.
        """
        
        return self._stations
