from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

@app.route('/')
def order():
    return render_template('order.html')

@app.route('/submit', methods=['POST'])
def submit_order():
    name = request.form['name']
    cake_type = request.form['cake_type']
    quantity = int(request.form['quantity'])

    # Initialize the cart if it doesn't exist
    if 'cart' not in session:
        session['cart'] = []

    # Add the order to the cart
    session['cart'].append({'name': name, 'cake_type': cake_type, 'quantity': quantity})
    session.modified = True  # Mark session as modified

    return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    return render_template('cart.html', cart_items=cart_items)
@app.route('/home')
def home():
    # Pass a list of featured cakes with multiple images to the template
    featured_cakes = [
        {
            'name': 'Chocolate Cake',
            'images': ['images/chocolate cake.jpg']
        },
        {
            'name': 'Vanilla Cake',
            'images': ['images/vanilla.jpg']
        },
        {
            'name': 'Red Velvet Cake',
            'images': ['images/REd valvet cake.jpg']
        },
        {
            'name': 'Carrot Cake',
            'images': ['images/carrot cake.jpg']
        },
        {
            'name': 'Black Forest',
            'images': ['images/black.jfif']
        },
        {
            'name': 'Marble Cake',
            'images': ['images/car.jfif']
        },
    ]
    return render_template('home.html', featured_cakes=featured_cakes)

@app.route('/checkout')
def checkout():
    # Here you would handle the checkout process
    return render_template('thank_you.html', cart_items=session.get('cart', []))

if __name__ == '__main__':
    app.run(debug=True)
