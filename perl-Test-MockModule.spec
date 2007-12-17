%define module	Test-MockModule
%define name	perl-%{module}
%define version	0.05
%define	release	%mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Override subroutines in a module for unit testing
License:	GPL or Artistic
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildArch:	noarch
%if %{mdkversion} < 1010
Buildrequires:perl-devel
%endif
BuildRequires:  perl(CGI)

%description
Test::MockModule is a Perl module that lets you temporarily redefine
subroutines in other packages for the purposes of unit testing.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Test/*
%{_mandir}/*/*

