Name:		kdegraphics-thumbnailers
Summary:	Postscript, PDF, DVI and RAW ThumbCreator
Version:	23.08.4
Release:	3
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

%description
PostScript, PDF, DVI and RAW files ThumbCreator.

%files
%{_qt5_plugindir}/kf5/thumbcreator/blenderthumbnail.so
%{_qt5_plugindir}/kf5/thumbcreator/gsthumbnail.so
%{_qt5_plugindir}/kf5/thumbcreator/rawthumbnail.so
%{_qt5_plugindir}/kf5/thumbcreator/mobithumbnail.so
%{_datadir}/metainfo/org.kde.kdegraphics-thumbnailers.metainfo.xml

#----------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
