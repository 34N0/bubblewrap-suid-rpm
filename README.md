# Bubblewrap Suid

## Build locally

This has to be done on a RPM based Linux distribution and is tested on Fedora Workstation 39 VM.

Install required RPM build tools:
```bash
sudo dnf install -y rpmdevtools rpmlint
```
Create the required file tree:
```bash
rpmdev-setuptree
```
Clone this repo and cd into it:
```bash
git clone https://github.com/34N0/bubblewrap-suid-rpm && cd bubblewrap-suid-rpm
```
Install the required build dependencies:
```bash
sudo dnf install docbook-style-xsl meson libcap-devel libselinux-devel
```
Build the RPM from spec:
```bash
rpmbuild -ba bubblewrap.spec
```