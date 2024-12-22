import pandas as pd
import matplotlib.pyplot as plt
from db_data_query import data_pull
from species_clean import rnm_cleaning


def plot_species_and_human_distribution(cleaned_rnm: pd.DataFrame) -> None:
    """
    Plots the distribution of species and human vs non-human data.

    This function creates a set of two pie charts:
    1. The first chart shows the distribution of species in the dataset.
    2. The second chart shows the distribution of 'is_human' values, 
       labeling them as 'Human' and 'Non-Human'.

    Args:
        cleaned_rnm (pd.DataFrame): A DataFrame containing the 'species' and 'is_human' columns.

    Returns:
        None: The function generates and displays two pie charts.
    """
    # Count the values in 'species' and 'is_human'
    species_counts = cleaned_rnm['species'].value_counts()
    is_human_counts = cleaned_rnm['is_human'].value_counts()

    # Define the subplots
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Plot for 'species' 
    axes[0].pie(species_counts, labels=species_counts.index, autopct='%1.1f%%', startangle=210,
                labeldistance=1.2)
    axes[0].set_title('Species Distribution')

    # Plot for 'is_human'
    axes[1].pie(is_human_counts, labels=is_human_counts.index.map({True: 'Human', False: 'Non-Human'}),
                autopct='%1.1f%%', startangle=90, labeldistance=1.1)
    axes[1].set_title('Human vs Non-Human')

    plt.tight_layout()
    plt.show()


def plot_species_breakdown(cleaned_rnm: pd.DataFrame) -> None:
    """
    Plots a bar chart showing the breakdown of species in the dataset.

    This function generates a bar chart of the species counts, highlighting the
    most popular species with a distinct color (green), while other species are
    shown in gray. It also adds data labels to the bars for better clarity.

    Args:
        cleaned_rnm (pd.DataFrame): A DataFrame containing the 'species' column.

    Returns:
        None: The function generates and displays a bar chart.
    """
    # Count the values in 'species'
    species_counts = cleaned_rnm['species'].value_counts()

    # Colors to highlight the most popular species
    colors = ['#00FF00' if i == 0 else '#808080' for i in range(len(species_counts))]

    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax = species_counts.plot.bar(color=colors, ax=ax, width=0.8)

    # Add data labels
    ax.bar_label(ax.containers[0])

    # Title and labels
    plt.title('Species Breakdown from Rick and Morty', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Species')
    plt.ylabel('Count')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()


def main():
    # Step 1: Pull the data
    rnm = data_pull()

    # Step 2: Clean the data
    cleaned_rnm = rnm_cleaning(rnm)

    # Step 3: Generate plots
    plot_species_and_human_distribution(cleaned_rnm)
    plot_species_breakdown(cleaned_rnm)


if __name__ == "__main__":
    main()
