# import pytest
# from src.lesson_5 import shorten_words
#
#
# # Тестируемая функция
# @shorten_words(4, end_symbol='!')
# def get_text():
#     return "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
#
#
# # Тесты
# def test_shortening():
#     assert get_text() == "Lore! ipsu! dolo! sit amet, cons! adip! elit!"
#
#
# def test_no_shortening():
#     @shorten_words(10, end_symbol='!')
#     def get_long_text():
#         return "Lorem ipsum dolor sit amet"
#     assert get_long_text() == "Lorem ipsum dolor sit amet"
#
#
# def test_end_symbol():
#     @shorten_words(3, end_symbol='?')
#     def get_questioned_text():
#         return "Lorem ipsum dolor"
#     assert get_questioned_text() == "Lor? ips? dol?"
#
#
# def test_different_lengths():
#     @shorten_words(5, end_symbol='.')
#     def get_different_length_text():
#         return "Hello beautiful world"
#     assert get_different_length_text() == "Hello beaut. world"
