Summary: varnish-agent
Name: varnish-agent
Version: 2.1
Release: 1%{?dist}
License: BSD
Group: System Environment/Daemons
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: varnish > 3.0

%description
Varnish Agent software that runs on all caches managed by Varnish
Administration Console (VAC).

%prep
%setup

%build
./configure --prefix=/usr
make

%check
make check || ( tail -n +1 tests/*.log ; false )

%install
make install DESTDIR=%{buildroot}
#install -D redhat/varnish-agent.sysconfig   %{buildroot}/etc/sysconfig/varnish-agent
#install -D redhat/varnish-agent.initrc      %{buildroot}/etc/init.d/varnish-agent

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/**
#%config(noreplace) /etc/init.d/varnish-agent
#%config(noreplace) /etc/sysconfig/varnish-agent

#%post
#/sbin/chkconfig --add varnish-agent

#%preun
#if [ $1 -lt 1 ]; then
#/sbin/service varnish-agent stop > /dev/null 2>&1
#/sbin/chkconfig --del varnish-agent
#fi

%changelog
* Wed Jan 30 2013 Kristian Lyngstol <kristian@bohemians.org> - 2.1-1
- 2.1 dev version
* Fri Jan 18 2013 Lasse Karstensen <lkarsten@varnish-software.com> - 2.0-1
- Initial version.
