from src.tasktracker.service import create_task, complete_task, delete_task, list_tasks


def test_create_task():
    task = create_task("New task")
    assert task.id == 1
    assert task.text == "New task"
    assert not task.completed


def test_complete_task():
    task = create_task("To complete")
    completed = complete_task(task.id)
    assert completed.completed
    assert completed.id == task.id


def test_list_tasks():
    create_task("First")
    create_task("Second")
    tasks = list_tasks()
    assert len(tasks) == 2
    texts = [t.text for t in tasks]
    assert "First" in texts and "Second" in texts


def test_delete_task():
    t1 = create_task("Del 1")
    t2 = create_task("Del 2")
    delete_task(t1.id)
    remaining = list_tasks()
    ids = [t.id for t in remaining]
    assert t1.id not in ids
    assert t2.id in ids
