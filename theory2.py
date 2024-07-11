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

sys.path.append('../data')

FILE_PATH = './data'

os.listdir(FILE_PATH)

warnings.filterwarnings('ignore')

df = pd.read_csv(f'{FILE_PATH}/movies_metadata.csv')

