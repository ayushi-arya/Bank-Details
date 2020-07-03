from __future__ import unicode_literals

 from django.db import migrations, models
 import django.db.models.deletion


 class Migration(migrations.Migration):

     initial = True

     dependencies = [
     ]

     operations = [
         migrations.CreateModel(
             name='Bank',
             fields=[
                 ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                 ('name', models.CharField(max_length=50)),
             ],
             options={
                 'ordering': ('name',),
             },
         ),
         migrations.CreateModel(
             name='Branch',
             fields=[
                 ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                 ('name', models.CharField(max_length=256)),
                 ('ifsc', models.CharField(max_length=20, unique=True)),
                 ('address', models.TextField()),
                 ('city', models.CharField(max_length=20)),
                 ('district', models.CharField(max_length=50)),
                 ('state', models.CharField(max_length=20)),
                 ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Bank')),
             ],
             options={
                 'ordering': ('name',),
                 'verbose_name_plural': 'Branch',
                 'verbose_name': 'Branch',
             },
         ),
     ]
