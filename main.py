import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash import Dash, dcc, html, Input, Output, State
from ferm_equetions import *
from START_VALUES import *


def main():
    
    app = Dash()

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

    app.layout = html.Div([
        top, gene_selector
    ],
    style={
        "display": "flex",
        "flexDirection": "column"
    }
    )

    @app.callback(
        Output("fermentation-graph","figure"),
        Input("run-btn", "n_clicks"),
        State("biomass", "value"),
        State("substrate", "value"),
        State("run_time", "value"),
        Input("gene_1", "value"),
        prevent_initial_call=True

    )
    def update_graph(n_clicks, biomass, substrate, run_time, gene_1):

        #initialising equations class
        fermentation = equations(
            biomass=biomass,
            substrate_concentration=substrate,
            vollume=vollume_start,
            mu_max=mu_max,
            dt=dt,
            max_time=run_time,
            product=product_start
        )

        print(gene_1)
        
        #calculating substrate/biomass over time
        fermentation.run()
    
        fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    
    #adding biomass trace
        fig.add_trace(
            go.Scatter(x=fermentation.time_steps,
                y=fermentation.biomass_steps,
                name = "biomass",
                line = dict(color = "Red", dash = "dash")
            ),
            secondary_y= False
        )

        #adding substrate trace
        fig.add_trace(
            go.Scatter(x=fermentation.time_steps,
                    y=fermentation.substrate_concentration_steps,
                    name = "substrate",
                    line = dict(color = "Blue", dash = "dash")

            ),
            secondary_y= True
        )

        # Set title
        fig.update_layout(
            title_text="Biomass over time",
            xaxis_domain=[0.05, 1.0],
        )

        #setting axis titles
        fig.update_xaxes(title_text = "time (min)")
        fig.update_yaxes(title_text = "biomassa (OD)", secondary_y= False)
        fig.update_yaxes(title_text = "substrate g/l", secondary_y= True)
    
        return fig


    app.run(debug=True, use_reloader=False)




if __name__ == "__main__":
    main()
