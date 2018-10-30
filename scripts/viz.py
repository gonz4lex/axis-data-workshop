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

top_houses = df.groupby('house').count().sort_values(by = 'name', ascending = False).head()

df = df[df['house'].isin(list(dev.index))]


df['gold'] = np.nan
df['weapons'] = np.nan

# df['gold_multiplier'] = np.nan
# df['weapons_multiplier'] = np.nan

# for i in range(len(df)):

#     if df['house'][i] == "Stark":  
#         df['gold_multiplier'][i] = 1.8
#         df['weapons_multiplier'][i] = 0.8

#     elif df['house'][i] == "Night's Watch":
#         df['gold_multiplier'][i] = 0.8
#         df['weapons_multiplier'][i] = 1.8

#     else:
#         df['gold_multiplier'][i] = 1
#         df['weapons_multiplier'][i] = 1

random.seed(2018)

for i in range(len(df)):
    df['gold'][i] = random.randint(20, 100)
    df['weapons'][i] = random.randint(20, 100)

# df = df[
#         df['house'].isin(
#             ['Stark', 'Night\'s Watch']
#         )
#     ]



sns.pairplot(x_vars = 'weapons', 
             y_vars = 'gold', 
             data = df, 
             hue = "house"
)

plt.show()

df.reset_index().drop('index', axis = 1)

