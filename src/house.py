class House:
    def __init__(self):
        self.street = None
        # todo: rename number
        self.address = None

    def ask(self):
        if self.street is None:
            return self._ask_street()
        elif self.address is None:
            return self._ask_address()
        else:
            return f'Ваша улица {self.street}, а дом {self.address}'

    def _ask_address(self):
        return 'Назовите номер дома? Например, 7'

    def _ask_street(self):
        return 'Какая улица вас интересует? Например, Кавалергардская'

    def set_answer(self, text: str):
        if self.street is None:
            self.street = text
        elif self.address is None:
            self.address = text