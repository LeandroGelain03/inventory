# Generated by Django 2.0.2 on 2018-03-05 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConsumIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_consum', models.DateField(db_column='Date_consum')),
                ('item_consum_qty', models.DecimalField(db_column='Item_consum_qty', decimal_places=2, max_digits=15)),
                ('item_consum_rate', models.DecimalField(db_column='Item_consum_rate', decimal_places=2, max_digits=15)),
            ],
            options={
                'db_table': 'consum_in',
            },
        ),
        migrations.CreateModel(
            name='IssueIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_issue', models.DateField(db_column='Date_issue')),
                ('item_issue_qty', models.DecimalField(db_column='Item_issue_qty', decimal_places=2, max_digits=15)),
                ('item_issue_rate', models.DecimalField(db_column='Item_issue_rate', decimal_places=2, max_digits=15)),
            ],
            options={
                'db_table': 'issue_in',
            },
        ),
        migrations.CreateModel(
            name='MasterIn',
            fields=[
                ('item_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('item_name', models.CharField(db_column='Item_name', max_length=15)),
                ('item_qty', models.DecimalField(db_column='Item_qty', decimal_places=2, max_digits=15)),
                ('item_rate', models.DecimalField(db_column='Item_rate', decimal_places=2, max_digits=15)),
                ('item_bal_qty', models.DecimalField(db_column='Item_bal_qty', decimal_places=2, max_digits=15)),
                ('item_new_rate', models.DecimalField(db_column='Item_new_rate', decimal_places=2, max_digits=15)),
            ],
            options={
                'db_table': 'master_in',
            },
        ),
        migrations.CreateModel(
            name='WhouseIn',
            fields=[
                ('whouse_code', models.IntegerField(primary_key=True, serialize=False)),
                ('whouse_name', models.CharField(max_length=20)),
                ('whouse_address', models.CharField(max_length=30)),
                ('whouse_location', models.CharField(max_length=20)),
                ('whouse_city', models.CharField(max_length=10)),
                ('whouse_phone', models.CharField(db_column='whouse_Phone', max_length=11)),
                ('whouse_mobile', models.CharField(max_length=11)),
                ('whouse_head_name', models.CharField(max_length=15)),
                ('whouse_pincode', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'whouse_in',
            },
        ),
        migrations.CreateModel(
            name='ItemIn',
            fields=[
                ('item_code', models.ForeignKey(db_column='item_code', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='webapp.MasterIn')),
                ('item_name', models.CharField(db_column='Item_name', max_length=15)),
                ('item_reorder_qty', models.DecimalField(db_column='Item_reorder_qty', decimal_places=2, max_digits=15)),
                ('item_reorder_rate', models.DecimalField(db_column='Item_reorder_rate', decimal_places=2, max_digits=15)),
                ('item_reorder_level', models.DecimalField(db_column='Item_reorder_level', decimal_places=2, max_digits=15)),
                ('item_vendor_name', models.CharField(db_column='Item_vendor_name', max_length=20)),
                ('item_vendor_address', models.CharField(db_column='Item_vendor_address', max_length=30)),
            ],
            options={
                'db_table': 'item_in',
            },
        ),
        migrations.AddField(
            model_name='masterin',
            name='whouse_code',
            field=models.ForeignKey(db_column='Whouse_code', on_delete=django.db.models.deletion.DO_NOTHING, to='webapp.WhouseIn'),
        ),
        migrations.AddField(
            model_name='issuein',
            name='item_code',
            field=models.ForeignKey(db_column='item_code', on_delete=django.db.models.deletion.DO_NOTHING, to='webapp.MasterIn'),
        ),
        migrations.AddField(
            model_name='consumin',
            name='item_code',
            field=models.ForeignKey(db_column='item_code', on_delete=django.db.models.deletion.DO_NOTHING, to='webapp.MasterIn'),
        ),
    ]
