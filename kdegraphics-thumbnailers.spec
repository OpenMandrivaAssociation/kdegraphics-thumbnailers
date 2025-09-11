#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
Name:		kdegraphics-thumbnailers
Summary:	Postscript, PDF, DVI and RAW ThumbCreator
Version:	25.08.1
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	GPLv2 LGPLv2
URL:		https://www.kde.org
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%if 0%{?git:1}
Source0:	https://invent.kde.org/graphics/kdegraphics-thumbnailers/-/archive/%{gitbranch}/kdegraphics-thumbnailers-%{gitbranchd}.tar.bz2#/kdegraphics-thumbnailers-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kdegraphics-thumbnailers-%{version}.tar.xz
%endif
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KExiv2Qt6)
BuildRequires:	cmake(KDcrawQt6)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(QMobipocket6)
Requires:	ghostscript

%rename plasma6-kdegraphics-thumbnailers

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildOption:	-DQT_MAJOR_VERSION=6

%description
PostScript, PDF, DVI and RAW files ThumbCreator.

%files
%{_datadir}/metainfo/org.kde.kdegraphics-thumbnailers.metainfo.xml
%{_qtdir}/plugins/kf6/thumbcreator/blenderthumbnail.so
%{_qtdir}/plugins/kf6/thumbcreator/gsthumbnail.so
%{_qtdir}/plugins/kf6/thumbcreator/mobithumbnail.so
%{_qtdir}/plugins/kf6/thumbcreator/rawthumbnail.so
