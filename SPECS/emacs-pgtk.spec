Name:           emacs-pgtk
Version:        29.2
Release:        1%{?dist}
Summary:        GNU Emacs text editor with Wayland support

License:        GPL-3.0-or-later AND CC0-1.0
URL:            http://www.gnu.org/software/emacs/
Source0:        https://ftp.gnu.org/gnu/emacs/emacs-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  glibc-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  libgccjit-devel
BuildRequires:  jansson-devel
BuildRequires:  gnutls-devel
BuildRequires:  libtree-sitter-devel
BuildRequires:  ncurses-devel
BuildRequires:  libotf-devel
BuildRequires:  libwebp-devel
BuildRequires:  sqlite-devel
BuildRequires:  librsvg2-devel
BuildRequires:  dbus-devel
BuildRequires:  texinfo
BuildRequires:  gzip

Requires:       info
Requires:       dejavu-sans-mono-fonts
Requires:       libgccjit

%description
Emacs is a powerful, customizable, self-documenting, modeless text
editor. Emacs contains special code editing features, a scripting
language (elisp), and the capability to read mail, news, and more
without leaving the editor.

This package provides an emacs binary with support for Wayland.


%prep
%setup -q -n emacs-%{version}


%build
LDFLAGS=-Wl,-z,relro;  export LDFLAGS;
%configure \
--enable-locallisppath=/usr/share/emacs/site-lisp \
--without-sound \
--with-tree-sitter \
--with-cairo \
--with-dbus \
--disable-build-details \
--with-harfbuzz \
--with-libsystemd \
--with-modules \
--with-json \
--with-native-compilation=aot \
--with-webp \
--with-rsvg \
--with-mailutils \
--without-lcms2 \
--with-pgtk

%make_build bootstrap NATIVE_FULL_AOT=1


%install
%make_install

rm -rf %{buildroot}/opt
rm %{buildroot}%{_bindir}/{ctags,ebrowse,emacs,emacsclient,etags}
mv %{buildroot}%{_bindir}/emacs-%{version} %{buildroot}%{_bindir}/emacs-%{version}-pgtk
rm -rf %{buildroot}%{_includedir}
rm -rf %{buildroot}%{_libdir}/systemd
rm -rf %{buildroot}%{_datadir}/applications
rm -rf %{buildroot}%{_datadir}/icons
rm -rf %{buildroot}%{_datadir}/info
rm -rf %{buildroot}%{_datadir}/man
rm -rf %{buildroot}%{_datadir}/metainfo
rm -rf %{buildroot}%{_datadir}/glib-2.0
rm -rf %{buildroot}%{_datadir}/emacs/site-lisp


%files
%license etc/COPYING
%doc etc/README
%{_bindir}/emacs-%{version}-pgtk
%{_datadir}/emacs/%{version}
%{_libdir}/emacs/%{version}
/usr/libexec/emacs/%{version}

%changelog
* Mon Mar 11 2024 mirko <srtlg@users.noreply.github.com>
- intial package
