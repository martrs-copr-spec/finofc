%{?!python3_pkgversion:%global python3_pkgversion 3}

%define _gitcommit bc9473d5023468b2d4af25a6aa20243bec051c02
%define _gitdate 20230831

%global srcname pygogo
%global srcver 1.3.0

Name:           python-%{srcname}
Version:        %{srcver}git%{_gitdate}
Release:        2%{?dist}
Summary:        Python logger with superpowers
License:        MIT
URL:            https://github.com/reubano/pygogo
Source0:        https://github.com/reubano/pygogo/archive/%{_gitcommit}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pkutils
BuildRequires:  python%{python3_pkgversion}-flake8
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  python%{python3_pkgversion}-pylint

%{?python_enable_dependency_generator}

%define _description %{expand:
pygogo is a Python logging library and command-line interface with
super powers. pygogo leverages the standard Python logging module under
the hood, so there's no need to learn yet-another logging library. The
default implementation sends all messages to stdout, and any messages
at level WARNING or above also to stderr.}
%description
%_description

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}


%description -n python%{python3_pkgversion}-%{srcname}
%_description


%prep
%autosetup -p1 -n %{srcname}-%{_gitcommit}
sed -i pygogo/__init__.py \
  -e 's/^\(__version__\s\+=\s\+\)"[0-9\.]\+"/\1"%{srcver}"/'


%build
%py3_build


%install
rm -rf $RPM_BUILD_ROOT
%py3_install
mv %{buildroot}%{_bindir}/gogo %{buildroot}%{_bindir}/pygogo


%check
# use what your upstream is using
%{__python3} -m nose


%files -n  python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst CONTRIBUTING.rst
%{_bindir}/pygogo
# For noarch packages: sitelib
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{srcver}-py%{python3_version}.egg-info/


%changelog
* Sat May  4 2024 Martin RS - 1.3.0git20230831
- Update
* Thu Oct 06 2022 Martin RS - 1.2.0
- Initial
