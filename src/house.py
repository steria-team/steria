class House:
    def __init__(self):
        self.street = None
        # todo: rename number
        self.number = None

    def ask(self):
        if self.street is None:
            return self._ask_street()
        elif self.number is None:
            return self._ask_address()
        else:
            return f'Ваша улица {self.street}, а дом {self.number}'

    def _ask_address(self):
        return 'Назовите номер дома? Например, 7'

    def _ask_street(self):
        return 'Какая улица вас интересует? Например, Кавалергардская'

    def set_answer(self, text: str):
        if self.street is None:
            self.street = text
        elif self.number is None:
            self.number = text