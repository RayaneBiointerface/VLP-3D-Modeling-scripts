from pymol import cmd


def chain_align(ref_obj, monomer):
    
    chains = cmd.get_chains(ref_obj)
    print("Chains found:", chains)  # Print the chains for debugging
    # Create an empty object to store aligned monomers
    cmd.create("aligned_monomers", "none")
    state=0

    for chain in chains:
        # Ensure that 'chain' is a valid selection
        selection = f"{ref_obj} and chain {chain}"
        
        if cmd.count_atoms(selection) == 0:
            print(f"Error: Selection '{selection}' is invalid or empty.")
        else:
            state +=1
            print(f"Aligning 'monomer' to chain {selection}")
            cmd.align(monomer, selection)  # Align 'monomer' to the current chain
            cmd.create("aligned_monomers", monomer, -1, state)
    num_states= cmd.count_states('aligned_monomers')
    print(f"Aligned monomers created with {num_states} states.")
    cmd.set("all_states", 1)
    selections = cmd.get_names("selections")

    # Delete each selection
    for sel in selections:
        cmd.delete(sel)

    print("All selections have been deleted.")
  
print(" You can call the function by using this command:")
print(" chain_align('name_of_your_reference_object', 'name_of_your_monomer')")
cmd.extend("chain_align", chain_align)

#chain_align(ref_obj='name of your refrennce object, monomer= 'name of the monomer') 
# run Reconstruct_VLP_V4.py


