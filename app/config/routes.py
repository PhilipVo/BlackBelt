from system.core.router import routes

routes['default_controller'] = 'Users'
routes['GET']['/users/<int:user_id>'] = 'Users#view'
routes['GET']['/logout'] = 'Users#logout'
routes['POST']['/login'] = 'Users#login'
routes['POST']['/register'] = 'Users#register'

routes['GET']['/products'] = 'Products#index'
routes['GET']['/products/new'] = 'Products#new'
routes['GET']['/products/edit/<int:id>'] = 'Products#edit'
routes['GET']['/products/show/<int:id>'] = 'Products#show'
routes['POST']['/products/create'] = 'Products#create'
routes['POST']['/products/update/<int:id>'] = 'Products#update'
routes['POST']['/products/destroy/<int:id>'] = 'Products#destroy'

