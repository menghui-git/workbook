# Generated by Django 3.0.7 on 2020-08-08 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('vocab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vocab.Word', unique=True)),
            ],
            options={
                'unique_together': {('user', 'word')},
            },
        ),
    ]
