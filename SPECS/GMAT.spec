Name:           GMAT
Version:        R2020a
Release:        1%{?dist}
Summary:        General Mission Analysis Tool: An open-source space mission analysis tool

License:        Apache
URL:            https://sourceforge.net/projects/gmat
Source0:        https://sourceforge.net/projects/gmat/files/GMAT/GMAT-%{version}/GMAT-src_and_data-%{version}.zip

BuildRequires:  cmake
BuildRequires:  f2c
BuildRequires:  patchelf
BuildRequires:  wxGTK3-devel
BuildRequires:  xerces-c-devel
BuildRequires:  python3-devel
BuildRequires:  GMAT-CSpice-devel

%description


%prep
%setup -q
sed -i -e 's?SET(CSPICE_LIB .*?SET(CSPICE_LIB "%{_libdir}/cspice.a")?' \
       -e 's?SET(CSPICE_INCLUDE_DIR .*?SET(CSPICE_INCLUDE_DIR "%{_includedir}")?' CMakeLists.txt
sed -i -e 's?typedef int?// &?' plugins/EstimationPlugin/src/base/measurement/Ionosphere/Ionosphere.hpp


%build
%cmake . -Wno-dev \
	-D F2C_DIR:PATH=/usr/include \
	-D CSPICE_DIR:PATH=/usr
%cmake_build


%install
mkdir -p %{buildroot}/opt
cp -dr --no-preserve='ownership' application  %{buildroot}/opt/%{name}-%{version}
rm %{buildroot}/opt/%{name}-%{version}/{README.txt,License.txt}
rm %{buildroot}/opt/%{name}-%{version}/bin/*.txt
rm -rf %{buildroot}/opt/%{name}-%{version}/matlab
find %{buildroot}/opt/%{name}-%{version} -name '*.m' -delete
find %{buildroot}/opt/%{name}-%{version} -name '.git*' -delete

# put all shared objects in accepted _libdir for rpath
# https://fedoraproject.org/wiki/RPath_Packaging_Draft#Rpath_for_Internal_Libraries
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

%files
%defattr(-, root, root)
%license License.txt
/opt/%{name}-%{version}
%{_libdir}/%{name}-%{version}

%changelog
* Wed Aug 17 2022 mirko <srtlg@users.noreply.github.com>
- 
