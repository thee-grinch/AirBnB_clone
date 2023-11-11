#!/usr/bin/python3
"""Represents the Command Interpreter for HBNB"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review


def parse_command(arg):
    """
    Parse the command string and return the class name and instance ID.
    """
    args = shlex.split(arg)
    class_name = None
    instance_id = None

    if len(args) >= 1:
        sections = args[0].split('.')
        if len(sections) == 1:
            class_name = sections[0]
        elif len(sections) == 2:
            class_name, instance_id = sections[0], sections[1]
    if len(args) >= 2:
        instance_id = args[1]
    return class_name, instance_id


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class to implement the command-line interpreter
    """

    prompt = "(hbnb) "
    __classes = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    ]

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
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        else:
            new_instance = eval(class_name)()

            storage.new(new_instance)
            storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
            Usage: show <class> <id> or <class>.show(<id>)"""
        class_name, instance_id = parse_command(arg)
        if not class_name:
            print("** class name missing **")
            return
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if not instance_id:
            print("** instance id missing **")
            return
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        else:
            print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Delete an instance by class name and ID.
        Usage: destroy <class name> <instance ID> or
        destroy <class name>.<instance ID>
        """
        class_name, instance_id = parse_command(arg)
        if not class_name:
            print("** class name missing **")
            return
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if not instance_id:
            print("** instance id missing **")
            return
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """
        Print the string representation of all instances based on class name.
        Usage: all [optional: <class name>]
        """
        class_name, _ = parse_command(arg)
        if class_name:
            if class_name not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
            instances = []
            for instance in storage.all().values():
                if instance.__class__.__name__ == class_name:
                    instances.append(str(instance))
            print(instances)
        else:
            instances = []
            for instance in storage.all().values():
                instances.append(str(instance))
            print(instances)

    def do_update(self, arg):
        """
        Update an instance's attribute by class name and ID.
        Usage: update <class name> <instance ID>
        <attribute name> "<attribute value>"
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return False
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_name = args[2]
        attribute_value = args[3]
        instance = storage.all()[key]
        if hasattr(instance, attribute_name):
            existing_attribute_type = type(getattr(instance, attribute_name))
            attribute_value = existing_attribute_type(attribute_value)
            setattr(instance, attribute_name, attribute_value)
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
