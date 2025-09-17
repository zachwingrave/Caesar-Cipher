from string import ascii_lowercase

def decrypt_dictionary(ciphertext, key=13):
  from_plaintext = {}
  for char in ascii_lowercase:
    new_char = ascii_lowercase.find(char) + key
    if new_char > 25:
      new_char = new_char - 26
    from_plaintext[char] = ascii_lowercase[new_char]

  from_ciphertext = {
    v: k for k, v in from_plaintext.items()
  }

  answer = ""
  for char in ciphertext:
    if char == " ":
      answer += " "
    else:
      answer += from_ciphertext[char]
  return answer

def decrypt_rotation(ciphertext, key=13):
  answer = ""
  for char in ciphertext:
    if char == " ":
      answer += " "
    else:
      new_char = ascii_lowercase.find(char) - key
      if new_char > 25:
        new_char = new_char - 26
      answer += ascii_lowercase[new_char]
  return answer

if __name__ == "__main__":
  ciphertext = input("Enter ciphertext:").lower().strip()
  key = int(input("Enter key value: ").lower().strip())

  print("1. Decrypt using dictionary")
  print("2. Decrypt using rotation")
  option = input("Enter your choice: ").lower().strip()

  if option == "1":
    print("Answer is:", decrypt_dictionary(ciphertext, key))
  elif option == "2":
    print("Answer is:", decrypt_rotation(ciphertext, key))
  else:
    print("Error, please try again.")
