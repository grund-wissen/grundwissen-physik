
.. _Bewegungen mit konstanter Geschwindigkeit:

Bewegungen mit konstanter Geschwindigkeit
=========================================

Im folgenden Abschnitt werden zunächst anhand von eindimensionalen Bewegungen
einige grundlegende Konzepte zur mathematischen Beschreibung von
Bewegungsvorgängen vorgestellt; diese werden dann auf zwei- beziehungsweise
dreidimensionale Vorgänge übertragen.

.. index::
    single: Bewegung; Geradlinige Bewegung
    single: Geradlinige Bewegung
.. _Geradlinige Bewegung:
.. _Geradlinige Bewegungen:
.. _Eindimensionale Bewegung:
.. _Eindimensionale Bewegungen:

Eindimensionale Bewegungen mit konstanter Geschwindigkeit
---------------------------------------------------------

Eine geradlinige Bewegung stellt die einfachste Variante eines Bewegungsvorgangs
dar: Es genügt bereits eine einzelne Raumachse als Koordinatensystem. Hat man
(willkürlich, aber verbindlich) den Nullpunkt sowie die Richtung der
Koordinatenachse einmalig festgelegt, so genügt folglich eine einzige
Längenangabe :math:`s`, um den Ort des Objekts bezüglich des
Koordinatenursprungs exakt angeben zu können:

* Hat der Ort :math:`s` einen positiven Wert, so befindet sich das Objekt um den
  entsprechenden Wert entlang der als positiv gewählten Raumrichtung vom
  Koordinatenursprung entfernt.

* Hat der Ort :math:`s` einen negativen Wert, so befindet sich das Objekt um den
  entsprechenden Wert entgegen der als positiv gewählten Raumrichtung vom
  Koordinatenursprung entfernt.

Bei Bewegungsvorgängen ändert sich der Ort :math:`s` des Objekts im zeitlichen
Verlauf; man schreibt daher häufig auch explizit :math:`s(t)`, um die
Abhängigkeit des Orts :math:`s` von der Zeit :math:`t` auszudrücken.

.. figure:: ../../pics/mechanik/kinematik/geradlinige-bewegung.png
    :name: fig-geradlinige-bewegung
    :alt:  fig-geradlinige-bewegung
    :align: center
    :width: 50%

    Die Bewegung eines Hundes, der einem Stöckchen nacheilt oder es
    zurückbringt, kann in guter Näherung als geradlinige Bewegung aufgefasst
    werden.

    .. only:: html

        :download:`SVG: Geradlinige Bewegung
        <../../pics/mechanik/kinematik/geradlinige-bewegung.svg>`

.. index:: Delta-Schreibweise
.. rubric:: Die :math:`\Delta`-Schreibweise

Das Symbol :math:`s` wird nicht nur für Ortsangaben verwendet, sondern ebenfalls
um zurückgelegte Wegstrecken anzugeben. In diesem Fall wählt man allerdings
bevorzugt die Schreibweise :math:`\Delta s`, um Verwechslungen zu vermeiden. Das
:math:`\Delta`-Symbol (ein griechisches "Delta") steht dabei für "Differenz" --
gemeint ist damit, inwiefern sich der Wert von :math:`s_{\mathrm{end}}` am Ende
des Bewegungsvorgangs von dem Wert :math:`s_{\mathrm{start}}` zu Beginn des
Bewegungsvorgangs unterscheidet:

.. math::

    \Delta s &= s_{\mathrm{end}} - s_{\mathrm{start}} \\
     &= \;s \;\;\; - \;\, s_0

Dass bei dieser Konvention der Startwert (meist mit :math:`s_0` bezeichnet) vom
Endwert (meist mit :math:`s` bezeichnet) abgezogen wird, hat folgenden Grund:

* Ist der Anfangswert :math:`s_0` kleiner als der Endwert :math:`s`, so verläuft
  die Bewegung entlang der als positiv definierten Bewegungsrichtung.

* Ist umgekehrt der Endwert :math:`s` kleiner als der Anfangswert :math:`s_0`,
  so verläuft die Bewegung in Richtung der negativen Koordinatenachse.

