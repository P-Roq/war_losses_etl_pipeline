from typing import Iterable

from dash import Dash, html, dcc 
from dashboard.src.data.data_loader import DataSource
from dashboard.src.components.styles import date_range_slider_styles

def render(
      app: Dash,
      source: DataSource,
      date_range_slider_id: str,
      ) -> html.Div:
    
    _dates = source.DATA.coords['date'].values

    def make_marks(dates: Iterable):

        nr_dates = len(dates)

        # We are going for about 20 permanent marks regardless of the increasing in data.
        if nr_dates >= 20: 
            steps = round(nr_dates / 20)
            marks={i: '' for i in range(len(dates)) if (i % steps == 0)}
        else:
            marks = {i: '' for i in range(len(dates))}
        
        return marks

    return html.Div(
        children=[
            dcc.RangeSlider(
                id=date_range_slider_id,
                marks=make_marks(dates=_dates),
                min=0,
                max=len(_dates),
                value=[0, len(_dates)]
                ),
            ],
        style=date_range_slider_styles['level_1'],
        )