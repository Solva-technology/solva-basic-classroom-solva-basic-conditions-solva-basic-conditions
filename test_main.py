import pytest
from unittest.mock import patch
from io import StringIO
import main

# Тесты для ask_for_age()

@pytest.mark.parametrize("age_input, expected_output", [
    ("25", "Вы совершеннолетний\n"),
    ("18", "Вы совершеннолетний\n"),
    ("17", "Вы несовершеннолетний\n"),
    ("10", "Вы несовершеннолетний\n"),
])
def test_ask_for_age(age_input, expected_output):
    """Тестирует функцию ask_for_age с разными значениями возраста."""
    with patch('builtins.input', return_value=age_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main.ask_for_age()
            assert fake_out.getvalue() == expected_output

# Тесты для check_password()

@pytest.mark.parametrize("password_input, expected_output", [
    ("secret", "Пароль верный\n"),
    ("password", "Пароль неверный\n"),
    ("12345", "Пароль неверный\n"),
])
def test_check_password(password_input, expected_output):
    """Тестирует функцию check_password с верным и неверным паролями."""
    with patch('builtins.input', return_value=password_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main.check_password()
            assert fake_out.getvalue() == expected_output

# Тесты для check_temperature()

@pytest.mark.parametrize("temp_input, expected_output", [
    ("10", "Холодно\n"),
    ("14", "Холодно\n"),
    ("15", "Тепло\n"),
    ("20", "Тепло\n"),
    ("25", "Тепло\n"),
    ("26", "Жарко\n"),
    ("30", "Жарко\n"),
])
def test_check_temperature(temp_input, expected_output):
    """Тестирует функцию check_temperature с разными температурами."""
    with patch('builtins.input', return_value=temp_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main.check_temperature()
            assert fake_out.getvalue() == expected_output

# Тесты для check_login_and_password()

@pytest.mark.parametrize("inputs, expected_output", [
    (["admin", "password123"], "Доступ разрешен\n"),
    (["user", "password123"], "Доступ запрещен\n"),
    (["admin", "wrongpassword"], "Доступ запрещен\n"),
    (["user", "wrongpassword"], "Доступ запрещен\n"),
])
def test_check_login_and_password(inputs, expected_output):
    """Тестирует функцию check_login_and_password с разными логинами и паролями."""
    with patch('builtins.input', side_effect=inputs):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main.check_login_and_password()
            assert fake_out.getvalue() == expected_output
