import pandas as pd
print('Opened')
dtypes = {'FULL': 'str', 'COUNT': 'int'}
mta = pd.read_csv('M100_month_W125_st.csv', error_bad_lines=False)
print(mta.shape)