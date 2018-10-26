"""
Visualizations for the Game of Thrones dataset.
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import json
import random

with open('axis-data-workshop\\thrones.json') as f:
    d = json.load(f)

HOUSE_NUMBER = 14

chars = pd.DataFrame()

for i in range(HOUSE_NUMBER):
    tmp = pd.DataFrame.from_dict(d['house'][i])
    chars = pd.concat([chars, tmp], ignore_index = True)

chars = chars.rename(index = str,
                     columns = {
                        'name': 'house',
                        'characters': 'name'
             })


chars.groupby('house').count().sort_values(by = 'name', ascending = False)

df = chars[
        chars['house'].isin(
            ['Lannister', 'Stark', 'Night\'s Watch']
        )
    ]


df['gold'] = np.nan
df['weapons'] = np.nan
df['gold_multiplier'] = np.nan
df['weapons_multiplier'] = np.nan

for i in range(len(df)):

    if df['house'][i] == "Stark":  
        df['gold_multiplier'][i] = 1.8
        df['weapons_multiplier'][i] = 0.8

    elif df['house'][i] == "Night's Watch":
        df['gold_multiplier'][i] = 0.8
        df['weapons_multiplier'][i] = 1.8

random.seed(2018)

for i in range(len(df)):
    df['gold'][i] = random.randint(50, 1000) * df['gold_multiplier'][i]
    df['weapons'][i] = random.randint(20, 100) * df['weapons_multiplier'][i] / 2

df = df[
        df['house'].isin(
            ['Stark', 'Night\'s Watch']
        )
    ]


sns.pairplot(x_vars = 'weapons', 
             y_vars = 'gold', 
             data = df, 
             hue = "house"
)

plt.show()

df.reset_index().drop('index', axis = 1)




