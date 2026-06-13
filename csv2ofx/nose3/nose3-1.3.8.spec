%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname nose3

Name:           nose3
Version:        1.3.8
Release:        2%{?dist}
Summary:        nose extends unittest to make testing easier
License:        GNU LGPL
URL:            https://github.com/jayvdb/nose3
Source0:        %{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%{?python_enable_dependency_generator}
%generate_buildrequires
%pyproject_buildrequires

%description
nose3 is a fork of nose v1 not using lib2to3 for compatibility with Python 3.

    nose extends the test loading and running features of unittest, making
    it easier to write, find and run tests.

    By default, nose will run tests in files or directories under the current
    working directory whose names include "test" or "Test" at a word boundary
    (like "test_this" or "functional_test" or "TestClass" but not
    "libtest"). Test output is similar to that of unittest, but also includes
    captured stdout output from failing tests, for easy print-style debugging.

    These features, and many more, are customizable through the use of
    plugins. Plugins included with nose provide support for doctest, code
    coverage and profiling, flexible attribute-based test selection,
    output capture and more. More information about writing plugins may be
    found on in the nose API documentation, here:
    http://readthedocs.org/docs/nose/

    If you encounter any problems, please raise an issue at:
    https://github.com/jayvdb/nose3
    


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%if %{undefined python_enable_dependency_generator} && %{undefined python_disable_dependency_generator}
# Put manual requires here:
Requires:       python%{python3_pkgversion}-foo
%endif

%description -n python%{python3_pkgversion}-%{srcname}
%summary


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
#py3_build
%pyproject_wheel


%install
rm -rf $RPM_BUILD_ROOT
#py3_install
%pyproject_install
mkdir ${RPM_BUILD_ROOT}%{_datadir}
mv ${RPM_BUILD_ROOT}/usr/man ${RPM_BUILD_ROOT}%{_mandir}


%files -n  python%{python3_pkgversion}-%{srcname}
%license lgpl.txt AUTHORS CHANGELOG DEVELOPERS.txt
%doc NEWS README.BDIST_RPM README.md README.txt 
%{_bindir}/nosetests*
%{_mandir}/man1/nosetests.1*
# For noarch packages: sitelib
%{python3_sitelib}/nose/
%{python3_sitelib}/%{srcname}-%{version}.dist-info/


%changelog
* Tue May 05 2026 Martin RS <martrs@github>
- 
