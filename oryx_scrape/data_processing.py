import re
from datetime import datetime
from pydantic import ValidationError

from .data_validation_model import ScrapedRawData, ScrapedSplitData

def process_data(raw_data: str) -> dict:
    """Example of raw data to process:
    `'(2513, of which destroyed: 1649, damaged: 140, abandoned: 176, captured: 548)'`
    """

    validated_raw_data = ScrapedRawData(raw_data=raw_data)

    now = datetime.utcnow()

    split_data = re.split(r'[\(\)]', validated_raw_data.raw_data)[1]
    

    str_unfolded = re.split(r'\D+', split_data)

    extracted = [int(loss_number) for loss_number in str_unfolded if loss_number != '']

    print('\n\n')
    print(f'{extracted = }')
    print('\n\n')

    try:
        validated = ScrapedSplitData(
            total=extracted[0],
            destroyed=extracted[1],
            damaged=extracted[2],
            abandoned=extracted[3],
            captured=extracted[4],
            scraped_at=datetime(now.year, now.month, now.day),
        )
        
    except ValidationError as e:
        print(f"Validation error: {e}")
        raise
    

    full_element = {
        'total': validated.total,
        'destroyed': validated.destroyed,
        'damaged': validated.damaged,
        'abandoned': validated.abandoned,
        'captured': validated.captured,
        'scraped_at': validated.scraped_at,
        }


    return full_element

