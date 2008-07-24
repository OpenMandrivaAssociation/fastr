%define name	fastr
%define version	2.04
%define release	%mkrel 11

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A tool for automatic indexing
Source0:	http://www.limsi.fr/Individu/jacquemi/FASTR/%{name}-%{version}.tar.bz2
Patch0:		%{name}-2.04.source.patch.bz2
Patch1:		%{name}-2.04.config.patch.bz2
Patch2:		%{name}-2.04.autotools.patch.bz2
Patch3:		%{name}-2.04.autotools.bis.patch.bz2
URL:		http://www.limsi.fr/Individu/jacquemi/FASTR/
License:	GPL
Group:		Sciences/Computer science
BuildRequires:	automake1.8
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Fastr is a parser for term and variant recognition. Fastr take as input a
corpus and a list of terms and ouputs the indexed corpus in which terms and
variants are recognized. 

Fastr can be used in two modes: 
- controlled indexing: input consists of a corpus and a list of terms, 
- free indexing: input only consists of a corpus, the list of terms is
  automatically acquired from the corpus. 

Fastr uses the following resources: 
- the corpus and the list of terms are tagged by the TreeTagger:
 http://www.ims.uni-stuttgart.de/Tools/DecisionTreeTagger.html 
- if available, a list of morphological families and a list of semantic links
  are used to calculate morphological and semantic variation. See sample files
  - /usr/share/fastr/der-families-xx 
  - /usr/share/fastr/sem-classes-xx or ./lib/sem-links-xx 
 for the format (xx is the name of the language [en|fr]). 
 Perl modules are provided in order to generate these data from WordNet and
 CELEXfor the English language. 

The formalism of Fastr is close to PATR-II.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
aclocal-1.8
autoconf
automake-1.8
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL README TODO doc/en/*.html
%config(noreplace) %{_sysconfdir}/*
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%{name}

