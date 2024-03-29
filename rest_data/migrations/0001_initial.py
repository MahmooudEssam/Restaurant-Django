# Generated by Django 4.1.4 on 2023-02-14 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_acc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=200)),
                ('tel', models.PositiveIntegerField()),
                ('DOB', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=20)),
                ('DOB', models.DateField()),
                ('email', models.EmailField(max_length=200)),
                ('tel', models.PositiveIntegerField()),
                ('salary', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu_rec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('img', models.URLField()),
                ('desc', models.TextField()),
                ('ingredients', models.TextField()),
                ('promos', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Resv_rec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seatsNum', models.IntegerField()),
                ('cu_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_data.customer_acc')),
            ],
        ),
        migrations.CreateModel(
            name='Rest_tab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.TextField()),
                ('tableNum', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rest_data.resv_rec')),
            ],
        ),
        migrations.CreateModel(
            name='Rest_seats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.TextField()),
                ('seatsNum', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rest_data.resv_rec')),
                ('tableNum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_data.rest_tab')),
            ],
        ),
        migrations.CreateModel(
            name='Order_rec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_Num', models.PositiveBigIntegerField()),
                ('order_time', models.DateTimeField()),
                ('E_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_data.employee')),
                ('menu_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_data.menu_rec')),
            ],
        ),
    ]
