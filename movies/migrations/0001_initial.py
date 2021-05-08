# Generated by Django 2.2.2 on 2021-05-07 05:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=100, verbose_name='ΤΙΤΛΟΣ')),
                ('director', models.CharField(blank=True, default='', max_length=100, verbose_name='ΣΚΗΝΟΘΕΤΗΣ')),
                ('actor', models.CharField(blank=True, default='', max_length=100, verbose_name='ΗΘΟΠΟΙΟΣ')),
                ('categoryId', models.IntegerField(choices=[(0, 'ALL'), (1, 'Δράσης'), (2, 'Επιστημονικής Φαντασίας'), (3, 'Δραματική'), (4, 'Ρομαντική'), (5, 'Ιστορική'), (6, 'Βιογραφική')], null=True, verbose_name='ΚΑΤΗΓΟΡΙΑ')),
                ('imbdUrl', models.CharField(blank=True, default='', max_length=400)),
                ('coverUrl', models.CharField(blank=True, default='', max_length=400, verbose_name='ΕΞΩΦΥΛΟ')),
                ('viewdate', models.DateField(default=datetime.date.today, verbose_name='ΗΜΕΡΟΜΗΝΙΑ ΠΡΟΒΟΛΗΣ')),
                ('timeId', models.IntegerField(choices=[(0, 'Όλα'), (1, 'Φοιτητικό/Στρατιωτικό: 5,5€'), (2, 'Παιδικό:7,5€'), (3, 'Αίθουσα 2D:10€'), (4, 'Αίθουσα 3D:11€'), (5, 'Αίθουσα DOLBY:11€'), (6, 'Αίθουσα DOLBY-3D:12€'), (7, 'Αίθουσα GOLD:20€')], default='', verbose_name='ΩΡΑ ΠΡΟΒΟΛΗΣ')),
                ('priceId', models.IntegerField(choices=[(0, '(Όλα)'), (1, '18:00 μμ'), (2, '19:00 μμ'), (3, '20:00 μμ'), (4, '21:00 μμ'), (5, '22:00 μμ'), (6, '23:00 μμ'), (7, '24:00 μμ')], default='', verbose_name='ΤΙΜΗ ΕΙΣΗΤΗΡΙΟΥ')),
                ('description', models.CharField(blank=True, default='', max_length=1000, verbose_name='ΠΕΡΙΓΡΑΦΗ ΤΑΙΝΙΑΣ')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='snippets', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ταινία',
                'verbose_name_plural': 'Ταινίες',
                'db_table': 'movie',
                'ordering': ['title'],
            },
        ),
    ]
