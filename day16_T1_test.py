from day16_T1 import main, top_asked_words, get_unique_words, counter_parsed_txt, parse_txt_file
import pytest
import sys

def test_counter_parsed_txt():
    list1 = ['hello', 'i', 'am', 'alireza', 'and', 'i', 'am', 'a', 'programmer']
    assert counter_parsed_txt(list1) == {'i': 2, 'am': 2, 'and': 1, 'alireza': 1, 'a': 1, 'programmer': 1, 'hello': 1}

def test_get_unique_words():
    list1 = ['hello', 'i', 'am', 'alireza', 'and', 'i', 'am', 'a', 'programmer']
    assert get_unique_words(list1) == {'hello', 'i', 'am', 'alireza', 'and', 'a', 'programmer'}

def test_top_asked_words():
    dict1 = {'a': 3, 'b': 2, 'c': 1}
    assert top_asked_words(100, dict1) == {'a': 3, 'b': 2, 'c': 1}
    assert top_asked_words(2, dict1) == {'a': 3, 'b': 2}

def test_parse_txt_file(tmp_path):
    file_path = tmp_path / "tmp.txt"
    file_path.write_text("Hello I am Alireza.", encoding="utf-8")

    result = parse_txt_file(str(file_path))
    assert result == ['hello', 'i', 'am', 'alireza']

def test_parse_file_txt_empty(tmp_path):
    file_path = tmp_path / "tmp1.txt"
    file_path.write_text("", encoding="utf-8")

    result = parse_txt_file(str(file_path))
    assert result == []

def test_main_successfull(tmp_path, monkeypatch):
    file_path = tmp_path / "tmp2.txt"
    file_path.write_text("Hello I am Alireza and I am a python programmer.")

    replaced_argv = ["day16_T1.py", str(file_path), "--top", "3"]
    monkeypatch.setattr(sys, "argv", replaced_argv)

    unique_words, asked_words = main()
    assert unique_words == {'hello', 'i', 'am', 'alireza', 'and', 'a', 'python', 'programmer'}
    assert asked_words == {'i': 2, 'am': 2, 'hello': 1}


def test_main_non_existing_file(tmp_path, monkeypatch):
    non_existing_file = tmp_path / "does_not_exist.txt"

    fake_argv = ["day16_T1.py", str(non_existing_file), "--top", "3"]
    monkeypatch.setattr(sys, "argv", fake_argv)

    with pytest.raises(FileNotFoundError) as e:
        main()
    assert f"File '{non_existing_file}' not found!" in str(e.value)

def test_main_empty_file(tmp_path, monkeypatch):
    empty_file = tmp_path / "empty_file.txt"
    empty_file.write_text("", encoding="utf-8")

    empty_argv = ["day16_T1.py", str(empty_file)]
    monkeypatch.setattr(sys, "argv", empty_argv)

    with pytest.raises(ValueError) as e:
        main()
    assert "Text file is empty!" in str(e.value)