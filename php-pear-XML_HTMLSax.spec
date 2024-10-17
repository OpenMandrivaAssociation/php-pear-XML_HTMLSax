%define		_class		XML
%define		_subclass	HTMLSax
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	3.0.0
Release:	16
Summary:	A SAX based parser for HTML and other badly formed XML documents
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/XML_HTMLSax/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
XML_HTMLSax is a SAX based XML parser for badly formed XML documents,
such as HTML. The original code base was developed by Alexander Zhukov
and published at http://sourceforge.net/projects/phpshelve/, who in
turn was inspired by the Python HTMLSax package. Alexander kindly gave
permission to modify the code and license for inclusion in PEAR.
PEAR::XML_HTMLSax takes the last release from Sourceforge
(HTMLSax2002082201) and changes the API to make using HTMLSax very
similar to using the native PHP Expat extension, opening it up for use
with projects like SAX filters:
http://phpxmlclasses.sourceforge.net/show_doc.php?class=class_sax_filters.html.
This version also fixes some bugs and adds further features such as
the ability to handle processing instructions and JSP/ASP markup.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 3.0.0-14mdv2012.0
+ Revision: 742301
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 3.0.0-13
+ Revision: 679605
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 3.0.0-12mdv2011.0
+ Revision: 613791
- the mass rebuild of 2010.1 packages

* Wed Nov 11 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.0.0-11mdv2010.1
+ Revision: 464952
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 3.0.0-10mdv2010.0
+ Revision: 441716
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 3.0.0-9mdv2009.1
+ Revision: 322826
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 3.0.0-8mdv2009.0
+ Revision: 237162
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 3.0.0-7mdv2007.0
+ Revision: 82852
- Import php-pear-XML_HTMLSax

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 3.0.0-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 3.0.0-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 3.0.0-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 3.0.0-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 3.0.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 3.0.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 3.0.0-1mdk
- initial Mandriva package (PLD import)

