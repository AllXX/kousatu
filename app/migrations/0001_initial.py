# Generated by Django 4.0.6 on 2022-07-15 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='タイトル')),
                ('message', models.TextField(verbose_name='メッセージ')),
                ('pub_data', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
            ],
            options={
                'verbose_name_plural': 'スレッド',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200, verbose_name='メッセージ')),
                ('pub_data', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.thread', verbose_name='スレッド')),
            ],
            options={
                'verbose_name_plural': 'コメント',
            },
        ),
    ]
