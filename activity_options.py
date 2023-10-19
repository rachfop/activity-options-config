from datetime import timedelta

from pydantic import BaseModel


class TaxonomyOptions(BaseModel):
    schedule_to_start_timeout: timedelta
    start_to_close_timeout: timedelta


valid_taxonomy = {
    "schedule_to_start_timeout": timedelta(seconds=10),
    "start_to_close_timeout": timedelta(seconds=10),
}

# This will raise a validation error if the data is invalid
taxonomy = TaxonomyOptions(**valid_taxonomy)
