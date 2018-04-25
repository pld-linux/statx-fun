Summary:	statx(2) sample implementation
Name:		statx-fun
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/System
Source0:	https://github.com/whotwagner/statx-fun/archive/v%{version}.tar.gz
# Source0-md5:	6b8b52a40b4d08877c974f6165af6717
URL:		https://github.com/whotwagner/statx-fun
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
statx(2) sample implementation.

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcppflags} %{rpmcflags} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

cp -p statx $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/statx
