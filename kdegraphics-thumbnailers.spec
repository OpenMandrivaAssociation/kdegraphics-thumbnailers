Name:		kdegraphics-thumbnailers
Summary:	Postscript, PDF, DVI and RAW ThumbCreator
Version:	22.12.2
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2 LGPLv2
URL:		http://www.kde.org
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5KExiv2)
BuildRequires:	cmake(KF5KDcraw)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(QMobipocket)
Conflicts:	kdegraphics4-common < 2:4.6.90
Conflicts:	kdegraphics4-core   < 2:4.6.90
Requires:	ghostscript
Obsoletes:	%{name} < 2:19.04.0-3

%description
PostScript, PDF, DVI and RAW files ThumbCreator.

%files
%{_qt5_plugindir}/blenderthumbnail.so
%{_qt5_plugindir}/gsthumbnail.so
%{_qt5_plugindir}/rawthumbnail.so
%{_qt5_plugindir}/mobithumbnail.so
%{_datadir}/kservices5/blenderthumbnail.desktop
%{_datadir}/kservices5/gsthumbnail.desktop
%{_datadir}/kservices5/rawthumbnail.desktop
%{_datadir}/kservices5/mobithumbnail.desktop
%{_datadir}/metainfo/org.kde.kdegraphics-thumbnailers.metainfo.xml

#----------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
