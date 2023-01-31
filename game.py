import random, math


class Game:
    """Game information"""
    __games = []

    def __init__(self):
        self.__coordinates = (
            random.randrange(1, 100),
            random.randrange(1, 100),
        )
        self.is_finished = False
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
    def is_available(id: int) -> bool:
        is_available = False
        if id in range(len(Game.__games)):
            is_available = not Game.__games[id].is_finished
        return is_available
    
    @staticmethod
    def check_hit(id: int, hit: tuple[int, int]) -> float:
        """Returns match rate for treasure and hit"""
        game = Game.__games[id]
        distance = game.get_distance(hit)
        
        if distance <= 10:
            game.is_finished = True
            return (5/5)    # "You Win!"
        elif distance <= 15:
            return (4/5)    # "Very Hot!"
        elif distance <= 25:
            return (3/5)    # "Hot!"
        elif distance <= 35:
            return (2/5)    # "Warm!"
        elif distance <= 45:
            return (1/5)    # "Cold!"

        return 0   # "Very Cold!"
