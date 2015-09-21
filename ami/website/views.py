from time import sleep
import thread

from django.shortcuts import render, HttpResponse

from website.models import User, AmI

def sched():
    admin = User.objects.get(username="_Frky")
    while AmI.objects.get(owner=admin).seen:
        obj = AmI.objects.get(owner=admin)
        obj.seen = False
        obj.save()
        sleep(10)
    obj = AmI.objects.get(owner=admin)
    obj.am_i = False
    obj.save()


def index(req):
    admin = User.objects.get(username="_Frky")
    obj = AmI.objects.get(owner=admin)
    ctxt = dict()
    tpl = "ami/index.html"
    if req.user == admin:
        obj.am_i = True
        obj.seen = True
        obj.save()
        thread.start_new_thread(sched, ())
    ctxt["ami"] = obj.am_i
    return render(req, tpl, ctxt)


def ping(req):
    admin = User.objects.get(username="_Frky")
    if req.user == User.objects.get(username="_Frky"):
        obj = AmI.objects.get(owner=admin)
        obj.seen = True
        obj.save()
        return HttpResponse("OK")
    return HttpResponse("KO")
