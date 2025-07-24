import json

import pytest

from src.utils import read_json_file


# Фикстура для создания временного файла
@pytest.fixture
def temp_json_file(tmp_path):
    """Создает временный JSON-файл для тестов."""

    def create_file(content):
        file_path = tmp_path / "test.json"
        with open(file_path, "w", encoding="UTF-8") as f:
            json.dump(content, f)
        return str(file_path)

    return create_file


def test_read_json_file_valid_data(temp_json_file):
    """Проверка чтения корректного JSON-файла с данными."""
    data = [{"name": "Apple", "price": 1.99}, {"name": "Banana", "price": 0.99}]
    file_path = temp_json_file(data)
    result = read_json_file(file_path)
    assert result == data


def test_read_json_file_empty_file(temp_json_file, capsys):
    """Проверка чтения пустого JSON-файла."""
    file_path = temp_json_file([])
    result = read_json_file(file_path)
    captured = capsys.readouterr()
    assert result == []
    assert "Файл содержит пустой список" in captured.out


def test_read_json_file_invalid_json(temp_json_file, capsys):
    """Проверка обработки некорректного JSON."""
    file_path = temp_json_file(None)  # Создаем файл с некорректным JSON
    with open(file_path, "w", encoding="UTF-8") as f:
        f.write("invalid json")  # Записываем некорректный JSON
    result = read_json_file(file_path)
    captured = capsys.readouterr()
    assert result == []
    assert "Невозможно декодировать JSON-данные" in captured.out


def test_read_json_file_not_found(capsys):
    """Проверка обработки отсутствующего файла."""
    result = read_json_file("non_existent_file.json")
    captured = capsys.readouterr()
    assert result == []
    assert "Файл не найден" in captured.out


def test_read_json_file_not_list(temp_json_file, capsys):
    """Проверка обработки JSON, содержащего не список."""
    data = {"name": "Apple", "price": 1.99}  # Не список
    file_path = temp_json_file(data)
    result = read_json_file(file_path)
    captured = capsys.readouterr()
    assert result == []
    assert "Тип объекта в файле не список" in captured.out


def test_read_json_file_encoding(temp_json_file):
    """Проверка чтения файла с корректной кодировкой UTF-8."""
    data = [{"name": "Яблоко", "price": 1.99}]  # Используем кириллицу
    file_path = temp_json_file(data)
    result = read_json_file(file_path)
    assert result == data
