"""
TLL Solutions
connections.py
"""

import pandas as pd


class Connections():
    """
    
    """
    
    def __init__(self, input_csv):
        """
        Load the needed variable onto initialization. 
        """
        
        self._connections = self.load_connections(input_csv)

    
    def load_connections(self, input_csv):
        """
        The stations csv file will be loaded here into a dataframe.
        """
        
        return pd.read_csv(input_csv)

    
    def data(self):
        """
        Returns all the data in the dataframe.
        """
        
        return self._connections
