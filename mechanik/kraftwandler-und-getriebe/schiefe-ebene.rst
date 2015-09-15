.. index::
    single: Kraftwandler; Schiefe Ebene
.. _Schiefe Ebene:

Die schiefe Ebene
==================

Wird ein Körper auf eine schiefe Ebene gestellt, so wird er aufgrund seiner
Gewichtskraft :math:`F _{\rm{G}}` entlang der schiefen Ebene hangabwärts
beschleunigt. Dies lässt sich erklären, wenn man die Gewichtskraft in zwei
Teilkräfte (entlang der schiefen Ebene und senkrecht zu ihr) zerlegt denkt:

* Die Kraft senkrecht zur schiefen Ebene wird Normalkraft :math:`F _{\rm{N}}`
  genannt. Dieser Kraftanteil würde ein Einsinken des Körpers in die schiefe
  Ebene bewirken, jedoch wirkt bei einem festen Untergrund der Boden aufgrund
  seiner Starrheit dagegen.

* Die Kraft parallel zur schiefen Ebene wird Hangabtriebskraft :math:`F
  _{\rm{HA}}` genannt. Dieser Kraftanteil bewirkt eine Beschleunigung des
  Körpers entlang der schiefen Ebene.

Ist die Hangabtriebskraft groß genug, um die zwischen Körper und schiefer Ebene
wirkende Reibungskraft zu überwinden, so beginnt der Körper zu gleiten.

.. figure:: ../../pics/mechanik/kraftwandler-und-getriebe/schiefe-ebene-schlittenfahren.png
    :name: fig-schiefe-ebene-schlittenfahren
    :alt:  fig-schiefe-ebene-schlittenfahren
    :align: center
    :width: 45%

    Schlittenfahren auf einer schiefen Ebene.

    .. only:: html

        :download:`SVG: Schlittenfahren (Schiefe Ebene)
        <../../pics/mechanik/kraftwandler-und-getriebe/schiefe-ebene-schlittenfahren.svg>`

Auf einer waagrechten Ebene ist die Gewichtskraft :math:`\vec{F} _{\rm{G}}`
gleich der Normalkraft :math:`\vec{F} _{\rm{N}}`, der Betrag der
Hangabtriebskraft ist gleich Null. Umgekehrt ist entlang einer vertikalen Wand
die Hangabtriebskraft gleich der Gewichtskraft, und die (anpressende)
Normalkraft ist gleich Null. Bei einem beliebigen Winkel :math:`\alpha` der
schiefen Ebene gelten für die Beträge der Normal- und Hangabtriebskraft folgende
Zusammenhänge:

.. math::
    :label: eqn-schiefe-ebene-kraftanteile

    F _{\rm{HA}} &= F _{\rm{G}} \cdot \sin{\alpha }\\[6pt]
    F _{\rm{N\phantom{A}}}  &= F _{\rm{G}} \cdot \cos{\alpha }

Hierbei wurde die genutzt, dass der Winkel zwischen der Gewichtskraft :math:`F
_{\rm{G}}` und Normalkraft :math:`F _{\rm{N}}` gleich dem Winkel :math:`\alpha`
der schiefen Ebene ist, da es sich um zwei :ref:`senkrecht zueinander stehende
Winkel <gwm:Zueinander senkrechte Winkel>` handelt. Bezeichnet man zusätzlich
mit :math:`l` die Länge der schiefen Ebene, so ergibt sich aufgrund der
Ähnlichkeit der beiden Kraftdreiecke und des Dreiecks der Schiefen Ebene
folgender Zusammenhang zwischen der Hangabtriebskraft und der Gewichtskraft des
Schlittens:

.. math::
    :label: eqn-schiefe-ebene-kraftverhaeltnis

    \frac{F _{\rm{H}}}{G} = \frac{h}{l}

Je länger also die schiefe Ebene ist, desto kleiner ist die entlang der Ebene
wirkende Hangabtriebskraft. Aus diesem Grund werden in Gebirgen Straßen und Wege
in Serpentinen angelegt.

.. figure:: ../../pics/mechanik/kraftwandler-und-getriebe/schiefe-ebene-kraftzerlegung.png
    :name: fig-schiefe-ebene-kraftzerlegung
    :alt:  fig-schiefe-ebene-kraftzerlegung
    :align: center
    :width: 45%

    Kraftzerlegung bei einer schiefen Ebene.

    .. only:: html

        :download:`SVG: Schiefe Ebene (Kraftzerlegung)
        <../../pics/mechanik/kraftwandler-und-getriebe/schiefe-ebene-kraftzerlegung.svg>`

