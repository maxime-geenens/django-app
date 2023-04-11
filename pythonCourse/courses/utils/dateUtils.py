from django.utils import timezone
from datetime import datetime as DT, timedelta

dateText: dict = {
    1: "day",
    2: "week",
    3: "month",
    4: "year"
}


def creation_or_update_date_info(creationDate: DT, updateDate: DT, user: str) -> str:
    operation = ""
    period = ""

    if creationDate is not None:
        operation = "Created"
        period = get_period_info(creationDate)
    elif updateDate is not None:
        operation = "Last Update"
        period = get_period_info(updateDate)

    return "{operation} less than 1 {period} by {user}".format(operation=operation, period=period, user=user)


def get_period_info(date: DT):

    period = ""

    if date >= timezone.now() - timedelta(days=1):
        period = dateText[1]
    elif date >= timezone.now() - timedelta(weeks=1):
        period = dateText[2]
    elif date >= timezone.now() - timedelta(weeks=4):
        period = dateText[3]
    elif date >= timezone.now() - timedelta(weeks=52):
        period = dateText[4]

    return period
