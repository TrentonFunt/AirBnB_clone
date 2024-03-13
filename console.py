#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class definition
    """
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """An empty line + ENTER should not execute anything"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel,
           saves it (to the JSON file) and prints the id"""
        if not args:
            print("** class name missing **")
            return

        try:
            new_instance = eval(args)()
            new_instance.save()
            print(new_instance.id)
        except Exception as e:
            print("**", e)

    def do_show(self, args):
        """Prints the string representation of an instance based on the class
           name and id"""
        if not args:
            print("** class name missing **")
            return
        arg_list = shlex.split(args)
        if len(arg_list) == 0:
            print("** class name missing **")
            return
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        try:
            obj_dict = storage.all()
            key = "{}.{}".format(arg_list[0], arg_list[1])
            print(obj_dict[key])
        except KeyError:
            print("** no instance found **")
        except Exception as e:
            print("**", e)

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return
        arg_list = shlex.split(args)
        if len(arg_list) == 0:
            print("** class name missing **")
            return
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        try:
            obj_dict = storage.all()
            key = "{}.{}".format(arg_list[0], arg_list[1])
            del obj_dict[key]
            storage.save()
        except KeyError:
            print("** no instance found **")
        except Exception as e:
            print("**", e)

    def do_all(self, args):
        """Prints all string representation of all instances based
           or not on the class name"""
        try:
            obj_dict = storage.all()
            if not args:
                print([str(obj) for obj in obj_dict.values()])
            else:
                arg_list = shlex.split(args)
                if arg_list[0] not in storage.classes:
                    print("** class doesn't exist **")
                    return
                print([str(obj) for key, obj in obj_dict.items()
                       if arg_list[0] in key])
        except Exception as e:
            print("**", e)

    def do_update(self, args):
        """Updates an instance based on the class name and id
           by adding or updating attribute"""
        if not args:
            print("** class name missing **")
            return
        arg_list = shlex.split(args)
        if len(arg_list) == 0:
            print("** class name missing **")
            return
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        if len(arg_list) == 2:
            print("** attribute name missing **")
            return
        if len(arg_list) == 3:
            print("** value missing **")
            return
        try:
            obj_dict = storage.all()
            key = "{}.{}".format(arg_list[0], arg_list[1])
            obj = obj_dict[key]
            setattr(obj, arg_list[2], arg_list[3])
            storage.save()
        except KeyError:
            print("** no instance found **")
        except Exception as e:
            print("**", e)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
