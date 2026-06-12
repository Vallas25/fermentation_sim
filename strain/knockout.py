import cobra
from cobra.io import read_sbml_model
import os

model = read_sbml_model("strain/yeast-GEM.xml")

print(f"reactions: {len(model.reactions)}")
print(f"metabolites: {len(model.metabolites)}")
print(f"genes: {len(model.genes)}")

ethanol = model.metabolites.get_by_id("s_0680")

print(f"ethanol formula: {ethanol.formula}")
print(f"amount of reactions: {len(ethanol.reactions)}")