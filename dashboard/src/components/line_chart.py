from typing import List
import pandas as pd

from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

from dashboard.src.components import ids
from dashboard.src.data.data_loader import AggregateLossesSchema


def render(app: Dash, source: pd.DataFrame, chart_id: str, dropdown_id: str) -> html.Div:
    @app.callback(
        Output(chart_id, "children"),
        [
            Input(dropdown_id, "value"),
        ],
        allow_duplicate=True
    )
    def update_line_chart(vehicle_type: List[str],) -> html.Div:

        if len(vehicle_type) == 0:
            return html.Div('Select a vehicle type via search bar or click on the "Select All" years button.')

        filtered_source = source.filter(
            vehicle_type, 
            axis=1, 
            )

        fig = px.line(
            filtered_source,
        )

        return html.Div(dcc.Graph(figure=fig), id=chart_id)

    
    return html.Div(id=chart_id)

