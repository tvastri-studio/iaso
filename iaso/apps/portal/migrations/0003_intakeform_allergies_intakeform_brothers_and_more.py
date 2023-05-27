# Generated by Django 4.2.1 on 2023-05-27 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_condition'),
    ]

    operations = [
        migrations.AddField(
            model_name='intakeform',
            name='allergies',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intakeform',
            name='brothers',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intakeform',
            name='children',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intakeform',
            name='extended_family',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intakeform',
            name='father',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intakeform',
            name='maternal_grandfather',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intakeform',
            name='maternal_grandmother',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intakeform',
            name='mother',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intakeform',
            name='other_conditions',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intakeform',
            name='paternal_grandfather',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intakeform',
            name='paternal_grandmother',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intakeform',
            name='sisters',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='condition',
            name='name',
            field=models.CharField(blank=True, choices=[('hypertension', 'Hypertension'), ('diabetes', 'Diabetes'), ('heart_attack', 'Heart Attack'), ('stroke', 'Stroke'), ('blood_clot', 'Blood Clot'), ('seizures', 'Seizures'), ('cancer', 'Cancer'), ('mental_illness', 'Mental Illness')], max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Surgery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('when', models.CharField(blank=True, max_length=100, null=True)),
                ('intake_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.intakeform')),
            ],
        ),
        migrations.CreateModel(
            name='Injury',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('when', models.CharField(blank=True, max_length=100, null=True)),
                ('intake_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.intakeform')),
            ],
        ),
    ]
