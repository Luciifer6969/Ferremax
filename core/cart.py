from .models import Producto

class Cart():
    def __init__(self,request):
        self.session = request.session 

        cart= self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart
            
    def add(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id]= {'precio': str(product.precio)}    

        self.session.modified = True


    def __len__(self):
        return len(self.cart)    

    def get_prods(self):
        product_ids = self.cart.keys()
        products = Producto.objects.filter(id__in=product_ids)

        return products
    
    def get_prodss(self):
        product_ids = self.cart.keys()
        products = Producto.objects.filter(id__in=product_ids)
        cart_products = {}
        for product in products:
            product_id = str(product.id)
            if product_id in self.cart:
                cart_products[product_id] = {
                    'product': product,
                    'quantity': self.cart[product_id],
                    'precio': product.precio
                }
        return cart_products
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        outcart = self.cart
        outcart[product_id] = product_qty

        self.session.modified = True    

        update = self.cart
        return update        