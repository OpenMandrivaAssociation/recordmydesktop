Summary:	Desktop session recorder
Name:		recordmydesktop
Version:	0.3.8.1
Release:	%mkrel 2
License:	GPLv2+
Group:		Video
URL:		http://recordmydesktop.sourceforge.net/
Source0:	http://downloads.sourceforge.net/recordmydesktop/%{name}-%{version}.tar.bz2
BuildRequires:	libalsa-devel
BuildRequires:	libogg-devel
BuildRequires:	libtheora-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libice-devel
BuildRequires:	libsm-devel
BuildRequires:	libxdamage-devel
BuildRequires:	libxext-devel
BuildRequires:	libxfixes-devel
BuildRequires:	zlib-devel
BuildRequires:  jackit-devel
Requires:	jackit-example-clients
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Simple command line tool that performs the basic tasks of capturing
and encoding desktop session. It produces files using only open
formats like Theora for video and Vorbis for audio, using the Ogg
container.

%prep
%setup -q

%build
%configure2_5x \
	--enable-oss=no \
	--enable-jack=yes

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_mandir}/man1/recordmydesktop.1*
