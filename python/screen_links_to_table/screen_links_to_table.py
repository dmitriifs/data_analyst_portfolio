#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd
import json


# In[27]:


#Считываем файлы, выдаем сообщения об ошибках при неудаче

while True:
    try:
        path_json = input("Введите название json файла (без расширения): ") + '.json'
        with open(path_json, 'r', encoding='utf-8') as file:
            df = json.load(file)
            df = pd.DataFrame(df)
            print("Файл успешно загружен")
        break
    except Exception as e:
        print(f'Произошла ошибка: {e}. Пожалуйста, попробуйте снова.')



# In[65]:


#Заменяем строки с названием файла на цифры для последующей фильтрации по возрастанию

df['initialFileName'] = df['initialFileName'].str.replace(r'\D', '', regex=True) #'\D' - регулярное выражение для поиска нецифровых символов, regex=True заменяет
df['initialFileName'] = df['initialFileName'].astype('int')


# In[77]:


df = df.sort_values(by='initialFileName')


# In[71]:


output_excel = input("Введите название excel файля для экспорта (без расширения): ")


# In[75]:


df.to_excel(output_excel+'.xlsx', index=False)


# In[ ]:


input("Скрипт успешно выполнен. Нажмите enter для выхода...")