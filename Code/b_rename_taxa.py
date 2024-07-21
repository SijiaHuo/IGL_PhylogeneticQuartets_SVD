"""
Changes taxa names to integers.

Author: Erin K. Molloy (emolloy2@illinois.edu)
"""
from decimal import Decimal
import dendropy
import os


def branch_lengths_2_decimals(str_newick_tree):
    """
    replaces branch lengths in scientific notation with decimals
    function taken from Phybase.py, see
    github.com/ngcrawford/CloudForest/blob/master/cloudforest/phybase.py
    """
    colon_s = 0
    comma_back_paren_s = 0
    num = ''
    new_tree = ''
    for count, char in enumerate(str_newick_tree):
        if char == ':':
            colon_s = count
            continue
        if char in (')', ','):
            comma_back_paren_s = 1
            num = '%1.12f' % Decimal(num)
            new_tree += ":" + num
            colon_s = 0
            num = ''
        if colon_s != 0:
            num = num + char
        if colon_s == 0:
            new_tree += char
    new_tree = new_tree.strip('\'').strip('\"').strip('\'') + '\n'
    return new_tree

def write_tree(tree, name):
    with open(name, 'w') as f:
            x = branch_lengths_2_decimals(tree.as_string(schema='newick'))
            #f.write(x[5:])
            f.write(x)


def rename_taxa(tax):
    nam = sorted([x.label for x in tax])
    dic = {}
    for i, n in enumerate(nam):
        dic[n] = str(i+1)

    for x in tax:
        x.label = dic[x.label]


def rename_simphy_data(ngen, pad):
    # Species tree
    stax = dendropy.TaxonNamespace()
    stre = dendropy.Tree.get(path="s_tree.trees",
                             schema="newick",
                             taxon_namespace=stax)
    rename_taxa(stax)
    stre.write(path="true-species.tre",
               schema='newick',
               suppress_rooting=True)
    write_tree(stre, "true-species.tre")

    for n in stre.nodes():
        n.edge.length = None
    stre.write(path="true-species-nolen.tre",
               schema='newick',
               suppress_rooting=True)
    os.remove("s_tree.trees")

    # Locus trees
    ltax = dendropy.TaxonNamespace()
    ltre = dendropy.TreeList.get(path="l_trees.trees",
                                 schema="newick",
                                 taxon_namespace=ltax)
    rename_taxa(ltax)
    ltre.write(path="true-loci.tre",
               schema='newick',
               suppress_rooting=True)
    os.remove("l_trees.trees")

    # Gene trees
    gs = [str(g).zfill(pad) for g in range(1, ngen+1)]
    for g in gs:
        gtax = dendropy.TaxonNamespace()
        gtre = dendropy.Tree.get(path="g_trees" + g + ".trees",
                                 schema="newick",
                                 taxon_namespace=gtax)
        rename_taxa(gtax)
        write_tree(gtre, "true-gene-" + g + ".tre")
        os.remove("g_trees" + g + ".trees")


if __name__ == "__main__":
    os.chdir("../data")

    ngen = [50, 1000]
    pads = [2, 4]
    mods = ["simphy-5tax-50gen-1000bps",
            "simphy-5tax-1000gen-50bps"]

    nrep = 10
    reps = [str(r).zfill(2) for r in range(1, nrep + 1)]

    for m, g, p in zip(mods, ngen, pads):
        os.chdir(m)
        for r in reps:
            os.chdir(r)
            rename_simphy_data(g, p)
            os.chdir("..")
        os.chdir("..")
