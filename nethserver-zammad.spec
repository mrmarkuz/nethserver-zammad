Summary: NethServer zammad integration
Name: nethserver-zammad
Version: 1.0.0
Release: 8%{?dist}
License: GPL
URL: %{url_prefix}/%{name}
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

Requires: nethserver-nginx, nethserver-postgresql, java-1.8.0-openjdk, elasticsearch, zammad

BuildRequires: perl
BuildRequires: nethserver-devtools

%description
NethServer Zammad integration

%prep
%setup

%build
perl createlinks
mkdir -p root/var/lib/nethserver/zammad/backup

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/share/cockpit/nethserver/applications/
mkdir -p %{buildroot}/usr/libexec/nethserver/api/%{name}/
mkdir -p %{buildroot}/usr/share/cockpit/%{name}/

cp -a %{name}.json %{buildroot}/usr/share/cockpit/nethserver/applications/
cp -a api/* %{buildroot}/usr/libexec/nethserver/api/%{name}/
cp -a ui/* %{buildroot}/usr/share/cockpit/%{name}/

(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} \
  --dir /var/lib/nethserver/zammad/backup 'attr(755, postgres, postgres)' \
  --file /etc/sudoers.d/50_nsapi_nethserver_zammad 'attr(0440,root,root)' \
  --file /usr/libexec/nethserver/api/%{name}/read 'attr(775,root,root)' \
%{buildroot} > %{name}-%{version}-filelist

%post

%preun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog
* Tue Mar 02 2021 Markus Neuberger <info@markusneuberger.at> - 0.0.1-7
- Add zammad requirement

* Sat Apr 11 2020 Markus Neuberger <info@markusneuberger.at> - 0.0.1-6
- Add cockpit application
- Add elasticsearch setup
