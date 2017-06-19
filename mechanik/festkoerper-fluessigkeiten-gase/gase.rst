.. _Mechanik der Gase:

Mechanik der Gase
=================

In der Ärodynamik werden die mechanischen Eigenschaften von Gasen,
insbesondere von Luft, untersucht.

.. _Gasdruck:
.. _Druck und Volumen:

Druck und Volumen
-----------------

Ein wesentlicher Unterschied zwischen Gasen und Flüssigkeiten besteht darin,
dass Gase verhältnismäßig leicht komprimierbar sind; ihr Volumen :math:`V` nimmt
also ab, wenn von außen ein erhöhter Druck :math:`p` auf einen verformbaren
Gasbehälter (beispielsweise einen Luftballon) ausgeübt wird. Lässt der Druck
wieder nach, so nimmt entsprechend auch das Volumen des Gases wieder zu. 

Bleibt die Temperatur des Gases während eines Kompressions- beziehungsweise
Expansionsvorgangs konstant, so gilt: [#]_

.. math::
    :label: eqn-boyle-mariotte

      p_1 \cdot V_1 = p_2 \cdot V_2

*Wichtig:* Für :math:`p_1` und :math:`p_2` müssen bei Verwendung dieser Formel
stets **absolute** Druckwerte eingesetzt werden; zu einem mittels eines
Manometers gemessenen Druckwert muss also stets der Luftdruck (rund
:math:`\unit[1]{bar}`) hinzu addiert werden.

.. _Vakuum:
.. _Vakuumpumpe:

Die Volumina eines Gases verhalten sich sich also indirekt proportional zu den
jeweils vorherrschenden Druckwerten. Grafisch kann dieser Zusammenhang
mittels eines :math:`p(V)`-Diagramms dargestellt werden:

.. figure:: ../../pics/mechanik/festkoerper-fluessigkeiten-und-gase/diagramm-boyle-mariotte.png
    :name: fig-boyle-mariotte
    :alt:  fig-boyle-mariotte
    :align: center
    :width: 50%

    Das Boyle-Mariottesche Gesetz: Indirekte Proportionalität zwischen Druck und
    Volumen.

    .. only:: html

        :download:`SVG: Diagramm Boyle-Mariotte
        <../../pics/mechanik/festkoerper-fluessigkeiten-und-gase/diagramm-boyle-mariotte.svg>`


Die Kurve im :math:`p(V)`-Diagramm entspricht wegen :math:`p \propto
\frac{1}{V}` einer :ref:`Hyperbel <gwm:Hyperbeln>`; man kann erkennen, dass das
Volumen des Gases auch bei sehr hohem Druck nicht gleich Null werden kann, und
umgekehrt durch eine zunehmende "Verdünnung" der Luft ebenso immer ein Restdruck
verbleibt. Mittels so genannten Vakuumpumpen, die im Gegensatz zu Kompressoren
die Luft lediglich immer weiter verdünnen, kann somit kein echtes Vakuum erzeugt
werden, sondern nur ein sich asymptotisch an :math:`p=\unit[0]{Pa}` annähernder
Druckwert.

.. _Luftdruck:
.. _Barometrische Höhenformel:
.. _Luftdruck und Barometrische Höhenformel:

Luftdruck und Barometrische Höhenformel
---------------------------------------

Gase haben -- im Verhältnis zu Flüssigkeiten -- eine nur sehr geringe Masse.
Während ein Liter Wasser ein Kilogramm schwer ist, wiegt ein Liter Luft unter
Normalbedingungen gerade einmal knapp :math:`1,3` Gramm. Dennoch bewirkt auf
unserem Planeten das Gewicht der Luft, ähnlich wie beim :ref:`Schweredruck in
Flüssigkeiten <Schweredruck>`, einen so genannten Luftdruck, der umso größer
ist, je weiter unten man sich in dem die Erde umgebenden "Luftmeer" befindet.

Der "normale" Luftdruck :math:`p_0 \approx \unit[1,0]{bar}` in Bodennähe
resultiert aus dem Gewicht der darüber liegenden Luftschichten. Da für
:math:`\unit[1]{bar} = \unit[10^5]{Pa} = \unit[10^5]{\frac{N}{m^2}}` gilt,
entspricht der durch die Luft ausgeübte Druck in Bodennähe rund einem Gewicht
von :math:`\unit[10]{t}` je Quadratmeter beziehungsweise :math:`\unit[1]{kg}` je
Quadrat-Zentimeter. [#]_

.. figure:: ../../pics/mechanik/festkoerper-fluessigkeiten-und-gase/luftdruck.png
    :name: fig-luftdruck
    :alt:  fig-luftdruck
    :align: center
    :width: 30%

    Veranschaulichung der Größe des "normalen" Luftdrucks (1 bar).

    .. only:: html

        :download:`SVG: Die Größe des Luftdrucks
        <../../pics/mechanik/festkoerper-fluessigkeiten-und-gase/luftdruck.svg>`

Bei Standardbedingungen, das heißt einem Luftdruck von :math:`p_0 =
\unit[1,01325]{bar}` und einer Temperatur von :math:`T_0 = \unit[0]{\degree C}`
nimmt ein Mol eines beliebigen Gases ein Volumen von :math:`V_0 =
\unit[22,4]{l}` ein (:ref:`"Normalvolumen" <Normalvolumen eines Gases>`). Da die
Masse eines Gases in einem geschlossenen System gleich bleibt, bewirkt eine
Veränderung des Gasvolumens :math:`V` neben einer Veränderung des Drucks auch
eine Veränderung der Gasdichte :math:`\rho`. Es gilt: [#]_

.. math::
    :label: eqn-gas-dichte

    \frac{\rho_1}{\rho_2} = \frac{p_1}{p_2}

Bei einem niedrigem Gasdruck nimmt das Volumen eines Gases zu, seine Dichte
hingegen ab; in höheren Luftschichten ist daher die Luft "dünner". Für den
Luftdruck :math:`p` gilt in Abhängigkeit von der Höhe :math:`h` die so
genannte "barometrische Höhenformel": [#]_

.. math::
    :label: eqn-barometrische-hoehenformel

    p = p_0 \cdot e^{-\frac{h}{h_{\mathrm{s}}}}

Hierbei ist :math:`p_0` der Luftdruck auf Meereshöhe und :math:`h_{\mathrm{s}}`
eine so genannte "Skalenhöhe", die angibt, ab wie vielen Metern der Druck auf
:math:`1/e \approx 36,8\%` des ursprünglichen Werts :math:`p_0` abfällt. Auf der
Erde ist :math:`h_{\mathrm{s}} \approx \unit[8,0]{km}`. Die Höhe, bei welcher der
Luftdruck bzw. die Luftdichte nur noch halb so groß ist, liegt damit etwa bei
:math:`\unit[5,5]{km}`.

Technisch wird der Zusammenhang zwischen Druck und Dichte beispielsweise in
Vakuumpumpen genutzt, mit deren Hilfe das zu evakuierende Luftvolumen
schrittweise verdünnt wird; im umgekehrten Fall kann mittels Kompressoren oder
Luftpumpen das Luftvolumen kontinuierlich verkleinert werden. Das Luftvolumen
kann jedoch nicht unendlich vergrößert oder verkleinert werden. Die Grenzen für
elektrische Vakuumpumpen liegen daher bei etwa :math:`\unit[10^{-2}]{mbar}`;
mit mehrstufigen Hochvakuum-Pumpen können Drücke von rund
:math:`\unit[10^{-3}]{mbar}`) erreicht werden, mit Ultrahochvakuum-Pumpen sind
sogar Drücke von :math:`\unit[10^{-7}]{mbar}` möglich. [#]_ Im umgekehrten
Anwendungsfall kann man mit Luftpumpen bis zu :math:`\unit[5]{bar}`, mit
Kompressoren oder guten Stand-Luftpumpen bis zu :math:`\unit[12]{bar}`
erreichen.


..  Die Volumenveränderungsarbeit
..  -----------------------------

..  Um ein Gas bei einer konstanten Temperatur :math:`T`  zu komprimieren, ist eine
..  so genannte Volumenänderungsarbeit :math:`W` notwendig. Diese kann in
..  Abhängigkeit vom Druck :math:`p` und Volumen :math:`V` des Gases ausgedrückt
..  werden. Allgemein gilt für die Defintion der Arbeit:

..  .. math::

    ..  \Delta W = F \cdot \Delta s

..  Befindet sich das Gas in einem zylinderförmigen Gefäß, dessen Volumen durch
..  einen Kolben mit einer Fläche :math:`A` komprimmiert werden kann
..  (beispielsweise einer Luftpumpe), so gilt für die obere Gleichung:

..  .. math::

    ..  \Delta W = \frac{F}{A} \cdot \Delta s \cdot A  = p \cdot \Delta V


..  einen Druck von :math:`p` und ein Volumen von :math:`V` hat,

.. Zabel 62
.. Der Luftdruck in der Lunge variiert von leichtem Unterdruck beim Einatmen von
.. ca. –500 Pa bis zum exspiratorischen leichten Überdruck von 150 Pa. 

.. Im Blutkreislauf wird durch die Herztätigkeit ein Druckunterschied von ca. 13
.. kPa zwischen der arteriellen und venösen Seite aufgebaut. Allerdings muss bei
.. allen biologischen Systemen berücksichtigen werden, dass die Wände nicht starr
.. sind, sondern dehnbar.

.. _Auftrieb in Gasen:

Auftrieb in Gasen
-----------------

Für die (statische) Auftriebskraft :math:`F_{\mathrm{A}}` in Gasen gilt die gleiche
Formel wie für die :ref:`Auftriebskraft in Flüssigkeiten <Schwimmen, Sinken und
Schweben>`:

.. math::
    :label: eqn-auftriebskraft-gase

    F_{\mathrm{A}} = \rho_{\mathrm{G}} \cdot g \cdot V_{\mathrm{K}}

Hierbei bezeichnet :math:`V_{\mathrm{K}}` das Volumen des Körpers, :math:`g =
\unit[9,81]{\frac{N}{kg}}` die Erdbeschleunigung und :math:`\rho_{\mathrm{G}}`
die Dichte des Gases. Da die Dichte von Luft :math:`\rho_{\mathrm{Luft}} \approx
\unit[1,3]{\frac{kg}{m^3}}` unter Normalbedingungen rund :math:`1000`-mal
kleiner ist als die Dichte von Wasser :math:`(\rho_{\mathrm{Wasser}} =
\unit[1000]{\frac{kg}{m^3}})`, können in Luft nur Körper mit einer sehr geringen
(durchschnittlichen) Dichte aufsteigen. Die Steighöhe beispielsweise von
Ballonen wird zudem dadurch begrenzt, dass die Dichte der Luft mit zunehmender
Höhe abnimmt.



.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Die Gleichung :eq:`eqn-boyle-mariotte` wird nach ihren Entdeckern `Robert Boyle
    <https://de.wikipedia.org/wiki/Robert_Boyle>`_ und `Edme Mariotte
    <https://de.wikipedia.org/wiki/Edme_Mariotte>`_ "Gesetz von Boyle-Mariotte"
    genannt und ist ein Sonderform der :ref:`Zustandsgleichung für ideale
    Gase <Zustandsgleichung eines idealen Gases>`.

.. [#] Nach der :ref:`Zustandsgleichung für ideale Gase <Zustandsgleichung eines
    idealen Gases>` gilt :math:`p \cdot V = n \cdot R \cdot T`, wobei :math:`n`
    die (konstante) Stoffmenge in Mol und :math:`R = \unit[8,31]{\frac{J}{mol
    \cdot K}}` die allgemeine Gaskonstante ist. Die Stoffmenge :math:`n` ist
    über die Beziehung :math:`n = \frac{m}{m_{\mathrm{Mol}}}` mit der Masse
    :math:`m` des Gases verknüpft, wobei :math:`m_{\mathrm{Mol}}` die
    stoffspezifische molare Masse des Gases angibt. Es gilt also:

    .. math::

        p \cdot V = \frac{m}{m_{\mathrm{Mol}}} \cdot R \cdot T \quad
        \Longleftrightarrow \quad p = \frac{m}{V} \cdot \frac{R \cdot
        T}{m_{\mathrm{Mol}}} 

    Der Term :math:`\frac{m}{V}` auf der rechten Gleichungsseite gibt die Dichte
    des Gases an. Da :math:`R` und :math:`m_{\mathrm{Mol}}` konstante Werte
    sind, gilt bei konstanter Temperatur :math:`\frac{p}{\rho} =
    \text{konstant}`, also :math:`\frac{p_1}{\rho_1} = \frac{p_2}{\rho_2}`.

.. [#] Bei der Herleitung der barometrischen Höhenformel wird vom
    :ref:`Schweredruck in Flüssigkeiten <Schweredruck>` ausgegangen; für den
    Druckunterschied :math:`\Delta p` bei einem Höhenunterschied :math:`\Delta
    h` gilt:

    .. math::

        \Delta p = - \rho \cdot g \cdot \Delta h

    Hierbei steht :math:`\rho` für die Dichte und :math:`g` für den Ortsfaktor.
    Das Minuszeichen ergibt sich daraus, dass der Druck mit zunehmender Höhe
    geringer wird (da bei Flüssigkeiten :math:`h` für die Eintauchtiefe steht,
    wird der Druck in diesem Fall größer, wenn :math:`h` größer wird.)

    Bei konstanter Temperatur hängt bei Gasen die Dichte :math:`\rho` und der
    Druck :math:`p` in der Höhe :math:`h`  über :math:`\frac{\rho}{\rho_0} =
    \frac{p}{p_0}` mit der Dichte :math:`\rho_0` und dem Druck :math:`p_0` in
    der Ausgangshöhe :math:`h=\unit[0]{m}` zusammen. Umgeformt gilt also:

    .. math::

        \rho = \frac{p}{p_0} \cdot \rho_0

    Setzt man diesen Ausdruck für :math:`\rho` in die vorherige Gleichung ein,
    erhält man folgenden Ausdruck:

    .. math::

        \Delta p = - \frac{p}{p_0} \cdot \rho_0 \cdot g \cdot \Delta h

    Dividiert man beide Seiten dieser Gleichung durch :math:`p`, so folgt:

    .. math::

        \frac{\Delta p}{p} = -\frac{\rho_0}{p_0} \cdot g \cdot \Delta h

    Wertet man die relativen Druckänderung für eine jeweils nur kleine
    Höhenänderung aus, so kann man alle Änderungen von :math:`0` bis :math:`h`
    aufsummieren; dies entspricht im mathematischen Sinn einem :ref:`Integral
    <gwm:Integralrechnung>`:

    .. math::

        \int_{p_0}^{p} \frac{\mathrm{d} p}{p} = \int_{0}^{h} -\frac{\rho_0}{p_0}
        \cdot g \cdot \mathrm{d}  h

    Auf der linken Seite wurden die Integralgrenzen gemäß einer
    :ref:`Integration durch Substitution <gwm:Integration durch Substitution>`
    umgerechnet. Auf der rechten Seite ist der Term :math:`-\frac{\rho_0}{p_0}
    \cdot g` nicht von der Höhe :math:`h` abhängig und kann somit als
    konstanter Faktor vor das Integral gezogen werden:

    .. math::

        \int_{p_0}^{p} \frac{\mathrm{d} p}{p} = -\frac{\rho_0}{p_0} \cdot g
        \cdot \int_{0}^{h} \mathrm{d} h

    Das Integral auf der linken Seite kann ebenfalls unmittelbar berechnet
    werden, wenn man :math:`p(h)` als Funktion der Höhe auffasst. Auf der linken
    Gleichungsseite steht damit eine zusammengesetzte Funktion, deren Zähler der
    Ableitung des Nenners entspricht. Mit der entsprechenden
    :ref:`Integrationsmethode
    <Integration-Zähler-gleich-Ableitung-des-Nenners>` folgt:

    .. math::

        \ln{(p)} - \ln{(p_0)} = - \frac{\rho_0}{p_0} \cdot g \cdot h

    Mit Hilfe der :ref:`Rechenregeln für Logarithmen <gwm:Rechenregeln für
    Logarithmen>` kann der Term auf der linken Seite als :math:`\ln{\left(
    \frac{p}{p_0}\right)}` geschrieben werden. Um die resultierende
    :ref:`Logarithmus-Gleichung <gwm:Lösen von Logarithmusgleichungen>`
    aufzulösen, kann man auf beiden Seiten der Gleichung :math:`e` mit den
    jeweigen Termen potenzieren. Wegen :math:`e^{\ln{(x)}} = x` folgt
    schließlich:

    .. math::

        p = p_0 \cdot e^{- \frac{\rho_0}{p_0} \cdot g \cdot h}

.. [#] Dieser Druck ist erheblich, wird aber von uns Menschen kaum wahrgenommen,
    da wir einen gleich großen Druck auch in unseren Lungen haben und daher
    nicht zusammengepresst werden.

.. [#] Mit einfachen Wasserstrahlpumpen lässt sich ein Druck von rund
    :math:`\unit[10]{hPa}` erreichen. Für viele prinzipielle Versuche,
    beispielsweise Magdeburger Halbkugeln oder Fallröhren reicht dieser Druck
    bereits aus.

.. raw:: html

    <hr />

.. hint::

    Zu diesem Abschnitt gibt es :ref:`Übungsaufgaben <Aufgaben Mechanik der
    Gase>`.

.. :ref:`Experimente <Experimente Mechanik der Gase>` und 


