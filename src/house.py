import os
import pathlib

import lxml
import lxml.html

DIR_SCRIPT: pathlib.Path = pathlib.Path(os.path.dirname(os.path.realpath(__file__)))


class NotFoundInfoHouse(Exception):
    pass


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

        try:
            info: str = self._get_info_house()
        except NotFoundInfoHouse:
            info: str = 'Error'
            self._reset()

        return info

    def _ask_address(self):
        return 'Назовите номер дома? Например, 7'

    def _ask_street(self):
        return 'Какая улица вас интересует? Например, Кавалергардская'

    def set_answer(self, text: str):
        if self.street is None:
            text = f'{text[0].upper()}{text[1:]}'
            self.street = text
        elif self.number is None:
            self.number = text

    def _get_info_house(self):
        text: str = '{header} \n {about}'
        header_xpath: str = f".//*[@class='address' and contains(., '{self.number}')]" \
                            f"/a[contains(text(), '{self.street}')]/parent::*/parent::*/parent::*/parent::*/h2"

        example_page_path: str = os.path.join(DIR_SCRIPT.parent, 'page_example', 'example2.html')
        with open(example_page_path, 'r', encoding='windows-1251') as f:
            html_text: str = f.read()

        tree: lxml.html.HtmlElement = lxml.html.fromstring(html=html_text)

        if len(tree.xpath(header_xpath)) == 0:
            raise NotFoundInfoHouse

        return tree.xpath(header_xpath)[0].text

    def _reset(self):
        self.street = None
        self.number = None
