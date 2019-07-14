# Generated by Django 2.1.10 on 2019-07-02 16:15

import autoslug.fields
import boogie.fields.enum_field
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import ej_conversations.models.vote
import ej_conversations.validators
import model_utils.fields
import re
import taggit.managers


class Migration(migrations.Migration):

    replaces = [
        ("ej_conversations", "0001_first_migration"),
        ("ej_conversations", "0002_change_meta_options"),
        ("ej_conversations", "0003_conversation_hidden"),
        ("ej_conversations", "0004_update_fields"),
        ("ej_conversations", "0005_auto_20190701_1443"),
    ]

    initial = True

    dependencies = [
        ("taggit", "0002_auto_20150616_2121"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="modified"
                    ),
                ),
                (
                    "status",
                    model_utils.fields.StatusField(
                        choices=[
                            ("pending", "awaiting moderation"),
                            ("approved", "approved"),
                            ("rejected", "rejected"),
                        ],
                        default="pending",
                        max_length=100,
                        no_check_for_status=True,
                        verbose_name="status",
                    ),
                ),
                (
                    "status_changed",
                    model_utils.fields.MonitorField(
                        default=django.utils.timezone.now, monitor="status", verbose_name="status changed"
                    ),
                ),
                (
                    "content",
                    models.TextField(
                        help_text="Body of text for the comment",
                        max_length=210,
                        validators=[
                            django.core.validators.MinLengthValidator(2),
                            ej_conversations.validators.is_not_empty,
                        ],
                        verbose_name="Content",
                    ),
                ),
                (
                    "rejection_reason",
                    models.TextField(
                        blank=True,
                        help_text="You must provide a reason to reject a comment. Users will receive this feedback.",
                        verbose_name="Rejection reason",
                    ),
                ),
                (
                    "is_promoted",
                    models.BooleanField(
                        default=False,
                        help_text="Promoted comments are prioritized when selecting random commentsto users.",
                        verbose_name="Promoted comment?",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CommentQueue",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="modified"
                    ),
                ),
                (
                    "comments",
                    models.TextField(
                        blank=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                re.compile("^\\d+(?:\\,\\d+)*\\Z"),
                                code="invalid",
                                message="Enter only digits separated by commas.",
                            )
                        ],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Conversation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="modified"
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="A short description about this conversations. This is used internally and to create URL slugs. (e.g. School system)",
                        max_length=255,
                        verbose_name="Title",
                    ),
                ),
                (
                    "text",
                    models.TextField(
                        help_text="A question that is displayed to the users in a conversation card. (e.g.: How can we improve the school system in our community?)",
                        verbose_name="Question",
                    ),
                ),
                ("slug", autoslug.fields.AutoSlugField(editable=False, populate_from="title", unique=True)),
                (
                    "is_promoted",
                    models.BooleanField(
                        default=False,
                        help_text="Promoted conversations appears in the main /conversations/ endpoint.",
                        verbose_name="promoted?",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        help_text="Only the author and administrative staff can edit this conversation.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="conversations",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["created"],
                "permissions": (
                    ("can_publish", "Can publish promoted conversations"),
                    ("can_moderate", "Can moderate comments in any conversation"),
                ),
            },
        ),
        migrations.CreateModel(
            name="ConversationTag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "content_object",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ej_conversations.Conversation"
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ej_conversations_conversationtag_items",
                        to="taggit.Tag",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="FavoriteConversation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "conversation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="followers",
                        to="ej_conversations.Conversation",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="favorite_conversations",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Vote",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "choice",
                    boogie.fields.enum_field.EnumField(
                        ej_conversations.models.vote.Choice,
                        help_text="Agree, disagree or skip",
                        verbose_name="Choice",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, verbose_name="Created at")),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="votes",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "comment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="votes",
                        to="ej_conversations.Comment",
                    ),
                ),
            ],
            options={"ordering": ["id"]},
        ),
        migrations.AddField(
            model_name="conversation",
            name="tags",
            field=taggit.managers.TaggableManager(
                help_text="A comma-separated list of tags.",
                through="ej_conversations.ConversationTag",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.AddField(
            model_name="commentqueue",
            name="conversation",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="ej_conversations.Conversation"
            ),
        ),
        migrations.AddField(
            model_name="commentqueue",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="conversation",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="ej_conversations.Conversation",
            ),
        ),
        migrations.AlterUniqueTogether(name="vote", unique_together={("author", "comment")}),
        migrations.AlterField(
            model_name="commentqueue",
            name="comments",
            field=models.TextField(
                blank=True,
                validators=[
                    django.core.validators.RegexValidator(
                        re.compile("^\\d+(?:,\\d+)*\\Z"),
                        code="invalid",
                        message="Enter only digits separated by commas.",
                    )
                ],
            ),
        ),
        migrations.AlterUniqueTogether(name="commentqueue", unique_together={("conversation", "user")}),
        migrations.AlterUniqueTogether(name="comment", unique_together={("conversation", "content")}),
        migrations.AlterModelOptions(
            name="conversation",
            options={
                "ordering": ["created"],
                "permissions": (
                    ("can_publish_promoted", "Can publish promoted conversations"),
                    ("is_moderator", "Can moderate comments in any conversation"),
                ),
            },
        ),
        migrations.AlterField(
            model_name="conversation",
            name="title",
            field=models.CharField(
                help_text="A short description about this conversation. This is used internally and to create URL slugs. (e.g. School system)",
                max_length=255,
                unique=True,
                verbose_name="Title",
            ),
        ),
        migrations.AddField(
            model_name="conversation",
            name="is_hidden",
            field=models.BooleanField(
                default=False,
                help_text="Hidden conversations does not appears in boards or in the main /conversations/ endpoint.",
                verbose_name="hidden?",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="content",
            field=models.TextField(
                help_text="Body of text for the comment",
                max_length=252,
                validators=[
                    django.core.validators.MinLengthValidator(2),
                    ej_conversations.validators.is_not_empty,
                ],
                verbose_name="Content",
            ),
        ),
    ]
