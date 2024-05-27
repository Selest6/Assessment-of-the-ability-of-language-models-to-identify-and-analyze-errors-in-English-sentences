import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Загружаем эксель-файл с результатами
file_path = path to your xlsx file'
df = pd.read_excel(file_path)

# Удаляем ненужные колонки и готовим файл к работе
df_cleaned = df.drop(columns=['Ваше имя (опционально)', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15'])
df_cleaned.columns = ['lang', 'dataset', 'model_name', 'scenario', 'prompt', 'accuracy', 'mcc']

# Функция для создания хитмапа по acc и mcc
def plot_heatmap(df, metric, title):
    heatmap_data = df.pivot(index='scenario', columns='model_name', values=metric).round(4)
    plt.figure(figsize=(12, 6))
    sns.heatmap(heatmap_data, annot=True, fmt=".4f", cmap="YlGnBu", cbar=True)
    plt.title(title)
    plt.show()

# Хитмапы
plot_heatmap(df_cleaned, 'accuracy', 'Heatmap of Accuracy Across Scenarios and Models')
plot_heatmap(df_cleaned, 'mcc', 'Heatmap of MCC Across Scenarios and Models')
