# Generated by database migrator
import datetime
from peewee import *
from app.classes.models.users import Users
from app.classes.models.servers import Servers


def migrate(migrator, database, **kwargs):
    migrator.drop_table("commands")
    """
    Write your migrations here.
    """


def rollback(migrator, database, **kwargs):
    db = database

    class Commands(Model):
        command_id = AutoField()
        created = DateTimeField(default=datetime.datetime.now)
        server_id = ForeignKeyField(Servers, backref="server", index=True)
        user = ForeignKeyField(Users, backref="user", index=True)
        source_ip = CharField(default="127.0.0.1")
        command = CharField(default="")
        executed = BooleanField(default=False)

        class Meta:
            table_name = "commands"
            database = db

    migrator.create_table(Commands)

    """
    Write your rollback migrations here.
    """