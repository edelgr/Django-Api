# Generated by Django 4.1.3 on 2022-11-03 00:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title_short', models.CharField(default=None, max_length=17, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('rating', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)])),
            ],
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reaction', models.CharField(choices=[('like', 'Like'), ('love', 'Love'), ('care', 'Care'), ('haha', 'Haha'), ('wow', 'Wow'), ('sad', 'Sad'), ('angry', 'Angry')], default='', max_length=200)),
                ('movies', models.ManyToManyField(to='peliculas_api.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peliculas_api.movie')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
