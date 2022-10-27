This library reduce the size of any data frame by allocating onky the needed memory to every numerical column.

It contains two functions: new_type and reduce

** new_type(col_type,col_min,col_max):
** col_type is the current column col_type
** col_min == min value in the column
** col_max == max value in the column
Using these given, informations the function will check
and return what is the suitable data type to be set for the columns


** reduce(df, verbose=True)
** This function takes as arguments 
1.) The dataframe `df` as it is loaded from the data source
2.) If verbose = True, you will get the information about the data size reduction
