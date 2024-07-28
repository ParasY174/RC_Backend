# Generated by Django 5.0.1 on 2024-04-19 02:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question_id', models.IntegerField(unique=True)),
                ('question_text', models.TextField()),
                ('correct_answer', models.IntegerField()),
                ('responses', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1', models.CharField(max_length=255)),
                ('user2', models.CharField(blank=True, max_length=255)),
                ('category', models.CharField(choices=[('JR', 'Junior'), ('SR', 'Senior')], max_length=2)),
                ('teamname', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('login_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('start_time', models.DateTimeField(null=True)),
                ('end_time', models.DateTimeField(null=True)),
                ('current_question', models.IntegerField(default=1)),
                ('question_list', models.CharField(max_length=256)),
                ('prev_answer', models.IntegerField(default=0)),
                ('correct_count', models.SmallIntegerField(default=0)),
                ('incorrect_count', models.SmallIntegerField(default=0)),
                ('isAttemptedFirst', models.BooleanField(default=False)),
                ('lifeline1', models.BooleanField(default=False)),
                ('lifeline2', models.BooleanField(default=False)),
                ('lifeline3', models.BooleanField(default=False)),
                ('lifeline_flag', models.SmallIntegerField(default=1)),
                ('team', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='progress', to='rc_app.team')),
            ],
        ),
    ]