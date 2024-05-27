from sklearn.metrics import accuracy_score, precision_score, recall_score, matthews_corrcoef
import pandas as pd

# Загрузка данныз из датасета
y_true = []
with open('path to the dataset - in_domain_dev.tsv', "r", encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split("\t")
        y_true.append(parts[1])

# Загрузка данных из tsv файла
file = 'path to our tsv file'
data = pd.read_csv(file, sep='\t')
y_pred = data['label'].tolist()

# Создаем списки чисел
y_true = [int(i) for i in y_true]
y_pred = [int(i) for i in y_pred]

# Рассчитываем метрики
accuracy = accuracy_score(y_true, y_pred)
mcc = matthews_corrcoef(y_true, y_pred)

print("Accuracy: ", accuracy)
print("Matthews correlation coefficient (MCC): ", mcc)
