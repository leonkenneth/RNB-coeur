# Generated by Django 5.1.7 on 2025-03-26 11:20
from django.db import connection
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("batid", "0100_diffusiondatabase"),
    ]

    def add_unique_constraint(apps, schema_editor):
        with connection.cursor() as cursor:
            cursor.execute(
                """
                ALTER TABLE auth_user
                ADD CONSTRAINT unique_user_email UNIQUE (email);
            """
            )

    def remove_unique_constraint(apps, schema_editor):
        with connection.cursor() as cursor:
            cursor.execute(
                """
                ALTER TABLE auth_user
                DROP CONSTRAINT IF EXISTS unique_user_email;
            """
            )

    operations = [
        migrations.RunPython(add_unique_constraint, remove_unique_constraint),
    ]
