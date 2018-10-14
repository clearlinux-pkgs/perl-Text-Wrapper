#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Text-Wrapper
Version  : 1.05
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/C/CJ/CJM/Text-Wrapper-1.05.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CJ/CJM/Text-Wrapper-1.05.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtext-wrapper-perl/libtext-wrapper-perl_1.05-2.debian.tar.xz
Summary  : 'Word wrap text by breaking long lines'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Text-Wrapper-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Text::Wrapper version 1.05, released January 18, 2014
This module provides simple word wrapping.  It breaks long lines,
but does not alter spacing or remove existing line breaks.  If
you're looking for more sophisticated text formatting, try the
Text::Format module.

%package dev
Summary: dev components for the perl-Text-Wrapper package.
Group: Development
Provides: perl-Text-Wrapper-devel = %{version}-%{release}

%description dev
dev components for the perl-Text-Wrapper package.


%package license
Summary: license components for the perl-Text-Wrapper package.
Group: Default

%description license
license components for the perl-Text-Wrapper package.


%prep
%setup -q -n Text-Wrapper-1.05
cd ..
%setup -q -T -D -n Text-Wrapper-1.05 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Text-Wrapper-1.05/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Text-Wrapper
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Text-Wrapper/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Text-Wrapper/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.26.1/Text/Wrapper.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Text::Wrapper.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Text-Wrapper/LICENSE
/usr/share/package-licenses/perl-Text-Wrapper/deblicense_copyright
