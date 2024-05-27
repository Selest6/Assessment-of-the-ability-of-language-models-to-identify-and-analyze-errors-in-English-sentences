# Assessment-of-the-ability-of-language-models-to-identify-and-analyze-errors-in-English-sentences

Данный репозиторий содержит файлы, созданные в рамках исследования "Оценка способности языковых моделей определять и анализировать ошибки в предложениях на английском языке" (Assessment of the ability of language models to identify and analyze errors in English sentences).

Ссылка на работу: https://docs.google.com/document/d/1eBJRw6_vJSvrYBVraj9MxkbsRATttihZQ5jAkFUBdbw/edit?usp=sharing

В файле "All the results" находятся результаты всех запусков кода со всеми моделями и промптами и с посчитанным acc и mcc.

В файле "Average values" находится посчитанное среднее значение и среднеквадратичное отклонение во всех сценариях с ролью Teacher у обеих моделей.

В папке Code and Evaluation/Access to models находятся все коды с обращением к моделям, соответствующие разным сценариям.

В папке Code and Evaluation/Automatic Evaluation находится код для рассчёта mcc и acc, а также код для отбора случайных 50 предложений из файлов-аутпутов модели.

В папке Code and Evaluation/Human evaluation - Mixtral 7x8 находятся файлы с размеченными объяснениями модели.

В папке Code and Evaluation/Visualization находятся коды для визуализации данных, а в папке "Files for visualization" - файлы в удобном для прогона через код формате.

В папке Output files находятся все файлы-аутпуты моделей, распределённые по ролям и номеру запуска кода. В конце названия файлов написано, с каким сценарием этот файл прогонялся.

