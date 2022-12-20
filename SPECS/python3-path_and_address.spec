%{?!python3_pkgversion:%global python3_pkgversion 3}

%global debug_package %{nil}
%global forgeurl https://github.com/joeyespo/path-and-address
Version:        2.0.1
%forgemeta
%global srcname path_and_address

Name:           python3-path_and_address
Release:        1%{?dist}
Summary:        Functions for server CLI applications used by humans. 
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pytest

%{?python_enable_dependency_generator}

%description
%{summary}


%prep
%forgesetup


%build
%py3_build


%install
rm -rf $RPM_BUILD_ROOT
%py3_install


%check
%{__python3} -m pytest


%files -n  python%{python3_pkgversion}-%{srcname}
%license LICENSE
# For noarch packages: sitelib
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/


%changelog
* Tue Dec 20 2022 Mirko Scholz <srtlg@users.noreply.github.com>
- initial package
