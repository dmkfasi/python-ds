import math

def running_median(stream):
  # Fill this in.

  # Define accumulator
  acc = []

  # Iterate over the stream
  for n in stream:
    # Push and sort accumulator
    acc.append(n)
    acc.sort()

    # Find median element index
    size = len(acc)

    if size % 2 == 1:
      # Odd size is just the number in the middle
      idx = math.floor(size / 2)
      median = acc[idx]
    else:
      # Even size is average between the two in the middle

      # Find lower and upper bounds for the range to sum and divide
      idx_dn = int(size / 2) - 1
      idx_up = idx_dn + 2
      median = sum(acc[idx_dn:idx_up]) / 2

    # Spit it out
    print(median)

running_median([2, 1, 4, 7, 2, 0, 5])
# 2 1.5 2 3.0 2 2.0 2
