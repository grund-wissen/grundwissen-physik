.. index:: Kraftarten
.. _Arten mechanischer Kräfte:

Arten mechanischer Kräfte
=========================

Bei einer mechanischen Kraft denkt man häufig an Muskelkraft oder die Kraft
eines Motors; weitere mechanische Kräfte, für die es jeweils eigene Formeln
als Rechengrundlage gibt, sind im folgenden Abschnitt näher beschrieben.


.. index:: Kraftarten; Gewichtskraft
.. _Gewichtskraft:

Gewichtskraft
-------------

Die Gewichtskraft eines Objekts ist diejenige Kraft, mit der es von der Erde
angezogen wird.

.. figure:: ../../pics/mechanik/dynamik/gewichtskraft-erde.png
    :name: fig-gewichtskraft
    :alt:  fig-gewichtskraft
    :align: center
    :width: 50%

    Die Richtung der Gewichtskraft auf der Erde.

    .. only:: html

        :download:`SVG: Gewichtskraft auf der Erde
        <../../pics/mechanik/dynamik/gewichtskraft-erde.svg>`

Je größer die Masse eines Objekts ist, desto stärker wird es von der Erde
angezogen. Bei einer größeren Masse ist allerdings auch eine größere Kraft
nötig, um sie zu beschleunigen; ohne Luftwiderstand werden daher alle Objekte,
die sich im freien Fall befinden, gleich schnell zum Erdmittelpunkt hin
beschleunigt.

.. index:: Ortsfaktor
.. _Ortsfaktor:

