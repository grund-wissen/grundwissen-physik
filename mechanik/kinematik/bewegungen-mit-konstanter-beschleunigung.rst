
.. _Bewegung mit konstanter Beschleunigung:
.. _Bewegungen mit konstanter Beschleunigung:

Bewegungen mit konstanter Beschleunigung
========================================

Das Modell einer Bewegung mit konstanter Beschleunigung stellt eine
Verallgemeinerung einer Bewegung mit konstanter Geschwindigkeit dar. Hat ein
sich bewegendes Objekt insbesondere eine konstante Beschleunigung mit einem Wert
von Null, so bewegt es sich mit konstanter Geschwindigkeit fort; Eine Bewegung
mit konstanter Gschwindigkeit kann also Spezialfall einer beschleunigten
Bewegung angesehen werden.

Durch das Einbeziehen von Beschleunigungen wird berücksichtigt, dass keine
abrupten, sondern stets nur kontinuierliche Geschwindigkeitsänderungen möglich
sind. Die allgemeinen Zusammenhänge zwischen Geschwindigkeitsänderung,
Beschleunigung und Zeit beziehungsweise Wegstrecke werden im folgenden Abschnitt
zunächst für geradlinige, dann auch für zusammengesetzte Bewegungsvorgänge näher
beschrieben.


.. _Geradlinige Bewegung mit konstanter Beschleunigung:
.. _Eindimensionale Bewegung mit konstanter Beschleunigung:
.. _Eindimensionale Bewegungen mit konstanter Beschleunigung:

Eindimensionale Bewegungen mit konstanter Beschleunigung
--------------------------------------------------------

Bei einer Bewegung mit konstanter Beschleunigung nimmt die Geschwindigkeit eines
Objekts in gleichen Zeitabschnitten um den jeweils gleichen Betrag zu
beziehungsweise  ab.

*Definition:*

    Die Beschleunigung :math:`a` eines sich geradlinig bewegenden Objekts ist
    gleich dem Verhältnis aus der Geschwindigkeitsänderung :math:`\Delta v` und
    der dazu benötigten Zeit :math:`\Delta t`:

    .. math::
        :label: eqn-konstante-beschleunigung

        a = \frac{\Delta v}{\Delta t}

.. Beginnt die Bewegung zur Zeit :math:`t_1 = 0` aus der Ruhelage (:math:`v_1 =
.. 0`), so ist :math:`\Delta v = v_2` und :math:`\Delta t = t_2`, also (unter
.. Vernachlässigung der Indizes) :math:`a = \frac{v}{t}`.

*Einheit:*

    Die Beschleunigung wird in Meter je Quadratsekunde
    :math:`(\unitfrac{m}{s^2})` angegeben.

*Beispiele:*

* :math:`\unitfrac[1]{m}{s^2}` ist die Beschleunigung eines Objekts, dessen
  Geschwindigkeit sich in :math:`\unit[1]{s}` um :math:`\unitfrac[1]{m}{s}` ändert.

* Ein Fahrzeug, das in einer Zeit von :math:`t=\unit[10]{s}` von
  :math:`\unitfrac[0]{km}{h}` auf :math:`\unitfrac[100]{km}{h} =
  \unitfrac[27,8]{m}{s}` angetrieben wird, weist eine Beschleunigung von
  :math:`\unitfrac[2,78]{m}{s^2}` auf.

.. index:: Erdbeschleunigung
.. _Erdbeschleunigung:

* Die Beschleunigung die ein Objekt im freier Fall auf der Erde erfährt
  ("Erdbeschleunigung"), beträgt rund :math:`\unitfrac[9,81]{m}{s^2}`. Häufig
  wird diese Beschleunigung, die bei vielerlei physikalischen Vorgängen eine
  Rolle spielt, mit dem Buchstaben :math:`g=\unitfrac[9,81]{m}{s^2}`
  bezeichnet und :ref:`Ortsfaktor <Ortsfaktor>` genannt.

Bei längeren Bewegungsvorgängen können aufeinander folgende Zeitabschnitte
unterschiedliche Beschleunigungen aufweisen. Beispielsweise beschleunigt ein
Sprinter zunächst gleichmäßig, bis er seine Höchstgeschwindigkeit erreicht
hat, hält diese Geschwindigkeit (möglichst) konstant bis zum Ziel, und
bremst nach der Ziellinie wieder gleichmäßig ab. Derartige Bewegungsvorgänge
lassen sich oftmals abschnittsweise durch jeweils konstante
(Durchschnitts-)Beschleunigungen beschreiben.

