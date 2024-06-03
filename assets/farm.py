from win32api import GetSystemMetrics

WIDTH = GetSystemMetrics(0)
HEIGHT = GetSystemMetrics(1)
FPS = 100

CREATURE_LIST = []
FOOD_LIST = []
STATS_TEMPLATE = """Creatures count - {}\t\nFood count - {}\t\nNewborn DNA - {}"""
STATS = {"creatures": 0, "food": 0, "dna": "no data"}
