from SPARQLWrapper import SPARQLWrapper, JSON
from Levenshtein import ratio

sparql = SPARQLWrapper("http://ops.few.vu.nl:8890/world")
sparql.setQuery("""
PREFIX dc: <http://purl.org/dc/elements/1.1/>

SELECT ?title ?s
FROM <http://ilp.data2semantics.org>
WHERE {?s dc:title ?title}
""")

sparql.setReturnFormat(JSON)
resultsILP = sparql.query().convert()

sparql = SPARQLWrapper("http://ops.few.vu.nl:8890/world")
sparql.setQuery("""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX vocab: <http://stcn.data2semantics.org/vocab/resource/>

SELECT ?publicationn ?publication
FROM <http://stcn.data2semantics.org> 
WHERE {?publication rdf:type vocab:Publicatie ;
                    rdfs:label ?publicationn . }
""")

sparql.setReturnFormat(JSON)
resultsSTCN = sparql.query().convert()


for x in resultsILP["results"]["bindings"]:
    for y in resultsSTCN["results"]["bindings"]:
        r = ratio(x["title"]["value"].encode('utf8'), 
                  y["publicationn"]["value"].encode('utf8'))
        if r > 0.9:
            sparql.setQuery("""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX vocab: <http://stcn.data2semantics.org/vocab/resource/>

SELECT ?words
FROM <http://stcn.data2semantics.org> 
WHERE {<""" + y["publication"]["value"] + """> vocab:publications_kmc3260 ?words . }
""")
            sparql.setReturnFormat(JSON)
            resultsILPPublication = sparql.query().convert()
            for z in resultsILPPublication["results"]["bindings"]:
                print x["s"]["value"], ",", y["publication"]["value"], ",", "Match with ratio", r, ",", z["words"]["value"]
