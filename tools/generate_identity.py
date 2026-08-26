import os, base64

def generate_identity():
    seed = os.urandom(32)
    did = f"did:key:z6Mk{base64.b58encode(seed[:16]).decode('ascii')}"
    print(f"Generated DID: {did}")

if __name__ == "__main__":
    generate_identity()
