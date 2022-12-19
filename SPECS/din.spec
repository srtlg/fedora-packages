Name:           din
Version:        55
Release:        1%{?dist}
Summary:        DIN is noise: A sound synthesizer and musical instrument.

License:        GPLv2
URL:            https://dinisnoise.org/
Source0:        https://archive.org/download/dinisnoise_source_code/din-%{version}.tar.gz
Patch0:         din-54-devendor_rtaudio_rtmidi.patch

BuildRequires:  SDL-devel
BuildRequires:  rtmidi-devel
BuildRequires:  rtaudio-devel
BuildRequires:  tcl-devel
BuildRequires:  boost-devel
BuildRequires:  pkgconfig
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++

# uses work by AUR https://github.com/archlinux/svntogit-community/blob/packages/din/trunk/PKGBUILD

%description
A sound syntesizer of a 3rd kind.


%prep
%autosetup -p1
rm -v src/{RtAudio,RtMidi}.*
autoreconf -fiv


%build
export CXXFLAGS+=" -D__UNIX_JACK__ $(pkg-config --cflags rtaudio rtmidi)"
export CFLAGS+=" -D__UNIX_JACK__ $(pkg-config --cflags rtaudio rtmidi)"
export LIBS+=" $(pkg-config --libs rtaudio rtmidi)"
%configure

%make_build


%install
%make_install


%files
%license COPYING
%doc README NEWS AUTHORS
%_bindir/din
%_datadir/applications/din.desktop
%_datadir/icons/hicolor/scalable/apps/din.svg
%_datadir/pixmaps/din.png
%_datadir/din

%changelog
* Mon Dec 19 2022 srtlg <srtlg@users.noreply.github.com>
- initial build
