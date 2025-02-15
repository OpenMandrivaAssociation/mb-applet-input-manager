%define name 	mb-applet-input-manager
%define version 0.6
%define release  9

Summary: 	Input manager for the Matchbox Desktop
Name: 		%name
Version: 	%version
Release: 	%release
Url: 		https://matchbox-project.org/
License: 	GPLv2+
Group: 		Graphical desktop/Other
Source: 	http://matchbox-project.org/sources/%name/%version/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(x11)
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


%changelog
* Sat Feb 05 2011 Funda Wang <fwang@mandriva.org> 0.6-7mdv2011.0
+ Revision: 636092
- tighten BR

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6-6mdv2011.0
+ Revision: 620303
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.6-5mdv2010.0
+ Revision: 429985
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.6-4mdv2009.0
+ Revision: 252074
- rebuild
- fix no-buildroot-tag
- kill re-definition of %%buildroot on Pixel's request

* Tue Nov 06 2007 Funda Wang <fwang@mandriva.org> 0.6-2mdv2008.1
+ Revision: 106289
- BR matchbox-devel
- Rebuild
- import mb-applet-input-manager


* Mon Jan 10 2005 Austin Acton <austin@mandrake.org> 0.6-1mdk
- 0.6

* Tue Jul 27 2004 Austin Acton <austin@mandrake.org> 0.5-1mdk
- initial package

