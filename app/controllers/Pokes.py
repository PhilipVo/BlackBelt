from system.core.controller import *

class Pokes(Controller):
	def __init__(self, action):
		super(Pokes, self).__init__(action)
		self.load_model('Poke')
		self.load_model('User')
		self.db = self._app.db

	############### GET ###################
	def index(self):
		if session.get('id'):
			pokes=self.models['Poke'].get_pokes(session['id'])			
			users=self.models['User'].get_users(session['id'])			
			return self.load_view('pokes.html', pokes=pokes, users=users)
		return redirect('/main')		

	def poke(self, user_id, receiver_id):
		self.models['Poke'].poke(user_id, receiver_id)
		return redirect('/pokes')
