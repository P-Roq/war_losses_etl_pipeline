from typing import List
 
from dash import Dash, html, dcc 
from dash.dependencies import Input, Output
from dashboard.src.components.styles import vehicle_dropdown_styles
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
            html.H5('Vehicle Type'),
            html.Div(
                children=[
                    dcc.Dropdown(
                        id=dropdown_id,
                        options=[{"label": vehicle, "value": vehicle} for vehicle in source.VEHICLE_TYPE],
                        value=source.VEHICLE_TYPE, 
                        style=vehicle_dropdown_styles['level_3']['dropdown'],
                        multi=True,
                    ),
                    html.Button(
                        className="dropdown-button",
                        children=["Select All"],
                        id=button_id
                    ),
                ],
                style=vehicle_dropdown_styles['level_2'],
            ),
        ],
        style=vehicle_dropdown_styles['level_1'],
    )