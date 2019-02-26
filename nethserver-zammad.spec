Summary: NethServer zammad integration
Name: nethserver-zammad
Version: 1.0.0
Release: 3%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

Requires: nethserver-nginx, nethserver-postgresql, java-1.8.0-openjdk, elasticsearch

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
(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist

%post

%preun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog
