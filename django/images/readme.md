```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Product Management

- **Create a Product:**
  - Navigate to the admin panel.
  - Click on "Products" and then "Add Product."
  - Fill in required fields and upload an image.
  - Save the product.

- **View and Edit Products:**
  - The "Products" section lists all products.
  - Click a product to view and edit details.

- **Manage Product Gallery:**
  - While editing a product, manage its gallery.
  - Add or remove images in the "Product Gallery" section.

### Advanced Customization

Use provided forms for customization:

- `ProductForm`: Customize fields for adding/editing products.
- `ProductGalleryForm`: Customize fields for managing the product gallery.

## Admin Panel Thumbnails

Admin panel includes thumbnail previews for product images.
