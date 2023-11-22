# Generated by Django 2.1.3 on 2020-04-11 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('number', models.IntegerField()),
                ('hobbies', models.CharField(blank=True, max_length=255)),
                ('gender', models.CharField(blank=True, max_length=50)),
                ('education', models.CharField(blank=True, max_length=50)),
                ('image', models.FileField(blank=True, upload_to='student_image')),
                ('age', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
