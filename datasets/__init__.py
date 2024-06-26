from termcolor import colored
import sys
import importlib.util

datasets = {}


def register(name):

    def decorator(cls):
        datasets[name] = cls
        return cls

    return decorator


def make(name, config):
    if name == "hmvs":
        found_opt1 = importlib.util.find_spec("R3DParser") is not None
        found_opt2 = importlib.util.find_spec("R3DUtil") is not None
        if found_opt1:
            import R3DParser
        elif found_opt2:
            import R3DUtil
        else:
            print(
                "In case you are deploying on", colored("cloud,",
                        'yellow'), "compiled parsers such as",
                colored("'R3DUtils'", 'yellow'), "or",
                colored("'R3DParser'", 'yellow'),
                "should be explicitly included,")
            print(colored("with", 'blue'),
                    "export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${HOME}/Documents/buildboat/R3DParser/3rd/R3DLib/bin/")
        from . import hmvs
    dataset = datasets[name](config)
    return dataset


from . import blender, colmap, dtu
