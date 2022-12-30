# Generated by Django 4.1.2 on 2022-11-11 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0004_remove_user_profile_pic_posts_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='VedioPost',
            field=models.FileField(blank=True, null=True, upload_to='vedios/'),
        ),
    ]