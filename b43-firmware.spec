#
Summary:	Firmware for the Broadcom wireless chipsets
Name:		b43-firmware
Version:	4
Release:	1
License:	Copyrighted by Broadcom Corporation
Group:		Base/Kernel
NoSource0:	http://downloads.openwrt.org/sources/broadcom-wl-4.80.53.0.tar.bz2
# NoSource0-md5:	a7d8dde3ce474c361143b83e1d9890b1
URL:		http://linuxwireless.org/en/users/Drivers/b43#devicefirmware
BuildRequires:	b43-fwcutter
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the firmware for the b43 driver.

%prep
%setup -q -c
tar xf %{SOURCE0}

%build
install -d fw
%{_bindir}/b43-fwcutter -w fw *//*/*.o

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware

cp -a fw/* $RPM_BUILD_ROOT/lib/firmware

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/lib/firmware/b43
