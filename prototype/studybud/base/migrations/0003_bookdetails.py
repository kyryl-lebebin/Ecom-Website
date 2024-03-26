# Generated by Django 5.0.3 on 2024-03-10 21:35

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_genre_book_genres'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookDetails',
            fields=[
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.book')),
            ],
        ),
    ]