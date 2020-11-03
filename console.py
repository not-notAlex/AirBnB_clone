#!/usr/bin/python3
"""
command interpreter
"""


import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    The command class
    """
    prompt = "(hbnb)"
    cls = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def do_exit(self, arg):
        """
        exits the console
        """
        return True

    def do_EOF(self, arg):
        """
        exits on EOF
        """
        print()
        return True

    def do_create(self, arg):
        """
        creates an object
        """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in self.cls:
            print("** class doesn't exist **")
        else:
            obj = eval(arg)()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """
        shows an object with given id
        """
        if len(arg) == 0:
            print("** class name missing **")
            return
        coms = tuple(arg.split())
        if coms[0] not in self.cls:
            print("** class doesn't exist **")
        elif len(coms) < 2:
            print("** instance id missing **")
        else:
            obj = coms[0] + "." + coms[1]
            if obj not in storage.all().keys():
                print("** no instance found **")
            else:
                print(storage.all()[obj])

    def do_destroy(self, arg):
        """
        deletes an object with given id
        """
        if len(arg) == 0:
            print("** class name missing **")
            return
        coms = tuple(arg.split())
        if coms[0] not in self.cls:
            print("** class doesn't exist **")
        elif len(coms) < 2:
            print("** instance id missing **")
        else:
            obj = coms[0] + "." + coms[1]
            if obj not in storage.all().keys():
                print("** no instance found **")
            else:
                del storage.all()[obj]
                storage.save()

    def do_all(self, arg):
        """
        shows all objects of given type
        """
        l = []
        if len(arg) == 0:
            for obj in storage.all().values():
                l.append(str(obj))
            print(l)
        else:
            coms = tuple(arg.split())
            if coms[0] in self.cls:
                for k, v in storage.all().items():
                    if coms[0] in k:
                        l.append(str(v))
                print(l)
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """
        upadates an object with new attribute
        """
        if len(arg) == 0:
            print("** class name missing **")
            return
        coms = tuple(arg.split())
        if coms[0] not in self.cls:
            print("** class doesn't exist **")
        elif len(coms) < 2:
            print("** instance id missing **")
            return
        obj = coms[0] + "." + coms[1]
        if obj not in storage.all().keys():
            print("** no instance found **")
        elif len(coms) < 3:
            print("** attribute name missing **")
        elif len(coms) < 4:
            print("** value missing **")
        else:
            typecast = type(eval(coms[3]))
            form = coms[3].strip('"')
            form = form.strip("'")
            setattr(storage.all()[obj], coms[2], typecast(form))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
