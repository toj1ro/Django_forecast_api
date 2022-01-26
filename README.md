# Django_forecast_api

Чтобы развернуть проект в дериктории с файлом manage.py введите команды:\
`$sudo docker-compose build`\
`$sudo docker-compose up`

Проект представляет из себя два отдельных приложения. Чтобы пользоваться API нужно пройти авторизацию для начала
отправить пост запрос со своими учетными данными по адресу:\

`http://0.0.0.0:8000/api/auth/users/`

Запрос должен содержать json вида: \
`{
"username":{ваше имя пользователя},
"password":{ваш пароль} }`

После чего получите токен авторизации, передав свои данные по адресу: \
`http://0.0.0.0:8000/api/auth/token`

Последующие запросы к **/api/get_city_forecast/** выполняются с Authorization Header вида:   
Token 50e2fb2d5be34595c36ecef2e01a3a6c9d4f8485

Запрос для получения прогноза погоды в городе Москва в цельсиях будет выглядить следущию образом  

`http://0.0.0.0:8000/api/get_city_forecast/?city=Moscow&temp_format=C`  

Аргумент `temp_format`   принимает С для возврата температуры в градусах Цельсия и F для возврата температуры в градусах Фаренгейта 
по умалчанию вернет температуру в Кельвинах 


Для получения статистики по 100 самым большим городам используйте метод:   

`http://0.0.0.0:8000/api/get_weather_stat/`  

Принимает два аргумента `start_time`, `end_time` в формате `YYYY-MM-DDTHH:MM:SS` пример запросы:  

`http://0.0.0.0:8000/api/get_weather_stat/?start_time=2020-01-02T21:08:02&end_time=2022-12-02T21:08:02` 
