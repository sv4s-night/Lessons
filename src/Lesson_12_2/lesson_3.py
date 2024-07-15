import logging

# получаем корневой логер
logger = logging.getLogger()

# получаем сообщение уровня Error
logger.error("Это ошибка")

# получаем логер с определенным именем
named_logger = logging.getLogger("mylogger")

# логирует сообщение уровня Critical
named_logger.critical("Очень критично")


# Logger.setLevel() - назначает регистратору с какого уровня происходит логирование
# получает регистратор с именем mylogging
named_logger = logging.getLogger("mylogger")
named_logger.setLevel(logging.WARNING)  # с какого уровня будут выводиться сообщения (включительно)

# Выводит данное сообщение
named_logger.warning("Я предупреждаю вас")

# этого сообщения не будет
named_logger.info("FYI")

