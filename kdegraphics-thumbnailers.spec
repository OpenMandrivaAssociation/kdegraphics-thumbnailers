Name:    kdegraphics-thumbnailers
Summary: Postscript PDF and DVI ThumbCreator
Version: 4.7.41
Release: 1
Epoch:   2
Group:   Graphical desktop/KDE
License: GPLv2 LGPLv2
URL:     http://www.kde.org
Source:  ftp://ftp.kde.org/pub/kde/stable/%version/src/%name-%version.tar.bz2
BuildRequires: kdelibs4-devel >= 2:%{version}
Conflicts:     kdegraphics4-common < 2:4.6.90
Conflicts:     kdegraphics4-core   < 2:4.6.90

%description
PostScript, PDF and DVI Files ThumbCreator.

%files
%doc COPYING COPYING.LIB
%_kde_libdir/kde4/gsthumbnail.so
%_kde_services/gsthumbnail.desktop

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build


