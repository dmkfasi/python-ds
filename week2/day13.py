def decodeString(s):
  # Fill this in.

  # Brackets quantity
  br = 0

  # Output String buffer
  strout = []

  # Transform String into a List
  char_list = list(s)

  while char_list:
    c = char_list.pop(0)

    # A number is a character sequence multiplier
    if c.isnumeric():
      c = int(c)
      # 0 annihilates the string sequence
      if c == 0:
        return

      for _ in range(0, c - 1):
        strout.append(decodeString(''.join(char_list)))

      continue

    if c == '[':
      # Add up bracket counter
      br += 1
      continue

    if c == ']':
      # Subtract bracket counter
      br -= 1

      if br < 0:
        return 'Invalid substring detected'

      # As soon as there are no brackets left, return joined List as a String
      if br == 0:
        return ''.join(strout)

      continue

    # Append any other characters
    strout.append(c)

  # Compose output buffer as a String
  return ''.join(strout)

print(decodeString('2[a2[b]c]'))
# abbcabbc

print(decodeString('1[a2[b]c3[d]]'))
# abbcddd

print(decodeString('1[a2[2b]c]'))
# aInvalid substring detectedbInvalid substring detectedbc

print(decodeString('0[a1[b]c]'))
# None, empty string
