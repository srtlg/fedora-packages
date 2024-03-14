%define debug_package %{nil}
%define forgeurl https://github.com/AdaCore/spawn
%define tag v24.0.0
%forgemeta

Name:           spawn-ada-static
Version:        %{fileref}
Release:        1%{?dist}
Summary:        Library for simple API to spawn processes and communicate with them

License:        Apache-2.0
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  gcc-gnat fedora-gnat-project-common
BuildRequires:  make
BuildRequires:  gprbuild
# Build only on architectures where GPRbuild is available:
ExclusiveArch:  %{GPRbuild_arches}

%description
Library for simple API to spawn processes and communicate with them


%prep
%forgesetup
ed Makefile <<EOF
?gnat/tests/spawn_tests.gpr
d
/gprinstall/s/$/ -XLIBRARY_TYPE=static-pic/
wq
EOF


%build
%make_build BUILD_MODE=prod "GPRBUILD_FLAGS=%{GNAT_builder_flags} -XLIBRARY_TYPE=static-pic"



%install
%make_install PREFIX=/usr \
GPRDIR=%{_GNAT_project_dir} \
LIBDIR=%{_libdir}

rm -rf %{buildroot}%{_GNAT_project_dir}/manifests
rm -rf %{buildroot}%{_includedir}/spawn/posix_const.c

%files
%doc README.md
%license LICENSE.txt
%{_includedir}/spawn/*.ads
%{_includedir}/spawn/*.adb
%{_libdir}/spawn/*.ali
%{_libdir}/spawn/*.a
%{_GNAT_project_dir}/*.gpr

%changelog
* Wed Mar 13 2024 Mirko <srtlg@users.noreply.github.com>
- initial package
