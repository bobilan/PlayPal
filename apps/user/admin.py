from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from .models import *
from .forms import CustomUserChangeForm, CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": (
            "first_name",
            "last_name",
            "bio",
            "location",
            "birthdate",
            "avatar",
            "gender",
            "marital_status",
            "blocked_users",
            "liked_users",
            "disliked_users",
        )
        }
         ),
    )  # fields grouped in editing form

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2"),
        }),  # fields displayed when adding a new user
    )

    list_display = ('email', 'first_name', 'last_name', 'is_staff')  # Fields to display in admin users list

    ordering = ("email",)


class CustomInterest(admin.ModelAdmin):
    list_display = [
        "interest_name",
        "get_categories",
    ]

    @admin.display(description="Categories")
    def get_categories(self, obj):
        return obj.category_id.category_name


class CustomUserPreference(admin.ModelAdmin):
    list_display = [
        "id",
        "get_parent_gender_pref",
        "get_parent_age_range",
        "get_marital_status",
        "get_child_age_range",
        "get_child_gender_pref",
        "get_childs_interests",
    ]

    @admin.display(description="Marital Status")
    def get_marital_status(self, obj):
        return ", ".join([ms.marital_status for ms in obj.marital_id.all()])

    @admin.display(description="Parent age range")
    def get_parent_age_range(self, obj):
        return f"{obj.parent_lower_age_range} - {obj.parent_upper_age_range}"

    @admin.display(description="Parent gender preference")
    def get_parent_gender_pref(self, obj):
        return ", ".join([gender.gender_name for gender in obj.parent_gender.all()])

    @admin.display(description="Child age range")
    def get_child_age_range(self, obj):
        return f"{obj.child_lower_age_range} - {obj.child_upper_age_range}"

    @admin.display(description="Child gender preference")
    def get_child_gender_pref(self, obj):
        return ", ".join([gender.gender_name for gender in obj.child_gender.all()])

    @admin.display(description="Child's interests")
    def get_childs_interests(self, obj):
        return ", ".join([obj.interest_name for obj in obj.child_interest.all()])


class CustomUserPhoto(admin.ModelAdmin):
    
    list_display = [
        "id",
        "get_user",
    ]

    @admin.display(description="Uploaded by")
    def get_user(self, obj):
        return obj.user_id.email


@admin.register(ChildPicture)
class ChildPictureAdmin(admin.ModelAdmin):
    list_display = ["id", "get_child_name", "display_picture"]

    def get_child_name(self, obj):
        return obj.child.first_name

    def display_picture(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="max-width: 100px; max-height: 100px;" />')

    get_child_name.short_description = "Child Name"
    display_picture.short_description = "Picture Preview"


class CustomGrade(admin.ModelAdmin):
    
    list_display = [
        "id",
        "get_user_given",
        "get_user_received",
        "grade"
    ]
    
    @admin.display(description="Rating User")
    def get_user_given(self, obj):
        return obj.user_id_given.email

    @admin.display(description="Receiving User")
    def get_user_received(self, obj):
        return obj.user_id_received.email


class CustomChild(admin.ModelAdmin):
    
    list_display = [
        "first_name",
        "get_parent",
        "birthdate",
        "get_gender",
    ]

    @admin.display(description="Parent User")
    def get_parent(self, obj):
        return obj.parent_id.email

    @admin.display(description="Gender")
    def get_gender(self, obj):
        return obj.gender_id.gender_name


# Register your models here.
admin.site.register(MaritalStatus)
admin.site.register(Gender)
admin.site.register(InterestCategory)
admin.site.register(Interest, CustomInterest)
admin.site.register(UserPreference, CustomUserPreference)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserPhoto, CustomUserPhoto)
admin.site.register(Grade, CustomGrade)
admin.site.register(Child, CustomChild)