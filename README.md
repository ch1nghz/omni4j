<p align="center">
    <img src="https://omni4j.com/logo.png" alt="omni4j Logo" width="150" />
</p>

The omni4j is a robust SAST tool designed for scanning Java projects. It employs advanced security analysis techniques, including data flow analysis, control flow analysis, taint analysis, and performance analysis, to provide thorough and comprehensive security assessments for Java codebases.

## Prerequisites

Ensure you have the following installed:
- Python 3.x
- Required Python packages: `pyyaml`, `requests`, `netifaces` (on macOS)

You can install the required Python packages using:
```sh
pip install pyyaml requests netifaces
```

## Usage

Registering a User
To register a user and obtain a license key, create a YAML file with the following structure:
```yaml
first_name: "YourFirstName"
last_name: "YourLastName"
company_name: "YourCompanyName"
email: "YourBusinessEmailAddress"
```

Run the registration command and then check your email box:
```sh
python3 cli.py --register --yaml path/to/user_info.yaml
```

## Executing the Binary
To execute the binary for scanning a Java project, use the obtained license key and specify the directory containing the Java project:

```sh
python3 cli.py --license YOUR_LICENSE_KEY --java-directory /path/to/java/project
```

## Arguments

- `--register`: Register and obtain a license key. Requires the `--yaml` argument.
- `--yaml`: Path to the YAML file containing user information for registration.
- `--license`: License key for executing the binary.
- `--java-directory`: Directory containing the Java project to scan.

## Supported Operating Systems

### Linux
- Ubuntu 21.10 and later versions
- Debian 11 (Bullseye) and later versions
- Fedora 34 and later versions
- Arch Linux (rolling release with updates)

### macOS
- macOS 11.0 (Big Sur) and later versions (only ARM architectures)

### Windows
- Windows 10 x64 and later versions
- Windows 11 x64

## Contact
Have questions or need support? Reach out to our team at [info@omni4j.com](mailto:info@omni4j.com) or visit our website for more details at [omni4j.com](https://omni4j.com).
