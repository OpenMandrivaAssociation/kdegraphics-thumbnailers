Name:		plasma6-kdegraphics-thumbnailers
Summary:	Postscript, PDF, DVI and RAW ThumbCreator
Version:	24.01.85
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2 LGPLv2
URL:		http://www.kde.org
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kdegraphics-thumbnailers-%{version}.tar.xz
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6KExiv2)
BuildRequires:	cmake(KF6KDcraw)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(QMobipocket)
Conflicts:	kdegraphics4-common < 2:4.6.90
Conflicts:	kdegraphics4-core   < 2:4.6.90
Requires:	ghostscript

%description
PostScript, PDF, DVI and RAW files ThumbCreator.

%files
%{_qt6_plugindir}/kf6/thumbcreator/blenderthumbnail.so
%{_qt6_plugindir}/kf6/thumbcreator/gsthumbnail.so
%{_qt6_plugindir}/kf6/thumbcreator/rawthumbnail.so
%{_qt6_plugindir}/kf6/thumbcreator/mobithumbnail.so
%{_datadir}/metainfo/org.kde.kdegraphics-thumbnailers.metainfo.xml

#----------------------------------------------------------------------

%prep
%autosetup -p1
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
