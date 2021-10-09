"""
Controller about Regression_gui
The property "extractions_id" is e number of extraction. Is a list
The property  "extraction_numbers" is a list of 6 umbers extract. Index is the single extraction
The property   "extraction_date" is a date of extraction
The property "extractions_head" is a name of columns for extractions_numbers
"""
# imports...
import Classi.EstrazioniSuperenalotto
import Classi.Excel_CSV
import Classi.Plotter

# -----------------
# PROPERTIES...
# -----------------
error_descriptions = [
    'OK, file caricato correttamente',
    'Percorso del file errato',
    'File non trovato'
]

__status_descriptions = [
    'Start. Nessuna azione effettuata. ',
    'File data caricato senza errori ma nessun calcolo di regressione è stato ancora effettuato',
    'Regressione calcolata',
    'Grafico della seerie richiesto e visualizzato'
]

__status = 0

extractions_id = []  # Its the extraction numbers
extraction_number_1 = []  # index is e single extraction, list is number 1 extract
extraction_number_2 = []  # index is e single extraction, list is number 2 extract
extraction_number_3 = []  # index is e single extraction, list is number 3 extract
extraction_number_4 = []  # index is e single extraction, list is number 4 extract
extraction_number_5 = []  # index is e single extraction, list is number 5 extract
extraction_number_6 = []  # index is e single extraction, list is number 6 extract
extraction_date = []  # date of all extractions. In list like record
extractions_head = []  # Heading about extraction numbers


def load_click(full_file_path):
    """
    Find e file with data and load its
    :param full_file_path: full file path of data
    :return: error, 0=OK, >0 error in load data
    """
    global __status
    global extractions_id
    global extraction_date
    global extractions_head
    global extraction_number_1
    global extraction_number_2
    global extraction_number_3
    global extraction_number_4
    global extraction_number_5
    global extraction_number_6

    # check if correct path...
    if len(full_file_path) == 0 or full_file_path.isspace():
        return error_descriptions[1]

    try:
        excel = Classi.Excel_CSV.Excel()
        retcode = excel.load_excel_file(full_file_path, 'Estrazioni anno 2021', 4, 1, 1000, 10, 3)
        if retcode == 0:
            # Memo of extractions field...
            extraction_date.clear()
            extractions_id.clear()
            extraction_number_1.clear()
            extraction_number_2.clear()
            extraction_number_3.clear()
            extraction_number_4.clear()
            extraction_number_5.clear()
            extraction_number_6.clear()
            extractions_head.clear()

            for t in range(0, excel.columns_with_data):
                extractions_head.append(excel.title_columns[t])

            i = 0
            last = len(excel.cells_values)
            for r in range(0, last):
                extractions_id.append(excel.cells_values[i][0])
                extraction_date.append(excel.cells_values[i][1])
                extraction_number_1.append(excel.cells_values[i][2])
                extraction_number_2.append(excel.cells_values[i][3])
                extraction_number_3.append(excel.cells_values[i][4])
                extraction_number_4.append(excel.cells_values[i][5])
                extraction_number_5.append(excel.cells_values[i][6])
                extraction_number_6.append(excel.cells_values[i][7])
                i = i + 1

        __status = 1  # file loaded without errors and no regression calculation done
        del excel
        return retcode
    except Exception as error:
        return error


def calc_linear_regression():


    __status = 2  # Regression done
    return 0


def graph_regression():
    global __status
    plotter = Classi.Plotter.Plotter()
    if __status == 1:  # load data but not regression calc
        if plotter.load_axis(extractions_id, extraction_number_1) == 0:   # TEMP
            if plotter.plot() == 0:  # plotting...
                __status = 3  # Graph show
                return 0
            else:
                return 1

    if __status == 2:  # after regression calc
        if plotter.load_axis(extractions_id, extraction_number_1) == 0:  # TEMP
            if plotter.plot() == 0:  # plotting...
                __status = 3  # Graph show
                return 0
            else:
                return 1

    return 0