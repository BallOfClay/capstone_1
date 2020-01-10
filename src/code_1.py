import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy as stats
import re
import dateparser
import datetime

pd.set_option('display.max_columns', None)

current_df = pd.read_csv('~/dsi/capstones/cap1/data/phone_dataset.csv', sep=',')

cop_df = current_df.copy()

# Different Date Formats

# 0: 2009  February. Released 2009  April
# 23: 2011  February
# 45: 2012  Q3
# 103: 1997
# 144: 2003 1Q
# 202: 2007. Released 2007
# 459: 2Q  2003
# 461: Exp. announcement 2012  August
# 1091: Not officially announced yet 
# 1097: (null) NaN
# 1649: Not officially announced yet. Released Exp. release 2009  Q4
# 1703: Feb-01
# 1708: Q2 2001 ?
# 2228: " "2013  February
# 2453: Exp. announcement 2015  Q3
# 2987: Not announced yet
# 5032: 2004 1 Q
# 5177: 2002  Oct
# 7090: Never
# 7379: 4Q 2001



# CLEAING - DATE CONVERSION

# Parsing variables
years = range(1994, 2017)

months = ['January', 'February', 'March', 'April', 'May', 'June', 
         'July', 'August', 'September', 'October', 'November', 'December']

months_short = ['Jan-', 'Feb-', 'Mar-', 'Apr-', 'May-', 'Jun-', 
                'Jul-', 'Aug-', 'Sep-', 'Oct-', 'Nov-', 'Dec-']

months_num = np.linspace(0.0, 1.0, num=12)

months_int = range(1, 12)

months_dict = {
    'January':1, 
    'February':2, 
    'March':3, 
    'April':4, 
    'May':5, 
    'June':6, 
    'July':7, 
    'August':8, 
    'September':9, 
    'October':10, 
    'November':11, 
    'December':12
}

quarters = ['Q1', '1Q', 'Q2', '2Q', 'Q3', '3Q', 'Q4', '4Q']

quarters_dict = {
  'Q1': 'February',
  '1Q': 'February',
  'Q2': 'May',
  '2Q': 'May',
  '3Q': 'August',
  'Q3': 'August',
  '4Q': 'November',
  'Q4': 'November'
}



# CLEANING - DATE PARSER

def parse_date(date_str):
    
    # Removes preceding and proceding spaces
    date_str = date_str.strip()
    
    # Changes strings with "?" to "remove"
    if '?' in date_str:
        date_str = 'remove'
    
    # Removes errant release dates
    if '.' in date_str:
        split_str = date_str.split('.')
        date_str = split_str[0]
    
    # Changes Quarter to Middle Month of Quarter
    for key, val in quarters_dict.items():
        if key in date_str:
            split_2 = date_str.split()
            split_2[split_2.index(key)] = val
            date_str = " ".join(split_2)

    # Converts Year Only to Year + ' July'
    if len(date_str) < 5:
        date_str += ' July'    
    
    # If date is formated in short form i.e. "Feb-01"
    m_index = 0
    for m in months_short:
        if m in date_str:
            split_3 = date_str.split('-')
            split_3[0] = months[m_index]
            split_3[1] = f'20{split_3[1]}'
            date_str = " ".join(split_3)
        m_index += 1
       
    # Date Parsing str using module dataparser    
    date_tm = dateparser.parse(date_str)
    if isinstance(date_tm, datetime.date):
        date_tm = date_tm - datetime.timedelta(days=date_tm.day-1)
            
    return date_tm


# Remove Date-less Objects
def refactor_df(df, col='announced'):
    step_df = df[df['announced'].notna()]
    
    step_df['announced'] = step_df['announced'].apply(parse_date)
    
    step_df['announced'] = step_df['announced'].dt.to_period('M')
    
    return step_df



# CLEANING - FINDING UNIQUE PHONE MODELS (NOT COMPLETE)

def unique_models(_list, split_1 = None, split_2 = None):
#     _list = model_list
    unique_list = []
    
    if split_1 is None and split_2 is None:
        for n in _list:
            unique_list.append(n)
            unique_list = is_unique(unique_list)

    elif split_1:
        for n in _list:
            n_dict = {}
            split_atr = n.split(split_1)
            n_dict[split_atr[0]] = []
            n_dict[split_atr[0]].extend(split_atr[1:])
            unique_list.append(n_dict)
    
    return unique_list



# CLEANING - CAST NaN/Null

make_nan = ['No', 'N/A', 'No cellular connectivity']

def cast_nan(step_df, make_nan):
#     if nan_str in nan_list:
#         nan_str = NaN
    df_obj = step_df.select_dtypes(['object'])

    step_df[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())

    step_df.replace(to_replace=make_nan, value=np.nan, inplace=True)
    
    return step_df



# Execute Cleaning

period_df = refactor_df(cop_df)

period_df = cast_nan(period_df, make_nan)


# Cleaning - Screen Size

def screen_refactor(s, split_char=' '):
    s = str(s)
    s = s.replace('| -', '')
    s = s.replace('|', '')
    s = s.strip()
    
    
    if isinstance(s, str):
        split_s = s.split(split_char)
        try 
        return split_s[0]
    else:
        return s
    

# Execute Cleaing

period_df['screen_in'] = period_df['display_size'].apply(screen_refactor)



# ANALYSIS - GENERAL TRENDS

# Average Price Over Time
fig = plt.figure(figsize=(12,4))

ax1 = period_df.groupby('announced').mean()['approx_price_EUR'].plot(
    xlim=[pd.Timestamp('2005-08-01'), pd.Timestamp('2017-10-01')], ylim=[0, 750])

ax1.set_ylabel('Average Price (EUR)')
ax1.set_xlabel('Month Announced')

# Average Screen Size Over Time
fig2 = plt.figure(figsize=(12,4))

ax2 = period_df.groupby('announced').mean()['screen_in'].plot(
    xlim=[pd.Timestamp('2005-08-01'), pd.Timestamp('2017-10-01')])

ax2.set_ylabel('Average Price (EUR)')
ax2.set_xlabel('Month Announced')

# Average Battery Capacity Over Time
ax3 = period_df.groupby('announced').mean()['screen_in'].plot(
    xlim=[pd.Timestamp('2005-08-01'), pd.Timestamp('2017-10-01')])

ax3.set_ylabel('Average Price (EUR)')
ax3.set_xlabel('Month Announced')


# ANALYSIS - SPECIFIC FEATURES

df_feature = period_df[['bluetooth', 'announced']]
    
date_max = df_feature['announced'].max()
date_min = df_feature['announced'].min()

month_period = month_diff(date_max, date_min)
day_period = date_max - date_min

date_counts = df_feature.groupby([df_feature['announced'].dt.year, df_feature['announced'].dt.month]).count()


