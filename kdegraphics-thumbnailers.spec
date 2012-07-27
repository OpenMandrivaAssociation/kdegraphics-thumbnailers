Name:		kdegraphics-thumbnailers
Summary:	Postscript, PDF, DVI and RAW ThumbCreator
Version:	4.8.97
Release:	1
Epoch:		2
Group:		Graphical desktop/KDE
License:	GPLv2 LGPLv2
URL:		http://www.kde.org
Source:		ftp://ftp.kde.org/pub/kde/unstable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(libkdcraw) >= 0.2.0
BuildRequires:	pkgconfig(libkexiv2) >= 0.2.0
Conflicts:	kdegraphics4-common < 2:4.6.90
Conflicts:	kdegraphics4-core   < 2:4.6.90

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
%cmake_kde4
%make

%install
%makeinstall_std -C build

