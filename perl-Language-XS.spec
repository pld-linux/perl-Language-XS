%include	/usr/lib/rpm/macros.perl
%define	pdir	Language
%define	pnam	XS
Summary:	Language::XS Perl module - write XS code on the fly
Summary(pl):	Modu³ Perla Language::XS - tworzenie kodu XS w locie
Name:		perl-Language-XS
Version:	0.01
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9b1aefc477bb425a101bcab054c2ad34
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	gcc
Requires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows C & XS-code creation "on-the-fly", i.e. while your
script is running.

%description -l pl
Ten modu³ pozwala na tworzenie kodu C i XS "w locie", czyli w trakcie
dzia³ania skryptu.

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
