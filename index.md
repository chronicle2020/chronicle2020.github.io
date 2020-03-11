---
layout: home
---

<p class="update-info">
<small>
<i>
{{ site.data.stats.today_date }} 更新：添加{{ site.data.stats.latest_count }}条，共收录{{ site.data.stats.total_count }}条，跨度{{ site.data.stats.days_covered }}天，有标示的条目为最新添加。另，被划掉的条目表示出现过但后来被全网删除。
</i>
</small>
</p>

<table class="table table-sm">
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
            <ul class="list-unstyled">
                {% for entry in row.news %}
                <li>
                    <div class="news-entry">
                        {% if entry.latest == "1" %}
                            <span class="latest-badge">新</span>
                        {% endif %}
                        {% if entry.url == "" %}
                            <a href="{% link 404.md %}"><strike>{{ entry.title }}</strike></a>
                        {% else %}
                            <a href="{{ entry.url }}">{{ entry.title }}</a> <code class="language-plaintext highlighter-rouge">{{ entry.source }}</code>
                        {% endif %}
                    </div>
                </li>
                {% endfor %}
            </ul>
        </td>
    </tr>
    {% endfor %}
</tbody>
</table>