from tg_bot import LOAD, NO_LOAD, LOGGER

def __list_all_modules():
    from os.path import dirname, basename, isfile
    import glob
    
    # Get the path to the current directory
    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    
    # Generate a list of all Python files (excluding __init__.py)
    all_modules = [basename(f)[:-3] for f in mod_paths if isfile(f) and f.endswith(".py") and not f.endswith('__init__.py')]

    # If LOAD or NO_LOAD is specified, filter the modules accordingly
    if LOAD or NO_LOAD:
        to_load = LOAD if LOAD else all_modules  # Use LOAD if specified, otherwise use all modules

        # Validate modules in LOAD
        if LOAD:
            if not all(any(mod == module_name for module_name in all_modules) for mod in LOAD):
                LOGGER.error("Invalid load order names. Quitting.")
                quit(1)

        # Exclude modules listed in NO_LOAD
        if NO_LOAD:
            LOGGER.info("Not loading: %s", NO_LOAD)
            to_load = [item for item in to_load if item not in NO_LOAD]

        return to_load

    return all_modules

# List all modules and sort them
ALL_MODULES = sorted(__list_all_modules())

# Log the modules to be loaded
LOGGER.info("Modules to load: %s", str(ALL_MODULES))

# Expose ALL_MODULES for other parts of the application to use
__all__ = ALL_MODULES + ["ALL_MODULES"]
