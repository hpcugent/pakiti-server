Summary:	Patching status monitoring tool
Name:		pakiti-server
Version:	3.1.1
%global rel	1
Release:	%{rel}.%{gittag}.ug
URL:		https://github.com/CESNET/pakiti-server
License:	BSD 2-Clause "Simplified" License
Group:		Applications/Internet
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch
BuildRequires:	perl
Requires:	php php-mysqlnd php-process php-xml mariadb-server

%description
Pakiti provides a monitoring mechanism to check the patching status of
Linux systems.

This package provides the server part that is able to receive information
about installed software from a Pakiti clients.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_localstatedir}/www/pakiti-server
mkdir -p %{buildroot}/%{_localstatedir}/spool/pakiti/reports
mkdir -p %{buildroot}/%{_localstatedir}/lib/pakiti
mkdir -p %{buildroot}/%{_sysconfdir}/pakiti

install -D src %{buildroot}/%{_localstatedir}/www/pakiti-server/src
install -D install %{buildroot}/%{_localstatedir}/www/pakiti-server/install

%clean
rm -rf %{buildroot}

%files

%defattr(-,apache,apache,-)
%{_localstatedir}/spool/pakiti/reports
%{_localstatedir}/lib/pakiti

%defattr(-,root,root,-)
%{_localstatedir}/www/pakiti-server/src/{common,dao,managers,model,modules}/*
%{_localstatedir}/www/pakiti-server/install/*.{php,sql}
%{_sysconfdir}/pakiti

