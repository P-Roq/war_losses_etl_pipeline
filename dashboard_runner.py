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
    app.title = "Russo-Ukrainian War - Daily Tracker Of Infantry Vehicle Losses" 
    app.layout = create_layout(app, [agg_losses_ukraine, agg_losses_russia,],)
    
    app.run(debug=False, host="127.0.0.5", port=8050)

if __name__ == "__main__":
    main()        
      