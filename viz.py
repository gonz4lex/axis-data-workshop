"""
Visualizations for the Game of Thrones dataset.
"""

import pandas as pd
import json


thrones = json.loads("thrones.json")

pd.DataFrame.from_dict(thrones)