Gilt für den Startwert :math:`s_0 = 0`, so beginnt die Bewegung am Nullpunkt des
Koordinatensystems, und für den Zeitpunkt :math:`t` gilt :math:`\Delta s = s
-s_0 = s`. In diesem Fall stimmt somit zu einem Zeitpunkt :math:`t` der Ort
:math:`s(t)` mit der zurückgelegten Wegstrecke :math:`\Delta s` überein, und das
:math:`\Delta` kann weggelassen werden; im Allgemeinen ist dies jedoch nicht der
Fall.

Die gleiche :math:`\Delta`-Schreibweise wird auch für einzelne Zeitabschnitte
verwendet; auch hier gilt beispielsweise :math:`\Delta t = t_{\mathrm{end}} -
t_{\mathrm{start}}`. Diese Schreibweise hat den Vorteil, dass man einen Vorgang
in verschiedenen Zeitabschnitten :math:`\Delta t_1 = t_1 - t_0`, :math:`\Delta
t_2 = t_2 - t_1`, usw. unterteilen kann, sofern in diesen beispielsweise
unterschiedliche Geschwindigkeiten oder Bewegungsrichtungen vorliegen; eine
komplexe Aufgabenstellung kann so in mehrere einfacher zu lösende Teile zerlegt
werden.


.. In der Physik versucht man die realen Vorgänge mit möglichst einfachen, aber
.. auch praktisch geeigneten Modellen zu beschreiben. Beispielsweise kann man für
.. vielerlei Bewegungsvorgänge, bei denen es nur um zurückgelegte Wegstrecken, aber
.. jedoch auf den konkreten Wegverlauf ankommt, auf das einfache Modell einer
.. geradlinigen Bewegung zurückgreifen.

.. Im eigentlichten Sinn verläuft eine geradlinige Bewegung eindimensional entlang
.. einer einzigen Raumrichtung. Um einen solchen Bewegungsvorgang mittels Formeln
.. beschreiben zu können, muss man sich zunächst für ein geeignetes
.. Koordinatensystem entscheiden. Insbesondere die Wahl des Koordinatenursprungs
.. ist dabei von Bedeutung: Sie kann einmalig zu Beginn einer Aufgabenstellung
.. willkürlich erfolgen, ist dann für den weiteren Verlauf jedoch bindend.

.. Zur Beschreibung einer geradlinigen Bewegungen genügt, da es sich um einen
.. eindimensionalen Prozess handelt, eine einzige Koordinatenachse. In welcher
.. Entfernung sich das beobachtete Objekt vom gewählten Nullpunkt dieser
.. Koordinatenachse befindet, kann -- in Abhängigkeit von der Zeit :math:`t` --
.. durch Angabe eines Punktes :math:`s (t)` auf dieser Achse bestimmt werden.

.. index:: Geschwindigkeit
.. _Geradlinige Bewegungen mit konstanter Geschwindigkeit:

.. rubric:: Definition von Geschwindigkeit

Bewegt sich ein Objekt mit konstanter Geschwindigkeit, so legt es in gleichen
Zeitabschnitten die jeweils gleiche Wegstrecke zurück.

*Definition:*

    Die Geschwindigkeit :math:`v` eines sich mit konstanter Geschwindigkeit
    bewegenden Objekts ist gleich dem Verhältnis aus der zurückgelegten
    Wegstrecke :math:`\Delta s` und der dazu benötigten Zeit :math:`\Delta t`:

    .. math::
        :label: eqn-geschwindigkeit

        v = \frac{\Delta s}{\Delta t}

..  = \frac{s_2 - s_1}{t_2 - t_1}

*Einheit:*

    Die Geschwindigkeit wird meist in Kilometer je Stunde
    (:math:`\unitfrac{km}{h}`) oder in Meter je Sekunde (:math:`\unitfrac{m}{s}`)
    angegeben.

*Beispiele:*

