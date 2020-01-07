from datetime import datetime

import pytest
import pytz
from django.urls import reverse
from model_mommy import mommy

from pythonpro.dashboard.models import TopicInteraction
from pythonpro.django_assertions import dj_assert_contains


@pytest.fixture
def interactions(logged_user, topic):
    return [
        mommy.make(
            TopicInteraction,
            user=logged_user,
            topic=topic,
            creation=datetime(2019, 7, 22, 0, 0, 0, tzinfo=pytz.utc),
            topic_duration=125,
            total_watched_time=125,
            max_watched_time=95
        ),
        mommy.make(
            TopicInteraction,
            user=logged_user,
            topic=topic,
            creation=datetime(2019, 7, 22, 1, 0, 0, tzinfo=pytz.utc),
            topic_duration=125,
            total_watched_time=34,
            max_watched_time=14
        ),
        mommy.make(
            TopicInteraction,
            user=logged_user,
            topic=topic,
            creation=datetime(2019, 7, 22, 0, 30, 0, tzinfo=pytz.utc),
            topic_duration=125,
            total_watched_time=64,
            max_watched_time=34
        ),
    ]


@pytest.fixture
def resp(client_with_lead, interactions):
    return client_with_lead.get(
        reverse('dashboard:home'),
        secure=True
    )


def test_table_instructions(resp, topic):
    dj_assert_contains(resp, 'Confira os dados consolidados por tópico')


def test_not_existing_aggregation_msg_is_present(resp, topic):
    dj_assert_contains(resp, "Ainda não existem dados agregados")
