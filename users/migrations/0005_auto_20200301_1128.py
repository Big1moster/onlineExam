# Generated by Django 2.0 on 2020-03-01 11:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200229_2124'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(blank=True, max_length=128, null=True)),
                ('grade', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_updated_time', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': '考试记录表',
                'verbose_name_plural': '考试记录表',
                'ordering': ['-last_updated_time'],
            },
        ),
        migrations.AlterField(
            model_name='exam',
            name='allot',
            field=models.ManyToManyField(related_name='allot_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='examrecord',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Exam'),
        ),
        migrations.AddField(
            model_name='examrecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
