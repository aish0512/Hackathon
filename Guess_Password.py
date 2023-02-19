with open('keylog.txt') as f:
    sequences = [line.strip() for line in f]
    
scs = set()
for seq in sequences:
    for i, char in enumerate(seq):
        if char not in scs:
            # Add new character to SCS
            scs.add(char)
            # Insert new character into all previous positions in SCS
            for j in range(i):
                if seq[j] in scs and char not in seq[:j]:
                    scs.remove(seq[j])
                    scs.add(char)
            break

print(''.join(scs))





