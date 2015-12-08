# coding: utf-8

from dj_diabetes.models.foods import Foods

from dj_diabetes.tests import MainTest


class FoodsTest(MainTest):

    def create_foods(self):
        title = 'Chocolate'
        return Foods.objects.create(title=title)

    def test_foods(self):
        s = self.create_foods()
        self.assertTrue(isinstance(s, Foods))
        self.assertEqual(s.show(), "%s" % s.title)

