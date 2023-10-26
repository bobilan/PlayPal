# Generated by Django 4.2.6 on 2023-10-26 09:15

import apps.user.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("verified_status", models.BooleanField(default=False)),
                ("bio", models.TextField(blank=True, null=True)),
                ("location", models.CharField(blank=True, max_length=10, null=True)),
                ("birthdate", models.DateField(blank=True, null=True)),
                (
                    "avatar",
                    models.ImageField(blank=True, null=True, upload_to="avatars/"),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Gender",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("gender_name", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Interest",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("interest_name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="InterestCategory",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("category_name", models.CharField(max_length=50)),
            ],
            options={
                "verbose_name_plural": "Interest categories",
            },
        ),
        migrations.CreateModel(
            name="MaritalStatus",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("marital_status", models.CharField(max_length=30)),
            ],
            options={
                "verbose_name_plural": "Marital statuses",
            },
        ),
        migrations.CreateModel(
            name="UserPreference",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("parent_lower_age_range", models.IntegerField()),
                ("parent_upper_age_range", models.IntegerField()),
                ("child_lower_age_range", models.IntegerField()),
                ("child_upper_age_range", models.IntegerField()),
                (
                    "child_gender",
                    models.ManyToManyField(
                        related_name="child_gender_preference", to="user.gender"
                    ),
                ),
                (
                    "child_interest",
                    models.ManyToManyField(
                        related_name="child_interest", to="user.interest"
                    ),
                ),
                (
                    "marital_id",
                    models.ManyToManyField(
                        related_name="parent_marital_preference",
                        to="user.maritalstatus",
                    ),
                ),
                (
                    "parent_gender",
                    models.ManyToManyField(
                        related_name="parent_gender_preference", to="user.gender"
                    ),
                ),
                (
                    "user_id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="preferences",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserPhoto",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "photos",
                    models.ImageField(blank=True, null=True, upload_to="user_photos/"),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="interest",
            name="category_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="user.interestcategory"
            ),
        ),
        migrations.CreateModel(
            name="Grade",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "grade",
                    models.IntegerField(
                        validators=[apps.user.validators.check_rating_range]
                    ),
                ),
                (
                    "user_id_given",
                    models.ManyToManyField(
                        related_name="grades_given", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "user_id_received",
                    models.ManyToManyField(
                        related_name="grades_received", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Child",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("birthdate", models.DateField()),
                ("bio", models.TextField()),
                (
                    "avatar",
                    models.ImageField(blank=True, null=True, upload_to="avatars/"),
                ),
                (
                    "gender_id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="child_gender",
                        to="user.gender",
                    ),
                ),
                (
                    "interest_id",
                    models.ManyToManyField(
                        related_name="child_interests", to="user.interest"
                    ),
                ),
                (
                    "parent_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Children",
            },
        ),
        migrations.AddField(
            model_name="customuser",
            name="gender",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="user.gender",
            ),
        ),
        migrations.AddField(
            model_name="customuser",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                related_name="user_set",
                related_query_name="user",
                to="auth.group",
                verbose_name="groups",
            ),
        ),
        migrations.AddField(
            model_name="customuser",
            name="marital_status",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="user.maritalstatus",
            ),
        ),
        migrations.AddField(
            model_name="customuser",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
    ]