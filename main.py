import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash import Dash, dcc, html, Input, Output, State
from ferm_equetions import *
from START_VALUES import *


def main():
    
    app = Dash()

    app.layout = html.Div([
        dcc.Slider(id="run_time",
                   min=10,
                   max=1000,
                   step=1,
                   value=max_time),
        dcc.Slider(id="biomass",
                   min=0,
                   max=1,
                   step=0.01,
                   value=biomass_start,),
        dcc.Slider(id="substrate",
                   min=1,
                   max=40,
                   step=1,
                   value=substrate_start),

        html.Button("Run simulation", id="run-btn"),

        dcc.Graph(id="fermentation-graph")
    ])

    @app.callback(
        Output("fermentation-graph","figure"),
        Input("run-btn", "n_clicks"),
        State("biomass", "value"),
        State("substrate", "value"),
        State("run_time", "value"),
        prevent_initial_call=True

    )
    def update_graph(n_clicks, biomass, substrate, run_time):

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
