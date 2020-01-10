# Cleaning functions

def parse_string_to_date(str):
    stripped_str = str.replace('.', '')
    split_str = stripped_str.split()

    if 'Exp' in split_str:
        return None

    # handle year
    year = [s for s in split_str if s.isdigit()]
    if len(year):
        year = year[0]
    else:
        return None

    # handle month
    month = [m for m in split_str if m in months_dict]
    if len(month):
        month = month[0]
    # elif handle quarters by looking up element in split_str and using it's key
    else:
        month = 'June'

    parsed_string = month + ' ' + year

    # if you need timestamp use dateparser or something
    # parsed_date = dateparser.parse(parsed_string)

    return parsed_string

parse_string_to_date('2003 1Q')


#     for key, val in quarters_dict.items():
# #         print(key)
#         if key in str:
#             print(key)
#             str = re.sub(r'key', r'val', str)
# #             months_dict[key] + ' ' + 

# date_list = df_col.tolist()

# date_list = toy_df['announced'].tolist()
# # date_list

# list_2 = [parse_date(n) for n in date_list]

# toy_series = pd.Series(list_2) 

# toy_series 


# toy_df['announced'] = toy_series

# print(list_2[-1])

# toy_df['announced_clean'] = list_2 

# remove_dateless(toy_df)

# print(toy_df['announced'])

def remove_dateless(df_col):
    
    for idx, d in enumerate(df['announced']):
        if type(d) is not datetime.date:
            print(idx)
#             print(df.index(idx))
#             df[df.announced != d]
            df.drop(idx, inplace=True)
            
    return df