* Licht legt in einer Sekunde :math:`\unit[300\,000]{km}` zurück. Die
  Lichtgeschwindigkeit beträgt somit :math:`\unitfrac[300\,000\,000]{m}{s}`.
* Eine Schnecke legt in einer Sekunde etwa :math:`\unit[0,8]{mm}` zurück.
  "Schneckentempo" entspricht somit ungefähr :math:`\unitfrac[0,0008]{m}{s}`.

.. index:: Geschwindigkeit; Umrechnung von km/h in m/s
.. _Umrechnung von Geschwindigkeitsangaben:
.. _Umrechnung von km/h in m/s:

.. rubric:: Umrechnung von km/h in m/s

Sowohl :math:`\unitfrac{km}{h}` als auch :math:`\unitfrac{m}{s}` sind als
Geschwindigkeits-Einheiten üblich. Um sie ineinander umzurechnen, kann man
folgende Zusammenhänge nutzen:

.. math::

    \unit[1]{km} &= \unit[1000]{m} \\
    \unit[1]{h} = \unit[60]{min} &= \unit[60 \cdot 60]{s} = \unit[3600]{s}

Daraus folgt:

.. math::

    \unit[1]{\frac{km}{h}} = \frac{\unit[1]{km}}{\unit[1]{h}} =
    \frac{\unit[1000]{m}}{\unit[3600]{s}} = \unit[\frac{1000}{3600}
    ]{\frac{m}{s} } = \unit[\frac{1}{3,6} ]{\frac{m}{s} }

und umgekehrt:

.. math::
    :label: eqn-umrechnung-geschwindigkeit

    \unit[1]{\frac{m}{s} } = \unit[3,6]{\frac{km}{h} }

Ein Spaziergänger beispielsweise, der sich mit knapp :math:`\unitfrac[5]{km}{h}`
bewegt, legt also in einer Sekunde etwas mehr als einen Meter zurück.

.. rubric:: Ort und zurückgelegte Wegstrecke

Der zeitliche Verlauf der Geschwindigkeit kann allgemein in Form eines
:math:`v(t)`-Diagramms darstellt werden. Hierbei wird der Betrag der
Geschwindigkeit in Abhängigkeit von der Zeit wie der Graph einer mathematischen
:ref:`Funktion <Eigenschaften von Funktionen>` in ein zweidimensionales
Koordinatensystem eingezeichnet.

.. figure:: ../../pics/mechanik/kinematik/v-t-diagramm-konstante-geschwindigkeit.png
    :name: fig-v-t-diagramm-konstante-geschwindigkeit
    :alt:  fig-v-t-diagramm-konstante-geschwindigkeit
    :align: center
    :width: 90%

    :math:`v(t)`-Diagramme einer konstanten Geschwindigkeit. Der Wert der
    Geschwindigkeit kann größer, gleich oder kleiner Null sein.

    .. only:: html

        :download:`SVG: v(t)-Diagramm: Konstante Geschwindigkeit
        <../../pics/mechanik/kinematik/v-t-diagramm-konstante-geschwindigkeit.svg>`

Im Fall einer zeitlich konstanten Geschwindigkeit entspricht der Graph der
Geschwindigkeit einer waagrechten Geraden. Der Wert der
:math:`v(t)`-Geraden hat folgende Bedeutung:

* Umso größer der Wert der Geschwindigkeit ist, desto weiter ist die
  :math:`v(t)`-Gerade von der horizontalen :math:`t`-Achse (entspricht dem Wert
  :math:`v=0`) entfernt.
* "Ruhe" ist der Spezialfall einer Bewegung mit konstanter Geschwindigkeit, für
  den gerade :math:`v = 0` gilt.
* Bewegt sich ein Objekt in die entgegengesetzt zur ursprünglich als "positiv"
  festgelegten Richtung, so erhält seine Geschwindigkeit ein negatives
  Vorzeichen.

.. _Zusammenhang-s-t:

