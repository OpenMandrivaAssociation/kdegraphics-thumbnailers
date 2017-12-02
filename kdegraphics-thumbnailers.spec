Name:		kdegraphics-thumbnailers
Summary:	Postscript, PDF, DVI and RAW ThumbCreator
Version:	17.11.90
Release:	1
Epoch:		2
Group:		Graphical desktop/KDE
License:	GPLv2 LGPLv2
URL:		http://www.kde.org
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5KExiv2)
BuildRequires:	cmake(KF5KDcraw)
Conflicts:	kdegraphics4-common < 2:4.6.90
Conflicts:	kdegraphics4-core   < 2:4.6.90
Requires:	ghostscript

%description
PostScript, PDF, DVI and RAW files ThumbCreator.

%files
%{_qt5_plugindir}/gsthumbnail.so
%{_qt5_plugindir}/rawthumbnail.so
%{_datadir}/kservices5/gsthumbnail.desktop
%{_datadir}/kservices5/rawthumbnail.desktop

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
