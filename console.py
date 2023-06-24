#!/usr/bin/python3
"""Console Module"""
import cmd
import sys
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

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        """Handles empty line"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, line):
        """Create a new instance of a class"""
        if not line:
            print("** class name missing **")
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.classes[line]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
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

    def do_destroy(self, line):
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

    def do_all(self, line):
        """Prints all string representations of instances"""
        objects = FileStorage().all()
        objects_list = []
        if not line:
            for key in objects:
                objects_list.append(str(objects[key]))
            print(objects_list)
        elif line in self.classes:
            for key in objects:
                if key.split(".")[0] == line:
                    objects_list.append(str(objects[key]))
            print(objects_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args = line.split()
        if not line:
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

    def do_EOF(self, line):
        """Handles end-of-file (EOF) signal"""
        return True

    def postloop(self):
        """Prints a new line after exiting the command loop"""
        print()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
