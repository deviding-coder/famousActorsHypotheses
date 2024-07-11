# Используя базу данных фильмов, необходимо проверить следующие гипотезы:
# 1) Большинство фильмов выпускаются по пятницам
# 2) Известные актеры снимаются в самых кассовых фильмах
# 3) Известные актеры снимаются в самыx дорогих фильмах

import sys
import os
import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# sys.path.append('../models')
# sys.path.append('../data')

FILE_PATH = './data'

os.listdir(FILE_PATH)

warnings.filterwarnings('ignore')

df = pd.read_csv(f'{FILE_PATH}/movies_metadata.csv')

# информация о дате выхода фильма есть у 45379 из 45466
# воспользуемся функцией df.dropna() для удаления строк со значением NaN
df.dropna(subset='release_date', inplace=True)

# составим колонку release_weekday с днем недели выхода фильма
df['release_weekday'] = pd.to_datetime(df['release_date'], errors='coerce').dt.day_of_week

# выведем информацию с процентами фильмов по дням недели
print(f"Процент фильмов, вышедших в понедельник: {(len(df[df['release_weekday'] == 0.0]) / len(df) * 100):.2f}% ({len(df[df['release_weekday'] == 0.0])} фильмов)")
print(f"Процент фильмов, вышедших во вторник: {(len(df[df['release_weekday'] == 1.0]) / len(df) * 100):.2f}% ({len(df[df['release_weekday'] == 1.0])} фильмов)")
print(f"Процент фильмов, вышедших в среду: {(len(df[df['release_weekday'] == 2.0]) / len(df) * 100):.2f}% ({len(df[df['release_weekday'] == 2.0])} фильмов)")
print(f"Процент фильмов, вышедших в четверг: {(len(df[df['release_weekday'] == 3.0]) / len(df) * 100):.2f}% ({len(df[df['release_weekday'] == 3.0])} фильмов)")
print(f"Процент фильмов, вышедших в пятницу: {(len(df[df['release_weekday'] == 4.0]) / len(df) * 100):.2f}% ({len(df[df['release_weekday'] == 4.0])} фильмов)")
print(f"Процент фильмов, вышедших в субботу: {(len(df[df['release_weekday'] == 5.0]) / len(df) * 100):.2f}% ({len(df[df['release_weekday'] == 5.0])} фильмов)")
print(f"Процент фильмов, вышедших в воскресенье: {(len(df[df['release_weekday'] == 6.0]) / len(df) * 100):.2f}% ({len(df[df['release_weekday'] == 6.0])} фильмов)")

# составим колонку weekday_name для более ясного представления гистограммы количества фильмов по дням недели
df['weekday_name'] = ""
weekday_name_list = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
weekday_count = [0, 0, 0, 0, 0, 0, 0]
df.loc[df['release_weekday'] == 0.0, 'weekday_name'] = "Понедельник"
df.loc[df['release_weekday'] == 1.0, 'weekday_name'] = "Вторник"
df.loc[df['release_weekday'] == 2.0, 'weekday_name'] = "Среда"
df.loc[df['release_weekday'] == 3.0, 'weekday_name'] = "Четверг"
df.loc[df['release_weekday'] == 4.0, 'weekday_name'] = "Пятница"
df.loc[df['release_weekday'] == 5.0, 'weekday_name'] = "Суббота"
df.loc[df['release_weekday'] == 6.0, 'weekday_name'] = "Воскресенье"

# построим гистограмму
plt.hist(df['weekday_name'], color = 'blue', edgecolor = 'black', bins = int(180/5))
plt.show()