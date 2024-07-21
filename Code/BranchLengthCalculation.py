import dendropy
import csv

def branch_length(tree):

    branch_lengths1 = [e.length for e in tree.postorder_edge_iter()]

    with open(r'length.csv','a') as myfile:
        wr=csv.writer(myfile,quoting=csv.QUOTE_ALL)
        wr.writerow(branch_lengths1)
    return(branch_lengths1)



if __name__ == "__main__":

    files=[]
    for i in range(1,10):
        files.append("g_trees"+"000"+str(i)+".trees")
    for i in range(10,100):
        files.append("g_trees"+"00"+str(i)+".trees")
    for i in range(100,1000):
        files.append("g_trees"+"0"+str(i)+".trees")
    files.append("g_trees"+str(1000)+".trees")

    tax = dendropy.TaxonNamespace()

    for j in range(0,1000):
        
        tr1 = dendropy.Tree.get(path=files[j],
                                schema='newick',
                                rooting='force-unrooted',
                                taxon_namespace=tax)

        branch_length(tr1)
