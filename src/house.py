import os
import pathlib
import typing
import enum

import lxml
import lxml.html

DIR_SCRIPT: pathlib.Path = pathlib.Path(os.path.dirname(os.path.realpath(__file__)))


class NotFoundInfoHouse(Exception):
    pass


class Subjects(enum.Enum):
    STREET = 0
    HELP = 1
    NUMBER = 2


class House:
    def __init__(self):
        self.street = None
        # todo: rename number
        self.number = None
        self._prev_subject: typing.Union[Subjects, None] = None

    # def ask(self):
    #     if self.street is None:
    #         self._change_subject(subject=Subjects.STREET)
    #         return self._ask_street()
    #     elif self.number is None:
    #         self._change_subject(subject=Subjects.NUMBER)
    #         return self._ask_number()
    #     else:
    #         return f'Ваша улица {self.street}, а дом {self.number}'

    def answer(self):
        if self._prev_subject == Subjects.HELP:
            return self._ask_street()
        elif self._prev_subject == Subjects.STREET:
            return self._ask_number()

        try:
            info: str = self._get_info_house()
            self._change_subject(subject=Subjects.HELP)
        except NotFoundInfoHouse:
            info: str = 'Возникла ошибка, попробуйте еще раз.'
            self.reset()
            self.help()

        return info

    def help(self):
        self._change_subject(subject=Subjects.HELP)
        return "Скажи 'СБРОС' если произойдет ошибка. Хорошо?"

    def _change_subject(self, subject: Subjects) -> typing.NoReturn:
        self._prev_subject = subject

    def _ask_number(self):
        self._change_subject(subject=Subjects.NUMBER)
        return 'Назовите номер дома? Например, 7'

    def _ask_street(self):
        self._change_subject(subject=Subjects.STREET)
        return 'Какая улица вас интересует? Например, Кавалергардская'

    def parse_response(self, text: str):
        if self._prev_subject == Subjects.STREET:
            text = f'{text[0].upper()}{text[1:]}'
            self.street = text
        elif self._prev_subject == Subjects.NUMBER:
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

    def reset(self):
        self.street = None
        self.number = None
