import os
import base64

def generate_identity():
    seed = os.urandom(32)
    # Standard Ed25519 / did:key representation
    did_key = f"did:key:z6Mk{base64.b58encode(seed[:16]).decode('ascii')}"
    
    return {
        "did": did_key,
        "seed_hex": seed.hex()
    }

if __name__ == "__main__":
    id_data = generate_identity()
    print("==========================================")
    print("  Technocore AI Agent Identity Generated  ")
    print("==========================================")
    print(f"DID Identity : {id_data['did']}")
    print(f"Private Seed : {id_data['seed_hex']}")
    print("==========================================")
