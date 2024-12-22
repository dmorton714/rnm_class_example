import pandas as pd
import matplotlib.pyplot as plt
from db_data_query import data_pull
from species_clean import rnm_cleaning
import dash
from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go

# Read and clean data
rnm = data_pull()
cleaned_rnm = rnm_cleaning(rnm)

# Create Dash app
app = dash.Dash(__name__)

# Function to create species distribution pie chart
def create_species_distribution_plot(cleaned_rnm):
    species_counts = cleaned_rnm['species'].value_counts()
    fig = px.pie(
        names=species_counts.index,
        values=species_counts.values,
        title="Species Distribution",
        hole=0.3,
    )
    return fig

# Function to create human vs non-human pie chart
def create_human_vs_nonhuman_plot(cleaned_rnm):
    is_human_counts = cleaned_rnm['is_human'].value_counts()
    labels = is_human_counts.index.map({True: 'Human', False: 'Non-Human'})
    fig = px.pie(
        names=labels,
        values=is_human_counts.values,
        title="Human vs Non-Human",
        hole=0.3,
    )
    return fig

# Function to create species breakdown bar chart
def create_species_breakdown_bar_chart(cleaned_rnm):
    species_counts = cleaned_rnm['species'].value_counts()
    colors = ['#00FF00' if i == 0 else '#808080' for i in range(len(species_counts))]
    fig = px.bar(
        x=species_counts.index,
        y=species_counts.values,
        labels={'x': 'Species', 'y': 'Count'},
        title="Species Breakdown from Rick and Morty",
    )
    fig.update_traces(marker_color=colors)
    fig.update_layout(xaxis_tickangle=-45)
    return fig

# Create Dash layout
app.layout = html.Div([
    html.H1("Rick and Morty Dashboard", style={'textAlign': 'center'}),

    html.Div([
        html.P("Important info on the plots we want to talk about."),
        dcc.Graph(id='species-distribution', figure=create_species_distribution_plot(cleaned_rnm)),
        html.P("More important info on the plots we want to talk about."),
        dcc.Graph(id='human-vs-nonhuman', figure=create_human_vs_nonhuman_plot(cleaned_rnm)),
        dcc.Graph(id='species-breakdown', figure=create_species_breakdown_bar_chart(cleaned_rnm)),
    ], style={'width': '80%', 'margin': '0 auto'}),
])

if __name__ == "__main__":
    app.run_server(debug=True)
