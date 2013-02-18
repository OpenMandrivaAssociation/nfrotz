%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define name    nfrotz
%define version 0.3.3
%define release 3

Name:           %{name}
Summary:        Z-machine interpreter for Interactive Fiction games, with support for Unicode
Version:        %{version}
Release:        %{release}
Source0:        http://mirror.ifarchive.org/if-archive/infocom/interpreters/frotz/%{name}-%{version}.tgz
URL:            http://www.stanford.edu/~mcmartin/if/
License:        GPLv2

Group:          Games/Other
BuildRequires:  ncursesw-devel
BuildRoot:      %{_tmppath}/%{name}-buildroot

%description
NFrotz is a Z-Machine interpreter. The Z-machine is a virtual machine
designed by Infocom to run all of their text adventures. It went
through multiple revisions during the lifetime of the company, and two
further revisions (V7 and V8) were created by Graham Nelson after the
company's demise. The specification is now quite well documented; this
version of Frotz supports version 1.1.

This version of Frotz fully supports all these versions of the Z-Machine
except for version 6. Version 6 is semi-supported by displaying the
outlines of V6 graphics with the picture number in the bottom-right corner.

NFrotz is a merged port of the original Unix Frotz, incorporating
extensions made by the WinFrotz port.
The primary visible difference between NFrotz and ordinary Frotz is
support for UTF-8 terminals and some awareness of iFiction-based meta-data
if present.

%prep
%setup -q -n %{name}-%{version}

perl -pi -e "s|/lib/|/%_lib/|" configure

%build

%configure
%make

%install
rm -rf %{buildroot}
make PREFIX=%{buildroot}/usr MAN_PREFIX=%{buildroot}/usr/share install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc AUTHORS ChangeLog COPYING HOW_TO_PLAY README
%{_mandir}/*/*
%{_bindir}/*



%changelog
* Fri Apr 27 2012 Crispin Boylan <crisb@mandriva.org> 0.3.3-3
+ Revision: 794037
- Rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Jul 30 2008 Michael Scherer <misc@mandriva.org> 0.3.3-1mdv2009.0
+ Revision: 254964
- fix build on x86_64 ( with /lib hardcoded in the script )
- remove wrong Requires
- update to 0.3.3
- import nfrotz

