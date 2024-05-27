# creating a file with random sentences
import pandas as pd
import random


cola_path = "path to the dataset - in_domain_dev.tsv"
dfc = pd.read_csv(cola_path, delimiter='\t', header=None)

file_path = "path to our tsv file"
dff = pd.read_csv(file_path, delimiter='\t')
headers = dff.columns.tolist()

data1 = {
    'dataset_labels': dfc[1],  # labels in dataset
    'file_labels': dff['label'],  # labels in our file
    'sentence': dfc[3]   # sentences
}
data = pd.DataFrame(data1)

filtered_sentences = data[(data['dataset_labels'] == 0) & (data['file_labels'] == 0)]['sentence']

random_sentences = random.sample(range(len(filtered_sentences)), 50)
df = filtered_sentences.iloc[random_sentences]


df.to_csv("path to the new tsv file", sep='\t', index=False)


path = "path to the new tsv file"
sentences_file = pd.read_csv(path, delimiter='\t')
sentences = sentences_file['sentence'].tolist()

dataframe1 = pd.DataFrame(columns=['input_sentence'])
dataframe2 = pd.DataFrame(columns=headers)

for index, line in dfc.iterrows():
  if line[3] in sentences:
    dataframe1.loc[len(dataframe1)] = [line[3]]
    info = dff.iloc[index]
    dataframe2.loc[len(dataframe2)] = info.values

result =  pd.concat([dataframe1, dataframe2], axis=1)

result.to_csv("path to the final file", sep='\t', index=False)
