import numpy as np

def new_type(col_type, col_min, col_max):
    ntype = None
    if str(col_type).startswith('int'):
        if col_min > np.iinfo(np.int8).min and col_max < np.iinfo(np.int8).max:
            ntype = np.int8
        elif col_min > np.iinfo(np.int16).min and col_max < np.iinfo(np.int16).max:
            ntype = np.int16
        elif col_min > np.iinfo(np.int32).min and col_max < np.iinfo(np.int32).max:
            ntype = np.int32
        elif col_min > np.iinfo(np.int64).min and col_max < np.iinfo(np.int64).max:
            ntype = np.int64
    elif col_min > np.finfo(np.float16).min and col_max < np.finfo(np.float16).max:
        ntype = np.float16
    elif col_min > np.finfo(np.float32).min and col_max < np.finfo(np.float32).max:
        ntype = np.float16
    else:
        ntype = np.float64
    
    return ntype

def reduce(df, verbose=True):
    numerics = ['int8','int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    start_mem = df.memory_usage().sum() / 1024**2
    for col in df.columns:
        col_type = df[col].dtypes
        if col_type in numerics:
            c_min = df[col].min()
            c_max = df[col].max()
            df[col] = df[col].astype(new_type(col_type,c_min,c_max))
    end_mem = df.memory_usage().sum() / 1024**2
    if verbose: print('Mem. usage decreased to {:5.2f} Mb ({:.1f}% reduction)'.format(end_mem, 100 * (start_mem - end_mem) / start_mem))
    return df