from peewee import *
from modules.model.database import db


class User(Model):
    id = AutoField(primary_key=True)
    username = CharField()
    password = DateField()

    class Meta:
        database = db

    def __str__(self) -> str:
        return f"username: {self.username}, password: ****"


if __name__ == '__main__':
    db.create_tables([User])
