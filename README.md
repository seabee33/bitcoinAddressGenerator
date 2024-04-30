# A Bitcoin brute force python script

This script uses the 'bitcoin' python library from Vitalik Buterin to:
  - generate a private key
  - generate the corresponding address
  - check the address against a list of addresses with balances


Steps to get the script going:

1 - Download the bitcoin address tsv file from https://blockchair.com/dumps OR http://addresses.loyce.club/ \
2 - Download this entire repo as a zip file\
3 - (optional) run the 0_checkLineCount.py to check how many lines are in the tsv file\
4 - Run the 1_cleanup.py file to remove:
 - The first line from the file (junk text)
 - Any address that start with '3' (script address) or a 'b' (Segwit and Taproot address)
 - The tab and balance

5 - Run the 2_main.py\
6 - Wait trillions of years or find a quantum computer with many many qubits

# Important! If you would like to improve or chance this code please edit the file in the (advanced) folder!
