# Generated by database migrator
import peewee


def migrate(migrator, database, **kwargs):
    migrator.add_columns("users", theme=peewee.CharField(default="default"))
    """
    Write your migrations here.
    """


def rollback(migrator, database, **kwargs):
    migrator.drop_columns("users", ["theme"])
    """
    Write your rollback migrations here.
    """