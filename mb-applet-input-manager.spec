%define name 	mb-applet-input-manager
%define version 0.6
%define release 1mdk

Summary: 	Input manager for the Matchbox Desktop
Name: 		%name
Version: 	%version
Release: 	%release
Url: 		http://matchbox.handhelds.org/
License: 	GPL
Group: 		Graphical desktop/Other
Source: 	ftp://ftp.handhelds.org/matchbox/sources/%name/%version/%{name}-%{version}.tar.bz2

Buildroot: 	%_tmppath/%name-%version-buildroot
BuildRequires:	pango-devel XFree86-devel jpeg-devel png-devel libXsettings-client-devel

%description
Input manager for the Matchbox Desktop

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS README 
%_bindir/mbinputmgr
%_datadir/applications/*
%_datadir/pixmaps/*

