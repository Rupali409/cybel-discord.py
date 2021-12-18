""" helper function to Database """
import pandas as pd
import datetime

from src.utils.db import DataBase, create_connection
from src.utils.utils import DATABASE_URL

connection, cursor = create_connection(DATABASE_URL)
db = DataBase(connection, cursor)


# FIX: create class here
class DBHelper:

    """
    Helper functions for the database
    
    methods:
        - create_report - create a report of a user in the database
        - get_report_csv - get a report of a user from the database
    """

    def __init__(self) -> None:
        pass


    def create_report(self, *args):
        """ Create a user report in the database 
        
        Arguments:
            args {list} -- list of columns to be inserted
        """
        db.insert_data("report_status", *args)


    def get_report_csv(self, condition):
        """ Get a user report from the database 
        
        Arguments:
            columns {list} -- list of columns to be selected
            condition {str} -- condition to be applied
        """
        results = db.select_data("report_status", condition)

        df = pd.DataFrame(results, columns=['timestamp_UTC', 'channel_id', 'reported_user', 'reported_by', 'reported_to', 'reason'])
        df["timestamp_UTC"] = df["timestamp_UTC"].apply(lambda x: datetime.datetime.fromtimestamp(x))
        return_df = df[['timestamp_UTC', 'reported_user', 'reported_by', 'reason']]
        return return_df

    
    def get_report_count(self, condition):
        """ Get the number of reports in the database 
        
        Arguments:
            condition {str} -- condition to be applied
        """
        counts = db.count_data("report_status", condition)
        return counts[0][0]


    def delete_user_report(self, condition):
        """ Delete a user report from the database 
        
        Arguments:
            condition {str} -- condition to be applied
        """
        db.delete_data("report_status", condition)
