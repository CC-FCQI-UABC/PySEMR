import os
import random
def randomize(file_name):
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data_mexicana', file_name)
    with open(file_path, 'r') as f:
        lines = f.readlines()
        return random.choice(lines).strip()
