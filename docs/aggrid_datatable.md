# How to intercept data sent by django view in javascript and render it with AgGrid table

Below is the code

You can see how javascript gets access to ```data``` sent by django view within double curly braces.

```html
{% extends "layout.html" %}

{% block extra_css %}
<!-- ag-Grid CSS -->
<link rel="stylesheet" href="https://unpkg.com/ag-grid-community/styles/ag-grid.css">
<link rel="stylesheet" href="https://unpkg.com/ag-grid-community/styles/ag-theme-material.css">
{% endblock %}

{% block title %}{{title}}{% endblock %}

{% block content %}
<h2 class="mb-4">{{ title }}</h2>
<!-- ag-Grid container -->
<div id="myGrid" class="ag-theme-material" style="height: 700px; width: 100%;"></div>

<!-- ag-Grid JS -->
<script src="https://unpkg.com/ag-grid-community@31.0.1/dist/ag-grid-community.min.js"></script>

<script>

    // Django JSON Data (Rendered from View)
    var rowData = {{ data | safe }};

    console.log(`data is ${JSON.stringify(rowData)}`)


    const columnDefs = Object.keys(rowData[0]).map((columnName)=>({headerName:columnName, field:columnName, filter: "agTextColumnFilter"}))
    // Grid Options
    var gridOptions = {
        columnDefs: columnDefs,
        rowData: rowData,
        pagination: true
    };

    // Initialize ag-Grid
    document.addEventListener('DOMContentLoaded', function () {
        var gridDiv = document.querySelector("#myGrid");
        //new agGrid.Grid(gridDiv, gridOptions);
        const gridApi = agGrid.createGrid(gridDiv, gridOptions);
    });
</script>

{% endblock %}
```
