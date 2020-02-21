class Library:
    def __init__(self, id, signup_days, ship, books):
        self.id = id
        self.signup_days = signup_days
        self.ship = ship
        self.unique_books = books
        self.score = 0
        self.sinupDate=0
        self.is_open = True
        self.scanned_book=0
        self.booktokeep = []
        self.max_score=0
