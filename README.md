# steria

### Подготовка окружения

1. Создать рабочую директорию

```bash
mkdir steria-dev
cd steria-dev
```


1. Клонировать репозиторий   
```bash
git clone https://github.com/pen-dev/steria.git
```

2. Создать виртуальное окружение

Установка `virtualenv`:

```bash
pip3 install virtualenv
```

Создание окружения:

У меня был `python3.7`,  теоретически можно `python3.8`

```bash
virtualenv -p python3.7 venv
# активируем его
source vevn/bin/activate
```

3. Установка `requirements`:

```bash
cd steria
pip install -r requirements.txt
```

4. Запуск

[Перейти на сайт](https://alice-dev.vitalets.xyz/)

На устройстве с Алисой запустить навык командой
```
запусти навык инструменты разработчика
```

Соединить его с компьютером по инструкции

Запустить сервер:

```bash
cd steria/src
export FLASK_APP=api.py && export FLASK_ENV=development && export FLASK_DEBUG=0
python -m flask run
```

