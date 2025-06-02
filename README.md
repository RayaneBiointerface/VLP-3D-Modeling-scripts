# VLP-3D-Modeling-scripts

PyMOL scripts for reconstructing designed virus-like particles (VLPs) from known parent capsid structures.

---

## Overview

This repository contains Python scripts that run inside PyMOL to align and reconstruct homomeric and heteromeric VLP assemblies based on a known reference capsid structure.  
The scripts automate structural alignment of monomeric subunits to the capsid chains, enabling 3D visualization and modeling of designed VLP variants.

- `chain_align(ref_obj, monomer)` aligns a single monomer to all chains of the reference object (for homomeric particles).  
- `chain_align(ref_obj, monomer1, monomer2)` aligns two different monomers to specific chains (for heteromeric particles based on AP205 capsid).  

---

## Requirements

- PyMOL (version 3.0 or later, (https://pymol.org/)— Tested on the latest version (V3.1)
- Python environment supporting PyMOL scripting  

---

## Usage

### 1. Homomeric particle reconstruction

In PyMOL, load your reference capsid structure and monomer model, then run the script on the Pymol command line:

      run path/to/script_file_name.py

Call the function:

      chain_align('your_reference_capsid', 'monomer_model')

After execution, a multi-state object will be created, representing the reconstructed VLP.
Using states instead of chains provides easier control over coloring individual residues across the full capsid.

This script can be used to reconstruct any newly designed VLP that is based on a known parent capsid structure (e.g., available in the PDB).

### 2. Heteromomeric AP205-based particle reconstruction
⚠️ This script currently supports only AP205-based heteromeric VLPs. To adapt it for other VLPs, you must manually modify the list of chain IDs inside the script.
 
In PyMOL, load your reference capsid structure and the two monomer models. Then run the script from the PyMOL command line:

run path/to/script_file_name.py

Call the function: 

chain_align('your_reference_capsid', 'monomer1_model', 'monomer2_model')

After execution, two multi-state objects will be created, representing the two monomer types and their positions within the VLP.
As with the homomeric case, using states enables easy coloring and manipulation of the full particle.
If you want both monomers in a single object, you can split states then merge them in a new object using PyMOL scripting.

## License

This repository is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).

You are free to use and adapt this work for **non-commercial** purposes, provided that you give appropriate **credit** and link to the license.
