# Generated by Django 2.1.7 on 2019-03-26 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vitrineapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_categoria', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProdutoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.TextField(max_length=100)),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vitrineapp.CategoriaModel')),
            ],
        ),
    ]
