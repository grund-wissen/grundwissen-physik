.. meta::
    :keywords:  Körper, Körpereigenschaften, Masse, Volumen, Dichte, Aggregatzustand

.. index:: Körper
.. _Körpereigenschaften:

Körpereigenschaften
===================

Alle physikalischen Körper, also räumlich begrenzte Materieformen, bestehen aus
Stoffen und besitzen gemeinsame physikalische Eigenschaften. Umgangssprachlich
bezeichnet man physikalische beziehungsweise geometrische Körper häufiger als
"Objekte".

.. TODO Längen, Längenmessung, Umrechnung Inch auf m
.. Formelzeichen
.. Nonius

.. index:: Masse, Masse (Körpereigenschaft)
.. _Masse:

Masse
-----

Jedes physikalische Objekt besteht aus Materie; jeder Materie-Baustein wiederum
"wiegt" etwas, so dass jedes physikalische Objekt auch stets eine gewisse Masse
:math:`m` als charakteristische Eigenschaft aufweist.

*Einheit:*

    Die Masse eines Objekts wird meist in Kilogramm :math:`(\unit{kg})`
    angegeben. Weitere gebräuchliche Einheiten sind die Tonne
    :math:`(\unit{t})` und das Gramm :math:`(\unit{g})`.

    .. math::

        \unit[1]{t} &= \unit[1000]{kg} \\
        \unit[1]{kg} &= \unit[1000]{g}

Die Masse :math:`m` eines Objekts kann man an seiner Schwere beziehungsweise an
seiner Trägheit erkennen:

