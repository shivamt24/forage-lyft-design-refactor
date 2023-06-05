
from car import Car
from engine import capulet_engine, willoughby_engine, sternman_engine
from battery import spindler_battery, nubbin_battery


class CarFactory:

    @staticmethod
    def create_calliope(last_service_date, current_mileage, last_service_mileage):
        return Car(capulet_engine.CapuletEngine(last_service_mileage, current_mileage),
                   spindler_battery.SpindlerBattery(last_service_date))
    @staticmethod
    def create_glissade(last_service_date, current_mileage, last_service_mileage):
        return Car(willoughby_engine.WilloughbyEngine(last_service_mileage, current_mileage),
                   spindler_battery.SpindlerBattery(last_service_date))
    @staticmethod
    def create_palindrome(last_service_date, warning_light_on):
        return Car(sternman_engine.SternmanEngine(warning_light_on),
                   spindler_battery.SpindlerBattery(last_service_date))
    @staticmethod
    def create_rorschach( last_service_date, current_mileage, last_service_mileage):
        return Car(willoughby_engine.WilloughbyEngine(last_service_mileage, current_mileage),
                   nubbin_battery.NubbinBattery(last_service_date))
    @staticmethod
    def create_thovex(last_service_date, current_mileage, last_service_mileage):
        return Car(capulet_engine.CapuletEngine(last_service_mileage, current_mileage),
                   nubbin_battery.NubbinBattery(last_service_date))