import fpdf
import sqlite3


class User:

    def __init__(self, name):
        self.name = name

    def buy(self, seat, card):
        pass


class Seat:

    database = "cinema.db"

    def __init__(self, seat_id):
        self.seat_id = seat_id

    def get_price(self):
        """Get the price of a specific seat"""
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "price" FROM "Seat" WHERE "seat_id" = ?
        """, [self.seat_id])
        price = cursor.fetchall()[0][0]
        return price

    def is_free(self):
        """Check if seat is available"""
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "taken" FROM "Seat" WHERE "seat_id" = ?
        """, [self.seat_id])
        result = cursor.fetchall()[0][0]

        if result == 0:
            return True
        else:
            return False

    def occupy(self):
        """Change the value of the taken seat in the database"""
        if self.is_free():
            connection = sqlite3.connect(self.database)
            cursor = connection.cursor()
            cursor.execute("""
                    UPDATE "Seat" SET "taken"=? WHERE "seat_id"=?
                    """, [1, self.seat_id])
            connection.commit()
            connection.close()


class Card:
    def database(self):
        pass

    def type(self):
        pass

    def number(self):
        pass

    def cvc(self):
        pass

    def holder(self):
        pass

    def validate(self, price):
        pass


class Ticket:
    def id(self):
        pass

    def user(self):
        pass

    def price(self):
        pass

    def seat(self):
        pass

    def to_pdf(self, path):
        pass


name = input("Enter your full name: ")
seat_id = input("Enter preferred seat number: ")