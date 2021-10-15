from django.contrib.auth import get_user_model
import factory
from faker import Faker
from apps.products.models import Product, Category, Tag
from apps.prestashop.models import PrestashopSynchronizer

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker("user_name")
    email = factory.Faker("email")
    first_name = factory.Faker("name")

    @factory.post_generation
    def password(self, create, extracted, **kwargs):
        password = (
            extracted
            if extracted
            else factory.Faker(
                "password",
                length=42,
                special_chars=True,
                digits=True,
                upper_case=True,
                lower_case=True,
            ).evaluate(None, None, extra={"locale": None})
        )
        self.set_password(password)

    class Meta:
        model = get_user_model()
        django_get_or_create = ["username"]


class ProductFactory(factory.django.DjangoModelFactory):
    name = fake.bothify("Product name ????-########")

    class Meta:
        model = Product


class TagFactory(factory.django.DjangoModelFactory):
    name = fake.bothify("Tag name ????-########")
    products = factory.SubFactory(ProductFactory)

    @factory.post_generation
    def products(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.products.add(extracted)

    class Meta:
        model = Tag


class CategoryFactory(factory.django.DjangoModelFactory):
    name = fake.bothify("Category name ????-########")
    products = factory.SubFactory(ProductFactory)

    @factory.post_generation
    def products(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.products.add(extracted)

    class Meta:
        model = Category


class PrestashopSynchronizerFactory(factory.django.DjangoModelFactory):
    entity_id = 1
    prestashop_entity_id = 1
    entity_type = PrestashopSynchronizer.PRODUCT

    class Meta:
        model = PrestashopSynchronizer
