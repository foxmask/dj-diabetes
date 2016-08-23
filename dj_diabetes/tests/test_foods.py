# coding: utf-8

from dj_diabetes.models.foods import Foods

from dj_diabetes.tests import MainTest


class FoodsTest(MainTest):

    def setUp(self):
        super(FoodsTest, self).setUp()
        title = 'Chocolate'
        self.food = Foods.objects.create(title=title)

    def test_foods(self):
        self.assertTrue(isinstance(self.food, Foods))
        self.assertEqual(self.food.__str__(), "%s" % self.food.title)
