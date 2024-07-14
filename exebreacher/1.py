import subprocess
import os

def extract_source(exe_path):
    # Ensure pyinstxtractor.py is in the current directory
    pyinstxtractor_path = "./pyinstxtractor.py"

    # Run pyinstxtractor.py to extract the source code from the .exe
    command = f"python \"{pyinstxtractor_path}\" \"{exe_path}\""
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"[!] Error: {e}")
        print(e.stderr)

def main():
    print("Drag the .exe file into the console and press Enter:")
    exe_path = input().strip()

    # Extract source code
    extract_source(exe_path)

if __name__ == "__main__":
    main()
