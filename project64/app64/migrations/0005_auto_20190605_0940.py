# Generated by Django 2.1.5 on 2019-06-05 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app64', '0004_auto_20190605_0920'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='author',
            new_name='Author',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='book_name',
            new_name='Book_name',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='card',
            new_name='Card',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='catalog',
            new_name='Catalog',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='photo',
            new_name='Photo',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='price',
            new_name='Price',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='art_path',
            new_name='Art_path',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='b_name',
            new_name='B_name',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='number',
            new_name='Number',
        ),
        migrations.RenameField(
            model_name='favorite',
            old_name='book_name',
            new_name='Book_name',
        ),
        migrations.RenameField(
            model_name='favorite',
            old_name='use_name',
            new_name='Use_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='author',
            new_name='Author',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='card',
            new_name='Card',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='level',
            new_name='Level',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='money',
            new_name='Money',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='Password',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='photo',
            new_name='Photo',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_name',
            new_name='User_name',
        ),
        migrations.RemoveField(
            model_name='article',
            name='info',
        ),
        migrations.AddField(
            model_name='article',
            name='Info',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
