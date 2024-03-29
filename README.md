# RDF Prefix Adder
Came out of issues working with GraphDB and not being able to refer to an imported ontology by its base prefix in SPARQL. This program is short and sweet: it takes an input RDF file **(currently Turtle only)** and adds your desired reference prefix to it. In GraphDB, if this does not exist, you cannot refer to an imported ontology's objects/properties. Most ontologies do not use the best-practice rdfs:isDefinedBy, so this was the simplest workaround.

This function exists in GraphDB manually (Setup -> Namespaces -> Add namespace) but I wanted to mess around in Python for a bit, so here we are.

# Use
* Make sure you have Python installed.
* Save the file [prefadd.py](prefadd.py)
* Open command window in the same folder.
* Type the following:

```
[python / python3] prefadd.py [path/filename.ttl] [desired namespace (e.g., foaf)]
```

File can be anywhere you want. Resultant Turtle file would look like:
```
@prefix : <http://www.w3.org/ns/mls#> .
@prefix mls: <http://www.w3.org/ns/mls#> .
```

Now, in GraphDB, you can use *mls:* to refer to anything in ML-Schema.

# Limitations
* Currently Turtle format only.
