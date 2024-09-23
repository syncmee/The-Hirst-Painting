#Question 2: Do django signals run in the same thread as the caller?
# Please support your answer with a code snippet that conclusively proves your stance.
# The code does not need to be elegant and production ready, we just need to understand your logic.

# >> Answer : Yes, Django signals run in the same thread as the caller by default.

import threading
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Signal handler
@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal received!")
    print(f"Signal is running in thread: {threading.current_thread().name}")  # Check current thread
    time.sleep(2)  # Simulate slow task
    print("Signal done!")


# Simulate saving a user
if __name__ == "__main__":
    print("Main code is running in thread:", threading.current_thread().name)  # Check main thread
    print("About to save user...")

    user = User(username='testuser', password='password')
    user.save()  # This triggers the post_save signal

    print("User saved!")
