from django.test import TestCase
from courses.models import *

from django.utils import timezone
from datetime import timedelta


class TopicTestCase(TestCase):
    
    def setUp(self):
        Topic.objects.create(
            name='Test Topic 1',
            created_by='test1',
            last_update=timezone.now(),
            last_update_user="test2")
        Topic.objects.create(
            name='Test Topic 2',
            created_by='test1',
            last_update=timezone.now() - timedelta(days=3),
            last_update_user="test2")
        Topic.objects.create(
            name='Test Topic 3',
            created_by='test1',
            last_update=timezone.now() - timedelta(weeks=2),
            last_update_user="test2")
        Topic.objects.create(
            name='Test Topic 4',
            created_by='test1',
            last_update=timezone.now() - timedelta(weeks=12),
            last_update_user="test2")
        
    def test_topic_date_info(self):
        now_topic = Topic.objects.get(name="Test Topic 1")
        week_topic = Topic.objects.get(name="Test Topic 2")
        month_topic = Topic.objects.get(name="Test Topic 3")
        year_topic = Topic.objects.get(name="Test Topic 4")

        self.assertEqual(now_topic.creation_date_info(), "Created less than 1 day by test1")
        self.assertEqual(now_topic.update_date_info(), "Last Update less than 1 day by test2")
        self.assertEqual(week_topic.update_date_info(), "Last Update less than 1 week by test2")
        self.assertEqual(month_topic.update_date_info(), "Last Update less than 1 month by test2")
        self.assertEqual(year_topic.update_date_info(), "Last Update less than 1 year by test2")