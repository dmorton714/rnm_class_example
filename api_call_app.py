import pandas as pd
import requests
import os


def load_or_fetch_data(csv_file_path: str, api_url: str) -> pd.DataFrame:
    """
    Load data from a CSV file if it exists. If the file does not exist, 
    fetch data from an API, save it to the CSV file, and return it as a DataFrame.

    Args:
        csv_file_path (str): The path to the CSV file.
        api_url (str): The base URL of the API to fetch data from.

    Returns:
        pd.DataFrame: The data loaded from the CSV or fetched from the API.
    """
    if os.path.exists(csv_file_path):
        print(f"CSV file '{csv_file_path}' found. Loading data from CSV.")
        return pd.read_csv(csv_file_path)
    else:
        print(f"CSV file '{csv_file_path}' not found. Fetching data from API.")

        results = []
        page = 1

        while True:
            response = requests.get(f'{api_url}?page={page}')
            data = response.json()

            if 'results' in data and len(data['results']) > 0:
                results.extend(data['results'])
                page += 1
            else:
                break

        if not os.path.exists(os.path.dirname(csv_file_path)):
            os.makedirs(os.path.dirname(csv_file_path))

        df = pd.DataFrame(results)
        df.to_csv(csv_file_path, index=False)
        print(f"Data fetched and saved to '{csv_file_path}'.")
        return df


def main():
    load_or_fetch_data()
    return


if __name__ == "__main__":
    # File path and API endpoint
    csv_path = "rick_n_morty_prod/data/rick_n_morty.csv"
    api_endpoint = "https://rickandmortyapi.com/api/character"

    # Load or fetch the data (assumes a function exists to either read from a CSV or fetch from an API)
    load_or_fetch_data(csv_path, api_endpoint)
