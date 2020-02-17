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
        <th>Date</th><th>News</th>
    </tr>
</thead>
<tbody>
    {% for row in site.data.chronicle %}
    <tr>
        <td>{{ row.date }}</td>
        <td>
            <ul>
                {% for entry in row.news %}
                <li>
                    <a href="{{ entry.url }}">{{ entry.title }}</a> <code class="language-plaintext highlighter-rouge">{{ entry.source }}</code>
                </li>
                {% endfor %}
            </ul>
        </td>
    </tr>
    {% endfor %}
</tbody>
</table>