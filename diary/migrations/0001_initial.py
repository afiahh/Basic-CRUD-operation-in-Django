# Generated by Django 5.1.3 on 2024-11-26 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiaryEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('mood', models.CharField(blank=True, choices=[('😊', 'Happy'), ('😢', 'Sad'), ('😡', 'Angry'), ('🤔', 'Thoughtful'), ('😄', 'Excited'), ('😴', 'Sleepy')], default='😴', max_length=2, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
