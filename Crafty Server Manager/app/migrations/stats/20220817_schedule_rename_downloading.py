# Generated by database migrator
import peewee


def migrate(migrator, database, **kwargs):
    migrator.rename_column("server_stats", "downloading", "importing")

    """
    Write your migrations here.
    """


def rollback(migrator, database, **kwargs):
    migrator.rename_column("server_stats", "importing", "downloading")
    """
    Write your rollback migrations here.
    """
