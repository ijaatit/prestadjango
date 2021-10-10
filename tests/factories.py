import factory
from faker import Faker
from apps.products.models import Product, Category, Tag

fake = Faker()


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
