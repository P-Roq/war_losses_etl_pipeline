import sys
import os
import re
import pandas as pd

from database.db_setup import SessionLocal
import database.db_models as models


current_module_path = os.path.abspath(__file__)

parent_directory = os.path.dirname(os.path.dirname(current_module_path))

project_root = os.path.dirname(parent_directory)

sys.path.insert(0, project_root)

path_endpoint = "/dashboard/src/data/data_loader.py"

oryx_folder_path = re.sub(path_endpoint, '', current_module_path)

sys.path.insert(0, oryx_folder_path)


class Country:
    UKRAINE: str = 'ukraine'
    RUSSIA: str = 'russia'


class AggregateLossesSchema:
    # Columns by country.
    TANK: str = 'tank' 
    AFV: str = 'afv' 
    IFV: str = 'ifv' 
    APC: str = 'apc' 
    IMV: str = 'imv' 

    # Loss Type
    TOTAL: str = 'total'
    DESTROYED: str = 'destroyed'
    DAMAGED: str = 'damaged'
    ABANDONED: str = 'abandoned'
    CAPTURED: str = 'captured'

    INDEX: str = 'date'


def get_aggregate_losses(country: str, loss_type: str):

    if country == 'ukraine':
        table_classes = models.table_classes_ukraine
    if country == 'russia':
        table_classes = models.table_classes_russia

    aggregate_losses = pd.DataFrame() 

    for table_class in table_classes:
        db_session = models.DBSession(SessionLocal, table_class)
        vehicle_type = re.sub(f'_{country}', '', table_class.__tablename__)

        losses = db_session.fetch_losses_by_loss_type(loss_type)
        losses = pd.DataFrame(losses, columns=[vehicle_type, AggregateLossesSchema.INDEX])
        losses.index = losses[AggregateLossesSchema.INDEX]
        losses = losses.drop(columns=[AggregateLossesSchema.INDEX]) 
        
        if losses.shape[1] == 0:
            aggregate_losses = losses.copy() 
        else:   
            aggregate_losses = pd.concat(
                [aggregate_losses, losses.copy()],
                axis=1, 
                )
            
    aggregate_losses = aggregate_losses.rename(columns={
        'tank': AggregateLossesSchema.TANK,
        'afv': AggregateLossesSchema.AFV,
        'ifv': AggregateLossesSchema.IFV,
        'apc': AggregateLossesSchema.APC,
        'imv': AggregateLossesSchema.IMV,
        }
    )

    return aggregate_losses