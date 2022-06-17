from datetime import date

from battery.battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, current_date: date, last_service_date: date):
        super().__init__()
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_services(self) -> bool:
        return (self.current_date - self.last_service_date).days > 365 * 2

