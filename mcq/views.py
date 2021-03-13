from django.shortcuts import render, redirect
from .models import *
import random
from django.contrib import messages
from json import dumps
from django.urls import reverse
import uuid
import json
# Create your views here.


def home(request):
    topics = QtsAnsSet.objects.values_list("subject", flat=True).distinct()
    context = {"topics": topics}
    return render(request, "home.html", context)


def topic_selector(request, topic):
    context = {"topic": topic}
    return render(request, "quiz.html", context)


def practice(request, topic):
    name = request.session.get("topic", None)
    if name is not None:
        data = list()
        qts_opts = list(QtsAnsSet.objects.filter(subject=topic))
        try:
            rand_qtsans = random.sample(qts_opts, 10)
            for i in rand_qtsans:
                data.append({
                    "qts": i.question,
                    "opt1": i.opt1,
                    "opt2": i.opt2,
                    "opt3": i.opt3,
                    "opt4": i.opt4,
                    "answer": i.answer,
                })
            json_data = dumps(data)
            context = {"topic": topic, "json_data": json_data}
            del request.session['topic']
            return render(request, "test.html", context)
        except ValueError:
            messages.info(request, "Questions are not available please try giving some another test.")
            return redirect("quizgame:home")
    else:
        return redirect("quizgame:home")


def view_result(request):
    if request.session.get("name", None) is not None:
        name = request.session.get("name")
        context = {"name": name}
        del request.session["name"]
        return render(request, "submit.html", context)
    return redirect("quizgame:home")


def set_session(request, topic):
    if request.method == "POST":
        name = request.POST.get("name")
        request.session["name"] = name
        request.session["topic"] = topic
        request.session.set_expiry(300)
        return redirect(reverse("quizgame:practice-test", kwargs={"topic": topic}))
    return render(request, "name.html")
