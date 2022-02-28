import rdflib
import os, sys
from rdflib.namespace import Namespace


def rdf2turtle(path, base):
    g = rdflib.Graph()
    new_path = path.split(".")[0]+".ttl"
    g.parse(path, format = "xml")
    g.base = base
    g.serialize(destination=new_path)
    
    
if __name__ == "__main__":

    args = sys.argv
    p = args[1]
    base = args[2]
    print(f"Parsing {p} with base {base}\n\n")
    rdf2turtle(p, base = base)
    print("Done\n")
    
    

