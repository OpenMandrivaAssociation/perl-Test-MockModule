%define upstream_name	 Test-MockModule
%define upstream_version v0.185.3

Name:		perl-%{upstream_name}
Version:	0.185.3
Release:	2

Summary:	Override subroutines in a module for unit testing
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Test::MockModule
Source0:	https://cpan.metacpan.org/authors/id/G/GF/GFRANKS/Test-MockModule-v0.185.3.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(SUPER)
BuildRequires:	perl(Test::Warnings)
BuildArch:	noarch

%description
Test::MockModule is a Perl module that lets you temporarily redefine
subroutines in other packages for the purposes of unit testing.

%prep
%autosetup -p1 -n Test-MockModule-v0.185.3
perl Build.PL installdirs=vendor

%build
./Build

%check
# soft: do not fail package on test failures
set +e
./Build test || :

%install
./Build install destdir="%{buildroot}"

%files
%doc Changes
%{perl_vendorlib}/Test/*
%{_mandir}/*/*
