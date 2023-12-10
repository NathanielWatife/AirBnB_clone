import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print()  # Add a newline before exiting
        return True

    def emptyline(self):
        """Do nothing while receiving an empty line."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
