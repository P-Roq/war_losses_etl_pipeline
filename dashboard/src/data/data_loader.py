import re
import pandas as pd
import xarray as xr
import numpy as np

from database.db_setup import SessionLocal
import database.db_models as models

class Country:
    UKRAINE: str = 'ukraine'
    RUSSIA: str = 'russia'


class AggregateLossesSchema:
    # Columns - vehicle type.
    TANK: str = 'tank' 
    AFV: str = 'afv' 
    IFV: str = 'ifv' 
    APC: str = 'apc' 
    IMV: str = 'imv' 

    INDEX: str = 'date'


def get_aggregate_losses(country: str,) -> pd.DataFrame:

    if country == 'ukraine':
        table_classes = models.table_classes_ukraine
    if country == 'russia':
        table_classes = models.table_classes_russia

    losses_container = []

    for table_class in table_classes:

        db_session = models.DBSession(SessionLocal, table_class)
        
        vehicle_type = re.sub(f'_{country}', '', table_class.__tablename__)

        losses = db_session.fetch_losses()

        losses_array = np.array([
                [row.total for row in losses],
                [row.destroyed for row in losses],
                [row.damaged for row in losses],
                [row.abandoned for row in losses],
                [row.captured for row in losses],
                ])

        table_losses = xr.DataArray(
            data=np.transpose(losses_array),
            coords=[
                [row.scraped_at for row in losses],
                ['total', 'destroyed', 'damaged', 'abandoned', 'captured'],
                ],
            dims=['date', 'loss_type'],
            attrs={'vehicle_type': vehicle_type}
            )
        
        losses_container.append(table_losses)

    concat_losses = xr.Dataset({table.attrs['vehicle_type']: table for table in losses_container})

    return concat_losses



class DataSource:
    def __init__(self, country: str):
        self.VEHICLE_TYPE = ['tank', 'afv', 'ifv', 'apc', 'imv']
        self.LOSS_TYPE = ['total', 'destroyed', 'damaged', 'abandoned', 'captured']
        self.DATA = get_aggregate_losses(country)



# print(DataSource('russia').DATA.sel(loss_type='destroyed'))