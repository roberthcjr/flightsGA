import pandas as pd

def fileToDataframe(filePath):
    return pd.read_csv(filePath)