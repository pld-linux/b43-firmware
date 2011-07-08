Summary:	Firmware for the Broadcom 43xx wireless chipsets
Summary(hu.UTF-8):	Broadcom 43xx wireless chipekhez firmware
Summary(pl.UTF-8):	Formware dla układów bezprzewodowych Broadcom 43xx
Name:		b43-firmware
Version:	5.10.56.27.3
Release:	1
License:	Copyrighted by Broadcom Corporation
Group:		Base/Kernel
Source0:	http://mirror2.openwrt.org/sources/broadcom-wl-%{version}_mipsel.tar.bz2
# NoSource0-md5:	3363e3a6b3d9d73c49dea870c7834eac	
NoSource:	0
URL:		http://linuxwireless.org/en/users/Drivers/b43#devicefirmware
BuildRequires:	b43-fwcutter >= 014
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the firmware for the Broadcom 43xx chipsets
using b43 driver.

%description -l hu.UTF-8
Ez a csomag tartalmazza a firmware-t azokhoz a Broadcom 43xx
chipekhez, amelyek a b43 meghajtót használják.

%description -l pl.UTF-8
Ten pakiet zawiera firmware dla układów bezprzewodowych Broadcom 43xx
wykorzystujących sterownik b43.

%prep
%setup -q -n broadcom-wl-%{version}

%build
install -d fw
%{_bindir}/b43-fwcutter -w fw driver/wl_apsta/wl_prebuilt.o

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware

cp -a fw/* $RPM_BUILD_ROOT/lib/firmware

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/lib/firmware/b43
