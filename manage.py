#!/usr/bin/python
from flask.ext.script import Server, Manager
from GUTG_Vote import create_app

manager = Manager(create_app)
manager.add_command("runserver", Server())


if __name__ == "__main__":
    manager.run()