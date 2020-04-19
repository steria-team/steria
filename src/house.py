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

    def answer(self):
        if self.street is None:
            return self._ask_street()
        if self.number is None:
            return self._ask_address()

        return self._get_info_house()

    def _ask_address(self):
        return 'Назовите номер дома? Например, 7'

    def _ask_street(self):
        return 'Какая улица вас интересует? Например, Кавалергардская'

    def set_answer(self, text: str):
        if self.street is None:
            self.street = text
        elif self.number is None:
            self.number = text

    def _get_info_house(self):
        house_info = "1973: Пирожковая - ул. Красной конницы, 10 ([211]. С.187) \n" \
"1980: Пирожковая - ул. Красной конницы, 10 (Краткий телефонный справочник ЛГТС. 1980 г. С.311) \n" \
"1986: Пирожковая - ул. Красной конницы, 10 ([212]. С.280) \n" \
"1988: Пирожковая - ул. Красной конницы, 10 ([125],[213]. С.340) \n" \
"2004: \"Ретро\" кафе - Кавалергардская ул., 10 (Телефонный справочник «Весь Петербург-2004»)"
        return house_info