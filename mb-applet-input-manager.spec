%define name 	mb-applet-input-manager
%define version 0.6
%define release %mkrel 7

Summary: 	Input manager for the Matchbox Desktop
Name: 		%name
Version: 	%version
Release: 	%release
Url: 		http://matchbox-project.org/
License: 	GPLv2+
Group: 		Graphical desktop/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source: 	http://matchbox-project.org/sources/%name/%version/%{name}-%{version}.tar.bz2
BuildRequires:	libx11-devel
BuildRequires:	libmatchbox-devel

%description
Input manager for the Matchbox Desktop

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS README 
%_bindir/mbinputmgr
%_datadir/applications/*
%_datadir/pixmaps/*
