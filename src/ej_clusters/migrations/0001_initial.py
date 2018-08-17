# Generated by Django 2.0.8 on 2018-08-17 16:48

import boogie.fields.enum_field
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import ej_clusters.types
import ej_conversations.models.vote
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ej_conversations', '0010_auto_20180817_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('description', models.TextField(blank=True, help_text='How was this cluster conceived?', verbose_name='Description')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Clusterization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('cluster_status', boogie.fields.enum_field.EnumField(ej_clusters.types.ClusterStatus, default=ej_clusters.types.ClusterStatus(0))),
                ('unprocessed_votes', models.PositiveSmallIntegerField(default=0, editable=False)),
                ('unprocessed_comments', models.PositiveSmallIntegerField(default=0, editable=False)),
                ('conversation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='clusterization', to='ej_conversations.Conversation')),
            ],
            options={
                'ordering': ['conversation_id'],
            },
        ),
        migrations.CreateModel(
            name='Stereotype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('description', models.TextField(blank=True, help_text='A detailed description of your stereotype for future reference. You can specify a background history, or give hints on the exact profile the stereotype wants to capture.', verbose_name='Description')),
                ('conversation', models.ForeignKey(blank=True, help_text='Conversation associated with the stereotype.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stereotypes', to='ej_conversations.Conversation')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StereotypeVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', boogie.fields.enum_field.EnumField(ej_conversations.models.vote.Choice)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='ej_clusters.Stereotype')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stereotype_votes', to='ej_conversations.Comment')),
            ],
        ),
        migrations.AddField(
            model_name='cluster',
            name='clusterization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clusters', to='ej_clusters.Clusterization'),
        ),
        migrations.AddField(
            model_name='cluster',
            name='stereotypes',
            field=models.ManyToManyField(related_name='clusters', to='ej_clusters.Stereotype'),
        ),
        migrations.AddField(
            model_name='cluster',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='clusters', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='stereotype',
            unique_together={('name', 'conversation')},
        ),
    ]
