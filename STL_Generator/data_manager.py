import pandas as pd


class Import_data:

    def from_excel(self, file_path):
        df = pd.read_excel(file_path)
        objlist = df['Nazwa projektowa'].tolist()
        comments = df['Komentarz:'].tolist()
        return objlist, comments