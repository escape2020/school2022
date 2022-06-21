import pandas as pd
from pandas.io.excel._xlrd import XlrdReader
from pandas.io.excel import ExcelFile

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()
filename = args.filename

class CustomXlrdReader(XlrdReader):

    def load_workbook(self, filepath_or_buffer):
        """Same as original, just uses ignore_workbook_corruption=True)"""
        from xlrd import open_workbook

        if hasattr(filepath_or_buffer, "read"):
            data = filepath_or_buffer.read()
            return open_workbook(file_contents=data, ignore_workbook_corruption=True)
        else:
            return open_workbook(filepath_or_buffer)

ExcelFile._engines['custom_xlrd'] = CustomXlrdReader
print('Monkey patching pandas XLS engines. See CustomXlrdReader')

df = pd.read_excel(filename, engine='custom_xlrd')

speakers = df[df['Catégorie']=='SPEAKER Escape Summer School June 19th to 24th  2022']
print(f"{len(speakers)} speakers")

participants = df[df['Catégorie']!='SPEAKER Escape Summer School June 19th to 24th  2022']


payes = pd.concat([participants[participants['Facture payée']=='Oui'], manual_list])
non_payes = participants[participants['Facture payée']=='Non']
virements_attente = participants[(participants['Paiement']=='VIREMENT') & (participants['Facture payée']=='Non')]
print(f"{len(participants)} participants et {len(payes)} payes\n\n")
print(f"{len(virements_attente)} virements en attente (?)")


inscrits = pd.concat([speakers, payes])
inscrits.to_excel('participants_final.xls')
non_payes.to_excel('participants_attente.xls')
