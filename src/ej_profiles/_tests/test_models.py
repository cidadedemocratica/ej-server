import datetime
from datetime import date

import pytest
from django.utils.translation import ugettext as _

from ej_profiles.enums import Gender, Race
from ej_profiles.models import Profile
from ej_users.models import User


class TestProfile:
    @pytest.fixture
    def profile(self):
        return Profile(
            user=User(email='user@domain.com', name='name'),
            profile_photo='profile_photo',
            birth_date=date(1996, 1, 17),
            country='country',
            city='city',
            state='state',
            biography='biography',
            occupation='occupation',
            gender=Gender.FEMALE,
            political_activity='political_activity',
            race=Race.INDIGENOUS,
            ethnicity="ethnicity",
            education="undergraduate",
        )

    def test_profile_invariants(self, profile):
        assert str(profile) == 'name\'s profile'
        assert profile.profile_fields() == [
            ('City', 'city'),
            ('Country', 'country'),
            ('Occupation', 'occupation'),
            ('Age', profile.age),
            ('Education', 'undergraduate'),
            ('Ethnicity', 'ethnicity'),
            ('Gender identity', 'female'),
            ('Race', 'indigenous'),
            ('Political activity', 'political_activity'),
            ('Biography', 'biography'),
        ]
        assert profile.is_filled
        assert profile.statistics() == {'votes': 0, 'comments': 0, 'conversations': 0}
        assert profile.role() == _('Regular user')

        # Remove a field
        profile.occupation = ''
        assert not profile.is_filled

    def test_profile_variants(self, db, profile):
        delta = datetime.datetime.now().date() - date(1996, 1, 17)
        age = abs(int(delta.days // 365.25))
        assert profile.age == age
        assert profile.gender_description == Gender.FEMALE.description
        profile.gender = Gender.UNDECLARED
        assert profile.gender_description == profile.gender_other
        assert profile.has_image


    def test_user_profile_default_values(self, db):
        user = User.objects.create_user('email@at.com', 'pass')
        assert user.profile.gender == Gender.NOT_FILLED
        assert user.profile.race == Race.NOT_FILLED
        assert user.profile.age is None
        assert user.profile.gender_other == ''
        assert user.profile.country == ''
        assert user.profile.state == ''
        assert user.profile.city == ''
        assert user.profile.biography == ''
        assert user.profile.occupation == ''
        assert user.profile.political_activity == ''