Die Größe des Winkels :math:`\alpha` lässt sich anhand des Verhältnis der Höhe
:math:`h` zur (horizontalen) Breite :math:`b` der schiefen Ebene berechnen.
Hierbei gilt für den Winkel :math:`\alpha`:

.. math::
    :label: eqn-schiefe-ebene-winkel

    \tan{\alpha} = \frac{h}{b} \quad \Leftrightarrow \quad \alpha = \text{atan
    }{\left( \frac{h}{b}\right)}

Je kleiner also der Winkel :math:`\alpha` ist, desto länger ist bei einer
bestimmten Steighöhe :math:`h` die horizontale Breite :math:`b` beziehungsweise
wegen :math:`l = \sqrt{b^2 + h^2}` auch die Länge :math:`l` der schiefen Ebene.

.. rubric:: Die Keilwirkung

Ein Keil, auf dessen Rückseite eine Kraft :math:`F` ausgeübt wird, kann das
umliegende Material auseinander treiben. Diese spaltende Wirkung, die
beispielsweise bei Äxten oder Meißeln genutzt wird, lässt sich ebenfalls mittels
der Kraftaufteilung an einer schiefen Ebene erklären, wenn man sich den Keil in
zwei rechtwinklige Dreiecke zerlegt denkt.

.. figure:: ../../pics/mechanik/kraftwandler-und-getriebe/schiefe-ebene-keilwirkung.png
    :name: fig-schiefe-ebene-keilwirkung
    :alt:  fig-schiefe-ebene-keilwirkung
    :align: center
    :width: 45%

    Keilwirkung als Normalkraft bei einer schiefen Ebene.

    .. only:: html

        :download:`SVG: Schiefe Ebene (Keilwirkung)
        <../../pics/mechanik/kraftwandler-und-getriebe/schiefe-ebene-keilwirkung.svg>`

Die Kraft :math:`F`, die auf den Keil ausgeübt wird, kann in zwei Normalkräfte
:math:`F _{\rm{N,1}}` und :math:`F _{\rm{N,2}}` senkrecht zu den Keilflächen
zerlegt werden.
Bezeichnet man die Breite des Keilrückens mit :math:`h`, die Länge einer
schrägen Keilflächen mit :math:`l` und den halben Keilwinkel als :math:`\alpha`,
so gilt:

.. math::

    \frac{F _{\rm{N}}}{F} = \frac{s}{b} \quad \Leftrightarrow \quad F _{\rm{N}}
    = \frac{s}{b} \cdot F

Da die Länge :math:`s` der schrägen Flächen üblicherweise länger ist als
die Breite :math:`b` des Keils, sind die spaltenden Normalkräfte größer als
die auf den Keil wirkende Kraft :math:`F`.

..  .. math::

    ..  F _{\rm{N}} = F \cdot \frac{s}{r} = \frac{F}{2 \cdot \sin{\alpha}}

..
    TODO Schraube als schiefe Ebene: Deutung als schiefe Ebene, die um eine Achse
    gewickelt wurde.

    Die passenden Muttern sind zylindrisch durchbohrte Körper mit
    eingeschnittenen Gewinden. Dreht man die Schraubenmutter bei fest stehender
    Spindel, so schiebt sie sich bei einer Umdrehung um eine Ganghöhe in
    Richtung der Zylinderachse vor. Dabei wird in Richtung der Zylinderachse
    eine Druckkraft ausgeübt; je kleiner die Ganghöhe ist, umso leichter kann
    bei vorhandener Gegenkraft die Mutter in die Spindel eingedreht werden.

    Wenn F1 die zur Drehung der Schraube erforderliche Kraft ist (wirksam im
    Abstand r), F2 die in Achsenrichtung wirkende Kraft, h die Ganghöhe der
    Schraube, r der mittlere Gewinderadius und \alpha der Neigungswinkel der
    geneigten Ebene, dann gilt:

    F1 / F2 = h:b = \tan{\alpha} \\
    F1 = F2 \cdot \tan{\alpha}


.. raw:: html

    <hr />

.. hint::

    Zu diesem Abschnitt gibt es :ref:`Versuche <Versuche zur schiefen Ebene>`
    und :ref:`Übungsaufgaben <Aufgaben zur schiefen Ebene>`.

