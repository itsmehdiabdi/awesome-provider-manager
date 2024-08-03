from typing import Literal

"""
    different ways of connection to a worker
"""
Connection = Literal["local", "queue", "http"]
