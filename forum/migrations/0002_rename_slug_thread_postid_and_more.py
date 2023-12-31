# Generated by Django 4.2.9 on 2024-01-07 01:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thread',
            old_name='slug',
            new_name='postID',
        ),
        migrations.RenameField(
            model_name='thread',
            old_name='title',
            new_name='threadname',
        ),
        migrations.AddField(
            model_name='thread',
            name='pinned',
            field=models.IntegerField(choices=[(0, 'Unpinned'), (1, 'Pinned')], default=0),
        ),
        migrations.AddField(
            model_name='thread',
            name='tags',
            field=models.IntegerField(choices=[(0, 'General'), (1, 'Pattern'), (2, 'Yarn'), (3, 'Technique')], default=0),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('replyID', models.SlugField(max_length=200, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(max_length=500)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to=settings.AUTH_USER_MODEL)),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='forum.thread')),
            ],
        ),
    ]
