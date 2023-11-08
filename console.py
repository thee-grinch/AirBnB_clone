#!/usr/bin/python3
"""Represents the console class"""
import cmd
from models.base_model import BaseModel
from models import file_storage

class HBNBCommand(cmd.Cmd):
    """Console for the HBNB project"""

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Does nothing"""
        pass

    def do_create(self, arg):
        """Create a new class instance and prints its id
            Usage: create <class>"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            base = BaseModel()
            print(base.id)
            file_storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()