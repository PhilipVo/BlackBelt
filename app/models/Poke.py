from __future__ import print_function
from system.core.model import Model
import sys

class Poke(Model):
	def __init__(self):
		super(Poke, self).__init__()


	def poke(self, user_id, receiver_id):
		query = """INSERT INTO pokes (user_id, receiver_id, created_at, updated_at)
							VALUES (:user_id, :receiver_id, NOW(), NOW())
						"""
		data =	{	'user_id': user_id,
							'receiver_id': receiver_id
						}
		self.db.query_db(query, data)	

	def get_pokes(self, receiver_id):
		query = """SELECT *, COUNT(pokes.user_id) AS poke_count FROM pokes
							LEFT JOIN users ON pokes.user_id = users.id 
							WHERE receiver_id = :receiver_id
							GROUP BY pokes.user_id
							ORDER BY poke_count DESC
						"""
		data = {'receiver_id': receiver_id}
		return self.db.query_db(query, data)

	def get_all_pokes(self):
		query = """SELECT *, count(receiver_id) AS poke_count
							FROM pokes GROUP BY receiver_id"""
		return self.db.query_db(query)

