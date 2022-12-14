# Generated by Django 3.2.5 on 2022-07-31 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('texto', models.TextField(null=True)),
                ('activo', models.BooleanField(default=True)),
                ('imagen', models.ImageField(default='noticia/default.png', upload_to='noticia')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='noticia.categoria')),
            ],
        ),
    ]
