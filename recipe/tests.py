from django.test import TestCase

from .models import Category, Recipe


class CategoryModelTests(TestCase):
    def test_category_can_be_created(self):
        category = Category.objects.create(name='Desserts')

        self.assertEqual(category.name, 'Desserts')

    def test_category_iter_returns_name(self):
        category = Category.objects.create(name='Breakfast')

        self.assertEqual(list(category), ['Breakfast'])


class RecipeModelTests(TestCase):
    def test_recipe_can_be_created_with_category(self):
        category = Category.objects.create(name='Soups')

        recipe = Recipe.objects.create(
            title='Tomato soup',
            description='Simple homemade tomato soup.',
            instructions='Simmer all ingredients and blend until smooth.',
            ingredients='Tomatoes, onion, garlic, vegetable stock',
            category=category,
        )

        self.assertEqual(recipe.title, 'Tomato soup')
        self.assertEqual(recipe.category, category)
        self.assertEqual(category.recipes.get(), recipe)
        self.assertIsNotNone(recipe.created_at)
        self.assertIsNotNone(recipe.updated_at)
