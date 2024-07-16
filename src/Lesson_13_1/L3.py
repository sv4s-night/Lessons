import pandas as pd
"""3. Создание и чтение данных в pandas"""


# Создание двумерной таблицы DataFrame
df = pd.DataFrame({'Yes': [50, 22, 25],
                  'No': [131, 2, 100]})
print(df["Yes"][0])
print(df["No"])     # так же будет выведена таблица Name: No, dtype: int64
# print(df)


df1 = pd.DataFrame({'Bob': ["KSMFM", "SL:ME"], "Sue": ["mge", "sea"]})
# print(df1)


# excel_data = pd.read_excel('example_data.xlsx')
# print(excel_data.share)  #
# print(excel_data.head)  #

# если в excel файле несколько страниц, то можно выбрать из какой страницы берется таблица
# excel_data_spec_sheet = pd.read_excel('example_data.xlsx', sheet_name="Sheet2")
# print(excel_data_spec_sheet)

# так же можно указать столбец, который след исп в качестве индекса
# excel_data_spec_sheet = pd.read_excel("example_data.xlsx", index_col=0)
# print(excel_data_spec_sheet)

df2 = pd.read_excel("../../data/winemag-data-130k-v2.xlsx")
print(df2.shape)        # вывод кол-во строк и столбцов (129971, 14)
print(df2.head())       # вывод первых 5и строк [5 rows x 14 columns]




