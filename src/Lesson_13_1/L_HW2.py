import pandas as pd
import csv
import logging


logger = logging.getLogger("utils")
file_handler = logging.FileHandler("../logs/financial.log", encoding="utf-8")
f_fo = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(f_fo)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def open_csv_data(file: str) -> list[dict]:
    """Функция считывающая cvs файл и возвращающая список словарей"""
    with open(file, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        header_in = next(reader)
        result = []
        for index in reader:
            row_dict = {
                "id": index[header_in.index("id")],
                "state": index[header_in.index("state")],
                "date": index[header_in.index("date")],
                "operationAmount": {
                    "amount": index[header_in.index("amount")],
                    "currency": {
                        "name": index[header_in.index("currency_name")],
                        "code": index[header_in.index("currency_code")],
                    },
                },
                "description": index[header_in.index("description")],
                "from": index[header_in.index("from")],
                "to": index[header_in.index("to")],
            }
            result.append(row_dict)
    return result


def open_excel_data(file: str) -> list[dict]:
    """Функция считывает файл в формат excel и возвращающая список словарей"""
    df = pd.read_excel(file)
    result = []
    rows_count = len(df)
    for i in range(0, rows_count):
        row_dict = {
            "id": df.at[i, "id"],
            "state": df.at[i, "state"],
            "date": df.at[i, "date"],
            "operationAmount": {
                "amount": df.at[i, "amount"],
                "currency": {
                    "name": df.at[i, "currency_name"],
                    "code": df.at[i, "currency_code"],
                },
            },
            "description": df.at[i, "description"],
            "from": df.at[i, "from"],
            "to": df.at[i, "to"],
        }
        result.append(row_dict)
    return result


print(open_excel_data("../data/transactions_excel.xlsx"))