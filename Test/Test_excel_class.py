"""
Test Excel_CSV Class
"""
import Classi.Excel_CSV

excel = Classi.Excel_CSV.Excel()

file_path = r'/Users/Giorgio/Library/Mobile Documents/com~apple~CloudDocs/WORKSPACES/Superenalotto/SuperEnalotto-archivio-40.xlsx'

print('-->', excel.load_excel_file(file_path, 'Estrazioni anno 2021', 4, 3, 40, 6, 3))

print('Intestazione colonne:', excel.title_columns)
print('riga  colonna ', excel.cells_values)


