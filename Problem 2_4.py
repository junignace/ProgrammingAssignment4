import pandas as pd

data = {'Box': ['Box 1','Box 1','Box 1','Box 2','Box 2','Box 2'],
        'Dimension':['Length', 'Width', 'Height','Length', 'Width', 'Height'],
        'Value': [6,4,2,5,3,4]}
df = pd.DataFrame(data, columns= ['Box', 'Dimension', 'Value'])

tidy= df.pivot_table(index=['Box'], columns='Dimension', values='Value').reset_index()

Vol = [2*6*4, 4*5*3]

tidy['Volume'] = Vol

print(tidy)                      