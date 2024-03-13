%define debug_package %{nil}
%define forgeurl https://github.com/AdaCore/VSS
%define tag v24.0.0
%forgemeta

Name:           vss-ada-static
Version:        %{fileref}
Release:        1%{?dist}
Summary:        A high level string and text processing library for Ada

License:        Apache-2.0 WITH LLVM-exception
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  gcc-gnat fedora-gnat-project-common
BuildRequires:  make
BuildRequires:  gprbuild
# Build only on architectures where GPRbuild is available:
ExclusiveArch:  %{GPRbuild_arches}

%description
A high level string and text processing library.


%prep
%forgesetup


%build
%make_build BUILD_MODE=prod "GPRBUILD_FLAGS=%{GNAT_builder_flags}" build-libs-static


%install
%{__make} DESTDIR=%{?buildroot} INSTALL="%{__install} -p" \
PREFIX=/usr \
GPRDIR=%{_GNAT_project_dir} \
LIBDIR=%{_libdir} \
install-libs-static

rm -rf %{buildroot}%{_GNAT_project_dir}/manifests


%files
%doc README.md
%license LICENSE.txt
%{_includedir}/vss/
%{_libdir}/vss/static/*.ali
%{_libdir}/vss/static/*.a
%{_GNAT_project_dir}/*.gpr

%changelog
* Wed Mar 13 2024 Mirko <srtlg@users.noreply.github.com>
- initial package
