# Author: Aline Lindholm Lima Botti
# GitHub username: Aline_Lima
# Date: 01/24/2023
# Description: Creates methods and members for the classes: LibraryItem, Patron and Library, and a class named Book, Album, and Movie. It is a Library simulator involving multiple classes.

from enum import Enum
   

Location = Enum("Location", ["ON_SHELF", "ON_HOLD_SHELF", "CHECKED_OUT"])


class LibraryItem:
    '''represents a library item that a patron can check out'''

    def __init__(self, id_code, title):
        '''takes a library item ID and title as parameters; checked_out_by and requested_by should be initialized to None;
      a new LibraryItem's location should be on the shelf'''
        self._id_code = id_code
        self._title = title
        # assumes location is by default ON_SHELF
        self._location = Location.ON_SHELF
        self._checked_out_by = None
        self._requested_by = None
        self._date_checked_out = None

    def get_id_code(self): return self._id_code

    def get_title(self): return self._title

    def get_location(self): return self._location

    "returns the Library Item's location"

    def get_checked_out_by(self): return self._checked_out_by

    def get_requested_by(self): return self._requested_by

    def get_date_checked_out(self): return self._date_checked_out

    def set_id_code(self, id_code): self._id_code = id_code

    def set_title(self, title): self._title = title

    def set_location(self, location): self._location = location

    def set_checked_out_by(self, checked_out_by): self._checked_out_by = checked_out_by

    def set_requested_by(self, request_by): self._request_by = request_by

    def set_date_checked_out(self, date_checked_out): self._date_checked_out = date_checked_out


class Book(LibraryItem):
    '''book class which contains author; get_check_out_length that returns the number of days that type of library
    item may be checked out for'''

    def __init__(self, id_code, title, author):
        super().__init__(id_code, title)
        self._author = author

    def get_author(self): return self._author

    def set_author(self, author): self._author = author

    # real code after getters and setters def get_check_out_length():
    def get_check_out_length(): return 21


class Album(LibraryItem):
    '''album class which contains artist; get_check_out_length that returns the number of days that type of library
        item may be checked out for'''

    def __init__(self, id_code, title, artist):
        super().__init__(id_code, title)
        self._artist = artist

    def get_check_out_length(): return 14

    def get_artist(self): return self._artist

    def set_artist(self, artist): self._artist = artist


class Movie(LibraryItem):
    '''album class which contains director; get_check_out_length that returns the number of days that type of library
            item may be checked out for'''

    def __init__(self, id_code, title, director):
        super().__init__(id_code, title)
        self._director = director

    def get_director(self): return \
        self._director

    def set_director(self, director):
        self._director = director

    # real code after getters and setters def get_check_out_length():
    def get_check_out_length(): return 7


class Patron():
    '''A Patron object represents a patron of a library. It has four data members: patron_id, name, checked_out_items, fine amount'''

    def __init__(self, idNum, name):
        self._id_num = idNum
        self._name = name
        self._checked_out_items = None
        self._fine_amount = 0

    # getters and setters
    def get_id_num(self):
        return self._id_num

    def get_name(self):
        return self._name

    def get_checked_out_items(self):
        return self._checked_out_items

    def get_fine_amount(self):
        return self._fine_amount

    def set_id_num(self, idNum):
        self._id_num = idNum

    def set_name(self, name):
        self._name = name

    def set_checked_out_items(self, items):
        self._checked_out_items = items

    def set_fine_amount(self, fine):
        self._fine_amount = fine

    # other code
    def add_library_item(self, item):
        if self._checked_out_items == None: self._checked_out_items = []
        self._checked_out_items.append(item)

    def remove_library_item(self, item):
        if self._checked_out_items == None:
            print("Error: nothing is checked out")
        self._checked_out_items.remove(item)

    def amend_fine(self, amount):
        self._fine_amount += amount


