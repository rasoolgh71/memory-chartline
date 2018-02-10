import string
from .models import Used
from django.utils.crypto import get_random_string
from django.shortcuts import HttpResponse
from celery import task, shared_task
import subprocess
import datetime

@shared_task(name="repeat_cheak")
def repeat_cheak_info():
    mem = []
    process = subprocess.Popen(["free "], stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE, shell=True)
    disk, err = process.communicate()
    disk = disk.decode('utf-8').split('\n')

    for i in disk:
        data = i.split()
        mem.append(data)
    # print(mem)
    get = mem[1][2]
    print('used:', get)
    new_used = Used(used=get)
    time = datetime.datetime.now()
    print('time is:',time)
    print('new_used',new_used)
    new_used.save()
    return '{} repeat  in one minutes!'.format(get)