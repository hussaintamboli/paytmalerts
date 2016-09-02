from datetime import datetime


def friendly_date(dt):
    """
    Convert Y-m-d date into d b, Y
    e.g. 2016-09-02 --> 02 Sep, 2016
    """
    return datetime.strptime(dt, "%Y-%m-%d").strftime("%d %b, %Y")
