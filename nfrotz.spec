Summary:	Z-machine interpreter for Interactive Fiction games, with support for Unicode
Name:		nfrotz
Version:	0.3.3
Release:	4
License:	GPLv2+
Group:		Games/Other
Url:		http://www.stanford.edu/~mcmartin/if/
Source0:	http://mirror.ifarchive.org/if-archive/infocom/interpreters/frotz/%{name}-%{version}.tgz
Patch0:		nfrotz-0.3.3-no-strip.patch
BuildRequires:	pkgconfig(ncursesw)

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

%files
%doc AUTHORS ChangeLog COPYING HOW_TO_PLAY README
%{_bindir}/*
%{_mandir}/man6/*

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

perl -pi -e "s|/lib/|/%{_lib}/|" configure

%build
%configure2_5x
%make OTHERCFLAGS="%{optflags}"

%install
make PREFIX=%{buildroot}%{_prefix} MAN_PREFIX=%{buildroot}%{_datadir} install

