%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname csv2ofx

Name:           python-%{srcname}
Version:        0.34.2
Release:        1%{?dist}
Summary:        Converts CSV files to OFX and QIF files
License:        MIT
URL:            https://github.com/reubano/csv2ofx
Source0:        https://github.com/reubano/csv2ofx/archive/refs/tags/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pytest-freezegun
BuildRequires:  python%{python3_pkgversion}-pytest-lazy-fixtures

%generate_buildrequires
%pyproject_buildrequires -r

%define _description %{expand:
csv2ofx is a Python library and command line interface program that
converts CSV files to OFX and QIF files for importing into GnuCash or
similar financial accounting programs. csv2ofx has built in support for
importing csv files from mint, yoodlee, and xero.}
%description
%_description


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}


%description -n python%{python3_pkgversion}-%{srcname}
%_description


%prep
%autosetup -p1 -n %{srcname}-%{version}
sed -i csv2ofx/mappings/ubs-ch-fr.py -e '/setlocale(.*fr_CH/d'


%build
%pyproject_wheel


%install
rm -rf $RPM_BUILD_ROOT
%pyproject_install
%pyproject_save_files '*' +auto


%check
%pytest

%files -n  python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}


%changelog
* Sat Jun 13 2026 Martin RS - 0.34.2
- Update
* Fri May 23 2025 Martin RS - 0.34.1
- Update
* Sat May 04 2024 Martin RS - 0.30.1git
- Initial
