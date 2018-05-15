from .models import Player, Constants
import json
from random import randint
import time


def slicelist(l,n):
    return [l[i:i + n] for i in range(0,len(l),n)]


def get_random_list():
    random_upper_boundary = randint(50, 99)
    max_len=100
    return [randint(10, random_upper_boundary) for i in range(max_len)]


def get_task():
    string_len = 10
    listx = get_random_list()
    listy = get_random_list()
    answer = max(listx) + max(listy)
    listx = slicelist(listx, string_len)
    listy = slicelist(listy, string_len)
    return {
        "mat1": listx,
        "mat2": listy,
        "correct_answer": answer,
    }


def tut_work_connect(message, worker_code, player_pk):
    print('worker connected')
    new_task = get_task()
    player = Player.objects.get(participant__code__exact=worker_code, pk=player_pk)
    player.last_correct_answer = new_task['correct_answer']
    player.save()
    message.reply_channel.send({'text': json.dumps(new_task)})


def tut_work_disconnect(message, worker_code, player_pk):
    print('worker disconnected')


def tut_work_message(message, worker_code, player_pk):
    print('TASK: ', get_task())
    jsonmessage = json.loads(message.content['text'])
    answer = jsonmessage.get('answer')
    player = Player.objects.get(participant__code__exact=worker_code, pk=player_pk)
    player.tasks_attempted += 1
    if int(answer) == int(player.last_correct_answer):
        player.tasks_correct += 1
        feedback = "Предыдущий ответ был верен."
    else:
        feedback = "Предыдущий ответ " + str(answer) + " был не верен, верный ответ " + str(player.last_correct_answer) + "."
    new_task = get_task()
    new_task['tasks_correct'] = player.tasks_correct
    new_task['tasks_attempted'] = player.tasks_attempted
    new_task['feedback'] = feedback
    player.last_correct_answer = new_task['correct_answer']
    player.save()
    time.sleep(0.01)
    if int(new_task['tasks_attempted']) < Constants.max_task_amount:
        message.reply_channel.send({'text': json.dumps(new_task)})
    if int(new_task['tasks_attempted']) >= Constants.max_task_amount:
        new_task['task_over'] = True
        message.reply_channel.send({'text': json.dumps(new_task)})
