%global debug_package %{nil}

Name:           GMAT-CSpice-devel
Version:        N00067
Release:        1%{?dist}
Summary:        A comprehensive toolkit and api to design, simulate and analyse space missions

License:        MIT 
URL:            https://naif.jpl.nasa.gov/naif/aboutspice.html
Source0:        http://naif.jpl.nasa.gov/pub/naif/toolkit//C/PC_Linux_GCC_64bit/packages/cspice.tar.Z

BuildRequires:  gcc
BuildRequires:  tcsh

%global extractdir cspice-%{version}

%description

%prep
%forgemeta
%forgesetup

%build
cd cspice
tcsh makeall.csh

%install
cd cspice
mkdir -p %{buildroot}%{_includedir}
cp include/Spice* %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_libdir}
cp lib/*.a %{buildroot}%{_libdir}


%files
%defattr(0644, root, root)
%doc cspice/doc/html/
%_includedir/*
%_libdir/*


%changelog
* Wed Aug 17 2022 Mirko <srtlg@users.noreply.github.com>
- 
