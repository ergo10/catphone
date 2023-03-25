# Generated by Django 4.1.7 on 2023-03-21 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catphone', '0004_order_pos_order_order_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chegue',
            fields=[
                ('date_print', models.DateTimeField(auto_now_add=True, verbose_name='Дата распечатки')),
                ('address_print', models.CharField(max_length=150, verbose_name='Место создания чека')),
                ('terminal', models.CharField(max_length=10, verbose_name='Код терминала')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='catphone.order', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'Чек',
                'verbose_name_plural': 'Чеки',
                'ordering': ['terminal', 'date_print'],
            },
        ),
    ]
