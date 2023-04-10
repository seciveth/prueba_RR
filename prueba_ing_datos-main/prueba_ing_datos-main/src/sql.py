"""
THIS IS A FILE FOR HELPER SCRIPTS 
DO NOT ERASE
"""

import sqlite3
import pandas as pd


# database name
DB_NAME = "database/dataset.db"


# Create your connection.
connection = sqlite3.connect(DB_NAME)

def execute_query(query : str) -> pd.DataFrame:
    """
    Executes queries given the global scoped
    database name
    """
    cnx = connection
    return pd.read_sql_query(query, cnx)
