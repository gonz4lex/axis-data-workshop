# Data Analysis and Introduction to Classification Algorithms with Python

## Loading data

    pd.read_csv('\data\dataset.csv')

    with open('dataset.json') as f:
        d = json.load(f)

### Pandas DataFrame

Select columns and rows using:

    df['column_name']
    df[0:100] # select first 100 rows

    df.loc[1:100, ['column_name']]

You can sample your data with:

    df.sample(5)

#### Filtering

Filter dataframes as follows:

    df[df['column_name'] == 'value']
    df[df['column_name'] > value]

#### Missing values

Drop rows from the dataset or fill them with values:

    df.dropna()
    df.fillna(mean)
    df.interpolate()

#### Grouping

    df.groupby('column_name').sum()

#### Creating new columns

    df['new_column'] = df['column_1'] / ['column_2']

#### Inspection

    df.shape
    df.head()
    df.tail()
    df.size()
    df.describe()
    df.isnull().sum()

### Data visualization

    import matplotlib.pyplot as plt

    plt.style.use('classic')

    plt.hist(df['column'], bins = 10, normed = 1, facecolor = 'blue', alpha = 0.7)
    plt.show()

    plotter = df.groupby('column').size()

    plot = plotter.plot(title = 'Plot')
    plot.set_xlabel('label')
    plot.set_ylabel('label')

### Statistics

    df.corr()

## k Nearest Neighbours

* Non parametric model
  * makes no assumptions on the distribution of the data
* For regression and classification
  * average of neighbours
  * majority vote

* The model finds the *k* nearest neighbours of any given data point based on a specified distance metric in a two-dimensional plane.

** scatter plot about here **

### Important decisions

* k: number of neighbours to choose - higher values return inaccurate predictions
* distance metric: depends on the problem - normally Euclidean is used

** distance metrics about here **
