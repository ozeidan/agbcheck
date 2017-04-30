import json
from elasticsearch import Elasticsearch

es = Elasticsearch(
    ['first-cluster-340082074.eu-west-1.bonsaisearch.net'],
    http_auth=('jan3osgggf', 'tvept1eq65'),
    port=443,
    use_ssl=True,
    verify_certs=False
)
with open('data/passagen.json') as data_file:
    data = json.load(data_file)

for passage in data["kritisch"]:
    res = es.index(index="agbcheck", doc_type='kritisch', body={'passage': passage})

es.indices.refresh(index="agbcheck")

#res = es.search(index="agbcheck", body={"query": {"match_all": {}}})
#print("Got %d Hits:" % res['hits']['total'])
