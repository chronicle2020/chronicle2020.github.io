---
layout: default
---

<small><i>最近一次更新：02/19/2020, 有New标示的新闻为最新添加</i></small>

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
                    <div class="news-entry">
                        {% if entry.latest == "1" %}
                            <span class="latest-badge">New</span>
                        {% endif %}
                        <a href="{{ entry.url }}">{{ entry.title }}</a>
                         <code class="language-plaintext highlighter-rouge">{{ entry.source }}</code>
                    </div>
                </li>
                {% endfor %}
            </ul>
        </td>
    </tr>
    {% endfor %}
</tbody>
</table>