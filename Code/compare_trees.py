import dendropy
from dendropy.calculate.treecompare \
    import false_positives_and_negatives
import numpy as np


def compare_trees(tr1, tr2):
    from dendropy.calculate.treecompare \
        import false_positives_and_negatives

    lb1 = [ l.taxon.label for l in tr1.leaf_nodes() ]
    lb2 = [ l.taxon.label for l in tr2.leaf_nodes() ]

    com = list(set(lb1).intersection(lb2))
    tns = dendropy.TaxonNamespace(com)

    tr1.retain_taxa_with_labels(com)
    tr1.migrate_taxon_namespace(tns)
    tr1.update_bipartitions()

    tr2.retain_taxa_with_labels(com)
    tr2.migrate_taxon_namespace(tns)
    tr2.update_bipartitions()

    #nl1 = len(lb1)
    #nl2 = len(lb2)

    ne1 = len(tr1.internal_edges(exclude_seed_edge=True))
    ne2 = len(tr2.internal_edges(exclude_seed_edge=True))

    nl = len(com)
    [fp, fn] = false_positives_and_negatives(tr1, tr2)
    rf = float(fp + fn) / (ne1 + ne2)

    return(nl, ne1, ne2, fp, fn, rf)


if __name__ == "__main__":
    import sys

    argc = len(sys.argv)
    assert (argc == 3), "Usage: compare_trees.py tr1 tr2"

    tax = dendropy.TaxonNamespace()
    tr1 = dendropy.Tree.get(path=sys.argv[1],
                            schema='newick',
                            rooting='force-unrooted',
                            taxon_namespace=tax)

    tr2 = dendropy.Tree.get(path=sys.argv[2],
                            schema='newick',
                            rooting='force-unrooted',
                            taxon_namespace=tax)

    # Recently added
    tr1.collapse_basal_bifurcation(set_as_unrooted_tree=True)
    tr2.collapse_basal_bifurcation(set_as_unrooted_tree=True)

    [nl, ei1, ei2, fp, fn, rf] = compare_trees(tr1, tr2)

    sys.stdout.write('%d,%d,%d,%d,%d,%f'
                     % (nl, ei1, ei2, fp, fn, rf))
