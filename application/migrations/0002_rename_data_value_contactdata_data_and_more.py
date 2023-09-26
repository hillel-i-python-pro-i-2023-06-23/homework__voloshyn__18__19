# Generated by Django 4.2.4 on 2023-09-26 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("application", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contactdata",
            old_name="data_value",
            new_name="data",
        ),
        migrations.RemoveField(
            model_name="contactdata",
            name="data_type",
        ),
        migrations.AlterField(
            model_name="contact",
            name="age",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="contactdata",
            name="contact",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="contact_data", to="application.contact"
            ),
        ),
    ]