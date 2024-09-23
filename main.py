# Question 1: By default are django signals executed synchronously or asynchronously?
# Please support your answer with a code snippet that conclusively proves your stance.
# The code does not need to be elegant and production ready, we just need to understand your logic.

# >> Answer : Django signals are executed synchronously.

import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


# Signal handler that waits for 5 seconds
@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal received!")
    time.sleep(5)  # Wait for 5 seconds to simulate slow processing
    print("Signal done!")


# Simulating saving a user
if __name__ == "__main__":
    print("About to save user...")

    # Create a new user (this will trigger the signal)
    user = User(username='newuser', password='mypassword')
    user.save()  # post_save signal is triggered here

    print("User saved!")



