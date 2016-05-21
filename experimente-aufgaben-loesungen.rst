.. _Aufgaben und Lösungen:
.. _Experimente, Übungsaufgaben und Lösungen:

Experimente, Übungsaufgaben und Lösungen
========================================

.. Anzahl der Aufgaben bzw. Versuche ausgeben:

.. find ./ -name "*aufgaben*.rst"    | xargs grep -c "^\* "         | awk -F ":" '{sum+=$2} END {print sum}'
.. find ./ -name "*loesungen*.rst"   | xargs grep -c "^\* "         | awk -F ":" '{sum+=$2} END {print sum}'
.. find ./ -name "*experimente*.rst" | xargs grep -c ".. rubric:: " | awk -F ":" '{sum+=$2} END {print sum}'

..  Now 2016-05-16 

.. *  68 Experimente, 17 Bilder
.. * 141 Übungsufgaben
.. * 141 Lösungen

.. _Experimente:

Experimente
-----------

..  Experimente sind in der Physik von besonderer Bedeutung. Mit einem geeigneten
..  Versuchsaufbau können Ursache-Wirkungs-Zusammenhänge anschaulich und
..  beliebig oft wiederholbar untersucht werden.

.. toctree::
    :maxdepth: 2

    mechanik/experimente.rst
    akustik/experimente.rst
    optik/experimente.rst
    waermelehre/experimente.rst
    elektrizitaet-und-magnetismus/experimente.rst


.. _Aufgaben:
.. _Übungsaufgaben:

Übungsaufgaben
--------------

.. .. raw:: html

..     <h2>Aufgaben<a class="headerlink" href="#aufgaben" title="Permalink zu dieser Überschrift"></a></h2>

.. toctree::
    :maxdepth: 2

    mechanik/aufgaben.rst
    akustik/aufgaben.rst
    optik/aufgaben.rst
    waermelehre/aufgaben.rst
    elektrizitaet-und-magnetismus/aufgaben.rst
    atomphysik/aufgaben.rst


.. _Lösungen:

Lösungen
--------

.. toctree::
    :maxdepth: 2

    mechanik/loesungen.rst
    akustik/loesungen.rst
    optik/loesungen.rst
    waermelehre/loesungen.rst
    elektrizitaet-und-magnetismus/loesungen.rst
    atomphysik/loesungen.rst

.. Papier hat in etwa gleiche Dicke wie menschliches Haar, rund 100 Mikrometer.
.. Ein Blatt Papier hat ca. 10 Millionen Fasern.

