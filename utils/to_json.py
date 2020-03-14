import csv
import json
import collections
from datetime import datetime

dt_format = '%m/%d/%Y'

with open('./_data/raw_data.csv', newline='', encoding='utf-8') as csvfile:
    news_by_date = collections.defaultdict(list)
    news_by_date_status = collections.defaultdict(bool)
    news_ct = 0
    latest_ct = 0
    start_dt = None
    end_dt = None
    for row in csv.reader(csvfile, delimiter=','):
        news_by_date[row[0]].append({
            "url":   row[1],
            "title": row[2],
            "source":row[3],
            "status":"latest" if row[4] == "1" else "old",
        })
        news_ct += 1
        latest_ct += row[4] == "1"
        if not end_dt: end_dt = datetime.strptime(row[0], '%m/%d/%Y')
        start_dt = datetime.strptime(row[0], dt_format)
        if row[4] == "1": news_by_date_status[row[0]] = True

    res = []
    for date,news in news_by_date.items():
        res.append({"date": date, "news": news, "status": "latest" if news_by_date_status[date] else "old"})

    with open('./_data/chronicle.json', 'w+', encoding='utf-8') as output:
        json.dump(res, output, sort_keys=True, indent=2, ensure_ascii=False)

    with open('./_data/stats.yml', 'w+', encoding='utf-8') as stats_output:
        stats_output.write("total_count: {}\n".format(news_ct))
        stats_output.write("latest_count: {}\n".format(latest_ct))
        stats_output.write("days_covered: {}\n".format((end_dt - start_dt).days))
        stats_output.write("today_date: {}\n".format(datetime.today().strftime(dt_format)))