.. figure:: ../../pics/mechanik/kinematik/a-t-diagramm-konstante-beschleunigung.png
    :name: fig-a-t-diagramm-konstante-beschleunigung
    :alt:  fig-a-t-diagramm-konstante-beschleunigung
    :align: center
    :width: 90%

    Beschleunigung-Zeit-Diagramme einer konstanten Beschleunigung. Der Wert der
    Beschleunigung kann größer, gleich oder kleiner Null sein.

    .. only:: html

        :download:`SVG: a-t-Diagramm: Konstante Beschleunigung
        <../../pics/mechanik/kinematik/a-t-diagramm-konstante-beschleunigung.svg>`

.. _Beschleunigung und Geschwindigkeit:

.. rubric:: Beschleunigung und Geschwindigkeit

Aus Gleichung :eq:`eqn-konstante-beschleunigung` folgt, dass sich die
Geschwindigkeit bei einer konstanten Beschleunigung :math:`a` in gleichen
Zeitabschnitten :math:`\Delta t` kontinuierlich um den Wert :math:`\Delta v = a
\cdot \Delta t` verändert.

Kennt man die (konstante) Beschleunigung :math:`a` eines Objekts und weiß, über
welchen Zeitabschnitt :math:`\Delta t` die Beschleunigung anhält, so kann man im
Allgemeinen jedoch nicht angeben, wie groß die Geschwindigkeit :math:`v` des
Objekt  zur Zeit :math:`t` ist. Hierzu muss man zusätzlich wissen, wie groß die
anfängliche Geschwindigkeit :math:`v_0` des Objekts war. Für den zeitlichen
Verlauf der Geschwindigkeit :math:`v(t)` gilt also:

.. math::

    v(t) = a \cdot \Delta t + v_0

Zeichnet man ein :math:`v(t)`-Diagramm einer solchen Bewegung, so entspricht der
Graph der Geschwindigkeit einer Geraden.

.. figure:: ../../pics/mechanik/kinematik/v-t-diagramm-konstante-beschleunigung.png
    :name: fig-v-t-diagramm-konstante-beschleunigung
    :alt:  fig-v-t-diagramm-konstante-beschleunigung
    :align: center
    :width: 90%

    Geschwindigkeit-Zeit-Diagramme einer konstanten Beschleunigung. Die Steigung der
    Geschwindigkeit-Zeit-Geraden kann größer, gleich oder kleiner Null sein.

    .. only:: html

        :download:`SVG: v(t)-Diagramm: Konstante Beschleunigung
        <../../pics/mechanik/kinematik/v-t-diagramm-konstante-beschleunigung.svg>`

Die Steigung einer :math:`v(t)`-Geraden hat folgende Bedeutung:

* Umso steiler die Geschwindigkeit-Zeit-Gerade ist, desto größer ist die
  Beschleunigung.
* Ist die Beschleunigung des beobachteten Objekts gleich Null, so entspricht die
  Geschwindigkeit-Zeit-Linie einer waagrechten Geraden. Dies gilt gleichermaßen
  für ruhende und sich mit konstanter Geschwindigkeit :math:`v_0`
  bewegende Objekte.
* Eine Beschleunigung entgegen der ursprünglich als "positiv" festgelegten
  Raumrichtung erhält ein negatives Vorzeichen -- egal, ob das beobachtete
  Objekt ruht oder sich mit einer konstanten Geschwindigkeit :math:`v_0`
  fortbewegt. Dies hat -- je nach Wert der Anfangsgeschwindigkeit :math:`v_0` --
  eine Beschleunigung "in Gegenrichtung" beziehungsweise ein kontinuierliches
  Abbremsen zur Folge.

Aus einem :math:`v(t)`-Diagramm kann also die Beschleunigung zu einem Zeitpunkt
:math:`t` ermittelt werden, indem man an dieser Stelle nicht den Wert, sondern
die *Steigung* der Diagramm-Linie betrachtet. Beispielsweise gilt für einen
Bremsvorgang :math:`v>0`, während für die Geschwindigkeitsänderung (und somit
für die Steigung des Graphen) :math:`\Delta v < 0` gilt.


