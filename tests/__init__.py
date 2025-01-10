import sys
from pathlib import Path

# Adds 'src' to PYTHONPATH for importing the 'constify/src/constify' package
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'src'))