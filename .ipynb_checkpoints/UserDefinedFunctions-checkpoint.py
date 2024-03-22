def remove_IN_OUT(df):
    dropColumns = [col for col in df.columns        # Create list and search through columns
                  if "IN" in col or "OUT" in col]   # Add column if contains IN or OUT
    df_Totals = df.drop(columns=dropColumns)        # Remove columns, column axis, leaving only total footfall counts
                                                        # return dropColumns #- (test)
    return df_Totals