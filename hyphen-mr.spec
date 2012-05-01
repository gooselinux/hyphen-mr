Name: hyphen-mr
Summary: Marathi hyphenation rules
%define upstreamid 20100204
Version: 0.%{upstreamid}
Release: 1%{?dist}
Source: http://git.savannah.gnu.org/cgit/smc.git/plain/hyphenation/hyph_mr_IN.dic
Group: Applications/Text
URL: http://wiki.smc.org.in
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv3+
BuildArch: noarch

Requires: hyphen

%description
Marathi hyphenation rules.

%prep
%setup -T -q -c
cp -p %{SOURCE0} .

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p *.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_datadir}/hyphen/*

%changelog
* Mon Feb 08 2010 Parag <pnemade AT redhat.com> - 0.20100204-1
- Resolves: rh#562095: update to 20100204

* Thu Sep 24 2009 Parag <pnemade@redhat.com> - 0.20090924-1
- update to 20090924

* Mon Aug 17 2009 Parag <pnemade@redhat.com> - 0.20090813-1
- initial version
