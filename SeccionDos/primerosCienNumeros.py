class PrimerosCienNumeros:
    def __init__(self):
        self.numbers = set(range(1, 101))  # Conjunto de los primeros 100 números naturales
        self.extracted_number = None

    def extract(self, number):
        if number not in self.numbers: #Si no esta dentro de los números incluidos
            raise ValueError("Numero no valido o ya extraido.")
        self.numbers.remove(number)
        self.extracted_number = number

    def calculate_extract_number(self):
        if self.extracted_number is None: 
            raise ValueError("No se ha extraido ningun numero.")
        return self.extracted_number
