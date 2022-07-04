#ต้อง import แบบนี้เสมอสำหรับ abstact class
from abc import ABC, abstractmethod


class Vehicle(ABC):
    def  __init__(self,brand,speed) -> None:
        super().__init__()
        self.brand = brand
        self.speed = speed
        self.gear = 0
        self.seat = 0

    