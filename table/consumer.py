import asyncio
import json
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from .models import tableModel
class table_consumer(AsyncConsumer):
	async def websocket_connect(self,event):
		print("connected successfully",event)
		chat_room = "only_channel"
		self.chat_room = chat_room
		await self.channel_layer.group_add(
			chat_room,
			self.channel_name
			)	
		await self.send({
			"type":"websocket.accept"
			})

	async def websocket_receive (self,event):
		print("recieve something",event)
		unloaded_text = event.get('text',None)
		if unloaded_text is not None:
			loaded_dict = json.loads(unloaded_text)
			print("name is ",loaded_dict.get('name'))
			myResponse = {
			'name':loaded_dict.get('name'),
			'address':loaded_dict.get('address'),
			'dob':loaded_dict.get('dob')
			}
			await self.addrow(loaded_dict.get('name'),loaded_dict.get('address'),loaded_dict.get('dob'))
			await self.channel_layer.group_send(
				self.chat_room,
				{
				"type":"row_added",
				"text":json.dumps(myResponse)
				}
			)

	async def row_added(self,event):
		# this sends the actual message
		await self.send({
			"type": "websocket.send",
			"text": event['text']
			})


	async def websocket_disconnect(self,event):
		print ("diconnect successfully",event)


	@database_sync_to_async
	def addrow(self,name,address,dob):
		return   tableModel.objects.create(name=name,address=address,DOB=dob)





	'''	name = event.get('name',None)
		address = event.get('address',None)
		dob = event.get('dob',None)
'''