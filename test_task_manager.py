from asyncio import tasks

import main
from unittest.mock import Mock

def test_add_task(monkeypatch):
    fake_save = Mock()
    tasks = []
    monkeypatch.setattr("builtins.input", lambda _: "Изучить pytest")
    monkeypatch.setattr(main, "save_tasks", fake_save)
    main.add_task(tasks)
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Изучить pytest"
    assert tasks[0]["completed"] == False
    assert fake_save.call_count == 1
    fake_save.assert_called_once_with(tasks)


def test_add_task_empty(monkeypatch):
    fake_save = Mock()
    tasks = []

    monkeypatch.setattr("builtins.input", lambda _: "   ")
    monkeypatch.setattr(main, "save_tasks", fake_save)
    main.add_task(tasks)
    assert len(tasks) == 0
    fake_save.assert_not_called()

def test_complete_task(monkeypatch):
    tasks = [
        {"title": "Изучить Python", "completed": False}
    ]
    fake_save = Mock()
    monkeypatch.setattr(main, "show_tasks", lambda _: None)
    monkeypatch.setattr(main, "get_task_index", lambda _: 0)
    monkeypatch.setattr(main, "save_tasks", fake_save)
    main.complete_task(tasks)
    assert tasks[0]["completed"] == True
    fake_save.assert_called_once_with(tasks)

def test_complete_task_already_completed(monkeypatch):
    tasks = [
        {"title": "Изучить Python", "completed": True}
    ]
    fake_save = Mock()
    monkeypatch.setattr(main, "show_tasks", lambda _: None)
    monkeypatch.setattr(main, "get_task_index", lambda _: 0)
    monkeypatch.setattr(main, "save_tasks", fake_save)
    main.complete_task(tasks)
    fake_save.assert_not_called()

def test_delete_task(monkeypatch):
    tasks = [
        {"title": "Изучить Python", "completed": False},
        {"title": "Изучить pytest", "completed": True}
    ]
    fake_save = Mock()
    monkeypatch.setattr(main, "show_tasks", lambda _: None)
    monkeypatch.setattr(main, "get_task_index", lambda _: 1)
    monkeypatch.setattr(main, "save_tasks", fake_save)
    main.delete_task(tasks)
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Изучить Python"
    fake_save.assert_called_once_with(tasks)

def test_delete_task_invalid_index(monkeypatch):
    tasks = [
        {"title": "Изучить Python", "completed": False},
        {"title": "Изучить pytest", "completed": True}
    ]
    tasks1 = tasks.copy()
    fake_save = Mock()
    monkeypatch.setattr(main, "show_tasks", lambda _: None)
    monkeypatch.setattr(main, "get_task_index", lambda _: None)
    monkeypatch.setattr(main, "save_tasks", fake_save)
    main.delete_task(tasks)
    assert tasks1 == tasks
    fake_save.assert_not_called()