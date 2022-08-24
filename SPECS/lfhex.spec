Name:           lfhex
Version:        0.44
Release:        1%{?dist}
Summary:        Large file hex editor

License:        GPLv2
URL:            https://github.com/srtlg/lfhex
Source0:        https://github.com/srtlg/lfhex/archive/refs/tags/v%{version}.tar.gz 

BuildRequires:  qt5-qtbase-devel
BuildRequires:  bison
BuildRequires:  flex

%description
%{summary}.

Provide a fast/easy to use hex editor for viewing/modifying files which are
too large to hold in system memory.


%prep
%autosetup


%build
cd src
%qmake_qt5
sed -e '/expr\.tab\.h/ s:.(MOVE) :cp -p :g' -i 'Makefile'
%make_build


%install
install -Dm755 src/lfhex %{buildroot}%{_bindir}/lfhex


%files
%license COPYING
%{_bindir}/lfhex


%changelog
* Wed Aug 24 2022 mirko <srtlg@users.noreply.github.com>
- initial packing for Qt5
