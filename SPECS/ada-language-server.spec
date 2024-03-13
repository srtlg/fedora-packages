%define debug_package %{nil}
%define forgeurl https://github.com/AdaCore/ada_language_server
%define tag 24.0.4
%forgemeta

Name:           ada-language-server
Version:        %{tag}
Release:        1%{?dist}
Summary:        Server implementing the Microsoft Language Protocol for Ada and SPARK

License:        GPLv3
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  gcc-gnat fedora-gnat-project-common
BuildRequires:  make
BuildRequires:  gprbuild
BuildRequires:  vss-ada-static
BuildRequires:  spawn-ada-static
BuildRequires:  gnatcoll-devel
# Build only on architectures where GPRbuild is available:
ExclusiveArch:  %{GPRbuild_arches}

%description
Server implementing the Microsoft Language Protocol for Ada and SPARK

%prep
%forgesetup
%setup -q -n %{topdir}


%build
%make_build LIBRARY_TYPE=static BUILD_MODE=prod "GPRBUILD_FLAGS=%{GNAT_builder_flags}"


%install
%make_install PREFIX=/usr \
GPRDIR=%{_GNAT_project_dir} \
LIBDIR=%{_libdir}

rm -rf %{buildroot}%{_GNAT_project_dir}/manifests


%files
%doc README.md
%license LICENSE
%{_includedir}/vss/
%{_libdir}/vss/*.ali
%{_libdir}/vss/*.a
%{_GNAT_project_dir}/*.gpr

%changelog
* Wed Mar 13 2024 Mirko <srtlg@users.noreply.github.com>
- initial package
