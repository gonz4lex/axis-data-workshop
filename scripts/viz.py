"""
Visualizations for the Game of Thrones dataset.
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import json
import random

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

random.seed(2018)

for i in range(len(df)):
    df['gold'][i] = random.gauss(200, 20)
    df['weapons'][i] = random.gauss(100, 1)

sns.pairplot(x_vars = 'weapons', 
             y_vars = 'gold', 
             data = df, 
             hue = "house"
)

plt.show()

df.reset_index().drop('index', axis = 1)