.. _Beschleunigung und Wegstrecke:
.. _Beschleunigung und Wegstrecke ohne Anfangsgeschwindigkeit:

.. rubric:: Beschleunigung und Wegstrecke

.. .. rubric:: Beschleunigung und Wegstrecke (ohne Anfangsgeschwindigkeit)

Zeichnet man in ein :math:`s(t)`-Diagramm die zurückgelegte Wegstrecke in
Abhängigkeit von der Zeit ein, so hat der Graph bei einer beschleunigten Bewegung
:math:`(a \ne 0)` ein parabelförmigen Verlauf. Die konkrete Form der Parabel
hängt von der Anfangsgeschwindigkeit :math:`v_0` und der anfänglichen Entfernung
:math:`s_0` des Objekts vom Beobachter (Koordinatenursprung) ab.

.. Eine anfängliche Entfernung :math:`s_0` des sich bewegenden
.. Objekts vom Beobachter hat lediglich eine senkrechte Verschiebung der
.. (Halb-)Parabel zur Folge: Für :math:`s_0 >  0` ist die Parabel nach oben,
.. für :math:`s_0 <0` nach unten verschoben.

.. Die Funktion :math:`s(t)` gibt also die tatsächliche Entfernung des sich
.. bewegenden Objekts zum Ort des Beobachters beziehungsweise dem Ursprung des
.. Koordinatensystems an; die zurückgelegte Wegstrecke :math:`\Delta s =
.. s_{\mathrm{end}} - s_{\mathrm{anfang}}` hingegen ist unabhängig vom Ort des
.. Beobachters.


.. * Gilt für die konstante Beschleunigung :math:`a > 0`, so nimmt die
  .. Geschwindigkeit :math:`v` linear mit der Zeit zu. In gleichen Zeitabschnitten
  .. legt das Objekt somit immer größere Wegstrecken zurück.

.. :math:`\Delta s` quadratisch.


.. figure:: ../../pics/mechanik/kinematik/s-t-diagramm-konstante-beschleunigung.png
    :name: fig-s-t-diagramm-konstante-beschleunigung
    :alt:  fig-s-t-diagramm-konstante-beschleunigung
    :align: center
    :width: 90%

    Weg-Zeit-Diagramme einer konstanten Beschleunigung. Für :math:`a > 0` ist
    die Weg-Zeit-Parabel nach oben, für :math:`a < 0` nach unten geöffnet
    (linkes bzw. rechtes Bild). Für :math:`a = 0` entspricht die
    Weg-Zeit-Funktion einer Bewegung mit konstanter Geschwindigkeit (mittleres
    Bild).

    .. only:: html

        :download:`SVG: s(t)-Diagramm: Konstante Beschleunigung
        <../../pics/mechanik/kinematik/s-t-diagramm-konstante-beschleunigung.svg>`


.. _Wegstrecken in v(t)-Diagrammen ablesen:

.. rubric:: Wegstrecken in :math:`v(t)`-Diagrammen ablesen

Zunächst soll angenommen werden, dass zum Zeitpunkt :math:`t_0=0` die Bewegung
am Koordinatenursprung :math:`s_0` mit einer Startgeschwindigkeit von
:math:`v_0=0` beginnt. In diesem Fall gilt:

  .. math::
      :label: eqn-konstante-beschleunigung-wegstrecke

      \Delta s = \frac{1}{2} \cdot a \cdot \Delta t^2

Diesen Zusammenhang kann man sich anschaulich erklären, indem man bedenkt, dass
sich eine zurückgelegte Wegstrecke letztlich ein Produkt aus Geschwindigkeit und
Zeit darstellt. Stellt man sich den Zeitabschnitt :math:`\Delta t`, in dem die
Beschleunigung stattfindet, nochmals in viele kleine Zeitabschnitte
:math:`\Delta t_1^{*}`, :math:`\Delta t_2^{*}`, :math:`\Delta t_3^{*}` usw.
unterteilt vor (wie bei einer Betrachtung des Vorgangs mit Stroboskop-Licht), so
kann man in diesen kurzen Momenten die jeweiligen Geschwindigkeiten
:math:`v_1^{*}`, :math:`v_2^{*}`, :math:`v_3^{*}` usw. jeweils in guter Näherung
als konstant annehmen.

