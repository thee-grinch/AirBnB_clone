#!/usr/bin/python3
"""Represents the Command Interpreter for HBNB"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.city import City


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
        args = shlex.split(arg)
        if len(args) == 0:
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
        else:
            print(storage.all()[key])

    def do_show(self, arg):
        """
        Delete an instance by class name and ID.
        Usage: destroy <class name> <instance ID>
        """
        args = shlex.split(arg)
        if len(args) == 0:
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
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """
        Print the string representation of all instances based on class name.
        Usage: all [optional: <class name>]
        """
        args = shlex.split(arg)
        instances = []
        if not args:
            for _, value in storage.all().items():
                instances.append(str(value))
            print(instances)
            return
        class_name = args[0]
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        for key, value in storage.all().items():
            if key.split(".")[0] == class_name:
                instances.append(str(value))
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
        if class_name not in storage.classes:
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
            instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
