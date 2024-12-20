from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from random import sample

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Veritabanı modeli
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # İlan No
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    city = db.Column(db.String(100), nullable=False)  # Şehir
    category = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(200), nullable=True)

# Ana sayfa rotası
@app.route("/")
def home():
    # Kategorilere göre ürünleri gruplandır ve her kategoriden 10 ürün al
    all_categories = {
        "ATV": Product.query.filter_by(category="ATV").all(),
        "Motosiklet": Product.query.filter_by(category="Motosiklet").all(),
        "SUV": Product.query.filter_by(category="SUV").all(),
        "Karavan": Product.query.filter_by(category="Karavan").all(),
        "Sedan": Product.query.filter_by(category="Sedan").all()
    }

    # Vitrine her kategoriden rastgele 2 ürün seç
    featured_products = []
    for category_products in all_categories.values():
        if len(category_products) > 2:
            featured_products.extend(sample(category_products, 2))  # Rastgele 2 ürün
        else:
            featured_products.extend(category_products)

    # Ana sayfa için kategori başlıklarında ürün sayısını göster
    category_counts = {category: len(products) for category, products in all_categories.items()}

    return render_template(
        "home.html", categories=all_categories, category_counts=category_counts, products=featured_products
    )

# Kategori detay rotası
@app.route("/category/<string:category_name>")
def category_detail(category_name):
    # Seçilen kategoriye ait tüm ürünleri getir
    products = Product.query.filter_by(category=category_name).limit(10).all()
    return render_template("category.html", category_name=category_name, products=products)

# Ürün detay sayfası rotası
@app.route("/product/<int:product_id>")
def product_detail(product_id):
    # Ürün detaylarını getir
    product = Product.query.get_or_404(product_id)
    return render_template("product_detail.html", product=product)

# Canlı arama rotası
@app.route("/search-live", methods=["GET"])
def search_live():
    query = request.args.get('q', '').strip().lower()  # Arama sorgusunu al ve temizle

    if not query:  # Arama sorgusu boşsa, hiçbir sonuç döndür
        return jsonify([])

    # Ürünleri filtrele
    products = Product.query.filter(
        Product.name.ilike(f"%{query}%") |  # Ürün ismi
        Product.description.ilike(f"%{query}%") |  # Açıklama
        Product.city.ilike(f"%{query}%") |  # Şehir
        Product.category.ilike(f"%{query}%") |  # Kategori
        Product.id.cast(db.String).ilike(f"%{query}%") |  # İlan numarası
        Product.price.cast(db.String).ilike(f"%{query}%")  # Fiyat
    ).all()

    # JSON sonuç döndür
    results = [
        {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "city": product.city,
            "category": product.category,
            "description": product.description,
            "image_url": product.image_url
        }
        for product in products
    ]
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
