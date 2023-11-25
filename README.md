# Bubblewrap Suid

## Build locally

This has to be done on a RPM based Linux distribution and is tested on a Fedora Silverblue 39 VM.

Install required RPM build tools:
```bash
sudo rpm-ostree install -y rpmdevtools rpmlint
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
sudo rpm-ostree install docbook-style-xsl meson libcap-devel libselinux-devel
```
Build the RPM from spec:
```bash
rpmbuild -ba bubblewrap.spec
```

## Test locally

Cd into the RPM folder:
```bash
cd ~/rpmbuild/RPMS/x86_64
```