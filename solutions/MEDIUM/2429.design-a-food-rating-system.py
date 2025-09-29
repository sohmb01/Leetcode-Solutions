# Problem ID: 2429
# Title: Design a Food Rating System
# Runtime: 247 ms

from sortedcontainers import SortedList
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_info = {}
        self.sorted_cuisine = defaultdict(SortedList)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_info[food] = (cuisine, rating)
            self.sorted_cuisine[cuisine].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, rating = self.food_info[food]
        self.food_info[food] = (cuisine, newRating)
        self.sorted_cuisine[cuisine].discard((-rating, food))
        self.sorted_cuisine[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.sorted_cuisine[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)