from whoosh.qparser import QueryParser
from whoosh import scoring
from whoosh.index import open_dir
import sys
import json

ix = open_dir("indexdir")

def query(query_str, topN=10):
    with ix.searcher(weighting=scoring.Frequency) as searcher:
        query = QueryParser("description", ix.schema).parse(query_str)
        results = searcher.search(query, limit=topN)
        query_results = []

        for i in range(min(len(results), topN):
            d={}
            d['url'] = "https://www.youtube.com/watch?v=%s" % results[i]['id']
            d['title'] = results[i]['title']
            d['description'] = results[i].highlights('description')
            d['score'] = results[i].score
            query_results.append(d)

        return query_results

if __name__ == "__main__":
    query_str = sys.argv[1]
    topN = int(sys.argv[2])
    query_results = query(query_str, topN)
    print(json.dumps(query_results))