.. meta::
    :description: Ein freies Physik-Lehrbuch mit Aufgaben und Lösungen.
    :keywords:  Physik, Grundwissen, Schule, Lehrbuch, Grundwissen Physik, Lehrbuch Physik, Physik Schule, Physik Aufgaben, Freies Lehrbuch

.. _Physik:

Physik
======

.. only:: html

    Früher hieß "Physik" die Lehre von der ganzen Natur (*physis* = griech. Natur).
    Heute geht es in der Physik um das Studium der unbelebten Natur ohne chemische
    Veränderungen -- Biologie und Chemie haben sich selbst zu großen
    Wissenschaftsbereichen entwickelt.

    .. sidebar:: Hinweis

        Eine Druckversion dieser Seite ist als :download:`PDF-Dokument
        <grundwissen-physik.pdf>` verfügbar.

        Der Quellcode zu diesem Projekt kann von `GitHub
        <https://www.github.com/grund-wissen/grundwissen-physik>`_ heruntergeladen werden.



.. toctree::
    :maxdepth: 2

    einleitung.rst
    mechanik/index.rst
    akustik/index.rst
    optik/index.rst
    waermelehre/index.rst
    elektrizitaet-und-magnetismus/index.rst
    atomphysik/index.rst
    experimente.rst
    aufgaben-und-loesungen.rst
    tabellen.rst
    links-und-quellen.rst

.. Anzahl der Aufgaben bzw. Versuche ausgeben:

.. find ./ -name "*aufgaben*.rst"  | xargs grep -c "^\* "         | awk -F ":" '{sum+=$2} END {print sum}'
.. find ./ -name "*loesungen*.rst" | xargs grep -c "^\* "         | awk -F ":" '{sum+=$2} END {print sum}'
.. find ./ -name "*versuche*.rst"  | xargs grep -c ".. rubric:: " | awk -F ":" '{sum+=$2} END {print sum}'

