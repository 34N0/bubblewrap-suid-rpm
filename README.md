# 📦 bubblewrap-suid

This repository contains the .spec file for bundling a setuid variant of [Bubblewrap](https://github.com/containers/bubblewrap) as an RPM.

This allows using flatpaks on immutable OSTree distributions with `user.max_user_namespaces = 0` and `kernel.unprivileged_userns_clone = 0` set.

## CI

*Currently the Bubblewrap releases are tracked manually. The goal for this repository is for it to track automatically*

## Install

The following commands are needed to replace an existing `bubblewrap` package with `bubblewrap-suid`.

### OSTree

Get the COPR `.repo` file
```bash
curl -s https://copr.fedorainfracloud.org/coprs/34n0s/bubblewrap-suid/repo/fedora-39/34n0s-bubblewrap-suid-fedora-39.repo | sudo tee /etc/yum.repos.d/34n0s-bubblewrap-suid-fedora-39.repo

```
Override `bubblewrap` (without suid) package
```bash
sudo rpm-ostree override replace --experimental --freeze --from repo='copr:copr.fedorainfracloud.org:34n0s:bubblewrap-suid' bubblewrap
```

### DNF

Enable the COPR `.repo` file
```bash
sudo dnf copr enable 34n0s/bubblewrap-suid 
```
Override `bubblewrap` (without suid) package
```bash
sudo dnf swap bubblewrap bubblewrap-suid
```

## Develop

### Build locally

This has to be done on a RPM based Linux distribution and is tested on a Fedora Silverblue 39 VM.

Install required RPM build tools and dependencies:
```bash
rpm-ostree install -y rpmdevtools rpmlint docbook-style-xsl meson libcap-devel libselinux-devel gcc
```
Create the required file tree:
```bash
rpmdev-setuptree
```
Clone this repo and cd into it:
```bash
git clone https://github.com/34N0/bubblewrap-suid-rpm && cd bubblewrap-suid-rpm
```
Download bubblewrap source
```bash
spectool -g -R bubblewrap-suid.spec
```
Build the RPM from spec:
```bash
rpmbuild -ba bubblewrap-suid.spec
```

### Test locally

Cd into the RPM folder:
```bash
cd ~/rpmbuild/RPMS/x86_64
```
Override the bubblewrap package:
```bash
rpm-ostree override replace bubblewrap-suid-<version>.fc39.x86_64.rpm
```

### disabling unprivileged user namespaces
Edit the sysctl config:
```bash
sudo nano /etc/sysctl.d/99-sysctl.conf 
```
add the following lines:
```bash
user.max_user_namespaces = 0
kernel.unprivileged_userns_clone = 0
```
load the parameters:
```bash
sudo sysctl --system
```
reboot the VM!

## Issues & Contributions

Feel free to open issues or pull requests for improvements, bug fixes. 😄
Be mindful that this repository is simply the [Bubblewrap](https://github.com/containers/bubblewrap) project with the SUID bit set.

