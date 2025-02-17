# How to render dynamic data table

To render database records dynamically into an HTML table using Django's ORM and templates, follow these steps:

---

## **✅ Steps**
1. **Query Data in Django View** (`views.py`)
2. **Extract Column Names Dynamically**
3. **Pass Column Names and Data to the Template**
4. **Render Table Using `{% for %}` in Django Template**

---

## **1️⃣ Query Data in Django View (`views.py`)**
Modify your Django **view function** to:
- **Retrieve all objects** from the model.
- **Dynamically extract column names**.
- **Pass the data and column names** to the template.

### **Example: `views.py`**
```python
from django.shortcuts import render
from .models import Language  # Change to your model

def view_languages(request):
    # Fetch all records
    queryset = Language.objects.all()

    # Extract column names dynamically (except ID)
    columns = [field.name for field in Language._meta.fields]

    # Convert queryset to a list of dictionaries
    data = list(queryset.values())

    # Pass column names and data to template
    return render(request, "data_table.html", {"columns": columns, "data": data, "title": "Languages"})
```

### **🔹 Explanation**
✔ **Dynamically extracts column names**: `Language._meta.fields`  
✔ **Converts QuerySet into a list of dictionaries**: `list(queryset.values())`  
✔ **Sends column names and data** to the template  

---

## **2️⃣ Render Dynamic Table in Django Template (`data_table.html`)**
Use Django's `{% for %}` loops to render the table.

### **Example: `data_table.html`**
```html
{% extends "layout.html" %}

{% block content %}
<h2 class="mb-4">{{ title }}</h2>

<!-- Table -->
<table border="1">
    <thead>
        <tr>
            {% for column in columns %}
                <th>{{ column|title }}</th>  <!-- Display column names as headers -->
            {% endfor %}
        </tr>
    </thead>
    <tbody>
        {% for row in data %}
        <tr>
            {% for column in columns %}
                <td>{{ row[column] }}</td>  <!-- Fetch values dynamically -->
            {% endfor %}
        </tr>
        {% endfor %}
    </tbody>
</table>

{% endblock %}
```

### **🔹 Explanation**
✔ **Renders column headers dynamically** using `{% for column in columns %}`.  
✔ **Loops through `data`** to create `<tr>` rows dynamically.  
✔ **Accesses each field dynamically** using `{{ row[column] }}`.  

---

## **3️⃣ Result: Rendered HTML Table**
If your `Language` model has:
```python
[
    {"id": 1, "name": "Python", "popularity": "High"},
    {"id": 2, "name": "JavaScript", "popularity": "Very High"}
]
```
Then the HTML table will render as:

| Id | Name       | Popularity  |
|----|-----------|------------|
| 1  | Python    | High       |
| 2  | JavaScript| Very High  |

---

## **🎯 Summary**
✔ **Django View (`views.py`)** extracts **column names** and **data**.  
✔ **Django Template (`data_table.html`)** dynamically renders the **table** using `{% for %}`.  
✔ **Works for any Django Model** without hardcoding fields.  

Now, your **Django app will display dynamic database records** in an HTML table! 🚀