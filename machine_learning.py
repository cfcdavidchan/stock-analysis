import os
import pandas as pd
from datetime import datetime
org_path = os.getcwd()
data_path = org_path + '/stock-data'
data_csv = [csv for csv in os.listdir(data_path) if csv.endswith('.csv')]
print (data_csv)

class