Bei einer solchen Aufteilung in viele kleine Zeitschritte mit jeweils konstanten
Geschwindigkeiten lassen sich die in den einzelnen Zeitschritten zurückgelegten
Wegstrecken mittels der Formel :math:`\Delta s = v \cdot \Delta t` berechnen;
die Einzelergebnisse können dann zum Gesamtergebnis aufsummiert werden. In einem
:math:`v(t)`-Diagramm entsprechen die so berechneten einzelnen Wegstrecken den
Rechteck-Flächen zwischen der (stufenförmigen) Geschwindigkeit und der
:math:`t`-Achse.

Ist die Beschleunigung konstant, so nimmt die Geschwindigkeit :math:`v` des sich
bewegenden Objekts linear mit der Zeit zu. Der Mittelwert der einzelnen
Geschwindigkeiten während des Beschleunigungsvorgangs entspricht wiederum der
Durchschnittsgeschwindigkeit :math:`\bar{v}` des Objekts:

.. math::
    :label: eqn-durchschnittsgeschwindigkeit-beschleunigte-bewegung

    \bar{v} = \frac{v_{\mathrm{0}} + v}{2}

Mit :math:`v_0` wird hierbei wiederum die Geschwindigkeit zu Beginn der
Beschleunigung, mit :math:`v` die (End-)Geschwindigkeit zum Zeitpunkt :math:`t`
bezeichnet. Ist insbesondere die Startgeschwindigkeit :math:`v_0 = 0`, so ist
:math:`\bar{v} = \frac{1}{2} \cdot v`, also gleich der Hälfte der
Endgeschwindigkeit. In diesem Fall gilt somit für die während des
Beschleunigungsvorgangs zurückgelegte Wegstrecke:

.. math::

    \Delta s = \bar{v} \cdot \Delta t &= \frac{1}{2} \;\;\; \cdot \;\; v \;\; \cdot \;\;\; \Delta t \\
    &= \frac{1}{2} \cdot (a \cdot \Delta t) \cdot \Delta t = \frac{1}{2} \cdot a
    \cdot \Delta t^2

