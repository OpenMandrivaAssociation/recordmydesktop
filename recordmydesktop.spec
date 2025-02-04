Summary:	Desktop session recorder
Name:		recordmydesktop
Version:	0.4.0
Release:	1
License:	GPLv2+
Group:		Video
URL:		https://recordmydesktop.sourceforge.net/
Source0:	http://downloads.sourceforge.net/recordmydesktop/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(ogg)
BuildRequires:  pkgconfig(popt)
BuildRequires:	pkgconfig(theora)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(xdamage)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	jackit-devel
Requires:		jackit-example-clients

%description
Simple command line tool that performs the basic tasks of capturing
and encoding desktop session. It produces files using only open
formats like Theora for video and Vorbis for audio, using the Ogg
container.

%prep
%setup -q

%build
%configure \
    --enable-oss=no \
    --enable-jack=yes

%make_build

%install
%make_install

%files
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_mandir}/man1/recordmydesktop.1*

