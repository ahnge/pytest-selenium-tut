from django.contrib.auth.models import User
import pytest

# Create your tests here.


@pytest.mark.django_db
def test_add_one():
    user1 = User.objects.create()
    count = User.objects.count()
    assert count == 1


@ pytest.mark.django_db
def test_add_two():
    count = User.objects.count()
    assert count == 0
