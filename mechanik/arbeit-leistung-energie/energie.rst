:keywords: Energie, Energieformen, Potentielle Energie, Höhenenergie, Kinetische
           Energie, Bewegungsenergie, Spannenergie, Energie-Umwandlung,
           Energie-Erhaltung

.. :description: Mechanische Energie

.. index:: Energie, Joule (Einheit)
.. _Energie:
.. _Mechanische Energie:

Mechanische Energie
===================

Zum Heben oder Beschleunigen eines beliebigen Körpers oder zum Verformen eines
elastischen Körpers -- beispielsweise zum Spannen einer Feder -- muss stets
:ref:`mechanische Arbeit <Mechanische Arbeit>` verrichtet werden. Der Körper
wird dadurch in einen neuen Zustand versetzt und ist dabei in der Lage
seinerseits Arbeit verrichten zu können. Dieser Zustand wird durch die
physikalische Größe "Energie" beschrieben.

*Definition:*

    Unter Energie versteht man die Fähigkeit eines Körpers, Arbeit zu
    verrichten. Energie ist damit mit "gespeicherter Arbeit" identisch.

*Einheit:*

    Die Energie wird in der gleichen Einheit wie die Arbeit, also in Joule
    :math:`(\unit{J})` angegeben.

.. math::

    \unit[1]{J} = \unit[1]{N} \cdot \unit[1]{m} = \unit[1]{W \cdot s}

Zur Beschreibung großer Energiemengen werden häufig die Einheiten Kilojoule
:math:`(\unit[1]{kJ} = \unit[1\,000]{J})` und Megajoule :math:`(\unit[1]{MJ} =
\unit[1\,000\,000]{J})` genutzt. Darüber hinaus werden Energiemengen anhand des
Zusammenhangs "Energie ist Leistung mal Zeit" oftmals auch in (Kilo-)Wattstunden
angegeben.

.. math::

    \unit[1]{Wh} = \unit[1]{W} \cdot
    \unit[3\,600]{s} &= \unit[3\,600]{W \cdot s} = \unit[3\,600]{J} \\[4pt]
    \unit[1]{kWh} &= \unit[1\,000]{Wh}

..  Energie ist die Fähigkeit, Arbeit zu verrichten.


.. index:: Energieformen
.. _Arten mechanischer Energie:

Arten mechanischer Energie
--------------------------

