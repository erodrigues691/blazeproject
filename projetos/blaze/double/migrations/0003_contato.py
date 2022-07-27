# Generated by Django 4.0.6 on 2022-07-27 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('double', '0002_rename_datanascimento_double_data_nascimento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=256)),
                ('telefone', models.CharField(max_length=20)),
                ('double', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='double.double')),
            ],
        ),
    ]