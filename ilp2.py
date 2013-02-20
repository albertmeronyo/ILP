from SPARQLWrapper import SPARQLWrapper, JSON
from Levenshtein import ratio

publications =  ['http://stcn.data2semantics.org/publicatie/306144050', 'http://stcn.data2semantics.org/publicatie/183961625', 'http://stcn.data2semantics.org/publicatie/202855368', 'http://stcn.data2semantics.org/publicatie/191622958', 'http://stcn.data2semantics.org/publicatie/038097451', 'http://stcn.data2semantics.org/publicatie/193254654', 'http://stcn.data2semantics.org/publicatie/33867053X', 'http://stcn.data2semantics.org/publicatie/095183698', 'http://stcn.data2semantics.org/publicatie/112421431', 'http://stcn.data2semantics.org/publicatie/11246369X', 'http://stcn.data2semantics.org/publicatie/203183827', 'http://stcn.data2semantics.org/publicatie/203184114', 'http://stcn.data2semantics.org/publicatie/203184556', 'http://stcn.data2semantics.org/publicatie/301117845', 'http://stcn.data2semantics.org/publicatie/329576941', 'http://stcn.data2semantics.org/publicatie/333564073', 'http://stcn.data2semantics.org/publicatie/333564812', 'http://stcn.data2semantics.org/publicatie/305645552', 'http://stcn.data2semantics.org/publicatie/263458504', 'http://stcn.data2semantics.org/publicatie/263458806', 'http://stcn.data2semantics.org/publicatie/26345939X', 'http://stcn.data2semantics.org/publicatie/263466833', 'http://stcn.data2semantics.org/publicatie/264413083', 'http://stcn.data2semantics.org/publicatie/264413210', 'http://stcn.data2semantics.org/publicatie/264414500', 'http://stcn.data2semantics.org/publicatie/264415205', 'http://stcn.data2semantics.org/publicatie/264418247', 'http://stcn.data2semantics.org/publicatie/264449967', 'http://stcn.data2semantics.org/publicatie/26445071X', 'http://stcn.data2semantics.org/publicatie/265020751', 'http://stcn.data2semantics.org/publicatie/265020824', 'http://stcn.data2semantics.org/publicatie/265022088', 'http://stcn.data2semantics.org/publicatie/265022339', 'http://stcn.data2semantics.org/publicatie/306311313', 'http://stcn.data2semantics.org/publicatie/309260744', 'http://stcn.data2semantics.org/publicatie/243016034', 'http://stcn.data2semantics.org/publicatie/297771299', 'http://stcn.data2semantics.org/publicatie/18298740X', 'http://stcn.data2semantics.org/publicatie/851637884', 'http://stcn.data2semantics.org/publicatie/305751174', 'http://stcn.data2semantics.org/publicatie/310388015', 'http://stcn.data2semantics.org/publicatie/314937552', 'http://stcn.data2semantics.org/publicatie/337730784', 'http://stcn.data2semantics.org/publicatie/268595712', 'http://stcn.data2semantics.org/publicatie/332746291', 'http://stcn.data2semantics.org/publicatie/038097451', 'http://stcn.data2semantics.org/publicatie/093387571', 'http://stcn.data2semantics.org/publicatie/117207691', 'http://stcn.data2semantics.org/publicatie/095184244', 'http://stcn.data2semantics.org/publicatie/112463487', 'http://stcn.data2semantics.org/publicatie/229668690', 'http://stcn.data2semantics.org/publicatie/328551090', 'http://stcn.data2semantics.org/publicatie/333564561', 'http://stcn.data2semantics.org/publicatie/85065789X']

for publication in publications:
    sparql = SPARQLWrapper("http://ops.few.vu.nl:8890/world")
    sparql.setQuery("""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX vocab: <http://stcn.data2semantics.org/vocab/resource/>

SELECT ?publicationn
FROM <http://stcn.data2semantics.org> 
WHERE {<""" + publication + """> rdfs:label ?publicationn . }
""")

    sparql.setReturnFormat(JSON)
    resultsILP = sparql.query().convert()
    for x in resultsILP["results"]["bindings"]:
        print publication, ",", x["publicationn"]["value"]
