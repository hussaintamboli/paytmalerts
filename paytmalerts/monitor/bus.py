from paytmalerts.lib.api import api_call
from paytmalerts.lib.common import friendly_date
from paytmalerts.notifier import notify


def alert_payload(bus):
    return {
        'module': 'notifysend',
        'title': '{} {}'.format(bus['travelsName'], friendly_date(bus['departureDate'])),
        'message': '{} - {} seats'.format(bus['busType'], bus['avalableSeats'])
    }


def available(dt, source, destination, search_for, search_term):
    data = {
        'date': dt,
        'destination': destination,
        'source': source
    }
    params = {
        'child_site_id': 1,
        'site_id': 1
    }
    buses = api_call('search', method='POST', data=data, params=params)
    # e.g. search_for travelsName
    for bus in buses:
        if search_term and search_term.lower() in bus[search_for].lower() and bus['avalableSeats'] > 0:
            notify(alert_payload(bus))