# What does {% load static %} do in django

### **What Does `{% load static %}` Do in Django Templates?**
The `{% load static %}` template tag **loads Django's static files system**, allowing you to use `{% static %}` to reference **CSS, JavaScript, images, and other static assets**.

---

### **1️⃣ Why Use `{% load static %}`?**
- It **enables** the `{% static %}` tag, which **generates URLs** for static files.
- It helps **Django manage static files properly**, especially in **production**.
- It ensures **static files work with different configurations (e.g., AWS S3, CDN, or `STATICFILES_STORAGE`)**.

---

### **2️⃣ Example Usage**
#### ✅ **Loading Static Files in `base.html`**
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Django Site</title>

    <!-- Load CSS -->
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>
<body>

    <h1>Welcome to My Django Site</h1>

    <!-- Load Image -->
    <img src="{% static 'images/logo.png' %}" alt="Site Logo">

    <!-- Load JavaScript -->
    <script src="{% static 'js/main.js' %}"></script>

</body>
</html>
```
🔹 **Without `{% load static %}`**, `{% static 'css/styles.css' %}` will **not work**.

---

### **3️⃣ Where to Place Static Files?**
Django **expects static files** inside the `static/` directory.

📂 **Project Structure**
```
myproject/
│── myapp/
│   ├── static/
│   │   ├── css/
│   │   │   ├── styles.css
│   │   ├── images/
│   │   │   ├── logo.png
│   │   ├── js/
│   │   │   ├── main.js
│   ├── templates/
│   │   ├── base.html
```

---

### **4️⃣ Configuring Static Files in `settings.py`**
Ensure **`STATIC_URL` and `STATICFILES_DIRS`** are set:

```python
import os

STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]  # For additional static files
```

---

### **5️⃣ Collect Static Files (For Production)**
In production, Django requires **collecting all static files** into `STATIC_ROOT`:

```sh
python manage.py collectstatic
```
This collects **all static files** into `STATIC_ROOT` (e.g., `staticfiles/`).

---

### **🚀 Summary**
✔ `{% load static %}` **enables** `{% static %}` for referencing static files.  
✔ `{% static 'path/to/file' %}` generates the **correct URL** for static assets.  
✔ Static files should be placed in a `static/` directory inside apps.  
✔ Use `collectstatic` in **production** to serve static files efficiently.  

Now you can correctly manage static assets in Django! 🚀