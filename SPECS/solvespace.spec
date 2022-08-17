%global debug_package %{nil}

Name: 	 solvespace
Version: 3.1
Release: 2%{?dist}

Summary: SolveSpace parametric 2d/3d CAD
License: GPLv3
Group: 	 Graphics
Url: 	 http://solvespace.com/

Source0: https://github.com/solvespace/solvespace/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires: libappstream-glib
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: zlib-devel
BuildRequires: libpng-devel
BuildRequires: cairo-devel
BuildRequires: freetype-devel
BuildRequires: json-c-devel
BuildRequires: fontconfig-devel
BuildRequires: gtkmm30-devel
BuildRequires: pangomm-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: libspnav-devel
BuildRequires: eigen3-devel

%description
SolveSpace is a parametric 2d/3d CAD program. Applications include:
* modeling 3d parts - draw with extrudes, revolves, and Boolean
  (union / difference) operations;
* modeling 2d parts - draw the part as a single section, and export DXF,
  PDF, SVG; use 3d assembly to verify fit;
* 3d-printed parts - export the STL or other triangle mesh expected by
  most 3d printers;
* preparing CAM data - export 2d vector art for a waterjet machine or
  laser cutter; or generate STEP or STL, for import into third-party
  CAM software for machining;
* mechanism design - use the constraint solver to simulate planar or
  spatial linkages, with pin, ball, or slide joints;
* plane and solid geometry - replace hand-solved trigonometry and
  spreadsheets with a live dimensioned drawing.

%package -n libslvs
Summary: SolveSpace geometric kernel
Group: System/Libraries

%description -n libslvs
SolveSpace is a parametric 2d/3d CAD. libslvs contains the geometric
kernel of SolveSpace, built as a library.

%package -n libslvs-devel
Summary: SolveSpace geometric kernel (development files)
Group: Development/C
Requires: libslvs

%description -n libslvs-devel
SolveSpace is a parametric 2d/3d CAD. libslvs contains the geometric
kernel of SolveSpace, built as a library.

This package includes development files for libslvs.

%prep
%setup -q
sed \
-e "s/include(GetGitCommitHash)/#/" \
-e "s/# set(GIT_COMMIT_HASH/set(GIT_COMMIT_HASH/" -i CMakeLists.txt

%build
%cmake . -Wno-dev
%cmake_build

%install
%cmake_install
#%find_lang %name

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%{__cmake_builddir}/bin/solvespace-testsuite

#%files -f %name.lang
%files -n solvespace
%doc COPYING.txt README.md wishlist.txt
%_bindir/%name
%_bindir/%name-cli
%_datadir/icons/hicolor/*/apps/%name.png
%_datadir/icons/hicolor/*/apps/%name.svg
%_datadir/icons/hicolor/*/mimetypes/application-x-solvespace.png
%_datadir/icons/hicolor/*/mimetypes/application-x-solvespace.svg
%_datadir/applications/%name.desktop
%_datadir/mime/packages/solvespace-slvs.xml
%_metainfodir/com.solvespace.SolveSpace.metainfo.xml
%_datadir/%name

%files -n libslvs
%_libdir/libslvs.so.*

%files -n libslvs-devel
%_libdir/libslvs.so
%_includedir/slvs.h

%changelog
* Tue Aug 9 2022 Mirko <srtlg@users.noreply.github.com> 3.1-1
- Upgrade to 3.1

* Sun Apr 18 2021 Andrey Cherepanov <cas@altlinux.org> 1:3.0-alt1
- New version.
- Build with GTK 3.

* Fri Apr 07 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:2.3-alt1.qa1
- Fixed build with glibc >= 2.25.

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 1:2.3-alt1
- New version

* Wed Oct 05 2016 Andrey Cherepanov <cas@altlinux.org> 1:2.1-alt2
- Use explicit commit hash

* Tue Jul 12 2016 Andrey Cherepanov <cas@altlinux.org> 1:2.1-alt1
- New version

* Tue Feb 16 2016 Andrey Cherepanov <cas@altlinux.org> 20160214-alt1
- Inital build in Sisyphus

