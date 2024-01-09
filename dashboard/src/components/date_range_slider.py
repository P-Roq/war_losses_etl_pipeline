from typing import List, Iterable
import pandas as pd
import numpy as np

from dash import Dash, html, dcc 
from dashboard.src.data.data_loader import DataSource

def render(
      app: Dash,
      source: DataSource,
      date_range_slider_id: str,
      ) -> html.Div:
    
    _dates = source.DATA.coords['date'].values
    
    def make_marks(dates: Iterable):

        dates = {i: {'label': np.datetime_as_string(dates[i], unit='D')} for i in range(len(dates))}

        for key in dates:
            if len(dates[key]['label']) > 0:
                if dates[key]['label'][-1] not in ['0', '5']:
                    dates[key]['label'] = ''

        return dates

    return html.Div(
        children=[
            html.H6('Time Range'),
            dcc.RangeSlider(
                id=date_range_slider_id,
                marks=make_marks(dates=_dates),
                min=0,
                max=len(_dates),
                step=1,
                value=[0, len(_dates)]
                ),
            ]
        )