*Formel:*

    Der Wert der Gewichtskraft :math:`F_{\mathrm{G}}`, die ein Objekt der Masse
    :math:`m` durch die Anziehungskraft eines Planeten erfährt, ist proportional
    zum so genannten Ortsfaktor :math:`\vec{g}`: [#]_

    .. math::
        :label: eqn-gewichtskraft

        \vec{F}_{\mathrm{G}} = m \cdot \vec{g}


.. index:: Gravitation
.. _Gravitation:

Auf der Erdoberfläche gilt für den Ortsfaktor, wie sich aus dem allgemeinen
Gravitationsgesetz ableiten lässt, näherungsweise :math:`g = |\vec{g}| =
\unit[9,81]{\frac{N}{kg}}`. [#]_

*Beispiele:*

* Ein Objekt mit einer Masse von :math:`\unit[1,0]{kg}` hat auf der Erde eine
  Gewichtskraft von

  .. math::

      F_{\mathrm{G, Erde}} = m \cdot g = \unit[1]{kg} \cdot
      \unit[9,81]{\frac{N}{kg}} = \unit[9,81]{N}

* Ein Objekt mit einer Masse von :math:`\unit[50]{kg}` hat auf der Erde eine
  Gewichtskraft von

  .. math::

      F_{\mathrm{G, Erde}} = \unit[50]{kg} \cdot \unit[9,81]{\frac{N}{kg}} =
      \unit[490,5]{N}

Das Gewicht eines Objekts ist nicht an allen Stellen auf der Erde exakt
gleich, sondern hängt vom Ort ab, an dem es sich befindet:

* Auf einem hohen Berg hat ein Objekt ein etwas geringeres Gewicht
  als in Höhe des Meeresspiegels.
* An verschiedenen Stellen der Erde hat jedes Objekt -- da die Erde keine
  ideale Kugelgestalt hat, sondern zu den Polen hin etwas "abgeflacht" ist
  -- ebenfalls ein geringfügig unterschiedliches Gewicht. Im Vergleich zu
  Mitteleuropa ist ein Objekt am Äquator etwas leichter, an den Polen etwas
  schwerer.
* Auf dem Mond oder auf anderen Planeten hängt die Gewichtskraft, die ein Objekt
  erfährt, von der Masse des jeweiligen Himmelskörpers ab: Je schwerer ein
  Planet ist, desto größer ist die Anziehungskraft, die er auf andere Massen
  ausübt.

.. list-table::
    :name: tab-ortsfaktoren-beispiele
    :widths: 40 40

    * - Ort
      - Ortsfaktor in :math:`\unit[]{\frac{N}{kg}}`
    * - Äquator
      - :math:`9,78`
    * - Mitteleuropa
      - :math:`9,81`
    * - Pole der Erde
      - :math:`9,83`
    * - :math:`\unit[300]{km}` über der Erde
      - :math:`8,96`
    * - :math:`\unit[40\, 000]{km}` über der Erde
      - :math:`0,19`
    * - Mond der Erde
      - :math:`1,60`
    * - Venus
      - :math:`8,87`
    * - Mars
      - :math:`3,69`
    * - Merkur
      - :math:`3,70`
    * - Jupiter
      - :math:`24,79`
    * - Saturn
      - :math:`10,44`
    * - Sonne
      - :math:`274`

Auf dem Mond hat ein Objekt der Masse :math:`\unit[1]{kg}` eine
Gewichtskraft von

.. math::

   F_{\mathrm{G, Mond}} = \unit[1]{kg} \cdot
   \unit[1,62]{\frac{N}{kg}} = \unit[1,62]{N}

Auf der Sonne erfährt ein Objekt der Masse :math:`\unit[1]{kg}` eine
Gewichtskraft von

.. math::

   F_{\mathrm{G, Sonne}} = \unit[1]{kg} \cdot \unit[274]{\frac{N}{kg}} =
   \unit[274]{N}

Im Universum haben Objekte also überall die gleiche Masse, jedoch nicht das
gleiche Gewicht.


.. index::
    single: Reibung
    single: Kraftarten ; Reibungskraft
.. _Reibungskraft:

Reibungskraft
-------------

Erfahrungsgemäß kommt jedes bewegte Objekt, das nicht angetrieben wird, nach
einer gewissen Zeit zur Ruhe. Da seine Geschwindigkeit abnimmt, muss eine
bremsende Kraft wirken. Eine derartige Kraft nennt man Reibungskraft
:math:`F_{\mathrm{R}}`.

Reibungskräfte treten immer auf, wenn sich Objekte berühren und gegeneinander
bewegen. Ursache dafür sind die unebenen Oberflächen der Objekte und
Kohäsionskräfte, die zwischen den Molekülen der aneinander reibenden Objekte
wirken.

.. index::
    single: Reibung; Haftreibung
    single: Haftreibung
.. _Haftreibung:

.. rubric:: Haftreibung

Bei starker Vergrößerung gleicht selbst eine geschliffene Oberfläche einem
kleinen Gebirge mit vielen Zacken und Spitzen. Haften zwei Objekte aneinander,
so verhaken sich diese Spitzen ineinander. Versucht man die Objekte
gegeneinander zu bewegen, so werden die Zacken etwas verformt; einer stärkeren
Zugkraft wirkt eine stärkere Haftreibungskraft entgegen.

.. figure:: ../../pics/mechanik/dynamik/haftreibung.png
    :name: fig-haftreibung
    :alt:  fig-haftreibung
    :align: center
    :width: 80%

    Stark vergrößerte Darstellung der Oberfläche von gleitenden Körpern
    und Modelldarstellung der Haftreibung.

    .. only:: html

        :download:`SVG: Haftreibung
        <../../pics/mechanik/dynamik/haftreibung.svg>`

Je stärker zwei Objekte aneinander gepresst sind, desto stärker ist die maximale
Haftreibungskraft (als anschauliches Beispiel kann man zwei Bürsten ineinander
stecken und versuchen sie gegeneinander zu bewegen).

*Formel:*

    Haften zwei Objekte aneinander, so ist der Betrag der maximalen
    Haftreibungskraft :math:`F_{\mathrm{R,Haft,max.}}` proportional zu der
    Normalkraft :math:`F_{\perp}`, die beide Körper aneinander presst:

    .. math::

        F_{\mathrm{R,Haft,max.}} = \mu_{\mathrm{H}} \cdot F_{\perp}

.. _Reibungszahl:
.. _Haftreibungszahl:

Die Proportionalitätskonstante heißt Haftreibungszahl :math:`\mu_{\mathrm{H}}`
und hängt vom Stoff und von der Oberflächenbeschaffenheit der Objekte ab. Ist
die angreifende Kraft größer als die maximale Haftreibungskraft, so beginnen die
Objekte relativ zueinander zu gleiten.

.. list-table:: Haft- und Gleitreibungszahlen einiger Materialien
    :name: tab-reibungszahlen-beispiele
    :widths: 50 50 50

    * - Stoffpaar
      - Haftreibungszahl :math:`\mu_{\mathrm{H}}`
      - Gleitreibungszahl :math:`\mu_{\mathrm{H}}`
    * - Holz auf Holz
      - :math:`0,5 \text{ bis } 0,6`
      - :math:`0,2 \text{ bis } 0,4`
    * - Stahl auf Stahl
      - :math:`0,15`
      - :math:`0,06`
    * - Stahl auf Eis
      - :math:`0,03`
      - :math:`0,01`
    * - Autoreifen auf Beton (trocken)
      - :math:`1,00`
      - :math:`0,60`
    * - Autoreifen auf Beton (nass)
      - :math:`0,50`
      - :math:`0,30`
    * - Autoreifen auf Eis
      - :math:`0,10`
      - :math:`0,05`

.. Tipler: Autoreifen auf Beton trocken 1,0 beziehungsweise 0,8.

.. index::
    single: Reibung; Gleitreibung
    single: Gleitreibung
.. _Gleitreibung:

.. rubric:: Gleitreibung

Bewegen sich zwei Objekte gegeneinander, so schlittern die rauhen Oberflächen
übereinander hinweg. Sie können sich -- anders als bei der Haftreibung -- nicht
völlig ineinander verhaken.

.. figure:: ../../pics/mechanik/dynamik/gleitreibung.png
    :name: fig-gleitreibung
    :alt:  fig-gleitreibung
    :align: center
    :width: 33%

    Modelldarstellung der Gleitreibung.

    .. only:: html

        :download:`SVG: Gleitreibung
        <../../pics/mechanik/dynamik/gleitreibung.svg>`

*Formel:*

    Die Gleitreibungskraft :math:`F_{\mathrm{R,Gleit}}` hängt -- wie auch die
    Haftreibungskraft -- von der zusammenpressenden Gewichts- oder Normalkraft
    :math:`F_{\perp}` und der Oberflächenbeschaffenheit der Objekte ab:

    .. math::

        F_{\mathrm{R,Gleit}} = \mu_{\mathrm{G}} \cdot F_{\perp}

Die Gleitreibungszahl :math:`\mu_{\mathrm{G}}` ist stets kleiner als die
`Haftreibungszahl`_ :math:`\mu_{\mathrm{H}}`.

.. index::
    single: Reibung; Rollreibung
    single: Rollreibung
.. _Rollreibung:

.. rubric:: Rollreibung

Rollt ein Objekt auf dem anderen entlang, so können die Unebenheiten der
Oberflächen deutlich leichter überwunden werden. Die Rollreibungskraft ist bei
gleicher zusammenpressender (Gewichts-)Kraft wesentlich kleiner als die
Gleitreibungskraft.

.. figure:: ../../pics/mechanik/dynamik/rollreibung.png
    :name: fig-rollreibung
    :alt:  fig-rollreibung
    :align: center
    :width: 80%

    Stark vergrößerte Darstellung eines auf einer Unterlage abrollenden
    Rades und Modellvorstellung der Rollreibung.

    .. only:: html

        :download:`SVG: Rollreibung
        <../../pics/mechanik/dynamik/rollreibung.svg>`

Um unerwünschte Reibungskräfte zu verringern, verwendet man Schmiermittel
(Fett, Öl). Dadurch wird der Raum zwischen den sich reibenden Flächen
ausgefüllt, so dass sich die Unebenheiten der Körper nicht mehr so störend
auswirken.

.. list-table:: Rollreibungszahlen einiger Materialien
    :name: tab-rollreibung
    :widths: 50 50

    * - Stoffpaar
      - Rollreibungszahl :math:`\mu_{\mathrm{R}}`
    * - Eisen auf Eisen
      - :math:`\text{circa } 0,005`
    * - Kugeln im Kugellager
      - :math:`\text{circa } 0,001`

In sehr vielen Fällen sind Reibungskräfte allerdings unterlässlich: Ohne
Reibungskräfte zwischen den Rädern von Fahrzeugen und der Straße wäre eine
gezielte Fortbewegung unmöglich: Die Räder würden durchdrehen. Um ihnen vielmehr
eine möglichst gute Straßenlage zu geben, werden die Reifen aus Spezialgummi
gefertigt und mit Profilen versehen. Ohne Reibung wären auch Bremsen
oder gar Klebstoffe unmöglich.


.. index:: Strömungswiderstand, Luftwiderstand
.. _Luftwiderstand:

.. rubric:: Strömungswiderstand

Bewegt sich ein Objekt durch ein flüssiges oder gasförmiges Medium, so muss es
stets einen Strömungswiderstand (beispielsweise Luftwiderstand) überwinden.
Hierbei hängt die Größe der Widerstandskraft von der Dichte :math:`\rho` des
durchquerten Mediums, der Querschnittsfläche :math:`A` des Körpers, dem Quadrat
seiner Geschwindigkeit :math:`v^2` sowie einem so genannten "Widerstandsbeiwert"
:math:`c_{\mathrm{w}}` ab; letzterer gibt den Einfluss der Objektform an.

Beispielsweise gilt für die Luftwiderstandskraft :math:`F_{\mathrm{L}}`
näherungsweise folgende Formel: [#LW]_

.. math::

    F_{\mathrm{L}} = \frac{1}{2} \cdot c_{\mathrm{w}} \cdot \rho_{\mathrm{L}}
    \cdot A \cdot v^2

Bei üblichen Straßenfahrzeugen kann der Widerstandsbeiwert im optimalen Falle
:math:`0,09` betragen, bei Omnibusssen sind Werte bis zu :math:`0,6` üblich.

.. list-table::
    :name: tab-luftwiderstandsbeiwerte-beispiele
    :widths: 50 50

    * - Gegenstand
      - :math:`c_{\mathrm{w}}`-Wert
    * - Halbkugel (konkav), Fallschirm
      - :math:`1,33`
    * - Rechteckige Platte
      - :math:`1,1` bis :math:`1,3`
    * - Kreisförmige Platte
      - :math:`1,11`
    * - Mensch (stehend)
      - :math:`0,78`
    * - LKW
      - :math:`0,6` bis :math:`0,9`
    * - Fahrradfahrer (Mountainbike)
      - :math:`0,5` bis :math:`0,7`
    * - Kugel
      - :math:`0,25` bis :math:`0,45`
    * - Halbkugel (konvex)
      - :math:`0,34`
    * - Tropfen (Stromlinienform)
      - :math:`0,02`


Die Dichte der Luft beträgt unter Normalbedingungen :math:`\rho_{\mathrm{Luft}} =
\unit[1,29]{kg/m^3}`. Für die Berechnung der Wasserwiderstandkraft muss mit der
entsprechend höheren Dichte von Wasser :math:`(\rho_{\mathrm{Wasser}} =
\unit[1000]{kg/m^3})` gerechnet werden.


.. index:: Kraftarten; Spannkraft, Federkraft
.. _Spannkraft:
.. _Federkraft:

Spannkraft
----------

Drückt man einen elastischen Gegenstand, beispielsweise eine Schraubenfeder,
zusammen oder zieht ihn auseinander, so wirkt in ihm eine entgegengesetzt
gerichtete Kraft, die ihn wieder auf ihre ursprüngliche Länge zurück zu formen
versucht.

*Formel:*

    Je weiter die Wegstrecke :math:`s` ist, um die eine Schraubenfeder gestaucht
    oder gedehnt wird, desto stärker ist die rückstellende Spannkraft
    :math:`F_{\mathrm{S}}` der Feder.

.. math::
  :label: eqn-spannkraft

  \vec{F}_{\mathrm{S}} = - D \cdot \vec{s}

Die Federkonstante :math:`D` ist dabei von der Form und dem Material der Feder
beziehungsweise des elastischen Körpers abhängig. Die Federkonstante (und damit
die Federhärte) einer Schraubenfeder ist beispielsweise umso größer, je dicker
der Draht ist und je enger er gewickelt ist; sie wird im Allgemeinen in Newton
je Meter :math:`(\unit{N/m})` angegeben.

Das Minuszeichen in Gleichung :eq:`eqn-spannkraft` bedeutet, dass die Richtung der
Auslenkung der Feder :math:`s` von ihrer Ruhelage der Richtung der Federkraft
entgegengesetzt ist. Gleichung :eq:`eqn-spannkraft` wird zu Ehren ihres
Entdeckers, `Robert Hooke <https://de.wikipedia.org/wiki/Robert_Hooke>`_, auch
als "Hookesches Gesetz" bezeichnet.


.. index::
    single: Kraftarten; Radialkraft
    single: Radialkraft
    single: Zentripetalkraft
    single: Zentrifugalkraft
.. _Radialkraft:
.. _Zentrifugalkraft:
.. _Zentripetalkraft:

Radialkraft
-----------

Ein Körper bewegt sich aufgrund seiner Masse stets entlang einer geradlinigen
Bahn, wenn keine Kraft auf ihn einwirkt. Eine :ref:`kreisförmige Bewegung
<Kreisförmige Bewegung>` ist somit nur möglich, wenn eine Kraft den Körper auf
der Kreisbahn hält, also ihn kontinuierlich zum Kreismittelpunkt hin
beschleunigt. Diese Kraft wird Radialkraft beziehungsweise Zentripetalkraft
genannt.

..
    TODO Pic: Kreis Bahngeschwindigkeit links links oben, zeigt nach rechts oben,
    Radialbeschleunigung zur Mitte

Für den Betrag der Radialkraft gilt ebenfalls das :ref:`Kraftgesetz
<Kraftgesetz>` :math:`F = m \cdot a`. Mit der :ref:`Radialbeschleunigung
<Radialbeschleunigung>` :math:`a = \frac{v^2}{r}` folgt für die Radialkraft
:math:`F_{\mathrm{rad}}`:

.. math::

    F_{\mathrm{rad}} = m \cdot \frac{v^2}{r}

Befindet man sich als Beobachter selbst auf einer Kreisbahn, so nimmt man
hingegen die entsprechende Gegenkraft ("Zentrifugalkraft") wahr. Sitzt man
beispielsweise in einem Fahrzeug, das nach links lenkt, so scheint eine Kraft zu
wirken, die den eigenen Körper zur rechten Seite hin beschleunigt
(:ref:`Scheinkraft <Scheinkraft>`). In Wirklichkeit versucht man sich aufgrund
der Trägheit geradeaus zu bewegen und wird erst durch die zum Kreismittelpunkt
hin wirkende Radialkraft auf die Kreisbahn gezwungen.

.. figure:: ../../pics/mechanik/dynamik/zentrifuge.png
    :name: fig-zentrifuge
    :alt:  fig-zentrifuge
    :align: center
    :width: 70%

    Modell einer einfachen Zentrifuge.

    .. only:: html

        :download:`SVG: Zentrifuge
        <../../pics/mechanik/dynamik/zentrifuge.svg>`

Technisch wird die Radialkraft beispielsweise in Zentrifugen genutzt. Dabei wird
ein zu trennendes Gemisch an Substanzen, die sich beispielsweise in einem
Reagenzglas befinden, in eine Kreisbewegung mit hoher Winkelgeschwindigkeit und
kleinem Bahnradius versetzt. Das Stoffgemisch wird dabei gemäß seiner
Dichte-Anteile aufgetrennt, die "schwereren" Substanzen bewegen sich dabei
aufgrund ihrer Trägheit nach außen und lagern sich so am Boden des rotierenden
Gefäßes ab. Diese Schichtung bleibt auch nach einem Abschalten der Zentrifuge
bestehen, da letztlich nichts anderes als ein Sedimentationsvorgang
stattgefunden hat -- nur ein sehr schneller. Die durch die Radialkraft bewirkte
Radialbeschleunigung kann mit Zentrifugen beziehungsweise Ultrazentrifugen ein
:math:`100`- bis :math:`250\,000`-faches der Erdbeschleunigung :math:`g`
betragen.

..  Damit lassen sich auch hochmolekulare Stoffe (beispielsweise Eiweiße)
..  auftrennen.


.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Der Ortsfaktor :math:`g = \unit[9,81]{\frac{N}{kg}} =
    \unit[9,81]{\frac{m}{s^2}}` wird bisweilen auch als :ref:`Erdbeschleunigung
    <Erdbeschleunigung>` bezeichnet. Er gibt diejenige Beschleunigung an,
    die ein Körper im freien Fall in Erdnähe erfährt, sofern der Luftwiderstand
    vernachlässigbar ist. Die Gleichheit der Einheiten ergibt sich aus dem
    :ref:`Newtonschen Kraftgesetz <Kraftgesetz>`:

    .. math::

        \unit{N} = \unit{kg \cdot \frac{m}{s^2}} \quad \Longleftrightarrow \quad
        \unit{\frac{N}{kg}} = \unit{\frac{m}{s^2}}

    Der Ortsfaktor kann somit einerseits als Beschleunigungs-Wert aufgefasst
    werden (wenn sich ein Objekt im freien Fall befindet) als auch als
    Umrechnungsfaktor zwischen der Masse :math:`m` und der Gewichtskraft
    :math:`F_{\mathrm{G}}`: :math:`\unit[1]{kg} \stackrel{\wedge}=
    \unit[9,81]{N}`.

.. [#] Genau genommen ist die obige Formel eine Näherung für das allgemeine
    Gravitationsgesetz, wonach auf zwei Körper mit den Massen :math:`m_1` und
    :math:`m_2` stets eine anziehende Kraft :math:`F_{\mathrm{G}}` wirkt. Ihr
    Betrag ist von den beiden Massen sowie vom Abstand :math:`r` zwischen ihren
    Schwerpunkten abhängig:

     .. math::

         F_{\mathrm{G}} = \gamma \cdot \frac{m_1 \cdot m_2}{r^2}

    Dabei ist :math:`\gamma = \unit[6,67 \cdot 10^{-11}]{\frac{m^3}{kg \cdot
    s^2}}` die allgemeine Gravitationskonstante. Für die Schwerkraft, die ein
    Körper in Nähe der Erdoberfläche erfährt, kann näherungsweise und :math:`r
    \approx r_{\mathrm{E}} = \unit[6371]{km}` gesetzt werden (der Abstand eines
    Gegenstands von der Erdoberfläche ist meist vernachlässigbar klein gegenüber
    dem Erdradius). Mit der Erdmasse :math:`m_{\mathrm{E}} = \unit[5,972 \cdot
    10^{24}]{kg}` kann der Ortsfaktor :math:`g` somit folgendermaßen definiert
    werden:

    .. math::

        g = \gamma \cdot \frac{m_2}{r_{\mathrm{E}}^2} \, \approx \, \unit[9,81]{\frac{m}{s^2}}

    Für die Gewichtskraft eines Körpers :math:`m` auf der Erde gilt damit in
    guter Näherung:

    .. math::

        F_{\mathrm{G}} = \gamma \cdot \frac{m \cdot m_{\mathrm{E}}}{r_{\mathrm{E}}^2}
        \approx m \cdot g

.. [#LW] Bei turbulenten Strömungen mit komplexen Luftverwirbelungen lässt sich
    der Luftwiderstand nicht mit Hilfe einer einzelnen Formel berechnen, sondern
    erfordert aufwendige Computer-Simulationen und numerische Verfahren.

    Die Formel :math:`F_{\mathrm{LW}} = \frac{1}{2} \cdot \rho_{\mathrm{L}}
    \cdot v^2 \cdot A \cdot c_{\mathrm{w}}` lässt sich aus dem Zusammenhang
    :math:`F = p_{\mathrm{dyn}} \cdot A` zwischen Kraft, :ref:`dynamischem Druck
    <Dynamischer Druck>`  und Fläche herleiten; der Luftwiderstandsbeiwert ist
    als reiner Zahlenwert lediglich ein zusätzlicher Gewichtungsfaktor.

.. raw:: html

    <hr />

.. hint::

    Zu diesem Abschnitt gibt es :ref:`Experimente <Experimente Arten
    mechanischer Kräfte>` und :ref:`Übungsaufgaben <Aufgaben Arten mechanischer
    Kräfte>`.

