import vis

def analyze(df):
    insight1 = """
        The dataset contains 1000 rows with information related to university transactions. 
        There are 10 columns in the dataset, with 4 columns having data type 'int64' and 6 columns having data type 'object'. 
        Notably, the 'transaction_type' column has missing values in 107 rows, while all other columns have complete data.
    """
    insight2 = """
        The 'date' and 'time_of_sale' columns are stored as objects (strings) and need to be converted to datetime data types for further analysis. 
        This conversion is essential for time-related analysis, such as extracting the year and month of transactions.
        So the pandas to_datetime function is used to convert and later divide date to month and year.
    """
    insight3 = """
    Data reduction has been applied by dropping the 'received_by' column and sampling 50% of the data randomly. 
    These steps help reduce the dimensionality of the dataset and make it more manageable for analysis without significantly compromising the representation of the original data.
    """

    with open('eda-in-1.txt', 'w') as f:
        f.write(insight1)
        
    with open('eda-in-2.txt', 'w') as f:
        f.write(insight2)

    with open('eda-in-3.txt', 'w') as f:
        f.write(insight3)

    vis.plot(df)

    