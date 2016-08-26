from __future__ import print_function
from system.core.model import Model
import sys

class Product(Model):
	def __init__(self):
		super(Product, self).__init__()

	def get_product(self, id):
		data = {'id': id}
		query = "SELECT * from products WHERE id = :id"
		return self.db.query_db(query, data)[0]

	def get_products(self):
		query = "SELECT * from products"
		return self.db.query_db(query)

	def create_product(self, data):
		log = []

		# Check for valid price:
		try:
			float(data['price'])
			if len((data['price']).rsplit('.')[-1]) != 2:
				int(data['price'])
		except:
			log.append('Error: please enter a valid price.')
			return {'status': False, 'log': log}

		# Check for unique product name:
		query = "SELECT name FROM products WHERE name = :name LIMIT 1"
		if len(self.db.query_db(query, data)) > 0:
			log.append('Error: {} already exists.'.format(data['name']))
			return {'status': False, 'log': log}

		# Insert valid entry:
		query = """INSERT INTO products (name, description, price, user_id, created_at, updated_at)
					VALUES (:name, :description, :price, 7, NOW(), NOW())
				"""
		self.db.query_db(query, data)	
		log.append("{} added to database.".format(data['name']))					
		return {'status': True, 'log': log}

	def update_product(self, id, dat):
		log = []
		data = {'id': id}

		for key, value in dat.iteritems():
			data[key] = value

		# Check for valid price:
		try:
			float(data['price'])
			if len((data['price']).rsplit('.')[-1]) != 2:
				int(data['price'])
		except:
			log.append('Error: please enter a valid price.')
			return {'status': False, 'log': log}

		# Check for unique product name:
		new = "SELECT name FROM products where name = :name LIMIT 1"
		cur = "SELECT name FROM products WHERE id = :id LIMIT 1"
		new_product = self.db.query_db(new, data)
		cur_product = self.db.query_db(cur, data)					

		if not (len(new_product) == 0 or new_product == cur_product):
			log.append('Error: {} already exists.'.format(data['name']))
			return {'status': False, 'log': log}

		# Update with valid information:
		query = """UPDATE products set name = :name, description = :description,
					price = :price, updated_at = NOW() WHERE id = :id
				"""
		self.db.query_db(query, data)	
		log.append("{} updated.".format(data['name']))					
		return {'status': True, 'log': log}			

	def destroy_product(self, id):
		data = {'id': id}
		query = "DELETE FROM products WHERE id = :id"
		return self.db.query_db(query, data)