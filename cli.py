import os
import sys
import yaml
import requests
import platform
import hashlib
import subprocess
import argparse

def read_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def register_license(user_info):
    url = "https://omni4j.com/license/register"
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=user_info, headers=headers)
    if response.status_code == 200:
        return response.json().get('message'), True
    else:
        return response.json().get('message'), False

def fetch_remote_function(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to download the function: {response.status_code}")
        sys.exit(1)

def get_unique_value():
    # This function will be dynamically fetched from the server
    func_url = "https://omni4j.com/script"
    func_code = fetch_remote_function(func_url)
    local_vars = {}
    exec(func_code, globals(), local_vars)
    return local_vars['a1']()

def md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

def download_binary(license_key):
    os_name = platform.system().lower()
    os_arch = platform.machine().lower()
    if 'darwin' in os_name and 'arm' in os_arch:
        architecture = 'macos-arm'
    elif 'win' in os_name:
        architecture = 'windows'
    elif 'linux' in os_name:
        architecture = 'linux'
    else:
        raise ValueError(f"Unsupported operating system: {os_name} with architecture: {os_arch}")

    url = f"https://omni4j.com/license/download_script?key={license_key}&architecture={architecture}"
    response = requests.get(url)
    if response.status_code == 200:
        script_path = "C:\\Users\\Public\\.omni4j.tmp" if 'windows' in os_name else "/tmp/.omni4j.tmp"
        with open(script_path, 'wb') as file:
            file.write(response.content)
        os.chmod(script_path, 0o755)
        return script_path
    else:
        return None

def register(yaml_file_path):
    user_info = read_yaml(yaml_file_path)
    unique_value = get_unique_value()
    if not unique_value:
        print("Failed to get Unique Value.")
        return

    unique_value_hash = md5_hash(unique_value)
    user_info['unique_value'] = unique_value_hash

    message, success = register_license(user_info)
    if success:
        print(f"Registration successful: {message}")
    else:
        print(f"Registration failed: {message}")

def execute(license_key, java_directory):
    unique_value = get_unique_value()
    if not unique_value:
        print("Failed to get Unique Value.")
        return

    unique_value_hash = md5_hash(unique_value)
    script_path = download_binary(license_key)
    if script_path:
        command = f"{script_path} {java_directory} {license_key} {unique_value_hash}"
        try:
            output = subprocess.check_output(command, shell=True, universal_newlines=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.output}")
        finally:
            os.remove(script_path)

def main():
    parser = argparse.ArgumentParser(description="Omni4j CLI")
    parser.add_argument("--register", help="Register and obtain a license key", action="store_true")
    parser.add_argument("--yaml", help="Path to the YAML file with user information", type=str)
    parser.add_argument("--license", help="License key for executing the binary", type=str)
    parser.add_argument("--java-directory", help="Directory containing Java project to scan", type=str)

    args = parser.parse_args()

    if args.register:
        if not args.yaml:
            print("YAML file path is required for registration.")
            sys.exit(1)
        register(args.yaml)
    else:
        if not args.license:
            print("License key is required for executing the CLI.")
            sys.exit(1)
        if not args.java_directory:
            print("Java project is required for executing the CLI.")
            sys.exit(1)
        execute(args.license, args.java_directory)

if __name__ == "__main__":
    main()
