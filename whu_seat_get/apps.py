from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'
class WhuSeatGetConfig(AppConfig):
    name = 'whu_seat_get'
