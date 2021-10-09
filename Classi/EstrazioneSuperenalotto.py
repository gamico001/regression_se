"""
SUPERENALOTTO
Classe della singola estrazione, con metodi per creare l'elemento della serie (i 5 numeri dell'estrazione,
nel formato 1122334455), per estrapolare dall'elemento i 5 numeri, ecc.
"""


class Estrazione:
    """
    Methods and properties about one extraction
    number1.2.3.4.5 --> single number
    string_extraction --> cast number to string
    numbers_extraction --> single number that represent the 5 numbers of extraction
    numbers_list --> a list about numbers
    error --> retcode
    method send_numbers_about_single_extraction --> to pass e list of numbers
    """
    def __init__(self):
        self.number1 = 0
        self.number2 = 0
        self.number3 = 0
        self.number4 = 0
        self.number5 = 0
        self.number6 = 0
        self.string_extraction = ""
        self.numbers_extraction = 0
        self.numbers_list = []
        self.error = 0

    def send_numbers_about_single_extraction(self, numbers):
        """
        Send the 5 Superenalotto extraction numbers
        :param numbers: list about 5 Superenalotto extraction numbers
        :return: rec code operation; 0=ok, 1=error!
        """

        # numbers must be in the range 1-90...
        self.error = 0
        for i in numbers:
            if i < 1 or i > 90:
                self.error = 1
                break

        self.number1 = numbers[0]
        self.number2 = numbers[1]
        self.number3 = numbers[2]
        self.number4 = numbers[3]
        self.number5 = numbers[4]
        self.number6 = numbers[5]
        self.numbers_list = numbers
        self.__create_string_single_extraction(numbers)
        return self.error

    def __create_string_single_extraction(self, numbers):
        """
        Private Method. Cast from List numbers to format string
        :param numbers: List about extraction numbers
        :return: error. 0=ok, 1=KO
        """
        self.string_extraction = f'{numbers[0]:02}{numbers[1]:02}{numbers[2]:02}{numbers[3]:02}{numbers[4]:02}{numbers[5]:02}'

        if self.error == 1:
            print("Errore, numeri non congruenti")
        else:
            self.numbers_extraction = int(self.string_extraction)
            # Controllo che il numero non sia fuori degli estremi tra min e max ammessi. Non può attivarsi l'errore!
            # perché controllato prima che ogni numero sia nel range 1-90.
            if self.numbers_extraction < 10203040506 or self.numbers_extraction > 908988878685:
                self.error = 2
                print("Strana incongruenza del numeri: fuori range!")

            return self.error

    def from_string_extraction_to_number_list(self, string_extraction):
        """
        Return a list of number about one extraction
        :param string_extraction: string with extraction numbers sequence
        :return: a list of number
        """


