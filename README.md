# finec

Сайт факультета финансовой экономики МГИМО Одинцово

Исходные данные:

- https://odin.mgimo.ru/fakuprav (переделать адрес)
- http://pk.odin.mgimo.ru/ (приемная комиссия)


## Установка


Для запуска сайта на локальном компьютере требуется [python 3](https://www.python.org/) и 
генератор сайтов `mkdocs`:

<!--
```python get-pip.py``` or ```pip install --upgrade pip``` to update
-->

Установите mkdocs и необходимые зависимости:

```
pip install -r requirements.txt 
```

## Запуск 

Для тестирования на локальном компьютере запустите:

```
mkdocs serve
```

## Деплой

Сайт размещается по адресу https://finec-mgimo.github.io/

Деплой делается через репо https://github.com/finec-mgimo/finec-mgimo.github.io

Также есть возможность вывешивать страницу на адрес <https://epogrebnyak.github.io/finec/>. 
Рекомендуется делать это отдельным коммитом коммитом через скрипт `push.bat`.  
