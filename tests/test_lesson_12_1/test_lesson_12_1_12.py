from src.Lesson_12_1.lesson_12_1_12 import add_week_to_dates, event_durations


def test_add_week_to_dates():
    """Задача 1"""
    assert add_week_to_dates(["2022.12.31", "2023.1.7"]) == ["January 7, 2023", "January 14, 2023"]
    assert add_week_to_dates([]) == []




def test_event_durations():
    """Задача 2"""
    json_str = ('[{"name": "Event 1", "start_date": "2022-01-01", "end_date": "2022-01-05"}, '
                '{"name": "Event 2", "start_date": "2022-02-15", "end_date": "2022-02-18"}, '
                '{"name": "Event 3", "start_date": "2022-03-10", "end_date": "2022-03-20"}]')
    assert event_durations(json_str) == [4, 3, 10]