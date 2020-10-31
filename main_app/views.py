from django.shortcuts import render, redirect
from django.http import JsonResponse
import random
from time import gmtime, strftime


def index(request):
    if request.session['total_gold']:
        print('TOTAL GOLD:', request.session['total_gold'])
    else:
        request.session['total_gold'] = 0
        request.session['activities'] = []
        print('TOTAL GOLD:', request.session['total_gold'])
        print('ACTIVITIES:', request.session['activities'])
    return render(request, "index.html")


def gold_api(request):
    return JsonResponse({"activities": request.session['activities']})


def process_money(request):
    print('proc money')
    print(request.POST['which_form'])
    time = strftime("%Y-%m-%d %H:%M %p", gmtime())
    if request.POST['which_form'] == 'farm':
        gold_from_farm = random.randint(10, 20)
        request.session['activities'].append(
            f"<div class='text-success'>Earned {gold_from_farm} gold from the farm! {time}</div>"
        )
        request.session['total_gold'] += gold_from_farm
    elif request.POST['which_form'] == 'cave':
        gold_from_cave = random.randint(5, 10)
        request.session['activities'].append(
            f"<div class='text-success'>Earned {gold_from_cave} gold from the cave! {time}</div>"
        )
        request.session['total_gold'] += gold_from_cave
    elif request.POST['which_form'] == 'house':
        gold_from_house = random.randint(2, 5)
        request.session['activities'].append(
            f"<div class='text-success'>Earned {gold_from_house} gold from the house! {time}</div>"
        )
        request.session['total_gold'] += gold_from_house
    else:
        gold_from_casino = random.randint(-50, 50)
        if gold_from_casino > -1:
            request.session['activities'].append(
                f"<div class='text-success'>Entered a casino and made {gold_from_casino} gold! {time}</div>"
            )
            request.session['total_gold'] += gold_from_casino

        else:
            gold_from_casino *= -1
            request.session['activities'].append(
                f"<div class='text-danger'>Entered a casino and lost {gold_from_casino} gold... Ouch! {time}</div>"
            )
            request.session['total_gold'] -= gold_from_casino
    return redirect("/")


def reset(request):
    request.session['total_gold'] = 0
    return redirect('/')
