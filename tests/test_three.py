import pytest

from django.contrib.auth.models import User


# def test_fakeuser(new_user1):
#     count = User.objects.all().count()
#     print(new_user1.username)
#     print(count)
#     assert True


# def test_fakeuser_again(new_user1):
#     count = User.objects.all().count()
#     print(new_user1.username)
#     print(count)
#     assert True

@pytest.mark.django_db
def test_product(product_factory):
    product = product_factory.create()
    print(product.category)
    print(product.description)
    assert True
