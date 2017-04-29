import sys
from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch(
    ['first-cluster-340082074.eu-west-1.bonsaisearch.net'],
    http_auth=('jan3osgggf', 'tvept1eq65'),
    port=443,
    use_ssl=True,
    verify_certs=False,
)

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}

res = es.index(index="agbcheck", doc_type='agb',  body=doc)
print(res['created'])

res = es.get(index="agbcheck", doc_type='agb', id=1)
print(res['_source'])

es.indices.refresh(index="agbcheck")

res = es.search(index="agbcheck", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])


def main(argv):
    if(len(argv) < 1):
        print("Not enough parameters!")
        return


if (__name__ == "__main__"):
    main(sys.argv[1:])
