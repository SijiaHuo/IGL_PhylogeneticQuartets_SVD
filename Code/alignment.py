"""
Functions for manipulating alignments

Copyright (C) 2016 Erin K Molloy (ekmolloy@uchicago.edu)
Modified by Sijia (Scarlett) Huo in November 2016.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


class alignment(object):
    """
    Creates a multiple sequence alignmemnt object.

    Parameters
    ----------
    nsq : integer
          number of sequences
    nbp : integer
          number of base pairs
    dat : dictionary
          sequence names datped to sequence data
    """

    def __init__(self):
        self.nsq = 0
        self.nbp = 0
        self.dat = {}

    def hamming_distance_matrix(self):
        """
        Computes a matrix of sequence-to-sequence hamming distances and returns
        an array. Taken from https://en.wikipedia.org/wiki/Hamming_distance

        Returns
        -------
        D : distance matrix object
        """
        from numpy import zeros

        names = sorted(self.dat.keys())
        D = zeros((self.nsq, self.nsq), dtype=float)
        for i in range(self.nsq):
            for j in range(self.nsq):
                D[i, j] = sum(x != y for x, y
                              in zip(self.dat[names[i]],
                                     self.dat[names[j]]))
                D[j, i] = D[i, j]
        D = D / self.nbp
        return D

    def summarize_p_distances(self):
        import numpy

        names = sorted(self.dat.keys())
        hs = []
        for i in range(self.nsq):
            for j in range(i+1, self.nsq):
                h = sum(x != y for x, y
                        in zip(self.dat[names[i]],
                        self.dat[names[j]]))
                hs.append(h)
        hs = numpy.array(hs)
        hmax = float(numpy.max(hs)) / self.nbp
        havg = numpy.mean(hs) / self.nbp
        hstd = numpy.std(hs) / self.nbp
        return [hmax, havg, hstd]

    def write_fasta(self, fasta, interleaved=False):
        with open(fasta, 'w') as f:
            for n in sorted(self.dat.keys()):
                f.write('>' + n + '\n' + self.dat[n] + '\n')

    def write_nexus(self, nexus, interleaved=False):
        names = sorted(self.dat.keys())
        with open(nexus, 'w') as f:
            f.write("#NEXUS\n\n")

            f.write("BEGIN TAXA;\n")
            f.write("    DIMENSIONS NTAX=%d;\n" % self.nsq)
            f.write("    TAXLABELS\n")
            for n in names:
                f.write("        %s\n" % n)
            f.write("    ;\n")
            f.write("END;\n\n")

            f.write("BEGIN CHARACTERS;\n")
            f.write("    DIMENSIONS NCHAR=%d;\n" % self.nbp)
            f.write("    FORMAT DATATYPE=DNA" + " GAP=-" +
                    " MISSING=?" + " MATCHCHAR=.;\n")  # FIX ME
            f.write("    MATRIX\n")
            for n in names:
                f.write("        %s    %s\n" % (n, self.dat[n]))
            f.write("    ;\n")
            f.write("END;")


def concatenate(alns, fill_gaps=True):
    """
    Concatenates alignments together.

    Parameters
    ----------
    alns : list of alignments
    """

    if fill_gaps is False:
        seqs = set(alns[0].dat.keys())
        for a in alns[1:]:
            seqs.intersection(set(a.dat.keys()))
    else:
        seqs = set()
        for a in alns:
            seqs.update(set(a.dat.keys()))  # union?

    c = alignment()
    c.nsq = len(seqs)
    c.nbp = sum([a.nbp for a in alns])

    for s in seqs:
        c.dat[s] = ''

    for a in alns:
        for s in seqs:
            c.dat[s] = c.dat[s] + a.dat.get(s, '-' * a.nbp)
        # del a

    return c


def read_fasta(fasta):
    import re
    a = alignment()

    with open(fasta, 'r') as f:
        f.read(1)  # '>'
        seqs = f.read().split('>')
        a.nsq = len(seqs)

        d = seqs[0]
        d = d.split('\n', 1)[1]
        d = d.replace('\n', '')
        d = d.replace('\r', '')  # Windows
        d = d.replace(' ', '')   # Added by Scarlett
        a.nbp = len(d)

        for s in seqs:
            [n, d] = s.split('\n', 1)
            n = n.replace(' ', '')
            d = d.replace('\n', '')  # interleaved
            d = d.replace('\r', '')  # Windows
            d = d.replace(' ', '')   # Added by Scarlett

            assert(len(d) == a.nbp), \
                "Error: Sequences are not all the same length!"

            a.dat[n] = d

    return a


def read_phylip(phylip,num):
    a = alignment()

    with open(phylip, 'r') as f:
        lines = f.read().split('\r\n')
        words = lines[0].split()
        a.nsq = int(words[0])
        a.nbp = num
        for s in range(1, a.nsq+1):
            [n, d] = lines[s].split(' ', 1)
            n = n.replace(' ', '')
            d = d.replace(' ', '')

#           assert(len(d) == a.nbp), \
#                "Error: Sequences are not all the same length!"

            a.dat[n] = d[0:num]

    return a
