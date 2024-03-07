# Generated by Django 4.2.7 on 2024-03-05 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_logger'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('college_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=50)),
                ('subject_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Principal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('college_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='first_app.college')),
            ],
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('article_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('liked_users', models.ManyToManyField(to='first_app.user')),
            ],
        ),
    ]