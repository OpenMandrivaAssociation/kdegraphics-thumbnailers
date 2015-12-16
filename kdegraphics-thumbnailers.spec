Name:		kdegraphics-thumbnailers
Summary:	Postscript, PDF, DVI and RAW ThumbCreator
Version:	15.12.0
Release:	1
Epoch:		2
Group:		Graphical desktop/KDE
License:	GPLv2 LGPLv2
URL:		http://www.kde.org
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs-devel
BuildRequires:	pkgconfig(libkdcraw) >= 0.2.0
BuildRequires:	pkgconfig(libkexiv2) >= 0.2.0
Conflicts:	kdegraphics4-common < 2:4.6.90
Conflicts:	kdegraphics4-core   < 2:4.6.90
Requires:	ghostscript

%description
PostScript, PDF, DVI and RAW files ThumbCreator.

%files
%doc COPYING COPYING.LIB
%{_kde_libdir}/kde4/gsthumbnail.so
%{_kde_libdir}/kde4/rawthumbnail.so
%{_kde_services}/gsthumbnail.desktop
%{_kde_services}/rawthumbnail.desktop

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 -DCMAKE_MINIMUM_REQUIRED_VERSION=2.6
%make

%install
%makeinstall_std -C build