Bei mechanischen Prozessen treten folgende Arten mechanischer Energie auf: [#]_

.. index:: Potentielle Energie, Energieformen; Potentielle Energie ("Höhenenergie")
.. _Potentielle Energie:
.. _Höhenenergie:

.. rubric:: Die potentielle Energie ("Höhenenergie")

Um einen Körper entgegen der Schwerkraft anzuheben, muss :ref:`Hubarbeit
<Hubarbeit>` verrichtet werden. Diese ist dann in Form von "Höhenenergie" im
Körper gespeichert. Die Höhenenergie wird häufig auch als potentielle Energie
bezeichnet, da sie durch den freien Fall des angehobenen Körpers wiedergewonnen
werden kann.

*Definition:*

    Die potentielle Energie :math:`E_{\mathrm{pot}}` ist gleich dem Produkt aus
    der Gewichtskraft :math:`F_{\mathrm{G}} = m \cdot g` eines Körpers mit Masse
    :math:`m` sowie der Höhe :math:`h`, die dieser angehoben wird:

.. math::
    :label: eqn-potentielle-energie

    E_{\mathrm{pot}} = F_{\mathrm{G}} \cdot h = m \cdot g \cdot h

Hierbei steht :math:`g` für den :ref:`Ortsfaktor <Ortsfaktor>`. Auf der
Erdoberfläche gilt :math:`g \approx \unit[9,81]{\frac{N}{kg}}`.

Die potentielle Energie eines Körpers als Resultat einer verrichteten Hubarbeit
lässt sich schwerlich als Absolutwert angeben. Steht beispielsweise ein
Gegenstand auf einem Tisch, so hat er gegenüber dem Boden meist eine andere
Höhenenergie als gegenüber der Meereshöhe. Bei Rechnungen legt man daher ein
Null-Niveau fest, auf das man dann die einzelnen potentiellen Energien bezieht.
[#]_

.. index:: Energieformen; Spannenergie, Spannenergie
.. _Spannenergie:

.. rubric:: Die Spannenergie

Beim Verformen eines elastischen Körpers wird die verrichtete :ref:`Spannarbeit
<Spannarbeit>` als Spannenergie im Körper gespeichert und bei einer
Rückverformung wieder freigesetzt. Bekannte Beispiele hierfür sind das Spannnen
einer Schraubenfeder, das Zusammendrücken einer Druckfeder, das Hüpfenlassen
eines Flummis, usw.

*Definition:*

    Die Spannenergie :math:`E_{\mathrm{Spann}}` eines verformten Körpers mit der
    Federkonstanten :math:`D` ist gleich dem Produkt aus der während der
    Verformung durchschnittlich wirkenden Spannkraft :math:`\bar{F} _{\mathrm{S}} =
    \frac{1}{2} \cdot F_{\mathrm{S}} = \frac{1}{2} \cdot D \cdot s` und der
    Ausdehnung :math:`s` aus der Ruhelage:

.. math::
    :label: eqn-spannenergie

    E_{\mathrm{Spann}} = \bar{F} _{\mathrm{S}} \cdot s = \frac{1}{2} \cdot D
    \cdot s^2

Die gespeicherte Spannenergie nimmt somit, solange es sich sich um einen
elastischen Prozess handelt, quadratisch mit der Verformung des Körpers zu.

.. index::
    single: Energieformen; Kinetische Energie ("Bewegungsenergie")
    single: Kinetische Energie
.. _Kinetische Energie:

.. rubric:: Die kinetische Energie ("Bewegungsenergie")

Um einen Körper zu beschleunigen, also ihn auf eine bestimmte Geschwindigkeit
:math:`v` zu bringen, muss die :ref:`Beschleunigungsarbeit
<Beschleunigungsarbeit>` :math:`W_{\mathrm{B}}` verrichtet werden. Diese ist
dann in Form von Bewegungsenergie (häufig auch "kinetische Energie" genannt) im
Körper gespeichert.

*Definition:*

    Die kinetische Energie :math:`E_{\mathrm{Kin}}` ist gleich dem Produkt aus der
    Masse :math:`m` eines Körpers und dem Quadrat seiner Geschwindigkeit
    :math:`v`:

.. math::
    :label: eqn-bewegungsenergie

    E_{\mathrm{B}} = \frac{1}{2} \cdot m \cdot v^2

Die Bewegungsenergie eines Körpers nimmt somit quadratisch mit seiner
Geschwindigkeit zu.

.. index::
    single: Energieformen; Rotationsenergie
    single: Rotationsenergie
.. _Rotationsnergie:

.. rubric:: Die Rotationsenergie

Um einen Körper auf eine bestimmte Winkelgeschwindigkeit :math:`\omega` zu
bringen, muss die :ref:`Rotationsarbeit <Rotationsarbeit>`
:math:`W_{\mathrm{rot}}` verrichtet werden. Diese ist dann in Form von
Rotationsenergie im Körper gespeichert.

*Definition:*

    Die Rotationsenergie :math:`E_{\mathrm{rot}}` ist gleich dem Produkt aus dem
    :ref:`Trägheitsmoment <Trägheitsmoment>` :math:`J` eines Körpers und dem
    Quadrat seiner Winkelgeschwindigkeit :math:`\omega`:

.. math::
    :label: eqn-rotationsenergie

    E_{\mathrm{rot}} = \frac{1}{2} \cdot J \cdot \omega^2


Die kinetische Gesamtenergie eines rollenden Körpers ist gleich der Summe seiner
Bewegungsenergie und seiner Rotationsenergie:

.. math::

    E_{\mathrm{kin,ges}} = E_{\mathrm{B}} + E_{\mathrm{Rot}} = \frac{1}{2} \cdot
    m \cdot v^2 + \frac{1}{2} \cdot J \cdot \omega^2


.. index:: Energie; Energie-Erhaltung
.. _Energieerhaltungssatz:
.. _Energie-Erhaltungssatz:

Der Energie-Erhaltungssatz
--------------------------

Bei rein mechanischen Vorgängen bleibt die Summe der mechanischen Energien
(Höhenenergie, Bewegungsenergie und Spannenergie) konstant.


.. epigraph::

    | "Energie kann weder erzeugt noch vernichtet,
    | sondern stets nur von einer Form in andere
    | umgewandelt werden."


In der Praxis treten allerdings in der Regel nicht zu vernachlässigende
Reibungseffekte auf, die mechanische Energie in Wärme umwandeln. [#]_


.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Weitere Energieformen sind :ref:`elektrische Energie <Elektrische Arbeit
    und Energie>`, magnetische Energie, thermische Energie (Wärme),
    Strahlungsenergie (beispielsweise Licht), Kernenergie und chemische Energie.

.. [#] Arbeit kann in diesem Sinn als Energiemenge aufgefasst werden, die zum
    Anheben eines Gegenstands auf ein anderes Energie-Niveau nötig ist.

.. [#] Diese für den weiteren mechanischen Prozess "verloren gegangene" Energie
    ist dann gleich der verrichteten Reibungsarbeit :math:`W_{\mathrm{R}} =
    F_{\mathrm{R}} \cdot s`.

.. raw:: html

    <hr />

.. hint::

    Zu diesem Abschnitt gibt es :ref:`Experimente <Experimente Mechanische Energie>` und
    :ref:`Übungsaufgaben <Aufgaben Mechanische Energie>`.


