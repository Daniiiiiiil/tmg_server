import random, math


class Game:
    """Game information"""
    __games = []

    def __init__(self):
        self.__coordinates = (
            random.randrange(1, 100),
            random.randrange(1, 100),
        )
        Game.__games.append(self)
    
    def get_id(self) -> int:
        """Returns game ID"""
        return Game.__games.index(self)
    
    def get_distance(self, hit: tuple[int, int]) -> float:
        """Returns distance between treasure and hit"""
        diff_x = hit[0] - self.__coordinates[0]
        diff_y = hit[1] - self.__coordinates[1]
        return math.sqrt((diff_x**2) + (diff_y**2))
    
    @staticmethod
    def is_exists(id: int) -> bool:
        if id in range(len(Game.__games)):
            return True
        
        return False
    
    @staticmethod
    def check_hit(id: int, hit: tuple[int, int]) -> str:
        """Returns match rate for treasure and hit"""
        game = Game.__games[id]
        distance = game.get_distance(hit)
        if distance <= 10:
            return "Very Hot!"
        elif distance <= 15:
            return "Hot!"
        elif distance <= 20:
            return "Warm!"
        elif distance <= 30:
            return "Cold!"

        return "Very Cold!"
