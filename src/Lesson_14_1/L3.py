"""3. Классы и объекты"""


class Employee:
    pass



emp_1 = Employee()          # () - это инициализация класса
emp_2 = Employee()

print(emp_1)        # <__main__.Employee object at 0x000001DFEE2E7890>  - 2 разных объекта
print(emp_2)        # <__main__.Employee object at 0x000001DFEE2E7800>

# ======================== работа с атрибутами ================================
emp_1.name = "Ivan"     # присваивание атрибута ИМЯ
emp_1.surname = "Ivanov"
emp_1.email = "Ivaniv.Ivan@email.com"
emp_1.pay = 50+000


emp_2.name = "Petr"     # присваивание атрибута ИМЯ
emp_2.surname = "Petrov"
emp_2.email = "Petr.Petrov@email.com"
emp_2.pay = 60_000



print(emp_1.name)

