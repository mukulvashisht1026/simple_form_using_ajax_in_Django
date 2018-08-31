#routing.py

from django.conf.urls import url
from django.urls import path,include
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator,AllowedHostsOriginValidator
from table.consumer import table_consumer
from django.urls import path,include
application = ProtocolTypeRouter({
	'websocket':AllowedHostsOriginValidator(
			AuthMiddlewareStack(
				URLRouter(
					[
						path('table/data/' ,table_consumer,name='enter'),
    					path('table/', table_consumer,name='table'),
					]
					)
				)

		)	

	})


''''
	'''