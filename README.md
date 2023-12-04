# sof-_engr_for_130962_gr_2.9
*This is the prject for course  SoftwareEngeneers*

## authors:
1. Сергеев В.В. (мск), tg: @vlvase
2. Запатоцкий Ю.М. (мск) tg: @VirtusTex

## Home work 1
### Запатоцкий Ю.М.
Приложение для перевода основанное на предобученной модели с Huggingface

Для запуска необходимо изменить переменную text и выполнить следующий код
```
python ./hw1/translator.py
```
Результат перевода выведится на экран

### Сергеев В.В.
Приложение для распознования  изображений основанное на предобученной модели с Huggingface

Для запуска необходимо изменить переменную url и выполнить следующий код
```
python ./hw1/img_clsf_model.py
```
Результат перевода выведится на экран

## Home work 2
### Запатоцкий Ю.М., Сергеев В.В.
Приложение для классификации изображения основанное на предобученной модели

Для запуска необходимо выполнить следующий код
```
streamlit run ./hw2/predictions.py
```
Открыть в браузере адрес http://localhost:8501/

Загрузить картинку

![Screenshot 1](https://github.com/vvsergey/sof-_engr_for_130962_gr_2.9/blob/main/hw2/screenshot-1.png)
Нажать кнопку "Распознать изображение"

Результат классификации выведится на экран

![Screenshot 2](https://github.com/vvsergey/sof-_engr_for_130962_gr_2.9/blob/main/hw2/screenshot-2.png)

## Home work 3
### Запатоцкий Ю.М., Сергеев В.В.
Приложение с реализацией API для классификации текста на предмет позитивного или негативного настроения.

Для запсука необходимо перейти в папку hw3 из корня проекта
```
cd hw3
```
Запустить приложение
```
uvicorn predict_with_api:app
```
Открыть запущенное приложение по адресу http://127.0.0.1:8000/docs

Раскрать строку "POST /predict"

Нажать кнопку "Try it out" справа

В поле "Example value" вместо строки text вставить свой текст для классификации

Нажать кнопку "Execute" снизу

В блоке "Server response" в блоке "Response body" будет результат классификации

В ключе "label" находится лейбл оценки, позитивная она или нет

В ключе "score" находится оценка вероятности классификации текста этому лейблу

## Home work 4
### Запатоцкий Ю.М., Сергеев В.В.
Приложение для классификации изображения основанное на предобученной модели

загруженной в облачный хостинг сервиса streamlit

Для запуска необходимо перейти на сайт https://softwareengineering-gvyhhqkrbuxpgk2zejc5sx.streamlit.app/

Загрузить картинку

![Screenshot 1](https://github.com/vvsergey/sof-_engr_for_130962_gr_2.9/blob/main/hw4/screenshot-1.png)
Нажать кнопку "Распознать изображение"

Результат классификации выведится на экран

![Screenshot 2](https://github.com/vvsergey/sof-_engr_for_130962_gr_2.9/blob/main/hw4/screenshot-2.png)

## Comamnds for linux:
- $ sudo apt insatall pip
- $ ssh-keygen -o
- $ cat ~/.ssh/id_rsa.pub 

### создание виртуального окружения
- $ sudo apt install python3.10-venv
- $ python3 -m venv venv_name
- $ source venv_name/bin/activate
- $ deactivate


### работа с GIT
- $ sudo apt install git
- $ git clone git@github.com:vvsergey/sof-_engr_for_130962_gr_2.9.git
- $ git pull origin master   *(забрать изменения с удаленного репозитория)*
- $ git add .
- $ git commit -m "add "
- $ git push -u origin main


### Установка пакетов python
- pip install
- pip freeze requirements.txt


