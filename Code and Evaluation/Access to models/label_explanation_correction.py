from hugchat import hugchat
from hugchat.login import Login
import pandas as pd
import time
from tqdm import tqdm
import csv
import re


class HuggingChat:
    """
    API for accessing HuggingChat
    List of models: https://huggingface.co/chat
    Requires email and password from https://huggingface.co to use
    """

    def __init__(
        self,
        email: str,
        password: str,
        system_prompt: str = "",
        cookie_path_dir: str = "./cookies_snapshot",
        model: str = "mistralai/Mixtral-8x7B-Instruct-v0.1",
    ):
        self.sign = Login(email, password)
        cookies = self.sign.login()
        self.sign.saveCookiesToDir(cookie_path_dir)
        self.chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
        # Check actual list of models on https://huggingface.co/chat/settings
        self.models = {
            "CohereForAI/c4ai-command-r-plus": 0,
            "meta-llama/Meta-Llama-3-70B-Instruct": 1,
            "HuggingFaceH4/zephyr-orpo-141b-A35b-v0.1": 2,
            "mistralai/Mixtral-8x7B-Instruct-v0.1": 3,
            "google/gemma-1.1-7b-it": 4,
            "NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO": 5,
            "microsoft/Phi-3-mini-4k-instruct": 6,
            "mistralai/Mistral-7B-Instruct-v0.2": 7,
        }
        self.system_prompt = system_prompt
        self.model = self.models[model]
        self.chatbot = hugchat.ChatBot(cookies=cookies.get_dict(), system_prompt=self.system_prompt)
        self.chatbot.switch_llm(self.model)
        self.chatbot.new_conversation(switch_to=True, system_prompt=self.system_prompt)

    def prompt(self, prompt: str) -> str:
        return str(self.chatbot.query(prompt))

    def delete_conversations(self) -> None:
        """
        Deletes all conversations in a user's profile
        """
        self.chatbot.delete_all_conversations()
        self.chatbot.new_conversation(switch_to=True,system_prompt=self.system_prompt)

    def switch_model(self, model: str) -> None:
        self.model = self.models[model]
        self.chatbot.switch_llm(self.model)
        self.chatbot.new_conversation(switch_to=True,system_prompt=self.system_prompt)

    def switch_system_prompt(self, system_prompt: str) -> None:
        self.system_prompt = system_prompt

# Работаем с датасетом

file_path = "in_domain_dev.tsv"
sentences = []
answers = []

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split("\t")
        sentences.append(parts[3])
        answers.append(parts[1])


# Создаем свой файл
# Список заголовков столбцов
#headers = ['label', 'explanation', 'correction']

# Имя файла для записи
filename = "your tsv file name"

# Запись заголовков столбцов в файл
with open(filename, 'w', encoding="utf-8", newline='') as file:
    writer = csv.writer(file, delimiter='\t')
    writer.writerow(headers)

mistral_hugginchat = HuggingChat("your hugging face nickname", "your hugging face password", model="name of the model",
                                 system_prompt='your prompt')

for sentence in tqdm(sentences):
    label = "Nothing"
    explanation = "Nothing"
    correction = "Nothing"
    while label == "Nothing" or explanation == "Nothing" or correction == "Nothing":
        try:
            time.sleep(8)
            data = mistral_hugginchat.prompt(sentence) 
            data = data.replace('\n\n', ' ')
            data = data.replace('\n', ' ')
            print(data)
            label_match = re.search(r'Label:.+(\d+).+Explanation:', data)
            explanation_match = re.search(r'Explanation:(.+?)Correct Sentence:', data)
            correct_sentence_match = re.search(r'Correct Sentence:(.+)', data)

            label = label_match.group(1).strip()
            explanation = explanation_match.group(1).strip()
            correction = correct_sentence_match.group(1).strip().replace('Correct Sentence: ', '')

        except Exception as e:
            print(e)
            label = "Nothing"
            explanation = "Nothing"
            correction = "Nothing"
            try:
                time.sleep(2)
                mistral_hugginchat.delete_conversations()
            except Exception as e:
                try:
                    time.sleep(2)
                    mistral_hugginchat.delete_conversations()
                except Exception as e:
                    time.sleep(2)
                    mistral_hugginchat.delete_conversations()

    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{label}\t{explanation}\t{correction}\n")

    try:
        time.sleep(2)
        mistral_hugginchat.delete_conversations()
    except Exception as e:
        try:
            time.sleep(2)
            mistral_hugginchat.delete_conversations()
        except Exception as e:
            time.sleep(2)
            mistral_hugginchat.delete_conversations()
