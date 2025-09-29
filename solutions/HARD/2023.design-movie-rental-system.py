# Problem ID: 2023
# Title: Design Movie Rental System
# Runtime: 688 ms

class MovieRentingSystem:

    from sortedcontainers import SortedSet
    def __init__(self, n: int, entries: List[List[int]]):
        self.movies = defaultdict(SortedSet) # movies -> (price,shop)
        self.rented = SortedSet()   #(price,shop,movie)
        self.moviePrice = {} #(movie,shop ) -> price
        for shop, movie, price in entries:
            self.movies[movie].add((price,shop))
            self.moviePrice[(movie,shop)] = price
        

    def search(self, movie: int) -> List[int]:
        return [m[1] for m in self.movies[movie][:min(len(self.movies[movie]),5)]]

    def rent(self, shop: int, movie: int) -> None:
        price = self.moviePrice[(movie,shop)]
        self.rented.add((price,shop,movie))
        self.movies[movie].discard(((price,shop)))

    def drop(self, shop: int, movie: int) -> None:
        price = self.moviePrice[(movie,shop)]
        self.rented.discard((price,shop,movie))
        self.movies[movie].add(((price,shop)))

    def report(self) -> List[List[int]]:
        return [[m[1],m[2]] for m in self.rented][:5]


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()