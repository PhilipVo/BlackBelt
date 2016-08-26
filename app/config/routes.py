from system.core.router import routes

routes['default_controller'] = 'Users'
routes['GET']['/main'] = 'Users#index'
routes['GET']['/logout'] = 'Users#logout'
routes['POST']['/login'] = 'Users#login'
routes['POST']['/register'] = 'Users#register'

routes['GET']['/pokes'] = 'Pokes#index'
routes['GET']['/pokes/poke/<int:user_id>/<int:receiver_id>'] = 'Pokes#poke'

