from pymol import cmd

def chain_align(ref_obj, monomer1, monomer2):
    # Get all chains in the reference object
    chains = sorted(cmd.get_chains(ref_obj))
    print(f"Total chains found in '{ref_obj}': {len(chains)}")

    # Manually defined chains for monomer1. 
    # These chain list is for AP205 VLP only. For heteromeric particles that are not based on AP205 this list of chains should be eddited 

    chains1 = ['AB', 'AE', 'AH', 'AK', 'AN', 'AQ', 'AT', 'AW', 'AZ', 'BC', 'BF', 'BI', 'BL', 'BO', 'BR', 'BU', 'BW', 'BX', 'CA', 'CD', 'CG', 'CJ', 'CM', 'CP', 'CS', 'CV', 'CY', 'DB', 'DE', 'DH', 'DK', 'DN', 'DQ', 'DT', 'DW', 'DZ', 'EC', 'EF', 'EI', 'EL', 'EO', 'ER', 'EU', 'EX', 'FA', 'FD', 'FG', 'FJ', 'FM', 'FP', 'FS', 'FV', 'FY', 'GB', 'GE', 'GH', 'GK', 'GN', 'GQ', 'GT', 'GW', 'AG', 'AJ', 'AM', 'AS', 'AY', 'BB', 'BK', 'BN', 'BZ', 'CF', 'CI', 'CR', 'CX', 'DJ', 'DP', 'EB', 'EH', 'EQ', 'ET', 'FC', 'FF', 'FO', 'FX', 'GA', 'GG', 'GM', 'GP', 'GS', 'GY']
    
    # Derive chains for monomer2 automatically
    chains2 = [chain for chain in chains if chain not in chains1]

    print(f"Chains used for monomer1 ({len(chains1)}): {chains1}")
    print(f"Chains used for monomer2 ({len(chains2)}): {chains2}")

    # Clean up previous objects if they exist
    cmd.delete("aligned_monomers1")
    cmd.delete("aligned_monomers2")

    cmd.create("aligned_monomers1", "none")
    cmd.create("aligned_monomers2", "none")

    def align_and_create(chains_subset, monomer_name, output_obj):
        state = 0
        for chain in chains_subset:
            selection = f"{ref_obj} and chain {chain}"
            if cmd.count_atoms(selection) == 0:
                print(f"Warning: No atoms found in selection '{selection}'")
                continue
            state += 1
            print(f"Aligning '{monomer_name}' to chain '{chain}'")
            cmd.align(monomer_name, selection)
            cmd.create(output_obj, monomer_name, -1, state)
        return state

    # Align both monomers
    num_states1 = align_and_create(chains1, monomer1, "aligned_monomers1")
    print(f"Aligned monomers1 created with {num_states1} states.")

    num_states2 = align_and_create(chains2, monomer2, "aligned_monomers2")
    print(f"Aligned monomers2 created with {num_states2} states.")

    # Set all_states to view all aligned monomers
    cmd.set("all_states", 1)

    # Clean up selections
    for sel in cmd.get_names("selections"):
        cmd.delete(sel)
    print("Temporary selections deleted.")

# Make it available as a PyMOL command
cmd.extend("chain_align", chain_align)

print("You can now call the function in PyMOL with:")
print("chain_align('ref_object', 'monomer1', 'monomer2')")