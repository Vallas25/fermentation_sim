import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash import Dash, dcc, html, Input, Output
import time
from ferm_equetions import *
from START_VALUES import *


def main():
    time_current = 0

    #initialising equations class
    fermentation = equations(
        biomass=biomass_start,
        substrate_concentration=substrate_start,
        vollume=vollume_start,
        mu_max= mu_max,
        dt = dt,
        max_time= max_time,
        product= product_start)
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    #calculating substrate/biomass over time
    fermentation.run()
    
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
        xaxis_domain=[0.05, 1.0]
    )

    #setting axis titles
    fig.update_xaxes(title_text = "time (min)")
    fig.update_yaxes(title_text = "biomassa (OD)", secondary_y= False)
    fig.update_yaxes(title_text = "substrate g/l", secondary_y= True)

    app = Dash()
    app.layout = html.Div([
    dcc.Graph(figure=fig)
    ])

    app.run(debug=True, use_reloader=False)




if __name__ == "__main__":
    main()
