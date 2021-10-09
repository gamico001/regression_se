# -------------------------------------
# test metodi di accesso a file Excel
# -------------------------------------
import Classi.EstrazioniSuperenalotto

path = "/Users/giorgio/Library/Mobile Documents/com~apple~CloudDocs/WORKSPACES/Superenalotto/SuperEnalotto-archivio" \
       "-40.xlsx"

e = Classi.EstrazioniSuperenalotto.Estrazioni()
# print("Esito: ", e.load_extraction_numbers_from_excel(path))
print("Esito: ", e.load_extraction_first_number_from_excel(path))
