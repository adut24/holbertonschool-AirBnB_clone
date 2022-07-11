#!/usr/bin/python3
"""
    Console Module from which everything is done
"""
import cmd
from models import storage
import shlex
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class HBNB Command"""
    cmd.Cmd.prompt = "(hbnb) "
    list_class = ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity',
                  'Review']

    def emptyline(self):
        """Do nothing when Enter is pressed"""
        pass

    def do_quit(self, line):
        """Quit the console"""
        exit()

    def help_quit(self):
        """Informations about quit"""
        print('Quit command to exit the program\n')

    def do_EOF(self, line):
        """Quit the console"""
        print()
        exit()

    def help_EOF(self):
        """Informations about EOF"""
        print('Ctrl + D to exit the program\n')

    def do_create(self, line):
        """Create an instance, print its id and save it"""
        list = line.split()
        if len(list) < 1:
            print('** class name missing **')
        elif list[0] in self.list_class:
            my_model = eval(list[0])()
            my_model.save()
            print(my_model.id)
        else:
            print("** class doesn't exist **")

    def help_create(self):
        """Informations about create"""
        print('Create an instance, print its id and save it\n')

    def do_show(self, line):
        """Show string representation of an instance"""
        my_list = line.split()
        my_dict = storage.all()
        check = 0
        if len(my_list) == 0:
            print("** class name missing **")
        elif len(my_list) == 1 and my_list[0] in self.list_class:
            print("** instance id missing **")
        elif my_list[0] not in self.list_class:
            print("** class doesn't exist **")
        else:
            for k, v in my_dict.items():
                if k == f"{my_list[0]}.{my_list[1]}":
                    print(v)
                    check = 1
            if check == 0:
                print('** no instance found **')

    def help_show(self):
        """Informations about show"""
        print('Show string representation of an instance\n')

    def do_destroy(self, line):
        """Destroy an instance with its id"""
        list = line.split()
        dict = storage.all()
        check = 0
        if len(list) == 0:
            print("** class name missing **")
        elif list[0] not in self.list_class:
            print("** class doesn't exist **")
        elif len(list) == 1:
            print("** instance id missing **")
        else:
            for k, v in dict.copy().items():
                if k == f"{list[0]}.{list[1]}":
                    dict.pop(k)
                    storage.save()
                    check = 1
            if check == 0:
                print("** no instance found **")

    def help_destroy(self):
        """Informations about destroy"""
        print('Destroy an instance with its id\n')

    def do_all(self, line):
        """Print the string representation of all instances"""
        my_list = line.split()
        my_dict = storage.all()
        list_value = []
        if len(my_list) == 1 and my_list[0] not in self.list_class:
            print("** class doesn't exist **")
        elif len(my_list) == 0:
            for value in my_dict.copy().values():
                list_value.append(str(value))
            print(list_value)
        else:
            for value in my_dict.copy().values():
                if value.__class__.__name__ == my_list[0]:
                    list_value.append(str(value))
            print(list_value)

    def help_all(self):
        """Informations about all"""
        print("Print the string representation of all instances\n")

    def do_update(self, line):
        """Adding or updating attribute of an instance"""
        list = shlex.split(line, posix=False)
        dict = storage.all()
        my_obj = None
        if len(list) == 0:
            print("** class name missing **")
        elif list[0] not in self.list_class:
            print("** class doesn't exist **")
        elif len(list) == 1:
            print("** instance id missing **")
        else:
            for key, value in dict.copy().items():
                if key == f"{list[0]}.{list[1]}":
                    my_obj = value
            if my_obj is None:
                print("** no instance found **")
            elif len(list) == 2:
                print("** attribute name missing **")
            elif len(list) == 3:
                print("** value missing **")
            else:
                if list[3][0] == '"' or list[3][0] == "'":
                    setattr(my_obj, list[2], list[3][1:-1])
                elif '.' in list[3]:
                    setattr(my_obj, list[2], float(list[3]))
                else:
                    setattr(my_obj, list[2], int(list[3]))
                my_obj.save()

    def help_update(self):
        """Informations about update"""
        print("Adding or updating attribute of an instance\n")

    def do_count(self, line):
        """Count the number of instances of a class"""
        count = 0
        my_list = line.split()
        my_dict = storage.all()
        for v in my_dict.values():
            if v.__class__.__name__ == my_list[0]:
                count += 1
        print(count)

    def help_count(self):
        """Informations about count"""
        print("Count the number of instances of a class\n")

    def default(self, line):
        """Occured when no function are found"""
        list_cmd = ['create', 'show', 'all', 'destroy', 'update', 'count']
        s = line.replace('(', '.').replace(')', '.')
        s = s.replace(',', '.').replace(' ', '.')
        s = s.replace('{', '.').replace('}', '.').replace(':', '.')
        my_list = s.split('.')
        my_list = [i for i in my_list if i != '']
        if len(my_list) < 2 or my_list[1] not in list_cmd:
            print(f"*** Unknown syntax: {line}")
            return
        my_list[0], my_list[1] = my_list[1], my_list[0]
        if len(my_list) > 2:
            my_list[2] = my_list[2][1:-1]
            for i in range(3, len(my_list), 2):
                my_list[i] = my_list[i][1:-1]
        str_cmd = (' '.join(my_list))
        if my_list[0] == 'update':
            if len(my_list) > 3:
                start_cmd = my_list[0] + ' ' + my_list[1] + ' ' + my_list[2]
                for i in range(3, len(my_list), 2):
                    str_cmd = start_cmd + ' ' + my_list[i]
                    if i + 1 < len(my_list):
                        str_cmd += ' ' + my_list[i + 1]
                    self.onecmd(str_cmd)
            elif len(my_list) == 3:
                str_cmd = (' '.join(my_list))
                self.onecmd(str_cmd)
            else:
                self.onecmd(str_cmd)
        else:
            self.onecmd(str_cmd)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
