import pandas as pd
from Data import getDataYF, getDataFM
import mplfinance as mpf
data=getDataFM('0050', '2020-01-01', '2021-01-01')
data.head()