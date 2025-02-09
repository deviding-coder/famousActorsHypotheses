# famousActorsTheories

Данный репозиторий содержит в себе анализ данных о фильмах, снятых до июля 2017 года посредством проверки трех гипотез:
1) Большинство фильмов выпускаются по пятницам
2) Известные актеры снимаются в самых кассовых фильмах
3) Известные актеры снимаются в самыx дорогих фильмах

В качестве обучающего датасета был выбран набор данных из 45000 фильмов, выпущенных в июле 2017 года или ранее. Данные включают актерский состав, съемочную группу, ключевые слова сюжета, бюджет, доходы, постеры, даты выхода, языки, производственные компании, страны, количество голосов на TMDB и средние значения голосов.

В этом наборе данных также есть файлы, содержащие 26 миллионов оценок от 270 000 пользователей для всех 45 000 фильмов. Оценки даны по шкале от 1 до 5 и были получены с официального веб-сайта GroupLens.

Также в наборе данных есть набор данных о [самых популярных актерах](https://www.imdb.com/list/ls524099236/)

## Гипотеза №1 (hypothesis1.py)
> Большинство фильмов выпускаются по пятницам

Путь к директории с данным хранятся в переменной FILE_PATH
```python
FILE_PATH = './data'
```

Читаем таблицу movies_metadata.csv из директории в директории FILE_PATH

```python
df = pd.read_csv(f'{FILE_PATH}/movies_metadata.csv')
```

Воспользуемся функцией df.dropna() для удаления строк со значением NaN в дате выхода
```python
df.dropna(subset='release_date', inplace=True)
```

Составим колонку release_weekday с днем недели выхода фильма
```python
df['release_weekday'] = pd.to_datetime(df['release_date'], errors='coerce').dt.day_of_week
```