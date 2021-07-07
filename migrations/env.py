import sys
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config
from sqlalchemy import pool


sys.path = ['', '..'] + sys.path[1:]

from config.db import db_url
from config.base import Base

config = context.config

fileConfig(config.config_file_name)

target_metadata = Base.metadata


# target_metadata = None

# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():

    # url = config.get_main_option("sqlalchemy.url")
    url = db_url
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():

    configuration = config.get_section(config.config_ini_section)
    configuration['sqlalchemy.url'] = db_url
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
