import numpy as np

def interweave(seq, s, t):
    if len(s) + len(t) == 0:
        return True
    elif len(s) == 0:
        return t[0] == seq[0] and interweave(seq[1:], s, t[1:])
    elif len(t) == 0:
        return s[0] == seq[0] and interweave(seq[1:], s[1:], t)
    else:
        return s[0] == seq[0] and interweave(seq[1:], s[1:], t) or t[0] == seq[0] and interweave(seq[1:], s, t[1:])

with open("Bio.txt", 'r') as f:
# with open("rosalind_itwv.txt", 'r') as f:
    seqs = f.read().rstrip().split('\n')

sequence, motifs, mat = seqs[0], seqs[1:], np.zeros([len(seqs) - 1, len(seqs) - 1])

for i in range(len(motifs)):
    for j in range(i, len(motifs)):
        mat[i, j] = mat[j, i] = any([interweave(sequence[k:], motifs[i], motifs[j]) for k in range(len(sequence) - len(motifs[i]) - len(motifs[j]) + 1)])

for row in mat:
    print(" ".join([str(int(x)) for x in row]))