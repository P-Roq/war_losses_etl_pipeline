from typing import List

from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

from dashboard.src.data.data_loader import DataSource


def render(
        app: Dash,
        source: DataSource,
        chart_id: str,
        dropdown_loss_type_id: str,
        dropdown_vehicle_type_id: str,
        date_range_slider_id: str,
        ) -> html.Div:
    @app.callback(
        Output(chart_id, "children"),
        [
            Input(dropdown_loss_type_id, "value"),
            Input(dropdown_vehicle_type_id, "value"),
            Input(date_range_slider_id, "value"),
        ],
    )
    def update_line_chart(
        _loss_type: str,
        _vehicle_type: List[str],
        date_range: List[int],
        ) -> html.Div:

        if not _loss_type:
            return html.Div('Select a loss type via search bar/dropdown.')

        if len(_vehicle_type) == 0:
            return html.Div('Select a vehicle type via search bar/dropdown or click on the "Select All" button.')

        filtered_source = (
            source.DATA
            .sel(loss_type=_loss_type, drop=True)[_vehicle_type]
            .isel(date=slice(date_range[0], date_range[1]))
            )
        
        fig = px.line(
            filtered_source,
        )

        fig.update_yaxes(title_text='units')

        return html.Div(dcc.Graph(figure=fig), id=chart_id)

    
    return html.Div(id=chart_id)

