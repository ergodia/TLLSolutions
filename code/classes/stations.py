"""
TLL Solutions
stations.py
"""

import pandas as pd
from pandas.core.frame import DataFrame


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
        
        read_data = pd.read_csv(input_csv)
        read_data = read_data.set_index("station")
        
        return read_data


    def data_from_stations(self, station_list: list) -> dict:
        """
        Returns a dictionary with the longitude and latitude for the stations in a given order.
        """

        # extract the data from the given stations
        station_data = self._stations.loc[station_list]     

        return station_data


    def bbox_limits(self):
        """
        Returns the bbox limits for the drawing of the graph.
        """

        return (self._stations.y.min(), self._stations.y.max(),      
         self._stations.x.min(), self._stations.x.max())


    def data(self):
        """
        Returns all the data in the dataframe.
        """
        
        return self._stations