Kennt man die (konstante) Geschwindigkeit :math:`v` eines Objekts und weiß, wie
lange es mit dieser Geschwindigkeit unterwegs ist, so kennt man allerdings noch
nicht den genauen Ort, an dem sich das Objekt zur Zeit :math:`t` befindet. Man
weiß nämlich nicht, von welchem Startpunkt aus die Bewegung begonnen hat. Um den
Ort :math:`s(t)` des Objekts in Abhängigkeit von der Zeit angeben zu können,
muss also die Startposition :math:`s_0` mit berücksichtigt werden:

.. math::

    s(t) = v_0 \cdot \Delta t + s_0

Der zeitliche Verlauf der zurückgelegten Wegstrecke kann ebenfalls graphisch in
Form eines so genannten Weg-Zeit-Diagramms (":math:`s(t)`-Diagramm") dargestellt
werden. Aus Gleichung :eq:`eqn-geschwindigkeit` folgt, dass sich die Wegstrecke
:math:`\Delta s` bei konstanter Geschwindigkeit :math:`v` in gleichen
Zeitabschnitten :math:`\Delta t` kontinuierlich um :math:`\Delta s = v \cdot
\Delta t` ändert -- die entsprechende Weg-Zeit-Linie entspricht also einer
Geraden.

.. figure:: ../../pics/mechanik/kinematik/s-t-diagramm-konstante-geschwindigkeit.png
    :name: fig-s-t-diagramm-konstante-geschwindigkeit
    :alt:  fig-s-t-diagramm-konstante-geschwindigkeit
    :align: center
    :width: 90%

    :math:`s(t)`-Diagramme einer konstanten Geschwindigkeit. Die Steigung der
    Weg-Zeit-Geraden kann größer, gleich oder kleiner Null sein.

    .. only:: html

        :download:`SVG: s(t)-Diagramm: Konstante Geschwindigkeit
        <../../pics/mechanik/kinematik/s-t-diagramm-konstante-geschwindigkeit.svg>`

Die :ref:`Steigung <gwm:Differenzen- und Differentialquotient>` der Geraden in
einem :math:`s(t)`-Diagramm hat folgende Bedeutung:

* Umso größer die (konstante) Geschwindigkeit ist, desto steiler ist der Verlauf
  der Geraden im :math:`s(t)`-Diagramm.
* Ist die Geschwindigkeit eines Objekts konstant gleich Null, so bleibt seine
  Entfernung vom Beobachter unverändert -- egal, ob sich das beobachtete Objekt
  an der Position des Beobachters oder in einer Entfernung :math:`s_0`
  vom Beobachter entfernt liegt. In beiden Fällen entspricht zeitliche Verlauf
  des zurückgelegten Weges einer waagrechten Geraden.
* Das Vorzeichen der Geschwindigkeit gibt an, ob die Gerade im
  :math:`s(t)`-Diagramm steigt oder fällt. Eine negative Steigung bedeutet
  hierbei, dass sich das beobachtete Objekt entgegen der ursprünglich als
  "positiv" festgelegten Raumrichtung bewegt -- egal, ob die Bewegung vom
  Beobachter oder von einer um die Strecke  :math:`s_0` entfernten
  Stelle aus beginnt.

Der Wert, den die Ortsfunktion :math:`s(t) = v \cdot t` zu einer bestimmten Zeit
:math:`t` annimmt, entspricht jeweils der Fläche zwischen der entsprechen
Geschwindigkeits-Zeit-Linie und der :math:`t`-Achse im :math:`v(t)`-Diagramm;
gegebenenfalls muss das Vorzeichen berücksichtigt werden und die anfängliche
Entfernung :math:`s_0` zum Ergebnis hinzu addiert werden.


.. index:: Durchschnittsgeschwindigkeit
.. _Durchschnittsgeschwindigkeit:

.. rubric:: Die Durchschnittsgeschwindigkeit

Auch wenn sich die Geschwindigkeit mit der Zeit beziehungsweise entlang einer
Wegstrecke mehrfach ändert, so kann man trotzdem für den gesamten
Bewegungsvorgang eine durchschnittliche Geschwindigkeit angeben.

.. index:: Geschwindigkeit; Durchschnittsgeschwindigkeit

