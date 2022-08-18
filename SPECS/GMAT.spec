%{?!python3_pkgversion:%global python3_pkgversion 3}

Name:           GMAT
Version:        R2020a
Release:        2%{?dist}
Summary:        General Mission Analysis Tool: An open-source space mission analysis tool

License:        Apache
URL:            https://sourceforge.net/projects/gmat
Source0:        https://sourceforge.net/projects/gmat/files/GMAT/GMAT-%{version}/GMAT-src_and_data-%{version}.zip

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  f2c
BuildRequires:  patchelf
BuildRequires:  wxGTK3-devel < 3.1.0
BuildRequires:  xerces-c-devel
BuildRequires:  python3-devel
BuildRequires:  swig
BuildRequires:  GMAT-CSpice-devel

%description -n GMAT
%{summary}

%package -n python%{python3_pkgversion}-gmat
Summary:        %{summary}

%description -n python%{python3_pkgversion}-gmat
%{summary}

This package contains the python modules.


%prep
%setup -q
sed -i -e 's?SET(CSPICE_LIB .*?SET(CSPICE_LIB "%{_libdir}/cspice.a")?' \
       -e 's?SET(CSPICE_INCLUDE_DIR .*?SET(CSPICE_INCLUDE_DIR "%{_includedir}")?' CMakeLists.txt
sed -i -e 's?typedef int?// &?' plugins/EstimationPlugin/src/base/measurement/Ionosphere/Ionosphere.hpp


%build
%cmake . -Wno-dev \
	-D GMAT_INCLUDE_API:BOOL=ON \
	-D API_GENERATE_JAVA:BOOL=OFF \
	-D F2C_DIR:PATH=/usr/include \
	-D CSPICE_DIR:PATH=/usr
%cmake_build


%install
## cmake_install does not work, it creates a whole system image
mkdir -p %{buildroot}/opt
cp -dr --no-preserve='ownership' application  %{buildroot}/opt/%{name}-%{version}
rm %{buildroot}/opt/%{name}-%{version}/{README.txt,License.txt}
rm %{buildroot}/opt/%{name}-%{version}/bin/*.txt
rm -rf %{buildroot}/opt/%{name}-%{version}/matlab
rm -rf %{buildroot}/opt/%{name}-%{version}/debug
find %{buildroot}/opt/%{name}-%{version} -name '*.m' -delete
find %{buildroot}/opt/%{name}-%{version} -name '.git*' -delete

## put all shared objects in accepted _libdir for rpath
## https://fedoraproject.org/wiki/RPath_Packaging_Draft#Rpath_for_Internal_Libraries
patchelf --set-rpath "%{_libdir}/%{name}-%{version}" \
%{buildroot}/opt/%{name}-%{version}/bin/{GMAT-%{version},GmatConsole-%{version},libGmatBase.so.%{version},libCInterface.so.%{version},libGmatUtil.so.%{version}}
find %{buildroot}/opt/%{name}-%{version}/plugins/ -name '*.so.%{version}' -exec \
patchelf --set-rpath "%{_libdir}/%{name}-%{version}" '{}' ';' -print

mkdir -p %{buildroot}%{_libdir}/%{name}-%{version}
mv %{buildroot}/opt/%{name}-%{version}/bin/*.so.%{version} %{buildroot}%{_libdir}/%{name}-%{version}/
rm %{buildroot}/opt/%{name}-%{version}/bin/*.so
mv %{buildroot}/opt/%{name}-%{version}/plugins/*.so.%{version} %{buildroot}%{_libdir}/%{name}-%{version}/
mv %{buildroot}/opt/%{name}-%{version}/plugins/*.so %{buildroot}%{_libdir}/%{name}-%{version}/

<application/bin/gmat_startup_file.public.txt \
  sed -e 's/^.*MATLAB_MODE\s*=\s*NO_MATLAB/MATLAB_MODE = NO_MATLAB/' \
| sed -e 's/^.*WRITE_PERSONALIZATION_FILE.*/WRITE_PERSONALIZATION_FILE = OFF/' \
| sed -e "s|ROOT_PATH\s*=.*|ROOT_PATH = /opt/%{name}-%{version}|" \
| sed -e "s|#\s*PLUGIN\s*=\s*../plugins/lib|PLUGIN = ../plugins/lib|" \
| sed -e "/libMatlabInterface/ d" -e "/libFminconOptimizer/ d" \
| sed -e "/libOpenFramesInterface/ d" \
| sed -e "/plugins.proprietary/ d" \
| sed -e "s|../plugins/|%{_libdir}/%{name}-%{version}/|" \
| sed -e "s|OUTPUT_PATH\s*=.*|OUTPUT_PATH = /tmp/|" \
>%{buildroot}/opt/%{name}-%{version}/bin/gmat_startup_file.txt

<application/bin/GMAT.ini \
  sed -e "s|Sample Missions=../samples|Sample Missions=/opt/%{name}-%{version}/samples|" \
| sed -e "s|http://gmat.sourceforge.net/docs/R2020a/|/opt/%{name}-%{version}/docs/help/|" \
>%{buildroot}/opt/%{name}-%{version}/bin/GMAT.ini

## python part
rm %{buildroot}/opt/%{name}-%{version}/api/{load_gmat.py,BuildApiStartupFile.py,API_README.txt}
mkdir -p %{buildroot}/%{python3_sitearch}
cat <<EOF > %{buildroot}/%{python3_sitearch}/load_gmat.py
__all__ = ['gmat']
import gmatpy as gmat
gmat.Setup('/opt/%{name}-%{version}/bin/gmat_startup_file.txt')
EOF
mv %{buildroot}/opt/%{name}-%{version}/bin/gmatpy %{buildroot}/%{python3_sitearch}
cat <<EOF > %{buildroot}/%{python3_sitearch}/gmatpy/__init__.py
__all__ = ["gmat_py", "station_py", "navigation_py"]

from .gmat_py import *
from .station_py import *
from .navigation_py import *

fileManager = gmat_py.FileManager.Instance()
fileManager.SetBinDirectory("gmatpy/gmat_py.py", "/opt/%{name}-%{version}/bin/")
EOF
patchelf --set-rpath "%{_libdir}/%{name}-%{version}" \
	%{buildroot}/%{python3_sitearch}/gmatpy/*.so

rm -rf %{buildroot}/opt/%{name}-%{version}/{plugins,output}

%files
%defattr(-, root, root)
%license License.txt
/opt/%{name}-%{version}/{bin,data,docs,extras,samples,userincludes,userfunctions,utilities}
%{_libdir}/%{name}-%{version}

%files -n python%{python3_pkgversion}-gmat
%license License.txt
/opt/%{name}-%{version}/api
%{python3_sitearch}/gmatpy
%{python3_sitearch}/load_gmat.py
%{python3_sitearch}/__pycache__/*.pyc

%changelog
* Wed Aug 17 2022 mirko <srtlg@users.noreply.github.com>
- initial package
