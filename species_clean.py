import sqlite3
import pandas as pd
import os
from db_data_query import data_pull


def rnm_cleaning(rnm: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the 'rnm' DataFrame by:
    1. Dropping unnecessary columns: 'type', 'origin', 'location', 'image', 'episode', and 'url'.
    2. Converting the 'created' column to a datetime format.
    3. Adding a new boolean column 'is_human' based on the 'species' column.

    Args:
        rnm (pd.DataFrame): The input DataFrame to be cleaned.

    Returns:
        pd.DataFrame: The cleaned DataFrame with dropped columns, converted 'created' column,
                      and the added 'is_human' column.
    """
    cols_to_drop = ['type', 'origin', 'location', 'image', 'episode', 'url']
    rnm = rnm.drop(columns=cols_to_drop)

    rnm['created'] = pd.to_datetime(rnm['created']).dt.date
    rnm['created'] = pd.to_datetime(rnm['created'])

    rnm['is_human'] = rnm['species'] == 'Human'
    return rnm


def main():
    # Fetch the data
    rnm = data_pull()

    # Clean the data
    rnm_cleaned = rnm_cleaning(rnm)

    # Print the cleaned DataFrame
    print(rnm_cleaned)

    # Return the cleaned DataFrame
    return rnm_cleaned


if __name__ == "__main__":
    # Run the script and get the cleaned DataFrame
    rnm_cleaned = main()