*Definition:*

    Die Durchschnittsgeschwindigkeit :math:`\bar{v}` eines Objekts ist gleich
    dem Verhältnis aus der Wegstrecke :math:`\Delta s_{\mathrm{ges}}`, die er
    insgesamt zurücklegt, und der dazu benötigten Zeit :math:`\Delta
    t_{\mathrm{ges}}`:

.. math::
    :label: eqn-durchschnittsgeschwindigkeit-zurueckgelegte-wegstrecke

    \bar{v} = \frac{\Delta s_{\mathrm{ges}}}{\Delta t_{\mathrm{ges}}}

*Beispiel:*

* Ein Radrennfahrer legt eine Etappe von :math:`\unit[130]{km}` in einer Zeit
  von :math:`\unit[4,0]{h}` zurück. Seine Durchschnittsgeschwindigkeit beträgt
  somit:

.. math::

  \bar{v} = \frac{\Delta s_{\mathrm{ges}}}{\Delta t_{\mathrm{ges}}} =
  \frac{\unit[130]{km}}{\unit[4]{h}} = \unit[32,5]{\frac{km}{h}}

Man sieht, dass auch bei diesem Vorgang das Modell der geradlinigen Bewegung
verwendet werden kann, auch wenn sich der Radfahrer sehr wahrscheinlich nicht
geradlinig fortbewegt. Bei vielerlei Fragestellungen ist allerdings nicht der
konkrete Streckenverlauf von Bedeutung, sondern nur die Länge der Strecke. Kennt
man zusätzlich die durchschnittliche Geschwindigkeit, so weiß man, wie lange der
Bewegungsvorgang dauern wird; derartige Abschätzungen sind beispielsweise bei
Wanderungen oder Fahrrad-Touren durchaus hilfreich.


.. index:: Relativgeschwindigkeit
.. _Relativgeschwindigkeit:

.. rubric:: Die Relativgeschwindigkeit

Bewegen sich zwei Objekte von einem gleichen Ausgangspunkt aus mit verschiedenen
Geschwindigkeiten :math:`v_1` und :math:`v_2` in die gleiche Richtung, so
entspricht ihre gegenseitige Entfernung der Differenz der zurückgelegten
Wegstrecken; die Objekte entfernen sich also mit zunehmender Zeit voneinander.
Die wachsende Entfernung kann durch die so genannte Relativgeschwindigkeit
:math:`v_{\mathrm{rel}}` ausgedrückt werden:

.. math::
    :label: eqn-relativgeschwindigkeit

    v_{\mathrm{rel}} = v_2 - v_1

Diese Gleichung gibt die Relativgeschwindigkeit des zweiten Objekts relativ zum
ersten Objekt an; umgekehrt gibt :math:`v_1 - v_2` die Geschwindigkeit des
ersten Objekts relativ zum zweiten an. Beide Relativgeschwindigkeiten haben den
gleichen Betrag, ein unterschiedliches Vorzeichen, da sie in ihren Richtungen
entgegengesetzt sind.

Das Rechnen mit Relativgeschwindigkeiten ist beispielsweise hilfreich, um die
für Überholvorgänge mit konstanten Geschwindigkeiten notwendigen Zeiten
beziehungsweise Wegstrecken zu berechnen. Zudem können, wie im folgenden
Abschnitt gezeigt wird, mittels Relativgeschwindigkeiten auch Entfernungen
zwischen Objekten berechnet werden, die sich mit konstanten Geschwindkeiten in
unterschiedlichen Raumrichtungen bewegen.

.. todo Beispiel?

.. Relativgeschwindigkeiten lassen sich auch für :ref:`Bewegungen mit
.. unterschiedlichen Richtungen <Verallgemeinerung für dreidimensionale
.. Geschwindigkeiten>` anwenden, wenn man die zurückgelegten Wegstrecken
.. :math:`\vec{s}` und die Geschwindigkeiten :math:`\vec{v}` als Vektoren
.. behandelt.

.. _Mehrdimensionale Bewegungen mit konstanter Geschwindigkeit:

