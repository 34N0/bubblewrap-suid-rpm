# Bubblewrap Suid

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
spectool -g -R bubblewrap.spec
```
Build the RPM from spec:
```bash
rpmbuild -ba bubblewrap.spec
```

### Test locally

Cd into the RPM folder:
```bash
cd ~/rpmbuild/RPMS/x86_64
```
Override the bubblewrap package:
```bash
rpm-ostree override replace bubblewrap-<version>.fc39.x86_64.rpm
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
reboot the VM!