import os
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
#%matplotlib inline
from urllib.request import urlretrieve
URL = "https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"

def get_freemont_data(filename='Freemont.csv',url=URL, force_download=False):
    """"
    Download and cache the freemont data
    
    parameters
    ---------------------------------------------
    filename : string (optional)
        location to save the data
    url : string (optional)
        web location of the data
    force_download : bool(optional)
        If true, force redownload of data
        
    returns
    ---------------------------------------------
    data: pandas.DataFrame
        The Freemont bridge data
        
    """""   
    
    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)
    data = pd.read_csv('Freemont.csv', index_col='Date',parse_dates=True)
    data.columns = ['West','East']
    data['Total'] = data['West'] + data['East']
    return data