Mehrdimensionale Bewegungen mit konstanter Geschwindigkeit
----------------------------------------------------------

Die im letzten Abschnitt vorgestellten Gesetzmäßigkeiten für eindimensionale
Bewegungen lassen sich auch ohne großen Aufwand auf zweidimensionale Bewegungen
übertragen. Ein Grundprinzip hierbei ist, dass jeder zweidimensionale
Bewegungsvorgang in eine :math:`x`- und eine :math:`y`-Komponente aufgeteilt
werden kann. Die Ausrichtung des Koordinatensystems kann wiederum einmalig frei
gewählt werden kann, ist für den Rest der Rechnung dann allerdings verbindlich.

Ein zweites Grundprinzip ist, dass einzelne Bewegungsvorgänge, auch wenn sie
entlang unterschiedlicher Raumrichtungen stattfinden, jeweils getrennt
voneinander betrachtet werden können.


.. _Addition von Teilgeschwindigkeiten:

.. rubric:: Addition von Teilgeschwindigkeiten

Verlaufen zwei Bewegungen geradlinig entlang einer gemeinsamen Linie, so genügt
eine einfache Addition der beiden Geschwindigkeitsbeträge :math:`v_1` und
:math:`v_2`, um die resultierende Geschwindigkeit zu erhalten.

*Beispiele:*

