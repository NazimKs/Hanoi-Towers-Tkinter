def hanoi(ids, source, destination, temp, hauteurs):
    if ids:
        # Move n-1 disks from source to temp, using destination as temporary storage
        hanoi(ids[1:], source, temp, destination, hauteurs)
        # Move the nth disk from source to destination
        print(ids[0], (source, hauteurs[source] - 1),
              (destination, hauteurs[destination]))
        # Update the heights of the source and destination towers
        hauteurs[source] -= 1
        hauteurs[destination] += 1
        # Move the n-1 disks from temp to destination, using source as temporary storage
        hanoi(ids[1:], temp, destination, source, hauteurs)

# Test the algorithm with 3 disks on tower A (0), moving them to tower B (1)
# starting with tower heights of [3, 0, 0]
hanoi([0, 1, 2], 0, 1, 2, [3, 0, 0])
