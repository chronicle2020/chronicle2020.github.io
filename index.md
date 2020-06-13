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

<div class="container pb-4">
  <div class="row">
    <div class="col">
        只看最新更新 <input id="toggle-latest" type="checkbox" data-toggle="toggle" data-onstyle="outline-primary" data-offstyle="outline-secondary" data-size="small" >
    </div>
    <div class="col old">
        <span class="inline">只看主题</span>
        <div class="btn-group-sm btn-group-toggle old pull-left" data-toggle="buttons" id="theme-checkbox">
            {% for topic in site.data.topics %}
            <label class="btn btn-secondary">
                <input type="checkbox" name="theme-checkbox" autocomplete="off" class="theme-checkbox" value="{{ topic.value }}"> {{ topic.name }}
            </label>
            {% endfor %}
        </div>
    </div>
  </div>
</div>

<table class="table table-sm">
<colgroup>
    <col width="25%" />
    <col width="75%" />
</colgroup>
<thead>
    <tr class="header text-center">
        <th>Date</th>
        <th>News</th>
    </tr>
</thead>
<tbody>
    {% for row in site.data.chronicle %}
    <tr class="{{ row.status }} {{ row.topics | join: " " }}">
        <td style="text-align: center; vertical-align: middle;">{{ row.date }}</td>
        <td>
            <ul class="list-unstyled">
                {% for entry in row.news %}
                <li class="{{ entry.status }} {{ entry.topics | join: " " }}">
                    <div class="news-entry">
                        {% if entry.status == "latest" %}
                            <span class="badge badge-pill badge-danger latest-badge">新</span>
                        {% endif %}
                        {% if entry.url == "" %}
                            <a href="{% link 404.md %}"><del>{{ entry.title }}</del></a>
                        {% else %}
                            <a href="{{ entry.url }}" target="_blank">{{ entry.title }}</a> <span class="badge badge-secondary">{{ entry.source }}</span>
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