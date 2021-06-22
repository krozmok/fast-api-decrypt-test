from app.models.frequencytable import FrequencyTable
from tortoise.contrib.pydantic import pydantic_model_creator


FrequencyTable_Pydantic = pydantic_model_creator(FrequencyTable, name="FrequencyTable")
FrequencyTableIn_Pydantic = pydantic_model_creator(FrequencyTable, name="FrequencyTableIn", exclude_readonly=True)