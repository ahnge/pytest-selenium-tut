import pytest
from app1.models import Product


# parametrizing in pytest 😲


@pytest.mark.parametrize(
    "title, category, description, slug, regular_price, discount_price, validity",
    [
        ("NewTitle", 1, "NewDescription", "slug", "4.99", "3.99", True),
        ("NewTitle", 1, "NewDescription", "slug", "5.99", "3.99", True),
    ],
)
@pytest.mark.django_db
def test_product_instance(
    product_factory, title, category, description, slug, regular_price, discount_price, validity
):

    test = product_factory(
        title=title,
        category_id=category,
        description=description,
        slug=slug,
        regular_price=regular_price,
        discount_price=discount_price,
    )

    item = Product.objects.all().count()
    print(test)
    print(item)
    assert item == validity
