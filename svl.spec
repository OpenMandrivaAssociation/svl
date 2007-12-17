%define realname	SVL

Name:		svl
Version:	0.29
Release:	%mkrel 5
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Decentralized version control system using Zeroconf
Source0:    http://search.cpan.org/CPAN/authors/id/A/AB/ABERGMAN/%{realname}-%{version}.tar.bz2
Patch0:     svl-0.29-makefile.diff 
Patch1:     svl-0.29-hostip_fix.diff
Patch2:     svl-0.29-better_help.diff
Patch3:     svl-0.29-help.diff
Patch4:     svl-0.29-svlserve_hostip_fix.diff 
Patch5:     svl-0.29-svlserve_beacon_detection_fix.diff
Url:		http://search.cpan.org/~abergman/SVL/
BuildRequires:	perl-SVK-Simple
BuildRequires: perl-App-CLI 
BuildRequires: perl-Catalyst 
BuildRequires: perl-Class-Accessor-Chained
BuildRequires: perl-Net-OpenDHT 
BuildRequires: perl-Net-Rendezvous 
BuildRequires: perl-Net-Rendezvous-Publish
BuildRequires: perl-Sys-HostIP 
BuildRequires: perl-Text-Tags
BuildArch:	noarch

%description
svl is a p2p versionning system built upon svk and Bonjour. It allows to
quickly organize a hacking/coding session without having to first deploy a
central cvs server or something like this.

%package -n perl-SVL
Summary:	Perl modules used by SVL
Group:		Development/Perl
# not detected by find-requires ( yet )
Requires:   perl-Text-Tags
Requires:   perl-Class-Accessor-Lvalue
Requires:   perl-Module-Pluggable
Requires:   perl-Net-OpenDHT
Requires:   perl-SVK-Simple
Requires:   subversion
%description -n perl-SVL
This package provides the base modules needed by svl.

%prep
%setup -q -n %{realname}-%{version}
%patch0 -p0 
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0
%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
# avoid conflict
mv -f $RPM_BUILD_ROOT/%_bindir/client $RPM_BUILD_ROOT/%_bindir/%{name}_client
rm -rf $RPM_BUILD_ROOT/%{perl_vendorarch}

%clean
rm -rf $RPM_BUILD_ROOT

%files -n perl-SVL
%defattr(-,root,root)
%doc  TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files
%defattr(-,root,root)
%doc txt/*
%{_bindir}/*

