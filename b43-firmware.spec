Summary:	Firmware for the Broadcom 43xx wireless chipsets
Summary(hu.UTF-8):	Broadcom 43xx wireless chipekhez firmware
Summary(pl.UTF-8):	Formware dla układów bezprzewodowych Broadcom 43xx
Name:		b43-firmware
Version:	6.30.163.46
Release:	1
License:	Copyrighted by Broadcom Corporation
Group:		Base/Kernel
Source0:	http://www.lwfinger.com/b43-firmware/broadcom-wl-%{version}.tar.bz2
# NoSource0-md5:	
NoSource:	0
URL:		http://wireless.kernel.org/en/users/Drivers/b43#devicefirmware
BuildRequires:	b43-fwcutter >= 018
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
%setup -q -c

%build
install -d fw
b43-fwcutter -w fw broadcom-wl-%{version}.wl_apsta.o

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware
cp -a fw/* $RPM_BUILD_ROOT/lib/firmware

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/lib/firmware/b43
