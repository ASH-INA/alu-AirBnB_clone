#!/usr/bin/python3
""" Command interpreter implementation """

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.storage import FileStorage

# Create an instance of FileStorage to manage object persistence
storage = FileStorage()
storage.reload()

class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB"""

    prompt = "(hbnb) "

    def do_create(self, args):
        """Create a new instance of a class"""
        if not args:
            print("** class name missing **")
            return
        class_name = args.split()[0]
        if class_name not in globals() or class_name not in globals()[class_name].__bases__:
            print("** class doesn't exist **")
            return
        instance = globals()[class_name]()
        instance.save()
        print(instance.id)

    def do_show(self, args):
        """Show an instance by ID"""
        args = args.split()
        if len(args) < 2:
            print("** class name or ID missing **")
            return
        class_name, instance_id = args
        if class_name not in globals() or class_name not in globals()[class_name].__bases__:
            print("** class doesn't exist **")
            return
        instances = storage.all()
        key = f"{class_name}.{instance_id}"
        if key in instances:
            print(instances[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """Destroy an instance by ID"""
        args = args.split()
        if len(args) < 2:
            print("** class name or ID missing **")
            return
        class_name, instance_id = args
        if class_name not in globals() or class_name not in globals()[class_name].__bases__:
            print("** class doesn't exist **")
            return
        instances = storage.all()
        key = f"{class_name}.{instance_id}"
        if key in instances:
            del instances[key]
            storage.save()
            print("** instance deleted **")
        else:
            print("** no instance found **")

    def do_all(self, args):
        """Show all instances of a class"""
        if args:
            class_name = args.split()[0]
            if class_name not in globals() or class_name not in globals()[class_name].__bases__:
                print("** class doesn't exist **")
                return
            instances = storage.all()
            result = [str(instance) for key, instance in instances.items() if key.startswith(class_name)]
            print(result)
        else:
            instances = storage.all()
            result = [str(instance) for instance in instances.values()]
            print(result)

    def do_update(self, args):
        """Update an instance by ID"""
        args = args.split()
        if len(args) < 4:
            print("** class name, ID, attribute name, or value missing **")
            return
        class_name, instance_id, attribute_name, attribute_value = args
        if class_name not in globals() or class_name not in globals()[class_name].__bases__:
            print("** class doesn't exist **")
            return
        instances = storage.all()
        key = f"{class_name}.{instance_id}"
        if key in instances:
            instance = instances[key]
            setattr(instance, attribute_name, attribute_value)
            instance.save()
            print("** instance updated **")
        else:
            print("** no instance found **")

    def do_quit(self, args):
        """Quit the command interpreter"""
        return True

    def do_EOF(self, args):
        """Handle End Of File"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
