.. index:: Leistung, Watt (Einheit)
.. _Leistung:
.. _Mechanische Leistung:

Mechanische Leistung
====================

Mechanische Arbeit kann unterschiedlich schnell verrichtet werden. Die
mechanische Leistung (umgangssprachlich auch "Arbeitstempo" genannt) gibt an,
wie schnell mechanische Arbeit verrichtet wird.

*Definition:*

    Die Leistung :math:`P` ist gleich dem Verhältnis aus der Arbeit :math:`W`
    und der Zeit :math:`t`, in der sie verrichtet wird. [#]_

.. math::
    :label: eqn-leistung

    P = \frac{W}{t}

*Einheit:*

    Die Leistung wird (zu Ehren des Ingenieurs `James Watt
    <https://de.wikipedia.org/wiki/James_Watt>`_) in Watt :math:`(\unit{W})`
    angegeben. Eine Leistung von einem Watt entspricht einer in einer Sekunde
    geleisteten Arbeit von einem Joule:

.. math::

    \unit[1]{W} = \frac{\unit[1]{J}}{\unit[1]{s}}

*Beispiel:*

* Zwei Kräne ziehen jeweils eine Palette mit Steinen, die einer Gewichtskraft
  :math:`F_{\mathrm{G}} = \unit[4\,000]{N}` entspricht, auf ein :math:`\unit[5]{m}` hohes
  Gerüst. Der eine Kran braucht für diese Arbeit eine Zeit von :math:`t
  _1 = \unit[10]{s}`, der andere Kran benötigt hingegen :math:`t
  _2 = \unit[20]{s}`. Damit können die Leistungen :math:`P_1` und
  :math:`P_2` der beiden Kräne berechnet werden:

  .. math::

      P_1 = \frac{W_{\mathrm{Hub} }}{t_1} = \frac{F_{\mathrm{G}} \cdot h}{t_1} =
      \frac{\unit[4\,000]{N} \cdot \unit[5]{m}}{\unit[10]{s}} =
      \frac{\unit[20\,000]{J}}{\unit[10]{s}} = \unit[2\,000]{W} \\[5pt]
      P_2 = \frac{W_{\mathrm{Hub} }}{t_2} = \frac{F_{\mathrm{G}} \cdot h}{t_2} =
      \frac{\unit[4\,000]{N} \cdot \unit[5]{m}}{\unit[20]{s}} =
      \frac{\unit[20\,000]{J}}{\unit[20]{s}} = \unit[1\,000]{W}

  Da der erste Kran die Arbeit in der halben Zeit verrichtet, ist seine Leistung
  (sein "Arbeitstempo") doppelt so hoch wie die des zweiten Kranes.

.. list-table:: Beispiele für Leistungen in Natur und Technik
    :name: tab-leistungen-in-natur-und-technik
    :widths: 50 50

    * - Spielzeugmotor
      - :math:`\phantom{0}3 \text{ bis } \unit[12]{W}`
    * - Mensch (Dauerleistung)
      - :math:`75 \text{ bis } \unit[100]{W}`
    * - Bohrmaschine
      - :math:`300 \text{ bis } \unit[1\,000]{W}`
    * - Motorrad
      - :math:`\text{Ca. } \unit[15\,000]{W}`
    * - PKW
      - :math:`\text{Ca. } \unit[55\,000]{W}`
    * - LKW
      - :math:`\text{Ca. } \unit[250\,000]{W}`
    * - Elektro-Lokomotive
      - :math:`\text{Ca. } \unit[5\,000\,000]{W}`
    * - Verkehrsflugzeug
      - :math:`\text{Ca. } \unit[35\,000\,000]{W}`
    * - Passagierschiff
      - :math:`\text{Ca. } \unit[40\,000\,000]{W}`
    * - Weltraum-Rakete
      - :math:`\text{Ca. } \unit[75\,000\,000\,000]{W}`
    * - Blitz
      - :math:`\text{Ca. } \unit[500\,000\,000\,000]{W}`

..
    D-Zug 1250 kW nach Gascha 61.

Die mechanische Leistung, die ein Mensch über einen langen Zeitraum aufrecht
erhalten kann, liegt bei etwa :math:`\unit[100]{W}`. Kurzzeitig kann ein gut
trainierter Mensch auch eine Leistung in der Größenordnung von
:math:`\unit[1\,000]{W}` erreichen. Große Leistungsmengen werden nach wie vor
häufig in Pferdestärken :math:`(\unit{PS})` anstelle in Kilowatt
:math:`(\unit{kW})` angegeben.

.. math::

    \unit[1]{kW} = \unit[1\,000]{W} \\
    \unit[1]{PS} \approx \unit[735,5]{W}

Eine weitere nützliche Formel erhält man, wenn man in der Definition
:eq:`eqn-leistung` für die Arbeit :math:`W = F \cdot s` schreibt. Für die
Leistung :math:`P` gilt damit:

.. math::
    :label: eqn-leistung2

    P = \frac{F \cdot s}{t} = F \cdot \frac{s}{t} = F \cdot v

Gemäß dieser Gleichung ist zum Beispiel eine höhere Leistung nötig, um einen
Gegenstand bei einer konstant wirkenden Reibung mit höherer Geschwindigkeit zu
ziehen. 


.. _Leistung von rotierenden Objekten:

.. rubric:: Leistung von rotierenden Objekten

Vorgänge, bei denen Verschiebungen (Translationen) oder Drehungen (Rotationen)
von Objekten stattfinden, lassen sich durch mathematisch ähnliche Gleichungen
beschreiben. Das Äquivalent zur Kraft :math:`F` ist bei Rotationen das
:ref:`Drehmoment <Drehmoment>`  :math:`M`, das Äquivalent zur Geschwindigkeit
:math:`v` ist die :ref:`Winkelgeschwindigkeit <Winkelgeschwindigkeit>`
:math:`\omega`. Ersetzt man in der obigen Formel :eq:`eqn-leistung2` die
jeweiligen Größen, so erhält man folgende Formel:

.. math::
    :label: eqn-leistung-rotation

    P = M \cdot \omega

Ein Motor kann somit eine bestimmte Leistung entweder durch eine große Drehzahl
oder ein großes Drehmoment erreichen; ist die Winkelgeschwindigkeit
:math:`\omega` gleich Null, so ist auch die mechanische Leistung des Motors
gleich Null, egal wie hoch sein Drehmoment ist.

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Das Symbol :math:`P` für die Leistung leitet sich vom englischen Wort
       "Power" ab.

.. raw:: html

    <hr />

.. hint::

    Zu diesem Abschnitt gibt es :ref:`Experimente <Experimente Mechanische
    Leistung>` und :ref:`Übungsaufgaben <Aufgaben Mechanische Leistung>`.
