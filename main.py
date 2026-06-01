import plotly.graph_objects as go
import time
from ferm_equetions import *
from START_VALUES import *


def main():
    #all the lists for the graph
    time_steps = []
    biomass_steps = []
    substrate_steps = []

    #initialising equations class
    organism = equations(
        biomass=biomass_start,
        substrate=substrate_start,
        vollume=vollume_start,
        mu_max= mu_max,
        dt = dt,
        product= product_start)
    
    fig = go.Figure()
    
    #calculating substrate/biomass over time
    while t < max_time:
        time_steps.append(t)
        biomass_steps.append(organism.biomass)
        substrate_steps.append(organism.substrate)
        organism.update()
        t += dt
    
    #adding biomass trace
    fig.add_trace(
        go.scatter(x=time_steps,
            y=biomass_steps,
            name = "biomass",
            line = dict(color = "Red", dash = "dash")
        )
    )

    #adding substrate trace
    fig.add_trace(
        go.scatter(x=time_steps,
                   y=biomass_steps,
                   name = "substrate",
                   line = dict(color = "Blue", dash = "dashed")

        )
    )
    # Set title
    fig.update_layout(
        title_text="Biomass over time",
        xaxis_domain=[0.05, 1.0]
    )

    fig.write_html(f"plot_{time.time}")




if __name__ == "__main__":
    main()
