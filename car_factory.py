from car import Car
from engine import capulet_engine, willoughby_engine, sternman_engine
from battery import spindler_battery, nubbin_battery
from tire import carrigan_tire, octoprime_tire


class CarFactory:

    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_array):
        return Car(capulet_engine.CapuletEngine(last_service_mileage, current_mileage),
                   spindler_battery.SpindlerBattery(current_date, last_service_date), carrigan_tire.CarriganTire(tire_array))

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_array):
        return Car(willoughby_engine.WilloughbyEngine(last_service_mileage, current_mileage),
                   spindler_battery.SpindlerBattery(current_date, last_service_date), carrigan_tire.CarriganTire(tire_array))

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on, tire_array):
        return Car(sternman_engine.SternmanEngine(warning_light_on),
                   spindler_battery.SpindlerBattery(current_date, last_service_date), carrigan_tire.CarriganTire(tire_array))

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_array):
        return Car(willoughby_engine.WilloughbyEngine(last_service_mileage, current_mileage),
                   nubbin_battery.NubbinBattery(current_date, last_service_date), octoprime_tire.OctoprimeTire(tire_array))

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_array):
        return Car(capulet_engine.CapuletEngine(last_service_mileage, current_mileage),
                   nubbin_battery.NubbinBattery(current_date, last_service_date), octoprime_tire.OctoprimeTire(tire_array))
