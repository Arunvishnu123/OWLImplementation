
from owlready2 import *

try:
    onto = get_ontology(
        r"C:\Users\ArunRAVEENDRANNAIRSH\Desktop\New folder (29)\dl.owl").load()

    # Initialize the reasoner
    with onto:
        sync_reasoner_pellet()

    # Check consistency
    if not onto.reasoning_owlready:
        print("The ontology is consistent.")
    else:
        print("The ontology is inconsistent.")
except:
    pass