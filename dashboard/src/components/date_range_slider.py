from typing import List, Iterable
import pandas as pd
import numpy as np

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

        # This list contains intervals of 50 up to 50K values.
        range_intervals = [range(50*i, 50*(i+1)) for i in range(0, 1000+1)] 

        nr_dates = len(dates)

        if nr_dates > 10: 
            for idx, range_ in enumerate(range_intervals):
                if nr_dates in range_:
                    marks = {i: np.datetime_as_string(dates[i], unit='D') for i in range(len(dates)) if (i % 5*idx == 0)}
        else:
            marks = {i: np.datetime_as_string(dates[i], unit='D') for i in range(len(dates))}

        return marks

    return html.Div(
        children=[
            dcc.RangeSlider(
                id=date_range_slider_id,
                marks=make_marks(dates=_dates),
                min=0,
                max=len(_dates),
                step=1,
                value=[0, len(_dates)]
                ),
            ],
        style=date_range_slider_styles['level_1'],
        )