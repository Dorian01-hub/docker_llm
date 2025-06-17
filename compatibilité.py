import requests
import re

# Script pour détecter les packages non compatibles Linux dans requirements.txt
# Usage : python check_compatibility.py requirements.txt

import sys

def parse_requirements(file_path):
    pattern = re.compile(r"^([a-zA-Z0-9_-]+)==([0-9a-zA-Z\.\-]+)")
    packages = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            match = pattern.match(line)
            if match:
                pkg, version = match.groups()
                packages.append((pkg, version))
    return packages


def check_linux_compatibility(pkg, version):
    url = f"https://pypi.org/pypi/{pkg}/{version}/json"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code != 200:
            return False, f"Version {version} non trouvée sur PyPI"
        data = r.json()
        files = data.get('releases', {}).get(version, [])
        # Cherche un wheel universel ou manylinux
        for file in files:
            filename = file.get('filename', '')
            if 'manylinux' in filename or 'py3-none-any' in filename:
                return True, None
        return False, 'Aucun wheel Linux trouvé'
    except Exception as e:
        return False, str(e)


def main():
    if len(sys.argv) != 2:
        print("Usage: python check_compatibility.py requirements.txt")
        sys.exit(1)

    req_file = sys.argv[1]
    packages = parse_requirements(req_file)

    incompatible = []
    for pkg, version in packages:
        ok, reason = check_linux_compatibility(pkg, version)
        if not ok:
            incompatible.append((pkg, version, reason))
            print(f"❌ {pkg}=={version}: {reason}")
        else:
            print(f"✅ {pkg}=={version} compatible Linux")

    if incompatible:
        print("\nPackages non compatibles Linux:")
        for pkg, version, reason in incompatible:
            print(f"- {pkg}=={version} → {reason}")
    else:
        print("\nTous les packages sont compatibles Linux !")

if __name__ == '__main__':
    main()
