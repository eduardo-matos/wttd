# coding: utf-8

from django.test import TestCase
from eventex.core.models import Course

class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title=u'Introdução ao Django',
            description=u'Descrição da palestra',
            start_time='10:00',
            slots=10,
            notes='Some notes'
        )

        self.course2 = Course.objects.create(
            title=u'Introdução ao Django 2',
            description=u'Descrição da palestra 2',
            start_time='17:00',
            slots=10,
            notes='Some notes'
        )

    def test_create(self):
        self.assertEqual(2, Course.objects.all().count())

    def test_unicode(self):
        self.assertEqual(u'Introdução ao Django', unicode(self.course))

    def test_speakers(self):
        'Course has many speakers and vice-versa'
        self.course.speakers.create(
                name='Eduardo Matos',
                slug='eduardo-matos',
                url='http://eduardodematos.com'
            )

        self.assertEqual(1, self.course.speakers.count())

    def test_Courses_by_period(self):
        '''
        morning method must return only Courses in the morning and
        afternoon Courses mus return only Courses in the afternoon
        '''
        self.assertEqual(1, Course.morning.count())
        self.assertEqual(1, Course.afternoon.count())