Der Hintergedanke bei dieser Gleichung ist, dass während des
Beschleunigungsvorgangs -- über alle kleinen Zeitschritte gemittelt -- die
durchschnittliche "Höhe" der Rechtecke gleich der Durchschnittsgeschwindigkeit
:math:`\bar{v}` ist; die Gesamt-Fläche zwischen der :math:`v(t)`-Linie und der
:math:`t`-Achse ist also identisch mit der Fläche, die man erhält, wenn man die
Durchschnittsgeschwindigkeit :math:`\bar{v}` mit :math:`\Delta t` multipliziert.
[#]_

Die gleiche Überlegung trifft ebenso zu, wenn die Anfangsgeschwindigkeit
:math:`v_0 \ne 0` ist. In diesem Fall gilt für die Durchschnittsgeschwindigkeit:

.. math::

    \bar{v} = \frac{v_0 + v}{2} = v_0 + \frac{1}{2} \cdot a \cdot \Delta t

Die Durchschnittsgeschwindigkeit ist also allgemein gleich dem Mittelwert
zwischen der Start- und Endgeschwindigkeit; bei einer konstanten Beschleunigung
:math:`a` wird sie zur Hälfte der Beschleunigungszeit :math:`\Delta t`, also zum
Zeitpunkt :math:`(t_{\mathrm{start}} +) \frac{1}{2} \cdot \Delta t` erreicht.
Setzt man wiederum diesen Term für :math:`\bar{v}` in die Bewegungsgleichung
ein, so erhält man:

.. math::
    :label: eqn-allgemeine-bewegungsgleichung-wegstrecke

    \Delta s = \bar{v} \cdot \Delta t = \frac{1}{2} \cdot a \cdot \Delta t^2 +
    v_0 \cdot \Delta t

Diese Gleichung gibt allgemein den Zusammenhang zwischen der zurückgelegten
Wegstrecke :math:`\Delta s`, der Beschleunigung :math:`a`, der
Anfangsgeschwindigkeit :math:`v_0` und der Zeitdauer :math:`\Delta t` an. 


.. _Allgemeine Bewegungsgleichung:
.. _Die allgemeine Bewegungsgleichung:

.. rubric:: Die allgemeine Bewegungsgleichung

Die Gleichung :eq:`eqn-allgemeine-bewegungsgleichung-wegstrecke` ist tatsächlich
eine Verallgemeinerung der bislang betrachteten Fälle:

* Ist die Beschleunigung :math:`a=0`, so erhält man die Ortsgleichung für
  Bewegungen mit konstanter Geschwindigkeit:

  .. math::

      a = 0 \quad \Rightarrow \quad \Delta s = \underbrace{\frac{1}{2} \cdot 0
      \cdot \Delta t^2}_{=0} + v_0 \cdot \Delta t = v_0 \cdot \Delta t


* Ist die Anfangsgeschwindigkeit :math:`v_0 = 0`, so erhält man die
  Ortsgleichung :eq:`eqn-konstante-beschleunigung-wegstrecke` für Bewegungen
  mit konstanter Beschleunigung ohne Anfangsgeschwindigkeit:

  .. math::

      v_0 = 0 \quad \Rightarrow \quad \Delta s = \frac{1}{2} \cdot a \cdot \Delta
      t^2 + \underbrace{0 \cdot \Delta t}_{=0} = \frac{1}{2} \cdot a \cdot
      \Delta t^2

Man kann sich eine beschleunigte Bewegung mit Anfangsgeschwindigkeit also als
zwei Prozesse vorstellen, die gleichzeitig ablaufen, ohne sich gegenseitig zu
beeinflussen (einmal die Bewegung mit der konstanten Anfangsgeschwindigkeit und
einmal die Bewegung mit der konstanten Beschleunigung ohne
Anfangsgeschwindigkeit). Beide Teilprozesse können somit getrennt voneinander
betrachtet und ihre Effekte addiert werden.

Den konkreten Ort :math:`s(t)` eines Objekts erhält man schließlich, indem man
bei der Bewegung dessen anfängliche Entfernung vom Koordinatenursprung
:math:`s_0` mit berücksichtigt:

.. math::
    :label: eqn-allgemeine-bewegungsgleichung

    s(t) = \bar{v} \cdot \Delta t + s_0 = \frac{1}{2} \cdot a \cdot \Delta t^2 +
    v_0 \cdot \Delta t + s_0

Diese Formel genügt in Kombination mit der Formel :math:`v(t) = a \cdot \Delta t +
v_0` bereits, um den Ort sowie die Geschwindigkeit eines Objekts zu jedem
beliebigen Zeitpunkt angeben zu können, sofern die Startwerte bekannt sind und
die Beschleunigung konstant ist. [#]_


.. index:: Bremsformel
.. _Bremsformel:
.. _Die Bremsformel:

Die Bremsformel
---------------

Insbesondere für Bremsvorgänge gibt es eine weitere nützliche Formel, die sich
aus der obigen Gleichung :eq:`eqn-allgemeine-bewegungsgleichung-wegstrecke`
herleiten lässt. [#]_ Mit einer Anfangsgeschwindigkeit :math:`v_0` gilt für den
Zusammenhang zwischen :math:`v`, :math:`a` und :math:`\Delta s`:

.. math::
   :label: eqn-bremsformel

    v^2 - v_0^2 = 2 \cdot a \cdot \Delta s

Diese Gleichung wird häufig "Bremsformel" genannt; im Fall :math:`v=0` lässt
sich damit der Bremsweg :math:`\Delta s = \frac{v_0^2}{2 \cdot |a|}` bei
bekannter Anfangsgeschwindigkeit und Beschleunigung unmittelbar berechnen.
Die "Bremsformel" lässt sich allerdings auch allgemein auf Bewegungen mit
konstanter Beschleunigung anwenden und erleichtert insbesondere dann das
Rechnen, wenn in der Aufgabenstellung keine Zeitangabe enthalten ist.

.. Der Nutzen der Bremsformel liegt darin, dass sie den Zusammenhang zwischen
.. Start- und Endgeschwindigkeit, der wirkenden Beschleunigung und der
.. zurückgelegten Wegstrecke *zeitunabhängig* beschreibt.

.. index:: Bremsweg, Anhalteweg
.. _Anhalteweg:
.. _Reaktionszeit und Anhalteweg:

.. rubric:: Reaktionszeit und Anhalteweg

Um die gesamte Strecke zu berechnen, die ein Fahrzeug zum Anhalten benötigt,
muss neben dem Bremsweg auch die Wegstrecke berücksichtigt werden, die der
Fahrer während der Reaktionszeit zurücklegt. Es gilt also:

.. math::

    \Delta s_{\mathrm{Anhalte}} = \Delta s_{\mathrm{Brems}} + \Delta
    s_{\mathrm{Reaktion}}

Während der Reaktionszeit, die oftmals vereinfacht als "Schrecksekunde"
angenommen wird, bewegt sich das Fahrzeug mit der konstanten Geschwindigkeit
:math:`v_0` weiter. Es ergibt sich somit mit :math:`t_{\mathrm{Reaktion}}
\stackrel{\wedge}= \unit[1]{s}`:

.. math::

    \Delta s_{\mathrm{Anhalte}} = \frac{v_0^2}{2 \cdot |a|} + v_0 \cdot t_{\mathrm{Reaktion}}

.. todo:: Pic / Diagramm!

Der Bremsweg (und somit auch der Anhalteweg) nimmt bei der gleichen
Bremsbeschleunigung quadratisch mit der Geschwindigkeit zu; aus diesem Grund
sind in Ortschaften sowie an unübersichtlichen Stellen
Geschwindigkeitsbegrenzungen für die Verkehrssicherheit wichtig.


.. _Beschleunigungen und Kräfte:

.. rubric:: Beschleunigungen und Kräfte

Beschleunigungen treten allgemein dann auf, wenn eine resultierende :ref:`Kraft
<Mechanische Kräfte>` :math:`F_{\mathrm{res}}` auf einen Gegenstand einwirkt;
für die Beschleunigung gilt dabei :math:`a = \frac{F}{m}`, wobei :math:`m` für
die Masse des Gegenstands steht. Kennt man also die auf einen Gegenstand
einwirkenden Kräfte, so kann mittels der obigen Formeln auch dessen Bewegung
vorhergesagt werden; umgekehrt können aus berechneten oder gemessenen
Beschleunigungswerten auch die entsprechenden Kräfte abgeschätzt werden.

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Eine andere, gleichwertige Überlegung ist, dass die Fläche zwischen der
    :math:`v(t)`-Linie und der :math:`t`-Achse ein Dreieck darstellt. Dieses
    Dreieck entspricht genau der Hälfte des Rechtecks, das man erhält, wenn man
    :math:`v(t) = a \cdot \Delta t` mit :math:`\Delta t` multipliziert. In
    beiden Fällen sind die berechneten Flächen identisch.

.. [#] Bei nicht konstanten Beschleunigungen müsste der Prozess in
    Teilabschnitte mit jeweils konstanten (Durchschnitts-)Beschleunigungen
    zerlegt werden. Die ist meist mit erheblich mehr Rechenaufwand verbunden und
    wird kaum ohne Hilfe von Computern berechnet.

.. [#] Die Bremsformel :eq:`eqn-bremsformel` lässt sich durch folgende
    Umformungen auf die ursprünglichen Gleichungen
    :eq:`eqn-konstante-beschleunigung` und
    :eq:`eqn-konstante-beschleunigung-wegstrecke` zurückführen:

    .. math::

        v^2 - v_0^2 &= (a \cdot t + v_0)^2 - v_0^2 \\
        &= a^2 \cdot t^2 + 2 \cdot a \cdot v_0 \cdot t + v_0^2 - v_0^2 \\
        &= a^2 \cdot t^2 + 2 \cdot a \cdot v_0 \cdot t  \\
        &= 2 \cdot a \cdot (\frac{1}{2} \cdot a \cdot t^2 + v_0 \cdot t) \\
        &= 2 \cdot a \cdot \Delta s \quad \checkmark

.. raw:: html

    <hr />

.. hint::

    Zu diesem Abschnitt gibt es :ref:`Experimente <Experimente Bewegungen mit
    konstanter Beschleunigung>` und :ref:`Übungsaufgaben <Aufgaben Bewegungen
    mit konstanter Beschleunigung>`.


