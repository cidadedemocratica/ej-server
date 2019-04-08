from random import choice

import pytest
from model_mommy.recipe import Recipe
from sidekick import record

from ej.testing import EjRecipes
from ej_profiles.enums import Gender, Race
from ej_profiles.models import Profile
from .models import Profile


class ProfileRecipes(EjRecipes):
    profile = Recipe(Profile)

    def get_data(self, request):
        data = super().get_data(request)
        profile = self.profile.make(user=data.user)
        return record(data, profile=profile)


def get_random_profile(
    user, genders=[Gender(i) for i in Gender], races=[Race(i) for i in Race]
):
    try:
        return user.profile
    except (Profile.DoesNotExist, AttributeError):
        profile = user.get_profile()
        profile.gender = choice(genders)
        profile.race = choice(races)
        return profile
