# ...existing Alembic env.py code...
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))
from models import Base

# ...existing code...

target_metadata = Base.metadata

# ...existing code...
