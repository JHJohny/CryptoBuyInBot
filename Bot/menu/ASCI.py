import random

"""ASCI - sotred ascis for menu mostly"""
#Have and import one python file is more simple and elegant than have json/yaml file and import whole json/yaml library + os


class classproperty(property):
    def __get__(self, obj, objtype=None):
        return super(classproperty, self).__get__(objtype)
    def __set__(self, obj, value):
        super(classproperty, self).__set__(type(obj), value)
    def __delete__(self, obj):
        super(classproperty, self).__delete__(type(obj))

class ASCI:
    asci_logo_first = """
 .d8888b.                            888                   888               888           .d8888b.       d888   
d88P  Y88b                           888                   888               888          d88P  Y88b     d8888   
888    888                           888                   888               888          888    888       888   
888        888d888 888  888 88888b.  888888  .d88b.        88888b.   .d88b.  888888       888    888       888   
888        888P"   888  888 888 "88b 888    d88""88b       888 "88b d88""88b 888          888    888       888   
888    888 888     888  888 888  888 888    888  888       888  888 888  888 888          888    888       888   
Y88b  d88P 888     Y88b 888 888 d88P Y88b.  Y88..88P       888 d88P Y88..88P Y88b.        Y88b  d88P d8b   888   
 "Y8888P"  888      "Y88888 88888P"   "Y888  "Y88P"        88888P"   "Y88P"   "Y888        "Y8888P"  Y8P 8888888 
                        888 888                                                                                  
                   Y8b d88P 888                                                                                  
                    "Y88P"  888                                                                                  """
    asci_logo_second = """
   ___                 _          _           _      ___   _ 
  / __\ __ _   _ _ __ | |_ ___   | |__   ___ | |_   / _ \ / |
 / / | '__| | | | '_ \| __/ _ \  | '_ \ / _ \| __| | | | || |
/ /__| |  | |_| | |_) | || (_) | | |_) | (_) | |_  | |_| || |
\____/_|   \__, | .__/ \__\___/  |_.__/ \___/ \__|  \___(_)_|
           |___/|_|                                          """

    asci_fancy_line_one = """####### ####### ####### ####### ####### ####### ####### ####### ####### #######"""
    asci_fancy_line_two = """ooooooooo ooooooooo ooooooooo ooooooooo ooooooooo ooooooooo ooooooooo"""
    asci_fancy_line_three = """>====> >====> >====> >====> >====> >====> >====> >====> >====> >====>"""
    asci_fancy_line_four = """|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____"""

    @classproperty
    def random_logo(cls):
        logos = [cls.asci_logo_first, cls.asci_logo_second]
        return random.choice(logos)

    @classproperty
    def random_fancy_line(cls):
        lines = [cls.asci_fancy_line_one, cls.asci_fancy_line_two, cls.asci_fancy_line_three, cls.asci_fancy_line_four]
        return random.choice(lines)
