from typing import List
import pandas as pd
import xarray as xr

from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

from dashboard.src.data.data_loader import DataSource


def render(
        app: Dash,
        source_1: DataSource,
        source_2: DataSource,
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
        _vehicle_type: str,
        date_range: List[int],
        ) -> html.Div:

        if not _loss_type:
            return html.Div('Select a loss type via search bar/dropdown.')

        if not _vehicle_type:
            return html.Div('Select a vehicle type via search bar/dropdown.')

        filtered_source_ukraine = (
            source_1.DATA
            .sel(loss_type=_loss_type, drop=True)[_vehicle_type]
            .isel(date=slice(date_range[0], date_range[1]))
            )
        
        filtered_source_russia = (
            source_2.DATA
            .sel(loss_type=_loss_type, drop=True)[_vehicle_type]
            .isel(date=slice(date_range[0], date_range[1]))
            )

        fig = px.line(
            y=[
                filtered_source_ukraine.values,
                filtered_source_russia.values,
            ],
            x=filtered_source_ukraine['date'].values,
            labels={'x': 'date', 'y': 'units'},
            )
        
        fig.update_yaxes(title_text='units')

        fig.data[0].name = 'Ukraine'  # update legend for the first trace
        fig.data[1].name = 'Russia'  # update legend for the second trace

        return html.Div(dcc.Graph(figure=fig), id=chart_id)

    
    return html.Div(id=chart_id)

