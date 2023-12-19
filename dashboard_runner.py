from dash import Dash
from dash_bootstrap_components.themes import SOLAR
from dashboard.src.components.layout import create_layout

from dashboard.src.data.data_loader import (
    get_aggregate_losses,
    Country,
    AggregateLossesSchema,
    )

def main() -> None:
    agg_losses_ukraine = get_aggregate_losses(Country.UKRAINE, AggregateLossesSchema.TOTAL)
    agg_losses_russia = get_aggregate_losses(Country.RUSSIA, AggregateLossesSchema.TOTAL)
    app = Dash(external_stylesheets=[SOLAR])
    app.title = "Russo-Ukrainian War - Tracking Of Military Infantry Vehicles Losses" 
    app.layout = create_layout(app, [agg_losses_ukraine, agg_losses_russia,],)
    
    app.run_server(debug=True, port=8051)

if __name__ == "__main__":
    main()        
      