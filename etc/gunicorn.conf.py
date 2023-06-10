import multiprocessing
import os
import sys
import pathlib

sys.path.append(
    pathlib.Path(__file__).parent.parent.__str__(),
)


bind = "127.0.0.1:8000"
workers = multiprocessing.cpu_count() + 1


