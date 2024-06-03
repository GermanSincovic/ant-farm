import time

import numpy
import pygame

from assets import Nature
from assets.Food import Food
from assets.farm import CREATURE_LIST, FOOD_LIST


class Creature:
    def __init__(self):
        self.__birthdate = int(time.time())
        self.position_x = None
        self.position_y = None
        self.color = None
        self.size = None
        self.sex = None
        self.dna = None
        self.body = None

        self.health = None
        self.aggression_rate = None
        self.strength_rate = None
        self.speed_rate = None
        self.sensitivity_rate = None

        self.__target = None

        self.direction = None

    def get_age(self):
        return int(time.time()) - self.__birthdate

    def move(self):
        if self.direction is not None:
            self.position_x += numpy.cos(self.direction) * self.speed_rate / 5
            self.position_y += numpy.sin(self.direction) * self.speed_rate / 5

        if self.meet_with(self.__target, Food):
            self.eat()

        if self.meet_with(self.__target, Creature) \
                and self.__target.sex == self.sex:
            self.attack()

        if self.meet_with(self.__target, Creature) \
                and self.__target.sex != self.sex:
            Nature.multiply(self.__target, self)

    def search_closest_food(self):
        self.__target = self.get_closest_object(FOOD_LIST)
        self.set_direction_to_target()

    def search_closest_partner(self):
        if self.sex == 1:
            self.__target = self.get_closest_object(CREATURE_LIST, sex=0)
        else:
            self.__target = self.get_closest_object(CREATURE_LIST, sex=1)
        self.set_direction_to_target()

    def eat(self):
        self.health += self.__target.value
        FOOD_LIST.remove(self.__target)

    def attack(self):
        self.__target.health -= 2 / self.aggression_rate

    def health_check(self):
        self.health -= 0.5 / self.strength_rate
        if self.health <= 0:
            self.die()

    def die(self):
        print("R.I.P. [" + str(self.dna) + "] lifetime - " + str(int(time.time()) - self.__birthdate) + " seconds")
        CREATURE_LIST.remove(self)

    def redraw(self):
        if self.health < 100:
            self.search_closest_food()
        else:
            self.search_closest_partner()
        self.move()
        self.health_check()
        pygame.draw.circle(pygame.display.get_surface(), self.color, (self.position_x, self.position_y), self.size)

    def get_closest_object(self, object_list, sex=None):
        closest_object = None
        min_distance = float('inf')

        if sex is not None:
            object_list = filter(lambda o: o.sex == sex, object_list)

        for obj in object_list:
            dx = self.position_x - obj.position_x
            dy = self.position_y - obj.position_y
            distance = numpy.hypot(dx, dy)

            if distance < min_distance:
                min_distance = distance
                closest_object = obj

        return closest_object

    def set_direction_to_target(self):
        if self.__target is not None:
            dx = self.__target.position_x - self.position_x
            dy = self.__target.position_y - self.position_y
            self.direction = numpy.arctan2(dy, dx)

    def meet_with(self, target, clazz):
        if isinstance(target, clazz) \
                and numpy.abs(self.__target.position_x - self.position_x) < 1 \
                and numpy.abs(self.__target.position_y - self.position_y) < 1:
            return True
