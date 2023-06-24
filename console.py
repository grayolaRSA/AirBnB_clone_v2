#!/usr/bin/python3
"""Console Module"""
import cmd
import sys
import shlex
import models
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
               "Place": Place, "Review": Review, "State": State, "User": User}

    def emptyline(self):
        """Handles empty line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def _key_value_parser(self, args):
        """creates a dictionary from a list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except ValueError:
                        try:
                            value = float(value)
                        except ValueError:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, arg):
        """Create a new instance of a class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            new_dict = self._key_value_parser(args[1:])
            instance = classes[args[0]](**new_dict)
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            objects = FileStorage().all()
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            objects = FileStorage().all()
            if key in objects:
                del objects[key]
                FileStorage().save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of instances"""
        objects = FileStorage().all()
        objects_list = []
        if not arg:
            for key in objects:
                objects_list.append(str(objects[key]))
            print(objects_list)
        elif arg in self.classes:
            for key in objects:
                if key.split(".")[0] == arg:
                    objects_list.append(str(objects[key]))
            print(objects_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            objects = FileStorage().all()
            if key in objects:
                obj = objects[key]
                attr_name = args[2]
                attr_value = args[3]
                if hasattr(obj, attr_name):
                    attr_type = type(getattr(obj, attr_name))
                    setattr(obj, attr_name, attr_type(attr_value))
                    obj.save()
                else:
                    print("** attribute doesn't exist **")
            else:
                print("** no instance found **")

    def do_EOF(self, arg):
        """Handles end-of-file (EOF) signal"""
        return True

    def postloop(self):
        """Prints a new line after exiting the command loop"""
        print()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
