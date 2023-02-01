from django.utils import timezone
from datetime import datetime as DT, timedelta

dateText: dict = {
    1: "day",
    2: "week",
    3: "month",
    4: "year"
}


def when_was_created(creationDate: DT) -> str:
    result = ""
    if creationDate >= timezone.now() - timedelta(days=1):
        result = "Created less than 1 ".join(dateText[1])
    elif creationDate >= timezone.now() - timedelta(weeks=1):
        result = "Created less than 1 ".join(dateText[2])
    elif creationDate >= timezone.now() - timedelta(weeks=4):
        result = "Created less than 1 ".join(dateText[3])
    elif creationDate >= timezone.now() - timedelta(weeks=52):
        result = "Created less than 1 ".join(dateText[4])

    return result
