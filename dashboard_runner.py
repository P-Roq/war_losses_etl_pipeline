from dash import Dash
from dash_bootstrap_components.themes import SOLAR
from dashboard.src.components.layout import create_layout

from dashboard.src.data.data_loader import (
    Country,
    DataSource,
    )

def main() -> None:
    agg_losses_ukraine = DataSource(Country.UKRAINE)
    agg_losses_russia = DataSource(Country.RUSSIA)
    app = Dash(external_stylesheets=[SOLAR])
    app.title = "Russo-Ukrainian War - Tracking Of Military Infantry Vehicles Losses" 
    app.layout = create_layout(app, [agg_losses_ukraine, agg_losses_russia,],)
    
    app.run_server(debug=True, port=8051)

if __name__ == "__main__":
    main()        
      