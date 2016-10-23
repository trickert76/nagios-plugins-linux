Name: nagios-plugins-linux
Version: 19
Release: 1%{?dist}
Summary: Linux monitoring program plugins for Nagios

Group: Applications/System
License: GPLv3+
URL: https://github.com/madrisan/nagios-plugins-linux/wiki
Source0: https://sites.google.com/site/davidemadrisan/files/%{name}-%{version}.tar.bz2

BuildRequires: gcc
BuildRequires: make
BuildRequires: glibc-devel

#Requires: nagios-common >= 3.3.1-1

%if 0%{?rhel} < 6
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)a
%endif

%description
A suite of Nagios/NRPE plugins for monitoring Linux servers and appliances.

%package all
Summary: Nagios Plugins Linux - All plugins
Group: Applications/System
Requires: nagios-plugins-linux-clock
Requires: nagios-plugins-linux-cpu
Requires: nagios-plugins-linux-cpufreq
Requires: nagios-plugins-linux-cswch
Requires: nagios-plugins-linux-ifmountfs
Requires: nagios-plugins-linux-intr
Requires: nagios-plugins-linux-iowait
Requires: nagios-plugins-linux-load
Requires: nagios-plugins-linux-memory
Requires: nagios-plugins-linux-multipath
Requires: nagios-plugins-linux-nbprocs
Requires: nagios-plugins-linux-network
Requires: nagios-plugins-linux-paging
Requires: nagios-plugins-linux-readonlyfs
Requires: nagios-plugins-linux-swap
Requires: nagios-plugins-linux-tcpcount
Requires: nagios-plugins-linux-temperature
Requires: nagios-plugins-linux-uptime
Requires: nagios-plugins-linux-users

%description all
A suite of Nagios/NRPE plugins for monitoring Linux servers and appliances.

%package clock
Summary: Nagios plugins for Linux - check_clock
Group: Applications/System

%description clock
This Nagios plugin returns the number of seconds elapsed between local time and Nagios time.

%package cpu
Summary: Nagios plugins for Linux - check_cpu
Group: Applications/System

%description cpu
This Nagios plugin checks the CPU (user mode) utilization.

%package cpufreq
Summary: Nagios plugins for Linux - check_cpufreq
Group: Applications/System

%description cpufreq
This Nagios plugin displays the CPU frequency characteristics.

%package cswch
Summary: Nagios plugins for Linux - check_cpu
Group: Applications/System

%description cswch
This Nagios plugin monitors the total number of context switches per second across all CPUs.

%package fc
Summary: Nagios plugins for Linux - check_fc
Group: Applications/System

%description fc
This Nagios plugin monitors the status of the fiber status ports.

%package ifmountfs
Summary: Nagios plugins for Linux - check_ifmountfs
Group: Applications/System

%description ifmountfs
This Nagios plugin checks whether the given filesystems are mounted.

%package intr
Summary: Nagios plugins for Linux - check_intr
Group: Applications/System

%description intr
This Nagios plugin monitors the interrupts serviced per second, including unnumbered architecture specific interrupts.

%package iowait
Summary: Nagios plugins for Linux - check_iowait
Group: Applications/System

%description iowait
This Nagios plugin monitors the I/O wait bottlenecks.

%package load
Summary: Nagios plugins for Linux - check_load
Group: Applications/System

%description load
This Nagios plugin checks the current system load average.

%package memory
Summary: Nagios plugins for Linux - check_memory
Group: Applications/System

%description memory
This Nagios plugin checks the memory usage.

%package multipath
Summary: Nagios plugins for Linux - check_multipath
Group: Applications/System

%description multipath
This Nagios plugin checks the multipath topology status.

%package nbprocs
Summary: Nagios plugins for Linux - check_nbprocs
Group: Applications/System

%description nbprocs
This Nagios plugin displays the number of running processes per user.

%package network
Summary: Nagios plugins for Linux - check_network
Group: Applications/System

%description network
This Nagios plugin displays some network interfaces statistics.

%package paging
Summary: Nagios plugins for Linux - check_paging
Group: Applications/System

%description paging
This Nagios plugin checks the memory and swap paging.

%package readonlyfs
Summary: Nagios plugins for Linux - check_readonlyfs
Group: Applications/System

%description readonlyfs
This Nagios plugin checks for readonly filesystems.

%package swap
Summary: Nagios plugins for Linux - check_swap
Group: Applications/System

%description swap
This Nagios plugin checks the swap usage.

%package tcpcount
Summary: Nagios plugins for Linux - check_tcpcount
Group: Applications/System

%description tcpcount
This Nagios plugin checks the tcp network usage.

%package temperature
Summary: Nagios plugins for Linux - check_temperature
Group: Applications/System

%description temperature
This Nagios plugin monitors the hardware's temperature.

%package uptime
Summary: Nagios plugins for Linux - check_uptime
Group: Applications/System

%description uptime
This Nagios plugin checks how long the system has been running.

%package users
Summary: Nagios plugins for Linux - check_users
Group: Applications/System

%description users
This Nagios plugin displays the number of users that are currently logged on.

%prep
%setup -q

%build
%configure --libexecdir=%{_libdir}/nagios/plugins \
%if 0%{?rhel} < 7
   --with-socketfile=/var/run/multipathd.sock
%endif

make %{?_smp_mflags}

%install
[ "%{buildroot}" != / ] && rm -rf "%{buildroot}"
make DESTDIR=%{buildroot} install

%files all
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README

%files clock
%defattr(-,root,root)
%{_libdir}/nagios/plugins/check_clock

%files cpu
%defattr(-,root,root)
%{_libdir}/nagios/plugins/check_cpu

%files cpufreq
%defattr(-,root,root)
%{_libdir}/nagios/plugins/check_cpufreq

%files cswch
%defattr(-,root,root)
%{_libdir}/nagios/plugins/check_cswch

%files fc
%defattr(-,root,root)
%{_libdir}/nagios/plugins/check_fc

%files ifmountfs
%defattr(-,root,root)
%{_libdir}/nagios/plugins/check_ifmountfs

%files intr
%defattr(-,root,root)
%{_libdir}/nagios/plugins/check_intr

%files iowait
%defattr(-,root,root)
%{_libdir}/nagios/plugins/check_iowait

%files load
%defattr(-,root,root)
%{_libdir}/nagios/plugins/check_load

%files memory
%defattr(-,root,root)
%{_libdir}/nagios/plugins/check_memory

%files multipath
%defattr(-,root,root)
%{_libdir}/nagios/plugins/check_multipath

%files nbprocs
%defattr(-,root,root)
%{_libdir}/nagios/plugins/check_nbprocs

%files network
%defattr(-,root,root)
%{_libdir}/nagios/plugins/check_network

%files paging
%defattr(-,root,root)
%{_libdir}/nagios/plugins/check_paging

%files readonlyfs
%defattr(-,root,root)
%{_libdir}/nagios/plugins/check_readonlyfs

%files swap
%defattr(-,root,root)
%{_libdir}/nagios/plugins/check_swap

%files tcpcount
%defattr(-,root,root)
%{_libdir}/nagios/plugins/check_tcpcount

%files temperature
%defattr(-,root,root)
%{_libdir}/nagios/plugins/check_temperature

%files uptime
%defattr(-,root,root)
%{_libdir}/nagios/plugins/check_uptime

%files users
%defattr(-,root,root)
%{_libdir}/nagios/plugins/check_users

%changelog
* Sat Nov 21 2015 Davide Madrisan <davide.madrisan@gmail.com> 19-1mamba
- ported version 19 from openmamba GNU/Linux