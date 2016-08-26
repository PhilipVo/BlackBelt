from __future__ import print_function
import sys
from system.core.controller import *

class Users(Controller):
	def __init__(self, action):
		super(Users, self).__init__(action)
		self.load_model('User')
		self.db = self._app.db

	########## GET ##########
	def index(self):
		if session.get('id'):
			return redirect('/products')
		return self.load_view('index.html')


	########## POST ##########		
	def register(self):
		output = self.models['User'].register(request.form)
		if output['status'] == True:
			session['id'] = output['user']['id']
			session['first_name'] = output['user']['first_name']			
			return redirect('/products')
		else:
			for message in output['log']:
				flash(message, 'error')
			return redirect('/')

	def login(self):
		output = self.models['User'].login(request.form)
		if output['status'] == True:
			session['id'] = output['user']['id']
			session['first_name'] = output['user']['first_name']
			return redirect('/products')
		else:
			for message in output['log']:
				flash(message, 'error')
			return redirect('/')

	def logout(self):
		session.clear()
		return redirect('/')			