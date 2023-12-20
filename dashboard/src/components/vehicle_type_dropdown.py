import sys
from typing import List
import pandas as pd

# dcc is a collection of user-interface supplied by dash.
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from dashboard.src.components import ids


def render(
      app: Dash,
      source: pd.DataFrame,
      dropdown_id: str,
      button_id: str,
      ) -> html.Div:

    @app.callback(
        Output(dropdown_id, "value"),
        Input(button_id, "n_clicks"),
        allow_duplicate=True,
    )
    def select_unique_years(_: int) -> List[str]:
      return source.columns

    return html.Div(
        children=[
            html.H6('Vehicle Type'),
            dcc.Dropdown(
                id=dropdown_id,
                options=[{"label": vehicle, "value": vehicle} for vehicle in source.columns],
                value=source.columns,
                multi=True
            ),
            html.Button(
                className="dropdown-button",
                children=["select_all"],
                id=button_id
            )
        ]
    )