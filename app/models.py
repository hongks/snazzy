from datetime import datetime

from sqlalchemy import event
from sqlalchemy.orm import Session

from app import db


<<<<<<< HEAD
class Topic(db.Model):
    __tablename__ = "topics"

    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.Text)

    created_by = db.Column(db.Integer, db.ForeignKey("users.id"))
    created_on = db.Column(db.DateTime)
    updated_by = db.Column(db.Integer, db.ForeignKey("users.id"))
    updated_on = db.Column(db.DateTime)


=======
>>>>>>> bddd5045e3799de99f6b3d41baa5627ba33d6ee7
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text)
    password = db.Column(db.Text)
    full_name = db.Column(db.Text)
    last_seen = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean)

    created_by = db.Column(db.Integer)
    created_on = db.Column(db.DateTime)
    updated_by = db.Column(db.Integer)
    updated_on = db.Column(db.DateTime)


@event.listens_for(User.__table__, "after_create")
def users_instances_after_create(target, connection, **kwargs):
    dt = datetime.utcnow()

    session = Session(bind=connection)
    user = User(
        username="SYSTEM",
        full_name="SYSTEM",
        is_active=True,
        created_by=1,
        created_on=dt,
        updated_by=1,
        updated_on=dt,
    )

    session.add(user)
    session.commit()
