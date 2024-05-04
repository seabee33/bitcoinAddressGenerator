import bitcoin

def generate_keypair():
    # Generate a new private key
    private_key = bitcoin.random_key()

    # Convert the private key to Wallet Import Format (WIF)
    wif_private_key = bitcoin.encode_privkey(private_key, 'wif')

    # Derive the public key from the private key
    public_key = bitcoin.privkey_to_pubkey(private_key)

    # Hash the public key to get the address
    address = bitcoin.pubkey_to_address(public_key)
    #address = '1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF'

    return wif_private_key, address

def check_address_in_file(address, filename):
    with open(filename, 'r') as file:
        for line in file:
            if address.strip() == line.strip():
                return True
    return False

if __name__ == "__main__":
    while True:
        # Generate keypair
        private_key, public_address = generate_keypair()
        print("Private Key (WIF):", private_key)
        print("Public Address:", public_address)
        
        # Check if generated address is in the file
        filename = 'addresses.txt'  # Replace with your file name
        if check_address_in_file(public_address, filename):
            print("Found a match!")
            break
        else:
            print("Generated address is not in the file.")
        print('=================================')
