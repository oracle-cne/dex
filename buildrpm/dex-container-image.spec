

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%{!?registry: %global registry container-registry.oracle.com/olcne}
%global app_name               dex
%global app_version            2.44.0
%global oracle_release_version 1
%global _buildhost             build-ol%{?oraclelinux}-%{?_arch}.oracle.com

Name:           %{app_name}-container-image
Version:        %{app_version}
Release:        %{oracle_release_version}%{?dist}
Summary:        Dex is an identity service that uses OpenID Connect to drive authentication for other apps
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/dexidp/dex.git
Source:         %{name}-%{version}.tar.bz2

%description
Dex is an identity service that uses OpenID Connect to drive authentication for other apps.

%prep
%setup -q -n %{name}-%{version}

%build
%global rpm_name %{app_name}-%{version}-%{release}.%{_build_arch}
%global docker_tag %{registry}/%{app_name}:v%{version}

yum clean all
yumdownloader --destdir=${PWD}/rpms %{rpm_name}

docker build --pull \
    --build-arg https_proxy=${https_proxy} \
    -t %{docker_tag} -f ./olm/builds/Dockerfile .
docker save -o %{app_name}.tar %{docker_tag}

%install
%__install -D -m 644 %{app_name}.tar %{buildroot}/usr/local/share/olcne/%{app_name}.tar

%files
%license LICENSE THIRD_PARTY_LICENSES.txt olm/SECURITY.md
/usr/local/share/olcne/%{app_name}.tar

%changelog
* Wed Nov 05 2025 Oracle Cloud Native Environment Authors <noreply@oracle.com> - 2.44.0-1
- Added Oracle specific build files for Dex.
