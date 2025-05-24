%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname pkutils
%global srcver 3.0.2

%define _gitcommit a1c5ffde53b6657f3cc648d1ae6f1932927d3c91
%define _gitdate 20230831

Name:           python-%{srcname}
Version:        %{srcver}git%{_gitdate}
Release:        2%{?dist}
Summary:        Python packaging utility library
License:        MIT
URL:            https://github.com/reubano/pkutils
Source0:        https://github.com/reubano/pkutils/archive/%{_gitcommit}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-semver
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-flake8
BuildRequires:  python%{python3_pkgversion}-pylint
BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  python%{python3_pkgversion}-coverage
BuildRequires:  python%{python3_pkgversion}-tox

%{?python_enable_dependency_generator}

%define _description %{expand:
pkutils is a Python library_ that simplifies python module packaging. It is
intended to be used in your package's setup.py file.

With pkutils, you can
- Parse requirements files
- Determine your project's development status
- Read text files
- and much more...}
%description
%_description

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
%_description


%prep
%autosetup -p1 -n %{srcname}-%{_gitcommit}
sed -i requirements.txt -e '/^semver/s/,.*//'
#sed -i pkutils.py -e 's/^\(__version__\s\+=\s\+"\)[0-9\.]\+"/\1%{srcver}"/'

%build
%py3_build


%install
rm -rf $RPM_BUILD_ROOT
%py3_install


%check
%{__python3} -m nose


%files -n  python%{python3_pkgversion}-%{srcname}
%license LICENSE 
%doc README.rst 
# For noarch packages: sitelib
%pycached %{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/%{srcname}-%{srcver}-py%{python3_version}.egg-info/


%changelog
* Sat May 04 2024 Martin RS - 3.0.2git20230831
- Update
* Thu Oct 06 2022 Martin RS - 3.0
- Initial
