import random

from colorhash import ColorHash

from assets import farm
from assets.Creature import Creature
from assets.Food import Food
from assets.farm import CREATURE_LIST, FOOD_LIST, STATS

DNA_LENGTH = 50


def get_position(parent1, parent2):
    return (parent1.get_position_x() + parent2.get_position_x()) / 2, \
           (parent1.get_position_y() + parent2.get_position_y()) / 2


def get_sex():
    return random.choice([1, 0])


def get_color(dna):
    return ColorHash(dna).rgb


def get_aggression_rate(dna):
    return str(dna).count('A')


def get_strength_rate(dna):
    return str(dna).count('C')


def get_speed_rate(dna):
    return str(dna).count('G')


def get_sensitivity_rate(dna):
    return str(dna).count('T')


def resolve_dna(parent1, parent2):
    return ''.join(random.choice([parent1.dna[i], parent2.dna[i]]) for i in range(DNA_LENGTH))


def multiply(parent1, parent2):
    if parent1.sex == 1:
        create_creature(parent1, parent2)
        parent1.health -= 50
        parent2.health -= 50


def generate_dna():
    return ''.join(random.choice(['A', 'C', 'G', 'T']) for _ in range(DNA_LENGTH))


def create_creature(parent1=None, parent2=None):
    new_creature = Creature()
    if parent1 is None and parent2 is None:
        new_creature.position_x = random.randrange(0, farm.WIDTH)
        new_creature.position_y = random.randrange(0, farm.HEIGHT)
        new_creature.dna = generate_dna()
        print(
            "New creature [" + new_creature.dna + "] was born by GOD")
    else:
        new_creature.position_x = parent1.position_x
        new_creature.position_y = parent1.position_y
        new_creature.dna = resolve_dna(parent1, parent2)
        print(
            "New creature [" + new_creature.dna + "] was born by [" + parent1.dna + "] and [" + parent2.dna + "]")
        STATS["dna"] = new_creature.dna

    new_creature.color = get_color(new_creature.dna)
    new_creature.sex = get_sex()
    new_creature.size = 15
    new_creature.health = 100
    new_creature.aggression_rate = get_aggression_rate(new_creature.dna)
    new_creature.strength_rate = get_strength_rate(new_creature.dna)
    new_creature.speed_rate = get_speed_rate(new_creature.dna)
    new_creature.sensitivity_rate = get_sensitivity_rate(new_creature.dna)

    CREATURE_LIST.append(new_creature)
    STATS["creatures"] = len(CREATURE_LIST)


def create_food():
    if random.random() < 0.1:
        new_food = Food()
        new_food.position_x = random.randrange(0, farm.WIDTH)
        new_food.position_y = random.randrange(0, farm.HEIGHT)
        new_food.value = random.randrange(30, 60)
        new_food.size = int(new_food.value / 10)
        FOOD_LIST.append(new_food)
        STATS["food"] = len(FOOD_LIST)
