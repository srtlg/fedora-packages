%global debug_package %{nil}
%global forgeurl https://github.com/open-simh/simh
%global commit   e444c674f6ec57a570dd42d07d03dd56a30cc9ff
%forgemeta

Name:           open-simh
Version:        3.12
Release:        1%{?dist}
Summary:        The Open SIMH simulators package 

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libpcap-devel
BuildRequires:  libreoffice-writer

Conflicts:      simh

%description


%prep
%forgesetup


%build
%make_build LTO=1



%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
for i in `ls BIN/ | grep -v buildtools`; do
	install -p -m 755 BIN/$i $RPM_BUILD_ROOT%{_bindir}/simh-$i
done

soffice                                                              \
  --headless                                                         \
  "-env:UserInstallation=file:///tmp/LibreOffice_Conversion_${USER}" \
  --convert-to pdf:writer_pdf_Export                                 \
  --outdir doc                                                       \
  doc/*.doc           

%files
%license LICENSE.txt
%doc doc/*.pdf
%doc ALTAIR/altair.txt NOVA/eclipse.txt 0readme_39.txt 0readme_ethernet.txt
%doc I7094/i7094_bug_history.txt Interdata/id_diag.txt
%doc PDP1/pdp1_diag.txt PDP10/pdp10_bug_history.txt PDP18B/pdp18b_diag.txt
%doc S3/haltguide.txt S3/readme_s3.txt S3/system3.txt SDS/sds_diag.txt
%doc VAX/vax780_bug_history.txt
%{_bindir}/*


%changelog
* Tue Dec 20 2022 Mirko Scholz <srtlg@users.noreply.github.com>
- initial build
