#Question 3: By default do django signals run in the same database transaction as the caller?
# Please support your answer with a code snippet that conclusively proves your stance.
# The code does not need to be elegant and production ready, we just need to understand your logic.

# >> Answer : By default, Django signals do not run in the same database transaction as the caller unless the signal is specifically tied to a transaction.

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from django.contrib.auth.models import User


# Signal handler for post_save
@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal received after user save!")
    print(f"User in signal: {instance.username}")


# Simulate saving a user with transaction
if __name__ == "__main__":
    print("Starting transaction...")

    try:
        with transaction.atomic():  # Start a transaction
            user = User(username='transaction_user', password='password')
            user.save()  # This triggers post_save signal
            print("User saved, but transaction not committed yet!")
            raise Exception("Simulating error, transaction will be rolled back!")

    except Exception as e:
        print(f"Error occurred: {e}")

    print("Transaction block ended.")

