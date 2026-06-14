%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname pynose

Name:           pynose
Version:        1.5.5
Release:        2%{?dist}
Summary:        pynose fixes nose to extend unittest and make testing easier
License:        GNU LGPL
URL:            https://github.com/mdmintz/pynose
Source0:        https://github.com/mdmintz/pynose/archive/refs/tags/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%generate_buildrequires
%pyproject_buildrequires -r


%define _description %{expand:
Pynose is an updated version of nose, originally made by Jason Pellerin.
This version of nose is compatible with Python 3.7+ (including 3.13+).

nose extends the test loading and running features of unittest, making
it easier to write, find and run tests.}

%description
%_description

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}


%description -n python%{python3_pkgversion}-%{srcname}
%_description


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%pyproject_wheel


%install
rm -rf $RPM_BUILD_ROOT
%pyproject_install
%pyproject_save_files '*' +auto


%files -n  python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}


%changelog
* Sat Jun 13 2026 Martin RS - 1.5.5
- Initial
