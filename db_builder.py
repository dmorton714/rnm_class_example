import pandas as pd
import sqlite3
from api_call_app import load_or_fetch_data


def building_db() -> None:
    """
    Builds a SQLite database by importing data from a CSV file and storing it into a table.

    The function performs the following steps:
    1. Loads data from a specified CSV file or fetches it from an API if the file does not exist.
    2. Reads the data into a pandas DataFrame.
    3. Creates a SQLite database and saves the data to a table named 'episodes'.

    Returns:
        None
    """
    csv_path: str = "rick_n_morty_prod/data/rick_n_morty.csv"
    api_endpoint: str = "https://rickandmortyapi.com/api/character"

    # Load or fetch the data (assumes a function exists to either read from a CSV or fetch from an API)
    load_or_fetch_data(csv_path, api_endpoint)

    # Importing our data
    db: pd.DataFrame = pd.read_csv(csv_path)

    # Converting db DataFrame to rnm.db
    conn: sqlite3.Connection = sqlite3.connect('rick_n_morty_prod/rnm.db')

    # Saving DataFrame to a table named 'episodes'
    db.to_sql('episodes', conn, if_exists='replace', index=False)

    # Close the connection
    conn.close()
    return


def main():
    building_db()
    return


if __name__ == "__main__":
    main()
