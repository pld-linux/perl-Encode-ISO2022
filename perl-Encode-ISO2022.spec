#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Encode
%define		pnam	ISO2022
Summary:	Encode::ISO2022 - ISO/IEC 2022 character encoding scheme
Summary(pl.UTF-8):	Encode::ISO2022 - schemat kodowania znaków ISO/IEC 2022
Name:		perl-Encode-ISO2022
Version:	0.04
Release:	8
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Encode/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f3b0717b470961da808d871362bf1c5f
URL:		https://metacpan.org/dist/Encode-ISO2022
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Encode >= 2.10
BuildRequires:	perl-Test-Simple
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a character encoding scheme (CES) switching a set
of multiple coded character sets (CCS).

%description -l pl.UTF-8
Ten moduł udostępnia schemat kodowania znaków przełączający zbiór
wielu zestawów kodowania znaków.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Encode/ISO2022/CCS.pod
rmdir $RPM_BUILD_ROOT%{perl_vendorarch}/Encode/ISO2022

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Encode/ISO2022.pm
%{perl_vendorarch}/Encode/ISO2022JP2.pm
%{perl_vendorarch}/Encode/ISOIRSingle.pm
%{perl_vendorarch}/Encode/JISLegacy.pm
%dir %{perl_vendorarch}/auto/Encode/ISO2022
%attr(755,root,root) %{perl_vendorarch}/auto/Encode/ISO2022/ISO2022.so
%dir %{perl_vendorarch}/auto/Encode/ISOIRSingle
%attr(755,root,root) %{perl_vendorarch}/auto/Encode/ISOIRSingle/ISOIRSingle.so
%dir %{perl_vendorarch}/auto/Encode/JISLegacy
%attr(755,root,root) %{perl_vendorarch}/auto/Encode/JISLegacy/JISLegacy.so
%{_mandir}/man3/Encode::ISO2022.3pm*
%{_mandir}/man3/Encode::ISO2022::CCS.3pm*
%{_mandir}/man3/Encode::ISO2022JP2.3pm*
%{_mandir}/man3/Encode::ISOIRSingle.3pm*
%{_mandir}/man3/Encode::JISLegacy.3pm*
