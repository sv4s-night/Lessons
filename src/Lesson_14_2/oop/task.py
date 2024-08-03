import datetime


class Task:
    name: str
    description: str
    status: str
    created_at: str

    def __init__(self, name, description, status="Ожидает старта", created_at=None):
                                                                    # self - ссылка на экземпляр класса
        self.name = name
        self.description = description                            # descriptions - описание
        self.status = status
        self.__created_at = created_at if created_at else datetime.date.today().strftime("%d.%m.%Y")
        # created_at - дата создания (применяем библиотеку datetime) .strtime() - переводит из даты в строку
                                                                    # .date.today() - подставляет сегодняшную дату



    @classmethod        # класс метод, принимает на вход параметры и создает новую задачу
    def new_task(cls, name, description, status="Ожидает старта", created_at=None):
        return cls(name, description, status, created_at)



    @property
    def created_at(self):
        return self.__created_at    # тут нам надо возвращать атрибут в изначальном виде


    @created_at.setter
    def created_at(self, new_date: str):                                                                 # в данный сеттер будет передаваться новая дата, которую нам нужно передавать в нашем экземпляре
        if datetime.datetime.strptime(new_date, '%d.%m.%Y').date() < datetime.datetime.now().date():     # данная новая дата превосходит или ровна текущему числу иначе она не должна переопределяться и должно всплывать соотв сообщение
            print("Нельзя изменить дату создания на дату из прошлого")
            return
        self.__created_at = new_date
