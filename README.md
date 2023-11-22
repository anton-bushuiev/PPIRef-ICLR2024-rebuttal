# PPIRef

Clustered dataset of protein--protein interactions

# Installation

To install the necessary environment run
```
. scripts/installation/install.sh
```
The `ppiref.surface.DR_SASA` is a wrapper of the [`dr_sasa` software](https://github.com/nioroso-x3/dr_sasa_n). In order to use it for the buried surface calcualtions build the C++ source code according to the [original doctumentation](https://github.com/nioroso-x3/dr_sasa_n#compiling). The resulting executable should match the `ppiref.defitions.DR_SASA_PATH`. By default it expects building `dr_sasa` in the `PPIRef/external` directory.

# TODO

- [ ] Remove `dill` from dependecies (need only for test)
- [x] Add prefix note to extracted PPI PDB files (e.g. `REMARK 000 SASA SOLVER`). Necessary to  modify `to_pdb` in biopandas.
- [ ] Make relative paths possible
- [ ] Add RASA values to classify residules according to (Levy 2010)
- [ ] Docstrings