class Library():
    '''A Library object represents a library that contains variaous library items, and is used by various patrons. It has three data members:
    holding, members, current_date'''

    def __init__(self):
        self._holdings = []
        self._members = []
        self._current_date = 0

    def add_library_item(self, item):
        self._holdings.append(item)

    def add_patron(self, patron):
        self._members.append(patron)

    def get_library_item(self, id):
        for item in self._holdings:
            if item.getIdCode() == id:
                return item

    # go through all items in list, if not there, return None return None
    def get_patron(self, id):
        for member in self._members:
            if member.getIdNum() == id: return member

        return None

    def lookup_library_item_from_id(self, item, patron):
        if item not in self._holdings:
            return "item not found"
        elif patron not in self._members:
            return "patron not found"
        elif item.get_location() == Location.CHECKED_OUT:
            return "item already checked out"
        elif item.get_location() == Location.ON_HOLD_SHELF and item.get_requested_by() != patron:
            return "item on hold by other patron"
        else:
            item.set_checked_out_by(patron)
            item.set_date_checked_out(self._current_date)
            item.set_location(Location.CHECKED_OUT)
        if item.get_requested_by() != None:
            item.set_requested_by(None)
            patron.add_library_item(item)
            return "check out successful"

    def lookup_patron_from_id(self, item, patron):
        if item not in self._holdings:
            return "item not found"
        elif patron not in self._members:
            return "patron not found"
        elif item.get_location() == Location.CHECKED_OUT:
            return "item already checked out"
        elif item.get_location() == Location.ON_HOLD_SHELF and item.getRequestedBy() != patron:
            return "item on hold by other patron"
        else:
            item.set_checked_out_by(patron)
            item.set_date_checked_out(self._current_date)
            item.set_location(Location.CHECKED_OUT)
            if item.get_requested_by() != None:
                item.set_requested_by(None)

            patron.add_library_item(item)
            return "check out successful"

    def check_out_library_item(self, item, patron):
        if item not in self._holdings:
            return "item not found"
        elif patron not in self._members:
            return "patron not found"
        elif item.get_location() == Location.CHECKED_OUT:
            return "item already checked out"
        elif item.get_location() == Location.ON_HOLD_SHELF and item.get_requested_by() != patron:
            return "item on hold by other patron"
        else:
            item.set_checked_out_by(patron)
            item.set_date_checked_out(self._current_date)
            item.set_location(Location.CHECKED_OUT)
            if item.get_requested_by() != None:
                item.set_requested_by(None)

            patron.add_library_item(item)
            return "check out successful"

    def return_library_item(self, id):
        for member in self._members:
            if member.get_checked_out_items() != None:
                for item in member.get_checked_out_items():
                    if id == item.get_id_number():
                        item.set_checked_out_by(None)
                        item.set_location(Location.ON_SHELF)
                        member.remove_library_item(item)

    def request_library_item(self, id_num, id_code):
        ''' Puts LibraryItem on hold for a Patron.
        Sets item's location to "ON_HOLD_SHELF" and item's requested_by status to Patron.'''
        for patron in self._members:
            if patron.get_id_num() == id_num:
                for item in self._holdings:
                    if item.get_id_code() == id_code:
                        if item.get_requested_by() != None:  # if already on hold:
                            return "item already on hold"
                            # update item:
                        else:
                            item.set_requested_by(patron)
                            if item.get_location() == "ON_SHELF":
                                item.set_location("ON_HOLD_SHELF")

                            return "request successful"
                    else:
                        return "item not found"
            else:
                return "patron not found"

    def pay_fine(self, id, amount):
        ''' Amount = amount being paid and is positive.'''
        for patron in self._members:
            if patron.get_id_num() == id:
                patron.amend_fine(amount * -1)
                return "payment successful"
        return "patron not found"

    def increment_current_date(self):
        ''' It sets the current_date to +1.
        It increseases all patron fines +10 cents per item checked out
        by members list, patron.amend_fine().
        '''

        self._current_date += 1
        for patron in self._members:
            if patron.get_checked_out_items() != None:
                for item in patron.get_checked_out_items():
                    if (self._current_date - item.get_date_checked_out()) > item.get_check_out_length():
                        patron.amend_fine(0.10)


b1 = Book("345", "Phantom Tollbooth", "Juster")
a1 = Album("456", "...And His Orchestra", "The Fastbacks")
m1 = Movie("567", "Laputa", "Miyazaki")
print(b1.get_author())
print(a1.get_artist())
print(m1.get_director())

p1 = Patron("abc", "Felicity")
p2 = Patron("bcd", "Waldo")

lib = Library()
lib.add_library_item(b1)
lib.add_library_item(a1)
lib.add_patron(p1)
lib.add_patron(p2)

lib.check_out_library_item("bcd", "456")
for _ in range(7):
    lib.increment_current_date()  # 7 days pass
lib.check_out_library_item("abc", "567")
loc = a1.get_location()
lib.request_library_item("abc", "456")
for _ in range(57):
    lib.increment_current_date()  # 57 days pass
p2_fine = p2.get_fine_amount()
lib.pay_fine("bcd", p2_fine)
lib.return_library_item("456")