import fpdf
import sqlite3


class User:

    def __init__(self, name):
        self.name = name

    def buy(self, seat, card):
        pass


class Seat:
    def database(self):
        pass

    def seat_id(self):
        pass

    def price(self):
        pass

    def is_free(self):
        pass

    def occupy(self):
        pass


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