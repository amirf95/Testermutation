import os
import sys
import shutil
import subprocess
from mutations import MUTATIONS

ORIGINAL = "example.py"
BACKUP = "backup.py"
TEST_FILE = "test_example.py"

def backup_original():
    shutil.copy(ORIGINAL, BACKUP)

def restore_original():
    shutil.copy(BACKUP, ORIGINAL)

def mutate_and_test():
    with open(BACKUP, 'r') as file:
        original_code = file.read()

    killed = 0
    total = 0

    for target, replacement in MUTATIONS.items():
        if target not in original_code:
            continue

        mutated_code = original_code.replace(target, replacement, 1)

        with open(ORIGINAL, 'w') as file:
            file.write(mutated_code)

        result = subprocess.run([sys.executable, "-m", "pytest", TEST_FILE], capture_output=True, text=True)

        if result.returncode != 0:
            print(f"KILLED: {target} → {replacement}")
            killed += 1
        else:
            print(f"SURVIVED: {target} → {replacement}")

        total += 1
        restore_original()

    print(f"\nMutation Score: {killed}/{total} = {(killed/total)*100:.2f}%")

if __name__ == "__main__":
    backup_original()
    mutate_and_test()
    restore_original()
