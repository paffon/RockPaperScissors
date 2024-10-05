import os
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <path>")
        sys.exit(1)

    given_path = sys.argv[1]

    for root, dirs, files in os.walk(given_path):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                relative_path = os.path.relpath(filepath, start=given_path)
                print(f"File: {given_path.split('\\')[-1]}\\{relative_path}")
                print("---")
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                except UnicodeDecodeError:
                    with open(filepath, 'r', encoding='latin1') as f:
                        content = f.read()
                print(content)

if __name__ == '__main__':
    main()
