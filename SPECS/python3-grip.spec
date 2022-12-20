%{?!python3_pkgversion:%global python3_pkgversion 3}

%global debug_package %{nil}
%global forgeurl https://github.com/joeyespo/grip
Version:        4.6.1
%forgemeta
%global srcname grip

Name:           python3-grip
Release:        1%{?dist}
Summary:        Preview GitHub README.md files locally before committing them. 
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-werkzeug
BuildRequires:  python%{python3_pkgversion}-flask
BuildRequires:  python%{python3_pkgversion}-responses

BuildRequires:  python%{python3_pkgversion}-path_and_address

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


#%check
## use what your upstream is using
#%{__python3} -m pytest


%files -n  python%{python3_pkgversion}-%{srcname}
%license LICENSE
%{_bindir}/grip
# For noarch packages: sitelib
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/


%changelog
* Tue Dec 20 2022 Mirko Scholz <srtlg@users.noreply.github.com>
- initial package
