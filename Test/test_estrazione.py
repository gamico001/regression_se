# ---------------------------------------------------
# test primi metodi della classe Estrazione
# ---------------------------------------------------

import Classi.EstrazioneSuperenalotto

ex = Classi.EstrazioneSuperenalotto.Estrazione()

print("esito: ", ex.send_numbers_about_single_extraction([1, 2, 3, 4, 5]))
print("Stringa numeri: ",ex.string_extraction)