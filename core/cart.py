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
                if 'quantity' not in self.cart[product_id]:
                    self.cart[product_id]['quantity'] = 1  # Asumimos una cantidad predeterminada de 1 si falta
                cart_products[product_id] = {
                    'product': product,
                    'quantity': self.cart[product_id]['quantity'],
                    'precio': self.cart[product_id]['precio']
                }
        return cart_products