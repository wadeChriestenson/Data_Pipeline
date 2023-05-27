import pandas as pd
from getData import get_table


def return_all_data(all_data):
  returnData = pd.DataFrame(all_data)
  return returnData


everything = get_table()
return_all_data(everything)
