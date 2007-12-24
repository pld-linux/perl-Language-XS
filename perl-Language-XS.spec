%include	/usr/lib/rpm/macros.perl
%define		pdir	Language
%define		pnam	XS
Summary:	Language::XS Perl module - write XS code on the fly
Summary(pl.UTF-8):	Moduł Perla Language::XS - tworzenie kodu XS w locie
Name:		perl-Language-XS
Version:	0.02
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f9a0c9e890de595669b1efc38c576188
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	gcc
Requires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows C & XS-code creation "on-the-fly", i.e. while your
script is running.

%description -l pl.UTF-8
Ten moduł pozwala na tworzenie kodu C i XS "w locie", czyli w trakcie
działania skryptu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Language/XS.pm
%{_mandir}/man3/*
