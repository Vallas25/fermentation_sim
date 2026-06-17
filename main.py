import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash import Dash, dcc, html, Input, Output, State
from ferm_equetions import *
from dividers import *
from START_VALUES import *
from strain.knockout import *


def main():
    
    app = Dash()

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
        State("max_volume","value"),
        State("initial_volume", "value"),
        State("feed_rate", "value"),
        State("fedbatch_concentration", "value"),
        Input("trigger_condition", "value"),
        State("triger_value", "value"),
        Input("fedbatch", "value"),
        Input("gene_1", "value"),
        Input("gene_2", "value"),
        Input("gene_3", "value"),
        Input("gene_4", "value"),
        prevent_initial_call=True

    )
    def update_graph(
    n_clicks,
    biomass,
    substrate,
    run_time,
    max_volume,
    initial_volue,
    feed_rate,
    fedbatch_concentration,
    trigger_condition,
    trigger_value,
    fedbatch,
    gene_1,
    gene_2,
    gene_3,
    gene_4
):

        #on of switch for fedbatch
        if fedbatch == ["fedbatch_on"]:
            fedbatch = True
        else:
            fedbatch = False
        
        #initialising equations class
        fermentation = equations(
            biomass=biomass,
            substrate_concentration=substrate,
            volume=initial_volue,
            mu_max=mu_max,
            dt=dt,
            max_time=run_time,
            is_fedbatch=fedbatch,
            feed_rate=feed_rate,
            max_volume=max_volume,
            trigger_condition=trigger_condition,
            trigger_value=trigger_value,
            feed_concentration= fedbatch_concentration,
            product=product_start
        )
        knockout(
            gene_1,
            gene_2,
            gene_3,
            gene_4
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

        fig.add_trace(
            go.Scatter(x=fermentation.time_steps,
                       y=fermentation.volume_steps,
                       name="vollume",
                       line=dict(color = "Green", dash = "dash")),
                       secondary_y= False
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
