Summary:	Desktop session recorder
Name:		recordmydesktop
Version:	0.3.8.1
Release:	10
License:	GPLv2+
Group:		Video
URL:		http://recordmydesktop.sourceforge.net/
Source0:	http://downloads.sourceforge.net/recordmydesktop/%{name}-%{version}.tar.bz2
Patch0:		recordmydesktop-fix-libtheora1.1.patch
Patch1:		recordmydesktop-fix-xorg-headers-1.patch
Patch2:		recordmydesktop-fix-xorg-headers-2.patch
Patch3:		recordmydesktop-fix-havejack.patch
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
BuildRequires:	jackit-devel
Requires:		jackit-example-clients

%description
Simple command line tool that performs the basic tasks of capturing
and encoding desktop session. It produces files using only open
formats like Theora for video and Vorbis for audio, using the Ogg
container.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure2_5x \
    --enable-oss=no \
    --enable-jack=yes

%make

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_mandir}/man1/recordmydesktop.1*


%changelog
* Thu Oct 27 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.3.8.1-7
+ Revision: 707446
- rebuild

* Thu Jul 15 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.3.8.1-6mdv2011.0
+ Revision: 553677
- rebuild to fix seg faulting when recording, should fix mdv bug#60187

* Mon May 31 2010 Frank Kober <emuse@mandriva.org> 0.3.8.1-5mdv2010.1
+ Revision: 546783
- add configure.ac patch from debian fixing missing -ljack linking
- fixes debian bug #544699

* Mon Jan 11 2010 Emmanuel Blindauer <blindauer@mandriva.org> 0.3.8.1-4mdv2010.1
+ Revision: 489599
- Fix compilation with xorg headers
- Fix defautls values with libtheora-1.1 (patch from Fedora)

* Sat Nov 07 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.8.1-2mdv2010.1
+ Revision: 462226
- add requires on jackit-example-clients (#mdvbz55041)

* Mon Dec 15 2008 Funda Wang <fwang@mandriva.org> 0.3.8.1-1mdv2010.0
+ Revision: 314425
- update URL

* Sun Dec 14 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.8.1-1mdv2009.1
+ Revision: 314382
- update to new version 0.3.8.1

* Mon Nov 24 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.8-1mdv2009.1
+ Revision: 306387
- update to new version 0.3.8
- drop patch0, as jak support is compiled-in instead of dlopen like it was till now

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.3.7.3-4mdv2009.0
+ Revision: 260181
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.3.7.3-3mdv2009.0
+ Revision: 248324
- rebuild

* Thu Feb 21 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.7.3-1mdv2008.1
+ Revision: 173738
- new version

* Sun Jan 27 2008 Funda Wang <fwang@mandriva.org> 0.3.7.1-1mdv2008.1
+ Revision: 158532
- update to new version 0.3.7.1

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.7-1mdv2008.1
+ Revision: 131678
- new version
- do not package COPYING file
- new license policy

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Oct 25 2007 Frederic Crozat <fcrozat@mandriva.com> 0.3.6-2mdv2008.1
+ Revision: 102080
- Patch0: fix jack dynamic library dlopening
- Enable jack support

* Sat Aug 18 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.6-1mdv2008.0
+ Revision: 65431
- new version
- drop patch 0 (fixed upstream)

* Thu Aug 16 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.5.1-3mdv2008.0
+ Revision: 64046
- add upstream patch, which should have fix bug #32307 (
  John Varouhakis)

* Wed Aug 01 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.5.1-2mdv2008.0
+ Revision: 57711
- rebuild

* Wed Jul 18 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.5.1-1mdv2008.0
+ Revision: 53330
- new version

* Sun Jul 15 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.5-1mdv2008.0
+ Revision: 52180
- new version

* Fri Apr 20 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.4-1mdv2008.0
+ Revision: 16158
- new version


* Tue Mar 06 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.3.1-1mdv2007.0
+ Revision: 133876
- new version

* Wed Feb 14 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.3-1mdv2007.1
+ Revision: 120652
- new version
- fix buildrequires
- set configure options
- add docs
- set correct bits on binary file
- Import recordmydesktop

