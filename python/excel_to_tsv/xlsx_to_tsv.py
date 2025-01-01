#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd


# In[58]:


#Считываем файлы, выдаем сообщения об ошибках при неудаче

while True:
    try:
        path_csv = input("Введите название файла (с расширением): ")
        df = pd.read_excel(path_csv)
        print("Файл успешно загружен")
        break  #Прерывем цикл, если файл успешно загружен
    except FileNotFoundError:
        print('Файл не найден. Пожалуйста, попробуйте снова.')
    except pd.errors.EmptyDataError:
        print('Файл пуст. Пожалуйста, попробуйте снова.')
    except pd.errors.ParserError:
        print('Ошибка парсинга файла. Убедитесь, что файл действительно является TSV.')
    except Exception as e:
        print(f'Произошла ошибка: {e}. Пожалуйста, попробуйте снова.')


# In[60]:


output_tsv = input("Введите название файла для вывода (без расширения): ")


# In[62]:


output_mix = input("Перемешать строки (ответ 'да' или 'нет')? ")


# In[64]:


if output_mix == 'да':
    df = df.sample(frac=1).reset_index(drop=True)
else: 
    pass


# In[68]:


df.to_csv(output_tsv+'.tsv',  sep="\t", index=False)


# In[ ]:


input("Скрипт успешно выполнен. Нажмите enter для выхода...")