- Die Eigenschaft "Schwere" gibt an, wie sehr ein Objekt in der Lage ist, sich
  selbst oder einen anderen Gegenstand im Gravitationsfeld eines Planeten zu
  beschleunigen. Als anschauliches Beispiel kann man an die "Gewichte" einer
  Kuckucksuhr denken, die beim Herabsinken in der Lage sind, die Zeiger der Uhr
  anzutreiben. [#]_

- Die Eigenschaft "Trägheit" gibt an, wie sehr sich ein Objekt einer von außen
  einwirkenden Kraft widersetzt; man kann die "Trägheit" eines Objekts somit als
  "Widerstand gegen Beschleunigung" auffassen.

Im Rahmen seiner Relativitätstheorie konnte Albert Einstein zeigen, dass beide
Eigenschaften stets im gleichen Maß vorhanden sind; es muss somit nicht explizit
zwischen schwerer und träger Masse unterschieden werden.


.. index:: Volumen
.. _Volumen:
.. _Volumen:

Volumen
-------

Jedes Objekt besitzt ein Volumen :math:`V`, also eine räumliche Ausdehnung.

*Einheit:*

    Das Volumen :math:`V` eines Objekts wird meist in Kubikmeter
    :math:`(\unit{m^3})` angegeben. Weitere gebräuchliche Einheiten sind der
    Liter :math:`(\unit[1]{l} = \unit[1]{dm^3})` und der Kubik-Zentimeter
    :math:`(\unit{cm^3})`:

    .. math::

        \unit[1]{m^3} &= \unit[10 \times 10 \times 10]{dm^3} = \unit[1000]{l} \\
        \unit[1]{l} &= \unit[10 \times 10 \times 10]{cm^3} = \unit[1000]{cm^3}

Ein Liter entspricht einem Kubik-Dezimeter, also einem Würfel von
:math:`\unit[10]{cm} \times \unit[10]{cm} \times \unit[10]{cm}` Kantenlänge.

.. figure:: ../pics/mechanik/volumen-kubikzentimeter-und-liter.png
    :name: fig-volumen-kubikzentimeter-und-liter
    :alt:  fig-volumen-kubikzentimeter-und-liter
    :align: center
    :width: 60%

    Ein Kubikzentimeter und ein Kubikdezimeter (Liter) im Vergleich.

    .. only:: html

        :download:`SVG: Kubikzentimeter und Liter
        <../pics/mechanik/volumen-kubikzentimeter-und-liter.svg>`

Zur Bestimmung des Volumens eines Objekts können folgende Methoden angewendet
werden:

* Das Volumen eines festen, *regelmäßig* geformten Objekts kann durch
  geometrische Berechnung bestimmt werden. Dazu müssen die charakteristischen
  Längen der jeweiligen Form gemessen werden.

* Das Volumen eines festen, *unregelmäßig* geformten Objekts kann durch
  Flüssigkeitsverdrängung ermittelt werden.

* Das Volumen von Flüssigkeiten kann mit Messzylindern gemessen werden

* Gase verteilen sich gleichmäßig in dem zur Verfügung stehenden Raum. Das
  Volumen eines Gases kann daher bestimmt werden, indem das Volumen des vom
  Gas ausgefüllten Raumes gemessen wird.


.. index:: Dichte
.. _Dichte:

Dichte
------

Die Dichte :math:`\rho` eines Gegenstands gibt an, welche Masse :math:`m` er bei
einem bestimmten Volumen :math:`V` besitzt.

*Definition:*

    Die Dichte :math:`\rho` eines Objekts ist gleich dem Verhältnis aus seiner
    Masse :math:`m` und seinem Volumen :math:`V`:

    .. math::
        :label: eqn-dichte

        \rho = \frac{m}{V}

*Einheit:*

    Verwendet man Standard-Einheiten, so ergibt sich als Einheit für die Dichte
    Kilogramm je Kubikmeter :math:`(\unitfrac{kg}{m^3})`. Eine weitere
    gebräuchliche Einheit ist Gramm je Kubik-Zentimeter
    :math:`(\unitfrac{g}{cm^3})`:

    .. math::

        \unit[1]{\frac{g}{cm^3} } = \unit[100 \times 100 \times
        100]{\frac{g}{m^3}} = \unit[1\,000\,000]{\frac{g}{m^3}} =
        \unit[1000]{\frac{kg}{m^3} }

    Folgende Dichte-Einheiten können als gleichwertig verwendet werden:

    .. math::

        \unit{\frac{g}{cm^3}} = \unit{\frac{kg}{dm^3}} = \unit{\frac{t}{m^3}}

Experimentell kann die Dichte eines Festkörpers bestimmt werden, indem man seine
Masse mit Hilfe einer Waage bestimmt und sein Volumen durch Eintauchen in eine
Flüssigkeit ermittelt. Nach dem Archimedischen Prinzip verdrängt jeder
Gegenstand beim Eintauchen ebenso viel Flüssigkeit, wie er selbst an Volumen
hat. Teilt man den Wert der Masse durch den Wert des Volumen, so erhält man die
Dichte des Objekts.

.. list-table::
    :name: tab-dichte-beispiele-festkoerper
    :widths: 50 50

    * - Stoff
      - Dichte in :math:`\unitfrac{kg}{m^3}`
    * - Aluminium
      - :math:`2700`
    * - Blei
      - :math:`11340`
    * - Eis
      - :math:`900`
    * - Glas
      - :math:`\text{ca. } 2500`
    * - Gold
      - :math:`19300`
    * - Hartgummi
      - :math:`\text{ca. } 1300`
    * - Holz
      - :math:`500 \text{ bis } 1200`
    * - Kork
      - :math:`200`
    * - Kupfer
      - :math:`8900`
    * - Schaumstoff
      - :math:`150`
    * - Silber
      - :math:`10500`
    * - Stahl
      - :math:`7800`

Die Dichte einer Flüssigkeit kann am einfachsten mit einem :ref:`Aräometer
<Aräometer>`  gemessen werden: Je kleiner die Dichte der Flüssigkeit ist, desto
weiter taucht das Aräometer in die Flüssigkeit ein. An der Skala des
eintauchenden Aräometers kann die Dichte der Flüssigkeit somit direkt abgelesen
werden.

.. list-table::
    :name: tab-dichte-beispiele-flüssigkeiten
    :widths: 50 50

    * - Stoff
      - Dichte in :math:`\unitfrac{kg}{m^3}`
    * - Ethanol
      - :math:`790`
    * - Glycerin
      - :math:`1260`
    * - Leichtbenzin
      - :math:`700`
    * - Petroleum
      - :math:`810`
    * - Quecksilber
      - :math:`13600`
    * - Schmieröl
      - :math:`900`
    * - Schwefelsäure
      - :math:`1836`
    * - Wasser (bei :math:`\unit[4]{\degree C}`)
      - :math:`1000`

Die Dichte von Gasen hängt stark vom Druck und von der Temperatur ab. Um die Dichten
verschiedener Gase dennoch vergleichen zu können, werden die entsprechenden
Werte für Normalbedingungen, also Druck :math:`p = \unit[1]{bar}` und :math:`T =
\unit[0]{\degree C}`, angegeben.

.. list-table::
    :name: tab-dichte-beispiele-gase
    :widths: 50 50

    * - Stoff (bei :math:`\unit[0]{\degree C }`)
      - Dichte in :math:`\unitfrac{kg}{m^3}`
    * - Chlor
      - :math:`3,21`
    * - Helium
      - :math:`0,18`
    * - Kohlenstoffdioxid
      - :math:`1,98`
    * - Luft
      - :math:`1,29`
    * - Methan
      - :math:`0,72`
    * - Wasserstoff
      - :math:`0,09`
    * - Xenon
      - :math:`5,90`

.. _Durchschnittliche Dichte:

.. rubric:: Durchschnittliche Dichte

Besteht ein Gegenstand aus mehr als einem Material, so setzt sich seine
durchschnittliche Dichte aus den jeweiligen Massen- und Volumenanteilen
zusammen:

.. math::

    m_{\mathrm{ges}} &= m_1 + m_2 + \ldots \\
    \rho_{\mathrm{ges}} \cdot V_{\mathrm{ges}} &= \rho_1 \cdot V_1 + \rho_2
    \cdot V_2 + \ldots \\[6pt]

Teilt man beide Seiten der Gleichung durch :math:`V_{\mathrm{ges}}`, so erhält
man für die durchschnittliche Dichte :math:`\rho_{\mathrm{ges}}` des Objekts:

.. math::

    \rho_{\mathrm{ges}} = \frac{m_1 + m_2 +
    \ldots}{V_{\mathrm{ges}}}= \frac{\rho_1 \cdot V_1 + \rho_2 \cdot V_2 +
    \ldots}{V_1 + V_2 + \ldots}

Da die Masse von Gasen gegenüber der von Festkörpern meist vernachlässigbar
klein ist, kann die obige Formel beispielsweise genutzt werden, um den
"Luftanteil" eines porösen Gegenstands zu bestimmen.

.. index:: Aggregatzustand
.. _Aggregatzustand:
.. _Aggregatzustände:

Aggregatzustand
---------------

Da Objekte aus chemischen Stoffen bestehen und diese im festen, flüssigen und
gasförmigen Aggregatzustand auftreten können, unterscheidet man entsprechend
auch zwischen Festkörpern, Flüssigkeiten und Gasen.

Je nach Aggregatzustand zeigen Objekte ein unterschiedliches Volumen- und
Formverhalten:

- Im festen Zustand sind die Atome einer Substanz in Kristallgittern oder
  Makro-Molekülen fest an ihre Plätze gebunden und können nur Schwingungen um
  ihre jeweilige Position ausführen.

- Im flüssigen Zustand können sich die einzelnen Atome beziehungsweise Moleküle
  innerhalb der Flüssigkeit frei bewegen. Der Austritt aus der Flüssigkeit wird
  jedoch durch zwischenmolekulare Kräfte stark erschwert.

- Im gasförmigen Zustand spielen zwischenmolekulare Kräfte so gut wie keine
  Rolle; die Atome beziehungsweise Moleküle können sich frei bewegen.

.. list-table:: Aggregatzustände und ihre Eigenschaften
    :name: tab-aggregatzustände-eigenschaften
    :widths: 30 15 15 35

    * - Aggregatzustand
      - Fest
      - Flüssig
      - Gasförmig
    * - Typisches Beispiel
      - Metall
      - Wasser
      - Luft
    * - Volumen
      - Bestimmt
      - Bestimmt
      - Angepasst an Gefäßvolumen
    * - Form
      - Bestimmt
      - Bestimmt
      - Angepasst an Gefäßform
    * - Abstand zwischen Teilchen
      - Klein
      - Klein
      - Sehr groß
    * - Verschiebbarkeit der Teilchen
      - Klein
      - Groß
      - Sehr groß
    * - Kompressibilität
      - Sehr gering
      - Sehr gering
      - Sehr groß

In welchem Aggregatzustand ein Material vorliegt, hängt vom Druck und von der
Temperatur ab; im Abschnitt :ref:`Phasenübergänge <Phasenübergänge>` wird
hierauf näher eingegangen.

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] "Gewicht" und "Schwere" sind nahezu gleichwertige Begriffe: 

    - Mit dem Begriff "Gewicht" gibt man die Kraft an, die ein ruhendes,
      beispielsweise am Boden liegendes Objekt aufgrund seiner Masse im
      Gravitationsfeld eines Planeten aufweist. 
    - Mit dem Begriff "Schwere" bezeichnet man die (beschleunigende) Kraft, die
      auf ein frei bewegliches Objekt im Gravitationsfeld eines Planeten wirkt.

    Die Unterscheidung zwischen "Schwere" und "Gewicht" ist somit vor allem allem
    sprachlicher Natur; beide Begriffe betonen, dass mit dem Vorhandensein von Masse
    stets auch :ref:`Gravitationskräfte <Gravitation>`  vorhanden sind.

.. raw:: latex

    \newpage

.. raw:: html

    <hr />

.. hint::

    Zu diesem Abschnitt gibt es :ref:`Experimente <Experimente
    Körpereigenschaften>` und :ref:`Übungsaufgaben <Aufgaben
    Körpereigenschaften>`.

