"""
Visualizations for the Game of Thrones dataset.
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import json
import random

pd.options.mode.chained_assignment = None

with open('thrones.json') as f:
    data = json.load(f)

HOUSE_NUMBER = len(data['house'])

chars = pd.DataFrame()

for i in range(HOUSE_NUMBER):
    tmp = pd.DataFrame.from_dict(data['house'][i])
    chars = pd.concat([chars, tmp], ignore_index = True)

with open('gender.json') as f:
    data = json.load(f)

gender = pd.DataFrame()

for i in range(2):
    tmp = pd.DataFrame.from_dict(data['gender'][i])
    gender = pd.concat([gender, tmp], ignore_index = True)

df = chars.merge(gender,
                  left_on = 'characters',
                  right_on = 'characters',
                  how = 'outer')

df = df.rename(index = str,
                     columns = {
                        'name': 'house',
                        'characters': 'name'
             })

top_houses = df.groupby('house').count().sort_values(by = 'name',
                                                     ascending = False).head()
                                                     

df = df[df['house'].isin(
                        list(top_houses.index)
                        )
                    ]
                    
df['gold'] = np.nan
df['weapons'] = np.nan
df['multiplier'] = np.nan

random.seed(2018)

full = pd.DataFrame()

for i in top_houses.index:
    tmp = df[df['house'] == i]
    tmp['gold_multiplier'] = abs(random.gauss(3, 6))
    tmp['weapons_multiplier'] = abs(random.gauss(3, 6))
    full = pd.concat([full, tmp], ignore_index = True)

for i in range(len(full)):
    full['gold'][i] = random.gauss(200, 50) * full['gold_multiplier'][i]
    full['weapons'][i] = random.gauss(100, 20) * full['weapons_multiplier'][i]

sns.pairplot(x_vars = 'weapons', 
             y_vars = 'gold', 
             data = full, 
             hue = "house"
)

plt.show()

df.reset_index().drop('index', axis = 1)
