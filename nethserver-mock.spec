Name:           nethserver-mock
Version: 1.6.3
Release: 1%{?dist}
Summary:        RPM build automation scripts for NethServer packages
BuildArch:	noarch

License:        GPLv3
URL:            http://www.nethserver.org
Source0:        %{name}-%{version}.tar.gz

Requires: mock => 1.1.41
Requires: rpmdevtools >= 7.5
Requires: git >= 1.7.1
Requires: bash
Requires: coreutils
Requires: expect
Requires: python3-requests
Requires: yum-utils

%description
Provides build automation scripts for NethServer packages

%prep
%setup -q

%build


%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}/%{_bindir} %{buildroot}/%{_sysconfdir}/mock
install -vp src/bin/* %{buildroot}/%{_bindir}
install -vp src/mock/* %{buildroot}/%{_sysconfdir}/mock

%files
%defattr(-,root,root,-)
%{_bindir}/make-rpms
%{_bindir}/make-srpm
%{_bindir}/sign-rpms
%{_bindir}/prep-sources
%{_bindir}/release-tag
%{_bindir}/upload-rpms
%{_bindir}/git-archive-all.sh
%{_bindir}/issue-refs
%{_bindir}/push-local-repo
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/mock/nethserver-6-x86_64.cfg
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/mock/nethserver-7-x86_64.cfg
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/mock/nethserver-7-armhfp.cfg
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/mock/nethserver-7-aarch64.cfg
%doc COPYING

%changelog
* Wed May 06 2020 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.6.3-1
- Initial support for el8 as development environment - NethServer/dev#6152

* Tue Apr 21 2020 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.6.2-1
- Fix build onf Fedora 31

* Thu Feb 06 2020 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.6.1-1
- Backport Python3 fixes from nethserver-makerpms
- Fix src RPM name capturing (#12)
- Remove deprecated 'yum localinstall' command. (#11)

* Thu Dec 20 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.6.0-1
- ARM arch 7.6.1810 beta release - NethServer/dev#5675

* Mon Feb 05 2018 Davide Principi <davide.principi@nethesis.it> - 1.5.0-1
- nethserver-mock: release-tag improvements - NethServer/dev#5418

* Thu Jan 25 2018 Davide Principi <davide.principi@nethesis.it> - 1.4.2-1
- Fix changelog date localization

* Mon Dec 04 2017 Davide Principi <davide.principi@nethesis.it> - 1.4.1-1
- Add yum-utils dependency -- NethServer/dev#5393

* Thu Nov 30 2017 Davide Principi <davide.principi@nethesis.it> - 1.4.0-1
- Fixed upload-rpms for Travis builds
- Added push-local-repo command
- Fix compatibility issue for mock 1.14

* Thu Sep 29 2016 Davide Principi <davide.principi@nethesis.it> - 1.3.2-1
- Fix initial whitespace on RPM changelog

* Tue Jul 12 2016 Davide Principi <davide.principi@nethesis.it> - 1.3.1-1
- Set ns7 as default target -- NethServer/nethserver-mock#3 

* Mon Jun 06 2016 Davide Principi <davide.principi@nethesis.it> - 1.3.0-1
- NethServer 6 configuration
- Fix RPM dependencies on el7 - Enhancement #3145 [NethServer]

* Fri Dec 04 2015 Davide Principi <davide.principi@nethesis.it> - 1.2.1-1
- Add documentation - Bug #2 [NethServer]

* Fri Aug 28 2015 Davide Principi <davide.principi@nethesis.it> - 1.2.0-1
- Mock configuration for NethServer 6.7 - Feature #3247 [NethServer]

* Tue May 19 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.2-1
- Support git submodules in package creation - Enhancement #3118 [NethServer]

* Fri Apr 03 2015 Davide Principi <davide.principi@nethesis.it> - 1.1.1-1
- Ignore git repo if source0 starts with http://

* Thu Mar 05 2015 Davide Principi <davide.principi@nethesis.it> - 1.1.0-1
- nethserver-devbox replacements - Feature #3009 [NethServer]
- build-rpm error on Fedora 20 - Bug #2879 [NethServer]
- Devbox: missing rpmspec command - Bug #2770 [NethServer]
- Changed URLs pointing to mirrorlist.nethserver.org
- YUM groups from nethserver-updates

* Thu Feb 12 2015 Davide Principi <davide.principi@nethesis.it> - 0.0.3-1
- Insert development changelog from `git log` output

* Tue Jan 27 2015 Davide Principi <davide.principi@nethesis.it> - 0.0.2-1
- Added NethServer 6.6 configuration

* Tue Dec 23 2014 Davide Principi <davide.principi@nethesis.it> - 0.0.1-1
- Initial version
