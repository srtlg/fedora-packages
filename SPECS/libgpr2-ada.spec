%define debug_package %{nil}
%define forgeurl https://github.com/AdaCore/gpr
%define tag v24.0.0
%forgemeta

Name:           libgpr2-ada-static
Version:        %{fileref}
Release:        1%{?dist}
Summary:        Implementation of a DPLL-based SAT solver in Ada.

License:        Apache-2.0
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  gcc-gnat fedora-gnat-project-common
BuildRequires:  gprbuild
BuildRequires:  xmlada-devel
BuildRequires:  gnatcoll-devel
# Build only on architectures where GPRbuild is available:
ExclusiveArch:  %{GPRbuild_arches}

%description
%{summary}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  fedora-gnat-project-common

%description devel
%{summary}

Development package



%prep
%forgesetup


%build
gprbuild \
-p -P src/kb/collect_kb.gpr
mkdir .build
cp -r src/kb/.build/kb .build

gprbuild %{GPRbuild_flags} \
-P gpr2.gpr -XLIBRARY_TYPE=relocatable -XBUILD_MODE=prod



%install
gprinstall %{GPRinstall_flags} \
-P gpr2.gpr -XLIBRARY_TYPE=relocatable -XBUILD_MODE=prod

rm -rf %{_GNAT_project_dir}/manifests


%files
%doc README.md
%license LICENSE-lib
%{_libdir}/*.so

%files devel
%{_includedir}/%{name}/*.ads
%{_includedir}/%{name}/*.adb
%{_libdir}/%{name}/*.ali
%{_GNAT_project_dir}/*.gpr


%changelog
* Wed Mar 13 2024 Mirko <srtlg@users.noreply.github.com>
- initial package
