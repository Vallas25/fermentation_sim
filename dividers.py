from dash import Dash, dcc, html, Input, Output, State
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from START_VALUES import *

fed_batch_panel = html.Div([
    html.Label("Fedbatch?"),
    dcc.Checklist(options=[
        {'label': 'Fed-Batch Mode', 'value': 'fedbatch_on'}
    ],
    value=[],
    id="fedbatch"),
    html.Div([
        html.Label("initial volume"),
        dcc.Input(type="number", id="initial_volume"),
    ],
    style={
        "display": "flex",
        "flexDirection": "column",
    }
    ),
    html.Label("feed rate (l/min)"),
    dcc.Slider(
        id="feed_rate",
        min=0,
        max=30,
        step=1,
        value=15
    ),
    html.Label("Substrate concentration (g/l)"),
    dcc.Slider(
        id="fedbatch_concentration",
        min=0,
        max=30,
        step=1,
        value=substrate_start
    )
])

controls_panel = html.Div([
        html.Label("Run time (min)"),
        dcc.Slider(id="run_time",
                   min=10,
                   max=1000,
                   step=1,
                   value=max_time),
        
        html.Label("initial biomass (OD)"),
        dcc.Slider(id="biomass",
                   min=0,
                   max=1,
                   step=0.01,
                   value=biomass_start,),

        html.Label("Initial substrate (g/l)"),
        dcc.Slider(id="substrate",
                   min=1,
                   max=40,
                   step=1,
                   value=substrate_start),
        
        html.Label("Max volume (l)"),
        dcc.Input(type="number", id="max_value"),

        fed_batch_panel,

        html.Button("Run simulation", id="run-btn"),
    ],
    style={
        "width": "25%",
        "padding": "20px"
    }
    )

plot = html.Div([
        dcc.Graph(id="fermentation-graph")
    ],
    style={
        "width": "75%"
    }
    )

gene_selector = html.Div([
        html.Label("Gene 1"),
        dcc.Dropdown(
            gene_types,
            "Wild type",
            id="gene_1"
        ),
        html.Label("Gene 2"),
        dcc.Dropdown(
            gene_types,
            "Wild type",
            id="gene_2"
        ),
        html.Label("Gene 3"),
        dcc.Dropdown(
            gene_types,
            "Wild type",
            id="gene_3"
        ),
        html.Label("Gene 4"),
        dcc.Dropdown(
            gene_types,
            "Wild type",
            id="gene_4"
        )
    ],
    style={
        "display": "flex",
        "flexDirection": "row",
    }
    )

top = html.Div([
        controls_panel, plot
    ],
    style={
        "display": "flex",
        "flexDirection": "row",
    }
    )