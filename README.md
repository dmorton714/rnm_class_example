# Rick and Morty Species Data Analysis
This project loads, cleans, and visualizes data related to species distribution and human vs non-human distribution from the Rick and Morty API. It performs the following key tasks:

- Loads the data either from a CSV file or by fetching it from the Rick and Morty API.
- creates a database 
- Cleans the data by removing unnecessary columns and adding relevant attributes.
- Generates two types of visualizations:
    - A pie chart of species distribution and human vs non-human distribution.
    - A bar chart showing the breakdown of species, highlighting the most popular species.

![Diagram]("images/rnm.pdf")

### Clone the repository:

```bash
git clone https://github.com/dmorton714/rnm_class_example.git
```
Navigate into the project directory:

```bash
cd rnm_class_example
```

## Create a virtual environment:

#### Virtual Environment Commands

| Command | Linux/Mac | GitBash |
| ------- | --------- | ------- |
| Create | `python3 -m venv venv` | `python -m venv venv` |
| Activate | `source venv/bin/activate` | `source venv/Scripts/activate` |
| Install | `pip install -r requirements.txt` | `pip install -r requirements.txt` |
| Deactivate | `deactivate` | `deactivate` |


## Usage

- Run api_call.py 
- Run db_builder.py
- Then you can run any of the other files. 
- presentation.ipynb shows results with code abstracted away
- dashboard_rnm.py is a web dashboard with our data 
