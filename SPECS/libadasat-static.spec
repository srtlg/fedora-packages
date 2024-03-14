%define debug_package %{nil}
%define forgeurl https://github.com/AdaCore/AdaSAT
%define tag v24.0.0
%forgemeta

Name:           libadasat-static
Version:        %{fileref}
Release:        1%{?dist}
Summary:        Implementation of a DPLL-based SAT solver in Ada.

License:        Apache-2.0
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  gcc-gnat fedora-gnat-project-common
BuildRequires:  gprbuild
# Build only on architectures where GPRbuild is available:
ExclusiveArch:  %{GPRbuild_arches}

%description
%{summary}


%prep
%forgesetup


%build
gprbuild %{GPRbuild_flags} \
-P adasat.gpr -XLIBRARY_TYPE=static-pic -XBUILD_MODE=prod



%install
gprinstall %{GPRinstall_flags} \
-P adasat.gpr -XLIBRARY_TYPE=static-pic -XBUILD_MODE=prod

rm -rf %{_GNAT_project_dir}/manifests


%files
%doc README.md
%license LICENSE
%{_includedir}/%{name}/*.ads
%{_includedir}/%{name}/*.adb
%{_libdir}/%{name}/*.ali
%{_libdir}/*.a
%{_GNAT_project_dir}/*.gpr


%changelog
* Wed Mar 13 2024 Mirko <srtlg@users.noreply.github.com>
- initial package
