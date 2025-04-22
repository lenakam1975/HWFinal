from sqlalchemy import create_engine, text

# строка подключения к вашей базе данных
db_connection_string = "postgresql://postgres:684000@localhost:5432/QA"
db = create_engine(db_connection_string)


# Добавление сущности (предмет Drawing)
def test_insert():
    connection = db.connect()
    transaction = connection.begin()
    sql = text("insert into subject (\"subject_title\") values (:new_name)")
    names = connection.execute(sql, {"new_name": "Drawing"})
    transaction.commit()

    result = connection.execute(text(
        "select subject_title from subject where subject_title = :new_name"),
        {"new_name": "Drawing"})
    row = result.fetchone()
    assert row[0] == 'Drawing'

    connection.close()


# Обновление сущности (добавлен ID для предмета Drawing)
def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql = text(
        "update subject set subject_id = :new_id where subject_id is NULL and subject_title = :title"
    )
    connection.execute(sql, {"new_id": 16, "title": "Drawing"})
    transaction.commit()

    result = connection.execute(text(
        "select subject_id from subject where subject_title = :title"),
        {"title": "Drawing"})
    row = result.fetchone()
    assert row[0] == 16

    connection.close()


# Удаление сущности (удален предмет Drawing)
def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("delete from subject where subject_id = :id")
    connection.execute(sql, {"id": 16})
    transaction.commit()

    result = connection.execute(text(
        "select * from subject where subject_id = :id"), {"id": 16})
    row = result.fetchone()
    assert row is None

    connection.close()
