import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time
from ferm_equetions import *
from START_VALUES import *


def main():
    #all the lists for the graph
    time_steps = []
    biomass_steps = []
    substrate_steps = []

    time_current = 0

    #initialising equations class
    fermentation = equations(
        biomass=biomass_start,
        substrate=substrate_start,
        vollume=vollume_start,
        mu_max= mu_max,
        dt = dt,
        product= product_start)
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    #calculating substrate/biomass over time
    while time_current < max_time and fermentation.substrate > 0:
        time_steps.append(time_current)
        biomass_steps.append(fermentation.biomass)
        substrate_steps.append(fermentation.substrate)
        fermentation.update()
        time_current += dt
    
    #adding biomass trace
    fig.add_trace(
        go.Scatter(x=time_steps,
            y=biomass_steps,
            name = "biomass",
            line = dict(color = "Red", dash = "dash")
        ),
        secondary_y= False
    )

    #adding substrate trace
    fig.add_trace(
        go.Scatter(x=time_steps,
                   y=substrate_steps,
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

    fig.write_html(f"plots/plot_{time.time()}.html")




if __name__ == "__main__":
    main()
