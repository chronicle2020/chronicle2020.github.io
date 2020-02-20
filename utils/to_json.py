import csv
import json
import collections

with open('./_data/raw_data.csv', newline='', encoding='utf-8') as csvfile:
    news_by_date = collections.defaultdict(list)
    for row in csv.reader(csvfile, delimiter=','):
        news_by_date[row[0]].append({
            "url":   row[1],
            "title": row[2],
            "source":row[3],
            "latest":row[4],
        })

    res = []
    for date,news in news_by_date.items():
        res.append({"date": date, "news": news})

    with open('./_data/chronicle.json', 'w+', encoding='utf-8') as output:
        json.dump(res, output, sort_keys=True, indent=2, ensure_ascii=False)
