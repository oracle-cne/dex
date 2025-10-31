{{{$version := printf "%s.%s.%s" .major .minor .patch }}}

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

%global app_name                dex
%global app_version             {{{$version}}}
%global oracle_release_version  1
%global _buildhost              build-ol%{?oraclelinux}-%{?_arch}.oracle.com

Name:           %{app_name}
Version:        %{app_version}
Release:        %{oracle_release_version}%{?dist}
Summary:        Dex is an identity service that uses OpenID Connect to drive authentication for other apps
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/dexidp/dex.git
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  golang >= 1.21
BuildRequires:	make
BuildRequires:  glibc-static

%description
Dex is an identity service that uses OpenID Connect to drive authentication for other apps.

%prep
%setup -q -n %{name}-%{version}

%build
make release-binary

%install
install -m 755 -d %{buildroot}%{_var}/dex
install -m 755 -d %{buildroot}%{_sysconfdir}/dex
install -m 755 config.docker.yaml %{buildroot}%{_sysconfdir}/dex/config.docker.yaml
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 /go/bin/dex %{buildroot}%{_bindir}/dex
install -m 755 -d %{buildroot}/srv/dex/web
cp -r web/* %{buildroot}/srv/dex/web

%files
%license LICENSE THIRD_PARTY_LICENSES.txt olm/SECURITY.md
%{_var}/dex
%{_sysconfdir}/dex/config.docker.yaml
%{_bindir}/dex
/srv/dex/web

%changelog
* {{{.changelog_timestamp}}} - {{{$version}}}-1
- Added Oracle specific build files for Dex.
