# Reusable template that renders data as table and plots horizontal bar chart

I would like to emphasize ```women_event/tempaltes/stats/count_stats_templates.html```, because it demonstrates the power of reusable code.

This template is used by multiple views that send data into it, and template renders data in a table and plots horizontal bar chart.

This templates accepts a dictionary that maps string to integer values and renders that data as ```table``` and plots that data as ```horizontal bar chart```

Below is how it renders the table. You can see it renders a table that consists of two columns.
First column name is received from the view under variable column_name.
It iterates over dictionary and renders key, value pairs.
Pay attention how the code doesn't call ```items()``` method with paranthesis. I was surprised that django template is able to retrieve key, values without using paranthesis.


```html
<table class="table table-hover orderByDateTable">
    <thead>
        <tr>
            <th scope="col">{{ column_name }}</th>
            <th scope="col">Count</th>
        </tr>
    </thead>
    <tbody>
    {% for key, value in stats_data.items %}
    <tr>
        <td>{{ key }}</td>
        <td>{{ value }}</td>
    </tr>
    {% endfor %}
    </tbody>
</table>
```


# Horizontal Bar Chart

Below is how it plots horizontal bar chart


```html
<script src="https://d3js.org/d3.v7.min.js"></script>

<script>
    // ✅ Capture JSON Data Safely for D3.js
    var rawData = JSON.parse('{{ stats_data_json|escapejs }}');

    // ✅ Convert Object to Array for D3.js
    var data = Object.entries(rawData).map(([name, count]) => ({ name, count }));

    console.log("Converted Data for D3:", data);

    // Set dimensions
    var width = 800, height = 500;
    var margin = { top: 20, right: 30, bottom: 50, left: 400 };

    var svg = d3.select("svg")
        .attr("width", width)
        .attr("height", height);

    var x = d3.scaleLinear()
        .domain([0, d3.max(data, d => d.count)])
        .range([0, width - margin.right - margin.left]);

    var y = d3.scaleBand()
        .domain(data.map(d => d.name))
        .range([margin.top, height - margin.bottom])
        .padding(0.1);

    var bars = svg.append("g")
        .attr("transform", `translate(${margin.left},0)`);

    bars.selectAll("rect")
        .data(data)
        .enter().append("rect")
        .attr("x", 0)
        .attr("y", d => y(d.name))
        .attr("width", d => x(d.count))
        .attr("height", y.bandwidth())
        .attr("fill", "steelblue");

    bars.selectAll("text")
        .data(data)
        .enter().append("text")
        .attr("x", d => x(d.count) + 10)
        .attr("y", d => y(d.name) + y.bandwidth() / 2)
        .attr("dy", "0.35em")
        .text(d => d.count)
        .style("fill", "black")
        .style("font-size", "18px")
        .style("font-family", "Arial, sans-serif");

    svg.append("g")
        .attr("transform", `translate(${margin.left},0)`)
        .call(d3.axisLeft(y))
        .selectAll("text")
        .style("font-size", "16px")
        .style("font-family", "Arial, sans-serif");

    svg.append("g")
        .attr("transform", `translate(${margin.left},${height - margin.bottom})`)
        .call(d3.axisBottom(x))
        .selectAll("text")
        .style("font-size", "16px")
        .style("font-family", "Arial, sans-serif");

</script>
```