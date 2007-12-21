%define name	xmlclitools
%define version 1.61
%define release %mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Command-line xml tools
Source:		http://robur.slu.se/jensl/xmlclitools/%{name}.tar.bz2
URL:		http://robur.slu.se/jensl/xmlclitools
License:	GPL
Group:		File tools
BuildRequires:	libglib-devel
BuildRequires:	libxml2-devel
BuildRequires:	pcre-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
xmlclitools provides four command-line tools for searching, modifying,
and formating XML data. The tools are designed to work in conjunction
with standard *nix utilities such as grep, sort, and shell scripts.

%prep
%setup -q -n %{name}
perl -pi \
    -e 's|^LIB_BASE=.*|LIB_BASE=%{_libdir}|;' \
    -e 's|^INCLUDE_BASE=.*|INCLUDE_BASE=%{_includedir}:%{_libdir}|;' \
    configure
perl -pi -e 's|gcc|gcc %{optflags}|' Makefile

%build
%configure
%make

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 xmlngrep xmlgrep xmlfmt xmlmod %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING MANUAL
%{_bindir}/*

