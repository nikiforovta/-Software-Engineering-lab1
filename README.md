# Software-Engineering-lab
[![Python application](https://github.com/nikiforovta/Software-Engineering-lab1/actions/workflows/python-app.yml/badge.svg)](https://github.com/nikiforovta/Software-Engineering-lab1/actions/workflows/python-app.yml)
## Лабораторные работы по курсу основ программной инженерии

### Запуск скрипта напрямую

Разрабатываемый в рамках данной лабораторной работы сервис является конвертером градусов Цельсия в градусы Фаренгейта.
Для получения результата необходимо передать входные данные в командной строке. Примеры входных данных:

- конвертация 30 градусов Цельсия в градусы Фаренгейта

```
>>>python main.py
>>>30
You entered:    30.0 °C
Result: 86.000 °F
 ```

- аналогичный результат

``` 
>>>python main.py
>>>-C 30
You entered:    30.0 °C
Result: 86.000 °F
```

- конвертация 30 градусов Фаренгейта в градусы Цельсия

``` 
>>>python main.py
>>>-F 30
You entered:    30.0 °F
Result: -1.111 °С
```

- конвертация нескольких температурных показателей в градусы Фаренгейта.

``` 
>>>python main.py 
>>>30 65 102.148
You entered:    30.0 °C
Result: 86.000 °F
You entered:    65.0 °C
Result: 149.000 °F
You entered:    102.148 °C
Result: 215.866 °F
``` 

### Запуск скрипта в контейнере

Для получения работающего сервиса необходимо запустить следующую команду:
```docker build .```

Для запуска собранного образа необходимо воспользоваться командой:
```docker run -it <image name>```, где image name - имя собранного образа.

Далее работа со скриптом аналогична описанной в предыдущем разделе.
