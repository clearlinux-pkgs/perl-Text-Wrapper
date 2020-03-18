#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Text-Wrapper
Version  : 1.05
Release  : 11
URL      : https://cpan.metacpan.org/authors/id/C/CJ/CJM/Text-Wrapper-1.05.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CJ/CJM/Text-Wrapper-1.05.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtext-wrapper-perl/libtext-wrapper-perl_1.05-2.debian.tar.xz
Summary  : 'Word wrap text by breaking long lines'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Text-Wrapper-license = %{version}-%{release}
Requires: perl-Text-Wrapper-perl = %{version}-%{release}
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
Requires: perl-Text-Wrapper = %{version}-%{release}

%description dev
dev components for the perl-Text-Wrapper package.


%package license
Summary: license components for the perl-Text-Wrapper package.
Group: Default

%description license
license components for the perl-Text-Wrapper package.


%package perl
Summary: perl components for the perl-Text-Wrapper package.
Group: Default
Requires: perl-Text-Wrapper = %{version}-%{release}

%description perl
perl components for the perl-Text-Wrapper package.


%prep
%setup -q -n Text-Wrapper-1.05
cd %{_builddir}
tar xf %{_sourcedir}/libtext-wrapper-perl_1.05-2.debian.tar.xz
cd %{_builddir}/Text-Wrapper-1.05
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Text-Wrapper-1.05/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Text-Wrapper
cp %{_builddir}/Text-Wrapper-1.05/LICENSE %{buildroot}/usr/share/package-licenses/perl-Text-Wrapper/ca1f55baa6dfa1bdd7932a90abbe4a62c01eec67
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Text-Wrapper/aefd1f59002622cdbf887f58f17c85a5562ed2fa
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Text::Wrapper.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Text-Wrapper/aefd1f59002622cdbf887f58f17c85a5562ed2fa
/usr/share/package-licenses/perl-Text-Wrapper/ca1f55baa6dfa1bdd7932a90abbe4a62c01eec67

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.2/Text/Wrapper.pm
