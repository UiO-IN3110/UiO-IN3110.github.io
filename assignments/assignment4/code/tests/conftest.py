import sys
from pathlib import Path

assignment4 = Path(__file__).parent.parent.absolute()

# Ensure assignment4 dir is on sys.path
sys.path.insert(0, str(assignment4))
