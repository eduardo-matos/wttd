# coding: utf-8

from django.test import TestCase
from django.template import Template, Context

class YoutubeTagTest(TestCase):
    def setUp(self):
        context = Context({'id': 'abc123'})
        template = Template('{% load youtube %}{% youtube id %}')

        self.content = template.render(context)

    def test_output(self):
        self.assertIn('<iframe', self.content)
        self.assertIn('/abc123', self.content)