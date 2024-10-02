from .config import settings
import os

if not os.path.exists("sessions"):
    os.makedirs("sessions")
