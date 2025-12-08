import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    # Return the First three rows of dataframe @Employees
    return employees.head(3)
