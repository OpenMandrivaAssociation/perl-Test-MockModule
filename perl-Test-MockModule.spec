%define upstream_name	 Test-MockModule
%define upstream_version 0.13

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Override subroutines in a module for unit testing
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/G/GF/GFRANKS/Test-MockModule-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(SUPER)
BuildArch:	noarch

%description
Test::MockModule is a Perl module that lets you temporarily redefine
subroutines in other packages for the purposes of unit testing.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir="%{buildroot}"

%files
%doc Changes
%{perl_vendorlib}/Test/*
%{_mandir}/*/*
