import pandas as pd


class Import_data:

    def from_excel(self):
        df = pd.read_excel('pt.xlsx')
        my_column = df.iloc[:, 0].tolist()
        return my_column
