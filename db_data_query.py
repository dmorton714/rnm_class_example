import sqlite3
import pandas as pd


def data_pull() -> pd.DataFrame:
    """
    Pulls data from the 'episodes' table in the SQLite database and returns it as a pandas DataFrame.

    The function performs the following steps:
    1. Connects to the SQLite database.
    2. Executes a SQL query to select all data from the 'episodes' table.
    3. Closes the database connection.

    Returns:
        pd.DataFrame: The data from the 'episodes' table.
    """
    # Connect to the database
    conn: sqlite3.Connection = sqlite3.connect('../rnm.db')

    # Execute the query
    query: str = "SELECT * FROM episodes"
    rnm: pd.DataFrame = pd.read_sql_query(query, conn)

    # Close the connection
    conn.close()

    # Return the DataFrame
    return rnm


def main():
    # Call data_pull and return the DataFrame
    rnm = data_pull()

    # Print the DataFrame inside the main function
    print(rnm)

    # Return the DataFrame (optional if you want to use it further)
    return rnm


if __name__ == "__main__":
    rnm = main()
