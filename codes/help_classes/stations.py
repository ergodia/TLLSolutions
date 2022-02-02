"""
TLL Solutions
stations.py
"""

import pandas as pd


class Stations():
    """
    Loads the stations for integration into a network graph. 
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

    def data_from_stations(self, station_list: list) -> pd.DataFrame:
        """
        Returns a Dataframe with the longitude and latitude for the stations in a given order.
        """

        # extract the data from the given stations
        station_data = self._stations.loc[station_list]     

        return station_data

    def bbox_limits(self):
        """
        Returns the bbox limits for the drawing of the graph.
        """
        
        return ((3.000), (7.500), (50.500), (54.000))

    def data(self):
        """
        Returns all the data in the dataframe.
        """
        
        return self._stations