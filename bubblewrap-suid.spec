Name:    bubblewrap-suid
Version: 0.8.0
Release: 1%{?dist}
Summary: Core execution tool for unprivileged containers (setuid variant)

License: LGPL-2.0-or-later
URL:     https://github.com/containers/bubblewrap/
Source0: https://github.com/containers/bubblewrap/releases/download/v%{version}/bubblewrap-%{version}.tar.xz

Provides: bubblewrap = %{version}

BuildRequires: pkgconfig(bash-completion) >= 2.0
BuildRequires: gcc
BuildRequires: docbook-style-xsl
BuildRequires: meson
BuildRequires: pkgconfig(libcap)
BuildRequires: pkgconfig(libselinux)
BuildRequires: /usr/bin/xsltproc

%description
Bubblewrap (/usr/bin/bwrap) is a core execution engine for unprivileged
containers that works as a setuid binary on kernels without
user namespaces. (setuid variant)

%prep
%setup -q -n bubblewrap-%{version}

%build
%meson -Dman=enabled -Dselinux=enabled
%meson_build

%install
%meson_install

%files
%license COPYING
%doc README.md
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/bwrap
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_bwrap
%{_bindir}/bwrap

%{_mandir}/man1/bwrap.1*

%post
chown root:root %{_bindir}/bwrap
chmod u+s %{_bindir}/bwrap

%changelog
* Mon Nov 27 2023 34n0 <uhchyf42o@mozmail.com> - 0.8.0-1
- Initial Release tracking Bubblewrap version