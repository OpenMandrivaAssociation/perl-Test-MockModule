%define upstream_name	 Test-MockModule

Name:		perl-%{upstream_name}
Version:	0.177.0
Release:	1

Summary:	Override subroutines in a module for unit testing
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/Test::MockModule
Source0:	http://search.cpan.org/CPAN/authors/id/G/GF/GFRANKS/Test-MockModule-v%{version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(SUPER)
BuildRequires:	perl(Test::Warnings)
BuildArch:	noarch

%description
Test::MockModule is a Perl module that lets you temporarily redefine
subroutines in other packages for the purposes of unit testing.

%prep
%autosetup -p1 -n %{upstream_name}-v%{version}
perl Build.PL installdirs=vendor

%build
./Build

%check
./Build test

%install
./Build install destdir="%{buildroot}"

%files
%doc Changes
%{perl_vendorlib}/Test/*
%{_mandir}/*/*
