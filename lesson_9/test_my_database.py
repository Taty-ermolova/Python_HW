from sqlalchemy import create_engine, inspect
from sqlalchemy import create_engine, text

db_connection_string = "postgresql://postgres:153624@localhost:5432/postgres"
db = create_engine(db_connection_string)


def test_select():
    connection = db.connect()
    result = connection.execute(text("SELECT * FROM student"))
    rows = result.mappings().all()
    row1 = rows[0]

    assert row1['user_id'] == 42568
    assert row1['education_form'] == "group"

def test_insert():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("INSERT INTO student(\"user_id\", \"level\", \"education_form\", \"subject_id\") VALUES (:new_user_id, :new_level, :new_education_form, :new_subject_id)")
    connection.execute(sql, {"new_user_id":777, "new_level":"Beginner", "new_education_form":"group", "new_subject_id":1})

    transaction.commit()
    connection.close()

def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("UPDATE student SET level = :new_level WHERE user_id = :user_id")
    connection.execute(sql, {"new_level": 'Elementary', "user_id": 777})

    transaction.commit()
    connection.close()

def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM student WHERE user_id = :user_id")
    connection.execute(sql, {"user_id": 777})

    transaction.commit()
    connection.close()