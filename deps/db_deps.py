from db.db_connect import Session

def get_db():

    db = Session()

    try:
        yield db
    finally:
        db.close()