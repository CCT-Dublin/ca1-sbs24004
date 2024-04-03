def remove_IN_OUT(df):
    dropColumns = [col for col in df.columns        # Create list and search through columns
                  if "IN" in col or "OUT" in col]   # Add column if contains IN or OUT
    df_Totals = df.drop(columns=dropColumns)        # Remove columns, column axis, leaving only total footfall counts
                                                        # return dropColumns #- (test)
    return df_Totals


def outlier_dates(df_column):
    iq1 = df_column.quantile(0.25)    # Define lower quantile
    iq3 = df_column.quantile(0.75)    # Define upper quantile
    iqr = iq3 - iq1                     # Define interquartile range
  
    outliers = df_column[(df_column > (iq3 + (1.5 * iqr)))]  # return outliers greater than normal, to identify periods of high activity
    
    return outliers