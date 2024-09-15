from django.db.models.signals import post_save
from django.dispatch import receiver
from . models import Mymodel
import threading
import time

@receiver(post_save, sender=Mymodel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal received for:", instance.name)
    print("Inside signal handler, Thread ID:", threading.get_ident())
    time.sleep(2)
    print("Signal handler finished")