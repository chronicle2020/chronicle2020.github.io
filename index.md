---
layout: default
---

<p class="update-info">
<small>
<i>
{{ site.data.stats.today_date }} 更新：添加{{ site.data.stats.latest_count }}条，共收录{{ site.data.stats.total_count }}条，跨度{{ site.data.stats.days_covered }}天，有标示的条目为最新添加。另，由于最近病毒全球蔓延，近期会加入全球新闻，stay tuned
</i>
</small>
</p>

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
                            <span class="latest-badge">新</span>
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