# https://leetcode.com/problems/valid-phone-numbers/
# Read from the file file.txt and output all valid phone numbers to stdout.

# grep -E '[0-9]{3}-[0-9]{3}-[0-9]{4}|\([0-9]{3}\) [0-9]{3}-[0-9]{4}' file.txt # Still not sure why this not work
grep -E '^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$' file.txt
