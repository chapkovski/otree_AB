from channels.routing import route
from .consumers import tut_work_connect, tut_work_disconnect, tut_work_message
from otree.channels.routing import channel_routing
from channels.routing import include, route_class

tut_work_path = r'^/(?P<worker_code>\w+)/(?P<player_pk>\w+)$'
tut_answer_path = r'^/(?P<participant_code>\w+)$'

tut_workpage_routing = [route("websocket.connect",
                          tut_work_connect, path=tut_work_path),
                    route("websocket.receive",
                          tut_work_message, path=tut_work_path),
                    route("websocket.disconnect",
                          tut_work_disconnect, path=tut_work_path), ]

channel_routing += [
    include(tut_workpage_routing, path=r"^/tutworkpage"),
]