* Eine Person bewegt sich mit einer Geschwindigkeit :math:`v_1` auf einem
  Laufband entgegen der Laufbandgeschwindigkeit :math:`v_2`. Sind beide
  Geschwindigkeiten gleich groß, so bleibt die Person an der gleichen Stelle --
  die resultierende Geschwindigkeit :math:`v` ist gleich Null.

  Sind beide Geschwindigkeiten unterschiedlich groß, so bewegt sich die Person
  in Richtung der größeren Geschwindigkeit. [#]_

* Stimmt die Bewegungsrichtung der Person mit der Richtung der
  Laufbandgeschwindigkeit überein, so addieren sich die Beträge beider
  Geschwindigkeiten. Die Geschwindigkeit :math:`v` der Person (relativ zum
  Erdboden) ist somit gleich :math:`v_1 + v_2`.

Die Addition der auftretenden Geschwindigkeiten ist auch möglich, wenn diese in
einem beliebigen Winkel zueinander stehen. Zeichnerisch stellt man dazu die
beiden Geschwindigkeiten :math:`\vec{v}_1` und :math:`\vec{v}_2`
als Pfeile dar, deren Richtungen mit denen der beiden Geschwindigkeiten
übereinstimmen und deren Längen die Beträge beider Geschwindigkeiten abbilden.
Nach den Regeln der :ref:`Vektor-Addition <gwm:Addition und Subtraktion von
Vektoren>` lässt sich damit aus beiden Geschwindigkeits-Pfeilen die Richtung und
der Betrag der resultierenden Geschwindigkeit :math:`\vec{v}` graphisch
ermitteln.

Betrag und Richtung der resultierenden Geschwindigkeit :math:`\vec{v}` können
auch rechnerisch bestimmt werden. Für eine zweidimensionale Bewegung (in einer
Ebene) gilt:

.. math::

    \vec{v} = \vec{v}_1 + \vec{v}_2 = \begin{pmatrix}
    v_{\mathrm{1x}} \\
    v_{\mathrm{1y}}
    \end{pmatrix}
    + \begin{pmatrix}
    v_{\mathrm{2x}} \\
    v_{\mathrm{2y}}
    \end{pmatrix} = \begin{pmatrix}
    v_{\mathrm{1x}} + v_{\mathrm{2x}} \\
    v_{\mathrm{1y}} + v_{\mathrm{2y}}
    \end{pmatrix}

Die resultierende Geschwindigkeit :math:`\vec{v}` entspricht somit einer
komponentenweisen Addition der beiden Geschwindigkeits-Vektoren
:math:`\vec{v}_{1}` und :math:`\vec{v}_{2}`. Für den Betrag der
resultierenden Geschwindigkeit :math:`v = | \, \vec{v} \, |` gilt:

.. math::

    v = \sqrt{v_1^2 + v_2^2}

Aus dem Verhältnis der :math:`y`- zur :math:`x`-Komponente lässt sich der
Winkel der resultierenden Geschwindigkeit bestimmen:

.. math::

    \tan{\varphi } = \frac{v_{\mathrm{y}}}{v_{\mathrm{x}}} \quad \Longleftrightarrow
    \quad \varphi = \tan ^{-1}{\left(\frac{v_{\mathrm{y}}}{v_{\mathrm{x}}}\right)}


*Beispiel:*

* Ein Boot überquert mit einer Geschwindigkeit :math:`v_1 =
  \unit[3]{\frac{m}{s}}` senkrecht einen Fluss, der mit einer Geschwindigkeit
  :math:`v_2 = \unit[1]{\frac{m}{s}}` strömt. Legt man ein Koordinatensystem so
  an, dass die :math:`y`-Achse in Richtung der Geschwindigkeit des Bootes und
  die :math:`x`-Achse in Richtung der Flussströmung zeigt, so folgt für die
  resultierende Geschwindigkeit :math:`\vec{v}`:

  .. math::

      \vec{v} = \vec{v}_1 + \vec{v}_2 = \begin{pmatrix}
      0 \\ 3
      \end{pmatrix} + \begin{pmatrix}
      1 \\ 0
      \end{pmatrix} = \begin{pmatrix}
      1 \\ 3
      \end{pmatrix}

  Der Betrag der resultierenden Geschwindigkeit ist hierbei:

  .. math::

      v = \sqrt{v_1^2 + v_2^2} = \sqrt{\left(\unit[1]{\frac{m}{s}}\right)^2 +
      \left( \unit[3]{\frac{m}{s}}\right)^2} = \sqrt{\unit[10]{\frac{m^2}{s^2}}}
      \approx \unit[3,16]{\frac{m}{s}}

  Der Winkel gegenüber der :math:`x`-Achse (Richtung des Flusses) beträgt:

  .. math::

      \alpha = \tan^{-1}{\left(\frac{v_{\mathrm{y}}}{v_{\mathrm{x}}}\right)} = \tan
      ^{-1}{\left( \frac{3}{1} \right)} \approx 71,6 \degree

  Das Boot driftet somit um einem Winkel von rund :math:`90\degree - 71,6\degree
  = 18,40\degree` ab.

Die in die jeweiligen Richtungen zurückgelegten Wegstrecken :math:`\Delta
s_{\mathrm{x}}` und :math:`\Delta s_{\mathrm{y}}` lassen sich wiederum
komponentenweise über die Formel :math:`\Delta s = v \cdot \Delta t` berechnen.

.. todo 2D-Relativgeschwindigkeiten 

Eine weitere Verallgemeinerung auf dreidimensionale Bewegungsvorgänge erfolgt
nach den gleichen Prinzipien, indem man zusätzlich eine :math:`z`-Komponente
betrachtet und folglich mit drei- anstelle mit zweidimensionalen Vektoren
rechnet.

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Definiert man die Bewegungsrichtung der Person (nach rechts) als positiv,
     so kann der Betrag der resultierenden Geschwindigkeit als Differenz beider
     Geschwindigkeiten :math:`v_1 - v_2` berechnet werden. Gilt :math:`v_2 >
     v_1`, so ist die resultierende Geschwindigkeit "negativ", sie verläuft
     somit von rechts nach links.

     Schreibt man die Differenz :math:`v_1 - v_2` als Summe :math:`v_1 +
     (-v_2)`, so zeigt sich, dass auch in diesem Fall -- unter Berücksichtigung
     der Bewegungsrichtungen -- die resultierende Geschwindigkeit gleich der
     Summe der Einzelgeschwindigkeiten ist.

.. raw:: html

    <hr />

.. hint::

    Zu diesem Abschnitt gibt es :ref:`Übungsaufgaben <Aufgaben Bewegungen mit
    konstanter Geschwindigkeit>`.


