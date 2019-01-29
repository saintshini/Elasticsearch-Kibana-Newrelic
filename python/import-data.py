from elasticsearch import helpers, Elasticsearch
import csv

from elasticsearch.helpers import bulk

es = Elasticsearch([{'host': '18.221.211.75', 'port': 9200}])

with open("Elasticsearch-Kibana-Newrelic/python/convertcsv.csv") as f:
    reader = csv.DictReader(f, delimiter=',')
    helpers.bulk(es, reader, index="people", doc_type='text')

