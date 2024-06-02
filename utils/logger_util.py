import inspect
import logging
import datetime

"""
Utility to help with logging.
"""


def logger_tool(log_level=logging.INFO):
    log_filename = f"C:\\Users\\james\\workspace_python\\SeleniumTestFrameworkPython\\logs\\{datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S")}.log"
    logger_caller_name = inspect.stack()[1][3]

    logger = logging.getLogger(logger_caller_name)
    logger.setLevel(log_level)

    file_handler = logging.FileHandler(log_filename, mode='a')
    file_handler.setLevel(log_level)

    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s: %(message)s",
        datefmt="%Y%m%d %I:%M:%S %p"
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
