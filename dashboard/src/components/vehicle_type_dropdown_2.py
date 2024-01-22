from dash import Dash, html, dcc # dcc is a collection of user-interface supplied by dash
from dash.dependencies import Input, Output
from dashboard.src.components.styles import vehicle_dropdown_2_styles
from dashboard.src.data.data_loader import DataSource

def render(
      app: Dash,
      source: DataSource,
      dropdown_id: str,
      ) -> html.Div:

    @app.callback(
        Output(dropdown_id, "value"),
        Input(dropdown_id, "value"),
    )
    def select_vehicle_type(selected_value: str) -> str:
        return selected_value

    return html.Div(
        children=[
            html.H5('Vehicle Type'),
            dcc.Dropdown(
                id=dropdown_id,
                options=[{"label": vehicle_type, "value": vehicle_type} for vehicle_type in source.VEHICLE_TYPE],
                value=source.VEHICLE_TYPE[0], # default value is 'total'
                style=vehicle_dropdown_2_styles['level_2'],
            ),
        ],
        style=vehicle_dropdown_2_styles['level_1'],
        )