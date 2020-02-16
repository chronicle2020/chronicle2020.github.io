---
layout: default
---

<table>
<colgroup>
    <col width="25%" />
    <col width="75%" />
</colgroup>
<thead>
    <tr class="header">
        <th>Date</th>
        <th>News</th>
    </tr>
</thead>
<tbody>
{% for row in site.data.test %}
    <tr>
        <td>{{ row.date }}</td>
        <td>
            <ul>
                {% for entry in row.news %}
                    <li><a href="{{ entry.url }}">{{ entry.title }}</a></li>
                {% endfor %}
            </ul>
        </td>
    </tr>
{% endfor %}
</tbody>
</table>
