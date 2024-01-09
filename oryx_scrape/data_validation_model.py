from datetime import datetime
from pydantic import BaseModel, ValidationError, Field


class ScrapedRawData(BaseModel):
    raw_data: str = Field(..., max_length=200)

class ScrapedSplitData(BaseModel):
    total: int
    destroyed: int 
    damaged: int 
    abandoned: int 
    captured: int 
    scraped_at: datetime

