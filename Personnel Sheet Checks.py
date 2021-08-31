import pandas as pd
import numpy as np

data = pd.read_excel('C:/Users/Aamir Zargham/Desktop/Python/Personnel_List.xlsx')

data = data.iloc[2:]
dataHeader = data.iloc[0]
data = data.iloc[1:]
data.columns = dataHeader

indexNoErrors = data[(~pd.isnull(data['Budget Status']))     & 
                     (~pd.isnull(data['Employment_Status'])) &
                     (~pd.isnull(data['Level']))             &
                     (~pd.isnull(data['Role Type']))         & 
                     (~pd.isnull(data['Contributor_Type']))  &
                     (~pd.isnull(data['Vertical']))          &
                     (~pd.isnull(data['Finance Start Date']))].index

indexBlanks   = data[(pd.isnull(data['Budget Status']))     & 
                     (pd.isnull(data['Employment_Status'])) &
                     (pd.isnull(data['Level']))             &
                     (pd.isnull(data['Role Type']))         & 
                     (pd.isnull(data['Contributor_Type']))  &
                     (pd.isnull(data['Vertical']))          &
                     (pd.isnull(data['Finance Start Date']))].index


data.drop(indexNoErrors, inplace=True)
data.drop(indexBlanks, inplace=True)
print("There are: " + str(len(data.index)) + " errors")

data.to_excel('C:/Users/Aamir Zargham/Desktop/Python/Personnel_List_Errors.xlsx', index=False)