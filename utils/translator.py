import pandas as pd

fullNameLocales = {
    "LIS": "Lisboa",
    "MAD": "Madrid" ,
    "CDG": "Paris",
    "DUB": "Dublin",
    "BRU": "Brussels",
    "LHR": "London",
    "FCO": "Rome"
}

def toHours(minutes):
    return f'{minutes//60}:{minutes%60}'

def toMinutes(df, column):
    return pd.to_datetime(df[column]).dt.hour * 60 + pd.to_datetime(df[column]).dt.minute

def readTxt(filePath, columns):
    return pd.read_csv(filePath, names=columns)