from typing import List
 
from dash import Dash, html, dcc 
from dash.dependencies import Input, Output
from dashboard.src.data.data_loader import DataSource

def render(
      app: Dash,
      source: DataSource,
      dropdown_id: str,
      button_id: str,
      ) -> html.Div:

    @app.callback(
        Output(dropdown_id, "value"),
        Input(button_id, "n_clicks"),
    )
    def select_vehicle_type(_: str) -> List[str]:
      return source.VEHICLE_TYPE 

    return html.Div(
        children=[
            html.H6('Vehicle Type'),
            dcc.Dropdown(
                id=dropdown_id,
                options=[{"label": vehicle, "value": vehicle} for vehicle in source.VEHICLE_TYPE],
                value=source.VEHICLE_TYPE, 
                style={'width': '45%'},
                multi=True,
            ),
            html.Button(
                className="dropdown-button",
                children=["select_all"],
                id=button_id
            ),
        ],
        # style={'display': 'flex', 'flexDirection': 'row'},
    )