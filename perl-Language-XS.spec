%include	/usr/lib/rpm/macros.perl
%define	pdir	Language
%define	pnam	XS
Summary:	Language::XS perl module - write XS code on the fly
Summary(pl):	Modu� perla Language::XS - tworzenie kodu XS w locie
Name:		perl-Language-XS
Version:	0.01
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	gcc
Requires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows C & XS-code creation "on-the-fly", i.e. while your
script is running.
	
%description -l pl
Ten modu� pozwala na tworzenie kodu C i XS "w locie", czyli w trakcie
dzia�ania skryptu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
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
%{perl_sitelib}/Language/XS.pm
%{_mandir}/man3/*
