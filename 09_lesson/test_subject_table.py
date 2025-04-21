from sqlalchemy import create_engine, text

# строка подключения к вашей базе данных
db_connection_string = "postgresql://postgres:684000@localhost:5432/QA"
db = create_engine(db_connection_string)


# Добавление сущности (предмет Swimming)
def test_insert():
    connection = db.connect()
    transaction = connection.begin()
    sql = text("insert into subject (\"subject_title\") values (:new_name)")
    connection.execute(sql, {"new_name": "Swimming"})

    transaction.commit()
    connection.close()


# Обновление сущности (добавлен ID для предмета Swimming)
def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql = text(
        "update subject set subject_id = :id where subject_title = :new_name"
    )
    connection.execute(sql, {"id": 16, "new_name": 'Swimming'})

    transaction.commit()
    connection.close()


# Удаление сущности (удален предмет Swimming)
def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("delete from subject where subject_id = :id")
    connection.execute(sql, {"id": 16})

    transaction.commit()
    connection.close()
